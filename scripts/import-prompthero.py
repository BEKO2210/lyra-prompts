#!/usr/bin/env python3
"""
Import-Script: PromptHero / Hugging Face Bild-Prompt Datasets -> Lyra Prompts

Holt hochwertige Bild-Prompts aus zwei Hugging Face Datasets:
  1. Falah/image_generation_prompts_SDXL (1M SDXL Prompts)
  2. vivym/midjourney-prompts (9M Midjourney Prompts)

Filtert nach Qualitaet, entfernt Duplikate, und erstellt Lyra-kompatible
Prompt-Dateien in der Kategorie bildbearbeitung-visualisierung.

Laeuft via GitHub Actions (max 50 pro Lauf, um Reviews zu ermoeglichen).
"""

import csv
import hashlib
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

import requests

# ── Konfiguration ──────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
KATEGORIEN_DIR = REPO_ROOT / "kategorien"
CREDITS_FILE = REPO_ROOT / "CREDITS.md"
IMPORTED_FILE = REPO_ROOT / "scripts" / "imported-prompthero.json"
LOG_FILE = REPO_ROOT / "scripts" / "import-prompthero-log.json"

MAX_PROMPTS = int(os.environ.get("MAX_PROMPTS", "50"))
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
SOURCE = os.environ.get("PROMPTHERO_SOURCE", "sdxl")  # "sdxl", "midjourney", "both"
TODAY = date.today().isoformat()

# Hugging Face Datasets API
HF_API = "https://datasets-server.huggingface.co/rows"
SOURCES = {
    "sdxl": {
        "dataset": "Falah/image_generation_prompts_SDXL",
        "config": "default",
        "split": "train",
        "prompt_field": "prompts",
        "model": "SDXL",
        "total_rows": 1_000_000,
    },
    "midjourney": {
        "dataset": "vivym/midjourney-prompts",
        "config": "default",
        "split": "train",
        "prompt_field": "prompt",
        "model": "Midjourney",
        "total_rows": 9_085_397,
    },
}

# Mindestlaenge fuer einen brauchbaren Prompt
MIN_PROMPT_LEN = 80
MAX_PROMPT_LEN = 2000

# Qualitaets-Keywords: Prompts mit diesen Begriffen werden bevorzugt
QUALITY_KEYWORDS = [
    "cinematic", "photorealistic", "ultra-realistic", "hyperrealistic",
    "8k", "4k", "hdr", "detailed", "professional", "masterpiece",
    "high quality", "studio lighting", "dramatic lighting", "golden hour",
    "portrait", "landscape", "architecture", "nature", "fantasy",
    "concept art", "digital art", "oil painting", "watercolor",
    "bokeh", "depth of field", "macro", "aerial", "panoramic",
    "surreal", "abstract", "minimalist", "vintage", "retro",
    "neon", "cyberpunk", "steampunk", "art nouveau", "art deco",
    "fashion", "editorial", "commercial", "product photography",
]


# ── Hilfsfunktionen ───────────────────────────────────────────

def slugify(text: str, max_len: int = 40) -> str:
    """URL-freundlicher Dateiname."""
    text = text.lower().strip()[:80]
    text = re.sub(r'[^a-z0-9\-]', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:max_len]


def prompt_hash(text: str) -> str:
    """Kurzer Hash eines Prompts fuer Duplikat-Check."""
    return hashlib.md5(text.strip().lower().encode()).hexdigest()[:12]


def quality_score(text: str) -> int:
    """Bewertet die Qualitaet eines Prompts (hoeher = besser)."""
    text_lower = text.lower()
    score = 0
    for kw in QUALITY_KEYWORDS:
        if kw in text_lower:
            score += 1
    # Bonus fuer laengere, detaillierte Prompts
    if len(text) > 200:
        score += 2
    if len(text) > 400:
        score += 2
    # Malus fuer zu kurze oder generische Prompts
    if len(text) < MIN_PROMPT_LEN:
        score -= 10
    return score


def extract_title(prompt_text: str) -> str:
    """Extrahiert einen kurzen Titel aus dem Prompt-Text."""
    # Erste 60 Zeichen als Basis nehmen
    text = prompt_text.strip()
    # Bis zum ersten Komma oder Punkt
    for sep in [',', '.', ';', ':', ' --', '\n']:
        idx = text.find(sep)
        if 8 < idx < 70:
            text = text[:idx]
            break
    else:
        text = text[:60]
    # Bereinigen
    text = text.strip(' .,;:')
    if len(text) < 5:
        text = prompt_text[:50].strip()
    return text


def extract_style_tags(prompt_text: str) -> list:
    """Extrahiert relevante Style-Tags aus dem Prompt."""
    text_lower = prompt_text.lower()
    tags = []
    style_map = {
        "portrait": "Portrait", "landscape": "Landschaft",
        "cinematic": "Cinematic", "photorealistic": "Fotorealistisch",
        "fantasy": "Fantasy", "sci-fi": "Sci-Fi", "cyberpunk": "Cyberpunk",
        "watercolor": "Aquarell", "oil painting": "Oelgemaelde",
        "digital art": "Digital Art", "concept art": "Concept Art",
        "anime": "Anime", "cartoon": "Cartoon", "3d": "3D",
        "minimalist": "Minimalistisch", "abstract": "Abstrakt",
        "vintage": "Vintage", "retro": "Retro", "neon": "Neon",
        "architecture": "Architektur", "nature": "Natur",
        "fashion": "Fashion", "food": "Food", "product": "Produkt",
        "macro": "Makro", "aerial": "Luftaufnahme",
        "black and white": "Schwarz-Weiss", "noir": "Noir",
        "surreal": "Surreal", "steampunk": "Steampunk",
    }
    for keyword, tag in style_map.items():
        if keyword in text_lower and tag not in tags:
            tags.append(tag)
        if len(tags) >= 5:
            break
    if not tags:
        tags = ["Bild-Prompt", "KI-Kunst"]
    return tags


def load_imported() -> dict:
    """Laedt die Liste bereits importierter Prompt-Hashes."""
    if IMPORTED_FILE.exists():
        return json.loads(IMPORTED_FILE.read_text(encoding="utf-8"))
    return {"hashes": [], "last_run": None, "total_imported": 0}


def save_imported(data: dict):
    """Speichert die Import-Tracking-Datei."""
    IMPORTED_FILE.parent.mkdir(parents=True, exist_ok=True)
    IMPORTED_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def get_next_id() -> int:
    """Liest die naechste freie ID aus CREDITS.md."""
    text = CREDITS_FILE.read_text(encoding="utf-8")
    m = re.search(r'Nächste freie Nummer:\*\*\s*#(\d+)', text)
    if m:
        return int(m.group(1))
    ids = [int(x) for x in re.findall(r'#(\d{3,})', text)]
    return max(ids) + 1 if ids else 352


def get_existing_hashes() -> set:
    """Sammelt Hashes bestehender Bild-Prompts fuer Duplikat-Check."""
    hashes = set()
    bild_dir = KATEGORIEN_DIR / "bildbearbeitung-visualisierung"
    if bild_dir.exists():
        for md_file in bild_dir.glob("*.md"):
            content = md_file.read_text(encoding="utf-8", errors="ignore")
            # Prompt-Text extrahieren
            match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
            if match:
                hashes.add(prompt_hash(match.group(1)))
    return hashes


def fetch_prompts(source_key: str, offset: int, length: int) -> list:
    """Holt Prompts vom Hugging Face Datasets Server."""
    src = SOURCES[source_key]
    params = {
        "dataset": src["dataset"],
        "config": src["config"],
        "split": src["split"],
        "offset": offset,
        "length": length,
    }
    resp = requests.get(HF_API, params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    rows = data.get("rows", [])
    field = src["prompt_field"]
    prompts = []
    for row in rows:
        r = row.get("row", {})
        text = r.get(field, "")
        if isinstance(text, str) and text.strip():
            prompts.append({
                "text": text.strip(),
                "model": src["model"],
                "source": source_key,
            })
    return prompts


def create_prompt_file(prompt_id: int, title: str, prompt_text: str,
                       model: str, tags: list, source: str) -> Path:
    """Erstellt eine Lyra-kompatible Bild-Prompt-Datei."""
    slug = slugify(title)
    filename = f"{prompt_id:03d}-{slug}.md"
    cat_dir = KATEGORIEN_DIR / "bildbearbeitung-visualisierung"
    cat_dir.mkdir(parents=True, exist_ok=True)
    filepath = cat_dir / filename

    tags_str = json.dumps(tags, ensure_ascii=False)
    safe_title = title.replace('"', "'")

    content = f'''---
id: "#{prompt_id:03d}"
titel: "{safe_title}"
kategorie: "Bildbearbeitung & KI-Visualisierung"
unterkategorie: "{model} Prompt"
tags: {tags_str}
plattformen: ["ChatGPT/DALL-E", "Midjourney", "Stable Diffusion", "Flux"]
schwierigkeit: "Anfänger"
quelle: "prompthero-{source}"
erstellt: "{TODAY}"
---

## Prompt

```
{prompt_text}
```

## Anwendung

Dieser Bild-Prompt wurde aus der **PromptHero**-Community kuratiert ({model}).
Kopiere den Prompt und fuege ihn in dein bevorzugtes KI-Bildgenerierungs-Tool ein.

- **Optimiert fuer:** {model}, aber auch mit anderen Tools nutzbar
- **Tipp:** Passe Details wie Farben, Stil oder Perspektive an deine Beduerfnisse an
- **Qualitaet:** Fuer beste Ergebnisse nutze die hoechste verfuegbare Aufloesung

## Variationen

- Aendere den Stil: Ersetze z.B. "cinematic" durch "watercolor" oder "anime"
- Aendere die Perspektive: "from above", "low angle", "close-up", "wide shot"
- Aendere die Beleuchtung: "golden hour", "studio lighting", "neon", "moody"
- Fuege Negativ-Prompts hinzu: "no blur, no artifacts, no watermark"
'''
    if not DRY_RUN:
        filepath.write_text(content, encoding="utf-8")
    return filepath


def update_credits(new_prompts: list, next_id: int):
    """Aktualisiert CREDITS.md mit den neuen Bild-Prompts."""
    text = CREDITS_FILE.read_text(encoding="utf-8")

    # Naechste freie Nummer aktualisieren
    text = re.sub(
        r'(Nächste freie Nummer:\*\*\s*)#\d+',
        f'\\g<1>#{next_id:03d}',
        text
    )

    # Gesamt aktualisieren
    total_match = re.search(r'(Gesamt:\*\*\s*)(\d+)', text)
    if total_match:
        old_total = int(total_match.group(2))
        new_total = old_total + len(new_prompts)
        text = text.replace(total_match.group(0), f'{total_match.group(1)}{new_total}')

    # Stand aktualisieren
    text = re.sub(r'(Stand:\*\*\s*)[\d-]+', f'\\g<1>{TODAY}', text)

    # Neuen Import-Abschnitt am Ende
    import_section = f"\n\n---\n\n## PromptHero Bild-Prompt Import ({TODAY})\n\n"
    import_section += f"**{len(new_prompts)} neue Bild-Prompts** importiert "
    import_section += "(Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):\n\n"
    import_section += "| ID | Titel | Modell | Datei |\n"
    import_section += "|----|-------|--------|-------|\n"
    for p in new_prompts:
        import_section += f"| #{p['id']:03d} | {p['title'][:40]} | {p['model']} | `bildbearbeitung-visualisierung/{p['filename']}` |\n"

    last_line_match = re.search(r'\n(\*Letzte Aktualisierung:.*\*)\s*$', text)
    if last_line_match:
        text = text[:last_line_match.start()] + import_section
    else:
        text += import_section

    text += f"\n*Letzte Aktualisierung: {TODAY} — {len(new_prompts)} Bild-Prompts importiert*\n"

    if not DRY_RUN:
        CREDITS_FILE.write_text(text, encoding="utf-8")


# ── Hauptprogramm ────────────────────────────────────────────

def main():
    print("=== Lyra Prompts: PromptHero Bild-Prompt Import ===")
    print(f"    Quelle: {SOURCE}")
    print(f"    Max Prompts: {MAX_PROMPTS}")
    print(f"    Dry Run: {DRY_RUN}")
    print()

    # 1. Tracking laden
    print("[1/5] Lade Import-Historie...")
    imported_data = load_imported()
    known_hashes = set(imported_data.get("hashes", []))
    print(f"      {len(known_hashes)} bereits importiert")

    # 2. Bestehende Hashes laden
    print("[2/5] Lade bestehende Bild-Prompts...")
    existing_hashes = get_existing_hashes()
    all_known = known_hashes | existing_hashes
    print(f"      {len(existing_hashes)} bestehende Bild-Prompts")

    # 3. Quellen bestimmen
    sources = []
    if SOURCE in ("sdxl", "both"):
        sources.append("sdxl")
    if SOURCE in ("midjourney", "both"):
        sources.append("midjourney")
    if not sources:
        sources = ["sdxl"]

    # 4. Prompts holen und filtern
    print("[3/5] Hole Prompts von Hugging Face...")
    candidates = []

    for src_key in sources:
        src = SOURCES[src_key]
        print(f"      Quelle: {src['dataset']} ({src['total_rows']} total)")

        # Strategie: Zufaellige Offsets samplen, um Vielfalt zu bekommen
        import random
        random.seed(TODAY)  # Reproduzierbar pro Tag

        batch_size = 100
        # Mehrere zufaellige Positionen im Dataset samplen
        max_offset = src["total_rows"] - batch_size
        offsets = sorted(random.sample(range(0, max_offset), min(20, max_offset // batch_size)))

        for offset in offsets:
            if len(candidates) >= MAX_PROMPTS * 3:
                break
            try:
                batch = fetch_prompts(src_key, offset, batch_size)
                for p in batch:
                    h = prompt_hash(p["text"])
                    if h in all_known:
                        continue
                    if len(p["text"]) < MIN_PROMPT_LEN or len(p["text"]) > MAX_PROMPT_LEN:
                        continue
                    score = quality_score(p["text"])
                    if score < 2:
                        continue
                    p["hash"] = h
                    p["score"] = score
                    candidates.append(p)
                    all_known.add(h)
            except Exception as e:
                print(f"      Warnung: Offset {offset} fehlgeschlagen: {e}")
                continue

        print(f"      {len(candidates)} Kandidaten nach Qualitaetsfilter")

    # 5. Beste Prompts auswaehlen
    print("[4/5] Waehle beste Prompts aus...")
    candidates.sort(key=lambda x: x["score"], reverse=True)
    selected = candidates[:MAX_PROMPTS]
    print(f"      {len(selected)} Prompts ausgewaehlt (Top-Qualitaet)")

    if not selected:
        print("\n[5/5] Keine neuen Prompts gefunden.")
        print(f"\nFertig! 0 neue Bild-Prompts importiert.")
        return 0

    # 6. Dateien erstellen
    print(f"[5/5] Erstelle {len(selected)} Prompt-Dateien...")
    next_id = get_next_id()
    new_prompts = []

    for p in selected:
        title = extract_title(p["text"])
        tags = extract_style_tags(p["text"])
        filepath = create_prompt_file(
            next_id, title, p["text"], p["model"], tags, p["source"]
        )
        slug = slugify(title)
        filename = f"{next_id:03d}-{slug}.md"

        new_prompts.append({
            "id": next_id,
            "title": title,
            "model": p["model"],
            "filename": filename,
            "hash": p["hash"],
            "score": p["score"],
        })

        known_hashes.add(p["hash"])
        print(f"      + #{next_id:03d} {title[:50]} ({p['model']}, Score: {p['score']})")
        next_id += 1

    # 7. CREDITS.md und Tracking aktualisieren
    if new_prompts and not DRY_RUN:
        update_credits(new_prompts, next_id)
        imported_data["hashes"] = sorted(known_hashes)
        imported_data["last_run"] = TODAY
        imported_data["last_count"] = len(new_prompts)
        imported_data["total_imported"] = imported_data.get("total_imported", 0) + len(new_prompts)
        save_imported(imported_data)

        # Log
        log = {
            "imported_count": len(new_prompts),
            "source": SOURCE,
            "date": TODAY,
            "dry_run": DRY_RUN,
        }
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")

    print(f"\nFertig! {len(new_prompts)} neue Bild-Prompts importiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
