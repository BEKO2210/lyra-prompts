#!/usr/bin/env python3
"""
Import-Script: awesome-chatgpt-prompts -> Lyra Prompts

Holt Prompts von github.com/f/awesome-chatgpt-prompts (prompts.csv),
filtert Duplikate, mappt Kategorien und erstellt Lyra-kompatible Prompt-Dateien.

Laeuft taeglich via GitHub Actions (max 50 neue Prompts pro Lauf).
"""

import csv
import io
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

import requests

# CSV-Feldlimit erhoehen (manche Prompts sind sehr lang)
csv.field_size_limit(1_000_000)

# ── Konfiguration ──────────────────────────────────────────────
SOURCE_URL = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
REPO_ROOT = Path(__file__).resolve().parent.parent
KATEGORIEN_DIR = REPO_ROOT / "kategorien"
CREDITS_FILE = REPO_ROOT / "CREDITS.md"
IMPORTED_FILE = REPO_ROOT / "scripts" / "imported-prompts.json"
LOG_FILE = REPO_ROOT / "scripts" / "import-log.json"

MAX_PROMPTS = int(os.environ.get("MAX_PROMPTS", "50"))
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
TODAY = date.today().isoformat()

# ── Kategorie-Mapping ─────────────────────────────────────────
# Mappt englische Prompt-Titel/Themen auf Lyra-Kategorien
KEYWORD_TO_CATEGORY = {
    # Technik & Alltag
    "linux": "technik-alltag",
    "terminal": "technik-alltag",
    "javascript": "technik-alltag",
    "python": "technik-alltag",
    "sql": "technik-alltag",
    "developer": "technik-alltag",
    "programmer": "technik-alltag",
    "software": "technik-alltag",
    "engineer": "technik-alltag",
    "architect": "technik-alltag",
    "database": "technik-alltag",
    "machine learning": "technik-alltag",
    "cyber security": "technik-alltag",
    "it ": "technik-alltag",
    "regex": "technik-alltag",
    "code": "technik-alltag",
    "ux": "technik-alltag",
    "ui ": "technik-alltag",
    "web design": "technik-alltag",
    "tech": "technik-alltag",
    "api": "technik-alltag",
    "devops": "technik-alltag",
    "blockchain": "technik-alltag",
    "solidity": "technik-alltag",
    "prompt": "technik-alltag",

    # Beruf & Karriere
    "recruiter": "beruf-karriere",
    "interviewer": "beruf-karriere",
    "manager": "beruf-karriere",
    "consultant": "beruf-karriere",
    "career": "beruf-karriere",
    "resume": "beruf-karriere",
    "cover letter": "beruf-karriere",
    "hr ": "beruf-karriere",
    "startup": "beruf-karriere",
    "ceo": "beruf-karriere",
    "business": "beruf-karriere",
    "entrepreneur": "beruf-karriere",
    "accountant": "beruf-karriere",
    "financial": "beruf-karriere",
    "real estate": "beruf-karriere",
    "salesperson": "beruf-karriere",
    "product manager": "beruf-karriere",

    # Kommunikation & Beziehungen
    "relationship": "kommunikation-beziehungen",
    "friend": "kommunikation-beziehungen",
    "debate": "kommunikation-beziehungen",
    "motivational": "kommunikation-beziehungen",
    "public speaking": "kommunikation-beziehungen",
    "speech": "kommunikation-beziehungen",
    "elocution": "kommunikation-beziehungen",
    "logistician": "kommunikation-beziehungen",

    # Kreativitaet & Freizeit
    "poet": "kreativitaet-freizeit",
    "storyteller": "kreativitaet-freizeit",
    "screenwriter": "kreativitaet-freizeit",
    "novelist": "kreativitaet-freizeit",
    "composer": "kreativitaet-freizeit",
    "songwriter": "kreativitaet-freizeit",
    "rapper": "kreativitaet-freizeit",
    "stand-up": "kreativitaet-freizeit",
    "comedian": "kreativitaet-freizeit",
    "magician": "kreativitaet-freizeit",
    "movie critic": "kreativitaet-freizeit",
    "film critic": "kreativitaet-freizeit",
    "music": "kreativitaet-freizeit",
    "classical": "kreativitaet-freizeit",
    "diy": "kreativitaet-freizeit",
    "interior": "kreativitaet-freizeit",
    "florist": "kreativitaet-freizeit",
    "artist": "kreativitaet-freizeit",
    "game": "kreativitaet-freizeit",
    "chess": "kreativitaet-freizeit",
    "tic-tac-toe": "kreativitaet-freizeit",
    "ascii": "kreativitaet-freizeit",
    "svg": "kreativitaet-freizeit",
    "diagram": "kreativitaet-freizeit",
    "emoji": "kreativitaet-freizeit",
    "trivia": "kreativitaet-freizeit",
    "dream": "kreativitaet-freizeit",
    "character": "kreativitaet-freizeit",
    "dungeon": "kreativitaet-freizeit",
    "fantasy": "kreativitaet-freizeit",

    # Lernen & Wachstum
    "tutor": "lernen-wachstum",
    "teacher": "lernen-wachstum",
    "instructor": "lernen-wachstum",
    "philosopher": "lernen-wachstum",
    "math": "lernen-wachstum",
    "history": "lernen-wachstum",
    "language": "lernen-wachstum",
    "translator": "lernen-wachstum",
    "etymology": "lernen-wachstum",
    "synonym": "lernen-wachstum",
    "proofreader": "lernen-wachstum",
    "plagiarism": "lernen-wachstum",
    "essay": "lernen-wachstum",
    "journal": "lernen-wachstum",
    "encyclopedia": "lernen-wachstum",
    "academician": "lernen-wachstum",
    "self-help": "lernen-wachstum",
    "coach": "lernen-wachstum",
    "mentor": "lernen-wachstum",
    "educational": "lernen-wachstum",

    # Gesundheit & Wohlbefinden
    "doctor": "gesundheit-wohlbefinden",
    "dentist": "gesundheit-wohlbefinden",
    "dietitian": "gesundheit-wohlbefinden",
    "nutritionist": "gesundheit-wohlbefinden",
    "trainer": "gesundheit-wohlbefinden",
    "yoga": "gesundheit-wohlbefinden",
    "hypnotherapist": "gesundheit-wohlbefinden",
    "psychologist": "gesundheit-wohlbefinden",
    "therapist": "gesundheit-wohlbefinden",
    "mental health": "gesundheit-wohlbefinden",
    "gnomist": "gesundheit-wohlbefinden",

    # Alltag & Leben
    "chef": "alltag-leben",
    "cook": "alltag-leben",
    "recipe": "alltag-leben",
    "tea": "alltag-leben",
    "travel": "alltag-leben",
    "guide": "alltag-leben",
    "travel": "alltag-leben",
    "automobile": "alltag-leben",
    "car ": "alltag-leben",
    "mechanic": "alltag-leben",
    "budget": "alltag-leben",
    "shopping": "alltag-leben",
    "personal": "alltag-leben",
    "pet": "alltag-leben",
    "babysitter": "alltag-leben",

    # Kommunikation (erweitert)
    "advertis": "kommunikation-beziehungen",
    "seo": "kommunikation-beziehungen",
    "social media": "kommunikation-beziehungen",
    "journal": "kommunikation-beziehungen",
    "reporter": "kommunikation-beziehungen",
    "commentariat": "kommunikation-beziehungen",
    "plagiarism": "kommunikation-beziehungen",

    # Spezielle Situationen
    "emergency": "spezielle-situationen",
    "legal": "spezielle-situationen",
    "lawyer": "spezielle-situationen",
    "fallacy": "spezielle-situationen",
    "astrologer": "spezielle-situationen",
    "talent": "spezielle-situationen",
}

# Standard-Kategorie wenn kein Keyword matcht
DEFAULT_CATEGORY = "technik-alltag"

# ── Hilfsfunktionen ───────────────────────────────────────────

def slugify(text: str, max_len: int = 40) -> str:
    """Erzeugt einen URL-freundlichen Dateinamen (deutsch-freundlich)."""
    text = text.lower().strip()
    # Englische -> Deutsche Uebersetzungen fuer gaengige Begriffe
    replacements = {
        "act as": "", "act as a": "", "act as an": "",
        " a ": "-", " an ": "-", " the ": "-",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    # Nur Buchstaben, Zahlen, Bindestriche
    text = re.sub(r'[^a-z0-9\-]', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:max_len]


def detect_category(title: str, prompt_text: str) -> str:
    """Erkennt die passende Lyra-Kategorie anhand von Keywords.
    Prioritaet: Titel-Match vor Prompt-Text-Match, laengere Keywords zuerst."""
    title_lower = title.lower()
    combined = (title + " " + prompt_text[:200]).lower()
    # Laengere Keywords zuerst pruefen (spezifischer)
    sorted_keywords = sorted(KEYWORD_TO_CATEGORY.keys(), key=len, reverse=True)
    # Erst im Titel suchen
    for keyword in sorted_keywords:
        if keyword in title_lower:
            return KEYWORD_TO_CATEGORY[keyword]
    # Dann im gesamten Text
    for keyword in sorted_keywords:
        if keyword in combined:
            return KEYWORD_TO_CATEGORY[keyword]
    return DEFAULT_CATEGORY


def generate_tags(title: str, prompt_text: str) -> list:
    """Generiert 3-5 relevante Tags aus Titel und Prompt."""
    words = re.findall(r'[a-z]{3,}', (title + " " + prompt_text[:150]).lower())
    # Haeufige Stoppwoerter entfernen
    stop = {"the", "and", "for", "are", "but", "not", "you", "all", "can",
            "had", "her", "was", "one", "our", "out", "has", "have", "from",
            "they", "been", "said", "each", "which", "their", "will", "other",
            "about", "many", "then", "them", "these", "some", "would", "make",
            "like", "into", "could", "time", "very", "when", "come", "that",
            "with", "this", "just", "know", "take", "people", "want", "act",
            "should", "need", "also", "back", "after", "use", "two", "how",
            "first", "well", "way", "even", "new", "because", "any", "give",
            "most", "being", "provide", "based", "must", "able", "such",
            "help", "response", "using", "role", "play", "please", "will",
            "your", "what", "more", "include", "ensure"}
    seen = set()
    tags = []
    for w in words:
        if w not in stop and w not in seen and len(w) > 3:
            seen.add(w)
            tags.append(w)
        if len(tags) >= 5:
            break
    return tags if tags else ["chatgpt", "prompt", "ai"]


def load_imported() -> dict:
    """Laedt die Liste bereits importierter Prompts."""
    if IMPORTED_FILE.exists():
        return json.loads(IMPORTED_FILE.read_text(encoding="utf-8"))
    return {"imported": [], "last_run": None}


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
    # Fallback: nach hoechster ID suchen
    ids = [int(x) for x in re.findall(r'#(\d{3,})', text)]
    return max(ids) + 1 if ids else 352


def get_existing_titles() -> set:
    """Sammelt alle bestehenden Prompt-Titel fuer Duplikat-Check."""
    titles = set()
    for md_file in KATEGORIEN_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r'titel:\s*"([^"]+)"', content)
        if m:
            titles.add(m.group(1).lower().strip())
    return titles


def is_duplicate(title: str, existing_titles: set) -> bool:
    """Prueft ob ein aehnlicher Prompt schon existiert."""
    title_lower = title.lower().strip()
    # Exakter Match
    if title_lower in existing_titles:
        return True
    # "Act as" entfernen und nochmal pruefen
    clean = re.sub(r'^act as (a |an )?', '', title_lower).strip()
    for existing in existing_titles:
        existing_clean = re.sub(r'^act as (a |an )?', '', existing).strip()
        if clean == existing_clean:
            return True
        # Aehnlichkeit: wenn >70% der Woerter uebereinstimmen
        words_new = set(clean.split())
        words_old = set(existing_clean.split())
        if words_new and words_old:
            overlap = len(words_new & words_old) / max(len(words_new), len(words_old))
            if overlap > 0.7:
                return True
    return False


CAT_DISPLAY_NAMES = {
    "alltag-leben": "Alltag & Leben",
    "beruf-karriere": "Beruf & Karriere",
    "bildbearbeitung-visualisierung": "Bildbearbeitung & Visualisierung",
    "gesundheit-wohlbefinden": "Gesundheit & Wohlbefinden",
    "kommunikation-beziehungen": "Kommunikation & Beziehungen",
    "kreativitaet-freizeit": "Kreativitaet & Freizeit",
    "lernen-wachstum": "Lernen & Wachstum",
    "pro": "Professionell & Business",
    "spezielle-situationen": "Spezielle Situationen",
    "technik-alltag": "Technik & Alltag",
}


def create_prompt_file(prompt_id: int, title: str, prompt_text: str, category: str,
                       contributor: str) -> Path:
    """Erstellt eine Lyra-kompatible Prompt-Datei."""
    slug = slugify(title)
    filename = f"{prompt_id:03d}-{slug}.md"
    cat_dir = KATEGORIEN_DIR / category
    cat_dir.mkdir(parents=True, exist_ok=True)
    filepath = cat_dir / filename

    tags = generate_tags(title, prompt_text)
    tags_str = json.dumps(tags, ensure_ascii=False)
    cat_display = CAT_DISPLAY_NAMES.get(category, category)

    # Prompt-Text aufbereiten: einruecken und formatieren
    # Original-Prompt beibehalten, aber als Lyra-Format
    content = f'''---
id: "#{prompt_id:03d}"
titel: "{title}"
kategorie: "{cat_display}"
unterkategorie: "Importiert"
tags: {tags_str}
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "{contributor}"
erstellt: "{TODAY}"
---

## Prompt

```
{prompt_text}
```

## Anwendung

Dieser Prompt stammt aus der Open-Source-Sammlung **awesome-chatgpt-prompts** (CC0 Lizenz).
Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.

- **Rolle:** {title}
- **Schwierigkeit:** Anfaenger — einfach kopieren und nutzen
- **Tipp:** Passe den Prompt an deine Beduerfnisse an, indem du spezifische Details hinzufuegst

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Kombiniere mit anderen Prompts: Nutze mehrere Rollen in einem Gespraech
- Erstelle eine Serie: Baue auf den Ergebnissen auf und verfeinere iterativ
'''
    if not DRY_RUN:
        filepath.write_text(content, encoding="utf-8")
    return filepath


def update_credits(new_prompts: list, next_id: int):
    """Aktualisiert CREDITS.md mit den neuen Prompts."""
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

    # Neuen Import-Abschnitt am Ende hinzufuegen
    import_section = f"\n\n---\n\n## Auto-Import von awesome-chatgpt-prompts ({TODAY})\n\n"
    import_section += f"**{len(new_prompts)} neue Prompts** automatisch importiert "
    import_section += f"(Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):\n\n"
    import_section += "| ID | Titel | Kategorie | Datei |\n"
    import_section += "|----|-------|-----------|-------|\n"
    for p in new_prompts:
        import_section += f"| #{p['id']:03d} | {p['title']} | {CAT_DISPLAY_NAMES.get(p['category'], p['category'])} | `{p['category']}/{p['filename']}` |\n"

    # Vor der letzten Zeile einfuegen
    last_line_match = re.search(r'\n(\*Letzte Aktualisierung:.*\*)\s*$', text)
    if last_line_match:
        text = text[:last_line_match.start()] + import_section
    else:
        text += import_section

    text += f"\n*Letzte Aktualisierung: {TODAY} — {len(new_prompts)} Prompts auto-importiert*\n"

    if not DRY_RUN:
        CREDITS_FILE.write_text(text, encoding="utf-8")


# ── Hauptprogramm ────────────────────────────────────────────

def main():
    print(f"=== Lyra Prompts: Auto-Import von awesome-chatgpt-prompts ===")
    print(f"    Max Prompts: {MAX_PROMPTS}")
    print(f"    Dry Run: {DRY_RUN}")
    print()

    # 1. CSV herunterladen
    print("[1/5] Lade prompts.csv herunter...")
    resp = requests.get(SOURCE_URL, timeout=30)
    resp.raise_for_status()
    reader = csv.DictReader(io.StringIO(resp.text))
    source_prompts = list(reader)
    print(f"      {len(source_prompts)} Prompts in der Quelle gefunden")

    # 2. Bereits importierte laden
    print("[2/5] Lade Import-Historie...")
    imported_data = load_imported()
    already_imported = set(imported_data.get("imported", []))
    print(f"      {len(already_imported)} bereits importiert")

    # 3. Bestehende Titel laden (Duplikat-Check)
    print("[3/5] Lade bestehende Prompts fuer Duplikat-Check...")
    existing_titles = get_existing_titles()
    print(f"      {len(existing_titles)} bestehende Prompts gefunden")

    # 4. Neue Prompts filtern und importieren
    print("[4/5] Filtere und importiere neue Prompts...")
    next_id = get_next_id()
    new_prompts = []
    skipped_dup = 0
    skipped_already = 0

    for row in source_prompts:
        if len(new_prompts) >= MAX_PROMPTS:
            break

        title = row.get("act", "").strip()
        prompt_text = row.get("prompt", "").strip()
        contributor = row.get("contributor", "unbekannt").strip()

        if not title or not prompt_text:
            continue

        # Schon importiert?
        prompt_key = slugify(title, 60)
        if prompt_key in already_imported:
            skipped_already += 1
            continue

        # Duplikat?
        if is_duplicate(title, existing_titles):
            skipped_dup += 1
            already_imported.add(prompt_key)  # Merken als "bearbeitet"
            continue

        # Kategorie erkennen
        category = detect_category(title, prompt_text)

        # Prompt-Datei erstellen
        filepath = create_prompt_file(next_id, title, prompt_text, category, contributor)
        slug = slugify(title)
        filename = f"{next_id:03d}-{slug}.md"

        new_prompts.append({
            "id": next_id,
            "title": title,
            "category": category,
            "filename": filename,
            "contributor": contributor,
        })

        already_imported.add(prompt_key)
        existing_titles.add(title.lower())
        print(f"      + #{next_id:03d} {title} -> {category}/{filename}")
        next_id += 1

    print(f"\n      Importiert: {len(new_prompts)}")
    print(f"      Uebersprungen (bereits importiert): {skipped_already}")
    print(f"      Uebersprungen (Duplikat): {skipped_dup}")

    # 5. CREDITS.md und Tracking aktualisieren
    if new_prompts and not DRY_RUN:
        print("[5/5] Aktualisiere CREDITS.md und Tracking...")
        update_credits(new_prompts, next_id)
        imported_data["imported"] = sorted(already_imported)
        imported_data["last_run"] = TODAY
        imported_data["last_count"] = len(new_prompts)
        save_imported(imported_data)
    else:
        print("[5/5] Keine Aenderungen (dry run oder keine neuen Prompts)")

    # Log fuer GitHub Actions
    log = {
        "imported_count": len(new_prompts),
        "skipped_duplicate": skipped_dup,
        "skipped_already": skipped_already,
        "date": TODAY,
        "dry_run": DRY_RUN,
    }
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")

    print(f"\nFertig! {len(new_prompts)} neue Prompts importiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
