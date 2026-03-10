#!/usr/bin/env python3
"""
Import-Script: Multi-Source Prompt Import fuer ALLE Kategorien

Holt diverse Prompts aus dem OpenRLHF/prompt-collection-v0.1 Dataset
(179K Prompts aus HelpSteer, UltraFeedback, OpenOrca, UltraInteract,
DIBT 10K, Capybara) und verteilt sie auf alle Lyra-Kategorien.

Laeuft woechentlich via GitHub Actions (max 50 neue Prompts pro Lauf).
"""

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
IMPORTED_FILE = REPO_ROOT / "scripts" / "imported-multisource.json"
LOG_FILE = REPO_ROOT / "scripts" / "import-multisource-log.json"

MAX_PROMPTS = int(os.environ.get("MAX_PROMPTS", "50"))
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
CATEGORY_FILTER = os.environ.get("CATEGORY_FILTER", "").strip()
TODAY = date.today().isoformat()

# Hugging Face Datasets Server API
HF_API = "https://datasets-server.huggingface.co/rows"
DATASET = "OpenRLHF/prompt-collection-v0.1"
TOTAL_ROWS = 179_465

# Mindest-/Maximallaenge
MIN_PROMPT_LEN = 60
MAX_PROMPT_LEN = 1500

# ── Kategorie-Erkennung ──────────────────────────────────────
# Keywords -> Kategorie (laengere Keywords zuerst matchen)
CATEGORY_RULES = {
    "alltag-leben": [
        "recipe", "cook", "meal", "food", "kitchen", "restaurant", "diet plan",
        "grocery", "shopping", "budget", "household", "cleaning", "organize",
        "travel", "vacation", "hotel", "flight", "packing", "trip",
        "car ", "automobile", "mechanic", "repair", "maintenance",
        "pet ", "dog ", "cat ", "garden", "plant", "home decor",
        "fashion", "outfit", "wardrobe", "clothing", "style",
        "parenting", "child", "family", "wedding", "gift", "party",
        "moving", "rental", "apartment", "house", "insurance", "tax",
    ],
    "beruf-karriere": [
        "resume", "cover letter", "job interview", "career", "hiring",
        "linkedin", "portfolio", "professional", "workplace",
        "business plan", "startup", "entrepreneur", "pitch",
        "marketing strategy", "sales", "revenue", "profit",
        "project management", "agile", "scrum", "leadership",
        "negotiat", "salary", "promotion", "manager", "ceo",
        "freelanc", "consulting", "client", "proposal", "invoice",
        "investor", "funding", "stock", "trading", "financial",
        "accounting", "roi", "kpi", "metrics", "analytics",
        "email template", "meeting", "presentation", "report",
    ],
    "lernen-wachstum": [
        "explain", "teach", "learn", "study", "education",
        "tutor", "lesson", "course", "curriculum", "textbook",
        "history of", "science", "physics", "chemistry", "biology",
        "math", "calcul", "algebra", "geometry", "statistic",
        "philosophy", "psychology", "sociology", "economics",
        "language", "translat", "grammar", "vocabulary",
        "essay", "research paper", "thesis", "dissertation",
        "summarize", "summary", "overview", "compare and contrast",
        "quiz", "flashcard", "exam", "test prep",
        "critical thinking", "analysis", "evaluate",
        "book review", "literature", "read",
    ],
    "kommunikation-beziehungen": [
        "email", "letter", "message", "respond to",
        "social media", "post", "caption", "hashtag",
        "blog", "article", "newsletter", "content",
        "copywriting", "headline", "slogan", "tagline",
        "speech", "presentation", "public speaking",
        "persuade", "convince", "argument", "debate",
        "relationship", "friend", "conflict", "apolog",
        "feedback", "review", "complaint", "customer",
        "interview question", "conversation", "dialog",
        "advertis", "branding", "influenc",
    ],
    "kreativitaet-freizeit": [
        "story", "creative writ", "fiction", "novel", "short story",
        "poem", "poetry", "haiku", "limerick", "sonnet",
        "song", "lyric", "rap", "music", "melody",
        "screenplay", "script", "dialog", "character",
        "joke", "humor", "funny", "comedy", "parody",
        "game", "puzzle", "riddle", "trivia", "quiz",
        "hobby", "craft", "diy", "art", "draw", "paint",
        "movie", "film", "book", "recommend",
        "fantasy", "sci-fi", "adventure", "mystery", "horror",
        "roleplay", "role play", "imagine", "pretend",
        "board game", "video game", "rpg",
        "travel itinerary", "bucket list", "fun",
    ],
    "gesundheit-wohlbefinden": [
        "health", "medical", "symptom", "diagnos", "treatment",
        "fitness", "workout", "exercise", "training", "gym",
        "nutrition", "calorie", "protein", "vitamin", "supplement",
        "weight loss", "weight gain", "bmi", "body",
        "mental health", "anxiety", "depression", "stress",
        "meditation", "mindful", "yoga", "breathing",
        "sleep", "insomnia", "rest", "recovery",
        "self-care", "wellness", "wellbeing", "balance",
        "therapy", "counsel", "psycholog",
        "habit", "routine", "productiv", "goal setting",
        "motivation", "disciplin", "focus", "concentrat",
    ],
    "technik-alltag": [
        "code", "program", "software", "develop", "debug",
        "python", "javascript", "html", "css", "sql",
        "api", "database", "server", "cloud", "deploy",
        "linux", "terminal", "command", "script", "automat",
        "machine learning", "ai ", "artificial intellig",
        "data analy", "data scien", "visualiz",
        "web", "app", "mobile", "frontend", "backend",
        "git", "github", "docker", "devops",
        "cyber", "security", "password", "encrypt",
        "excel", "spreadsheet", "google sheets",
        "wordpress", "seo", "website",
        "smartphone", "computer", "tech", "digital",
        "troubleshoot", "fix", "error", "bug",
    ],
    "spezielle-situationen": [
        "legal", "lawyer", "contract", "rights",
        "emergency", "crisis", "disaster", "accident",
        "grief", "loss", "funeral", "mourn",
        "divorce", "separation", "custody",
        "immigrat", "visa", "passport", "citizenship",
        "ethic", "moral", "dilemma", "controversy",
        "politic", "govern", "policy", "regulation",
        "religion", "spiritual", "faith", "belief",
        "climate", "environment", "sustainab",
        "volunteer", "charit", "donat", "nonprofit",
        "retire", "pension", "estate plan", "will",
    ],
}

# ── Stoppwoerter fuer Tag-Generierung ─────────────────────────
STOP_WORDS = {
    "the", "and", "for", "are", "but", "not", "you", "all", "can",
    "had", "was", "one", "our", "has", "have", "from", "they", "been",
    "said", "each", "which", "their", "will", "other", "about", "then",
    "them", "these", "some", "would", "make", "like", "into", "could",
    "time", "very", "when", "come", "that", "with", "this", "just",
    "know", "take", "want", "should", "need", "also", "back", "after",
    "use", "how", "first", "well", "way", "even", "new", "because",
    "any", "give", "most", "what", "more", "your", "help", "please",
    "write", "create", "provide", "generate", "give", "make", "list",
    "describe", "tell", "explain", "suggest", "include", "using",
    "based", "must", "able", "such", "following", "example", "could",
}

# Kategorie-Anzeigenamen
CAT_DISPLAY = {
    "alltag-leben": "Alltag & Leben",
    "beruf-karriere": "Beruf & Karriere",
    "lernen-wachstum": "Lernen & Wachstum",
    "kommunikation-beziehungen": "Kommunikation & Beziehungen",
    "kreativitaet-freizeit": "Kreativitaet & Freizeit",
    "gesundheit-wohlbefinden": "Gesundheit & Wohlbefinden",
    "technik-alltag": "Technik & Alltag",
    "spezielle-situationen": "Spezielle Situationen",
}


# ── Hilfsfunktionen ───────────────────────────────────────────

def slugify(text: str, max_len: int = 40) -> str:
    text = text.lower().strip()[:80]
    text = re.sub(r'[^a-z0-9\-]', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text[:max_len]


def prompt_hash(text: str) -> str:
    return hashlib.md5(text.strip().lower().encode()).hexdigest()[:12]


def detect_category(text: str) -> str:
    """Erkennt die Kategorie eines Prompts anhand von Keywords."""
    text_lower = text.lower()
    scores = {}
    for cat, keywords in CATEGORY_RULES.items():
        score = 0
        for kw in keywords:
            if kw in text_lower:
                score += len(kw)  # Laengere Keywords = hoehere Gewichtung
        if score > 0:
            scores[cat] = score
    if not scores:
        return ""
    return max(scores, key=scores.get)


def extract_title(text: str) -> str:
    """Kurzer Titel aus dem Prompt-Text."""
    text = text.strip()
    # Entferne gaengige Prefixe
    for prefix in ["Can you ", "Could you ", "Please ", "Write ", "Create ",
                    "Generate ", "Help me ", "I need ", "I want "]:
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    # Bis zum ersten Satzzeichen
    for sep in ['.', '?', '!', '\n', ',']:
        idx = text.find(sep)
        if 8 < idx < 70:
            text = text[:idx]
            break
    else:
        text = text[:60]
    text = text.strip(' .,;:!?')
    # Erster Buchstabe gross
    if text:
        text = text[0].upper() + text[1:]
    return text if len(text) >= 5 else "Nuetzlicher Prompt"


def generate_tags(text: str) -> list:
    """3-5 relevante Tags aus dem Prompt."""
    words = re.findall(r'[a-z]{4,}', text.lower()[:200])
    seen = set()
    tags = []
    for w in words:
        if w not in STOP_WORDS and w not in seen:
            seen.add(w)
            tags.append(w)
        if len(tags) >= 5:
            break
    return tags if tags else ["prompt", "ai", "nuetzlich"]


def quality_check(text: str) -> bool:
    """Prueft ob ein Prompt qualitativ gut genug ist."""
    if len(text) < MIN_PROMPT_LEN or len(text) > MAX_PROMPT_LEN:
        return False
    # Zu viele Sonderzeichen = Code/Daten statt Prompt
    special = sum(1 for c in text if c in '{}[]<>|\\`~^')
    if special > len(text) * 0.1:
        return False
    # Muss eine Frage oder Anweisung sein
    text_lower = text.lower()
    has_intent = any(w in text_lower for w in [
        "?", "write", "create", "explain", "help", "suggest",
        "recommend", "list", "describe", "generate", "design",
        "plan", "analyze", "compare", "summarize", "how to",
        "what is", "can you", "give me", "i need", "i want",
        "tell me", "show me", "provide", "develop", "build",
    ])
    return has_intent


def load_imported() -> dict:
    if IMPORTED_FILE.exists():
        return json.loads(IMPORTED_FILE.read_text(encoding="utf-8"))
    return {"hashes": [], "last_run": None, "total_imported": 0}


def save_imported(data: dict):
    IMPORTED_FILE.parent.mkdir(parents=True, exist_ok=True)
    IMPORTED_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def get_next_id() -> int:
    text = CREDITS_FILE.read_text(encoding="utf-8")
    m = re.search(r'Nächste freie Nummer:\*\*\s*#(\d+)', text)
    if m:
        return int(m.group(1))
    ids = [int(x) for x in re.findall(r'#(\d{3,})', text)]
    return max(ids) + 1 if ids else 352


def get_existing_hashes() -> set:
    """Hashes aller bestehenden Prompts."""
    hashes = set()
    for md_file in KATEGORIEN_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8", errors="ignore")
        match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
        if match:
            hashes.add(prompt_hash(match.group(1)))
    return hashes


def fetch_prompts(offset: int, length: int) -> list:
    """Holt Prompts vom Hugging Face Datasets Server."""
    resp = requests.get(HF_API, params={
        "dataset": DATASET, "config": "default",
        "split": "train", "offset": offset, "length": length,
    }, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    prompts = []
    for row in data.get("rows", []):
        r = row.get("row", {})
        # Prompt-Text aus context_messages extrahieren (erster user-Message)
        msgs = r.get("context_messages", [])
        text = ""
        for msg in msgs:
            if msg.get("role") == "user" and msg.get("content"):
                text = msg["content"].strip()
                break
        # Fallback: context Feld
        if not text:
            text = (r.get("context") or "").strip()
        if text:
            prompts.append({
                "text": text,
                "source_id": r.get("id", ""),
                "source_dataset": r.get("dataset", "unknown"),
            })
    return prompts


def create_prompt_file(prompt_id: int, title: str, prompt_text: str,
                       category: str, tags: list, source_ds: str) -> Path:
    """Erstellt eine Lyra-kompatible Prompt-Datei."""
    slug = slugify(title)
    filename = f"{prompt_id:03d}-{slug}.md"
    cat_dir = KATEGORIEN_DIR / category
    cat_dir.mkdir(parents=True, exist_ok=True)
    filepath = cat_dir / filename

    tags_str = json.dumps(tags, ensure_ascii=False)
    safe_title = title.replace('"', "'")
    cat_display = CAT_DISPLAY.get(category, category)

    content = f'''---
id: "#{prompt_id:03d}"
titel: "{safe_title}"
kategorie: "{cat_display}"
unterkategorie: "Importiert"
tags: {tags_str}
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "openrlhf-{source_ds}"
erstellt: "{TODAY}"
---

## Prompt

```
{prompt_text}
```

## Anwendung

Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.
Passe die Platzhalter und Details an deine Situation an.

- **Kategorie:** {cat_display}
- **Schwierigkeit:** Anfaenger — einfach kopieren und anpassen
- **Tipp:** Fuer bessere Ergebnisse, fuege spezifische Details zu deiner Situation hinzu

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Aendere die Laenge: "Kurz und knapp" oder "Ausfuehrlich mit Beispielen"
- Aendere den Ton: "Formell", "Locker", "Professionell", "Freundlich"
'''
    if not DRY_RUN:
        filepath.write_text(content, encoding="utf-8")
    return filepath


def update_credits(new_prompts: list, next_id: int):
    """Aktualisiert CREDITS.md."""
    text = CREDITS_FILE.read_text(encoding="utf-8")

    text = re.sub(
        r'(Nächste freie Nummer:\*\*\s*)#\d+',
        f'\\g<1>#{next_id:03d}', text
    )

    total_match = re.search(r'(Gesamt:\*\*\s*)(\d+)', text)
    if total_match:
        old_total = int(total_match.group(2))
        text = text.replace(total_match.group(0),
                            f'{total_match.group(1)}{old_total + len(new_prompts)}')

    text = re.sub(r'(Stand:\*\*\s*)[\d-]+', f'\\g<1>{TODAY}', text)

    # Statistik pro Kategorie
    cat_counts = {}
    for p in new_prompts:
        cat_counts[p["category"]] = cat_counts.get(p["category"], 0) + 1

    section = f"\n\n---\n\n## Multi-Source Import ({TODAY})\n\n"
    section += f"**{len(new_prompts)} neue Prompts** importiert "
    section += "(Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):\n\n"
    section += "| Kategorie | Anzahl |\n|-----------|--------|\n"
    for cat, count in sorted(cat_counts.items()):
        section += f"| {CAT_DISPLAY.get(cat, cat)} | {count} |\n"
    section += f"\n<details><summary>Alle {len(new_prompts)} Prompts anzeigen</summary>\n\n"
    section += "| ID | Titel | Kategorie |\n|----|-------|-----------|\n"
    for p in new_prompts:
        section += f"| #{p['id']:03d} | {p['title'][:45]} | {CAT_DISPLAY.get(p['category'], p['category'])} |\n"
    section += "\n</details>\n"

    last_line = re.search(r'\n(\*Letzte Aktualisierung:.*\*)\s*$', text)
    if last_line:
        text = text[:last_line.start()] + section
    else:
        text += section
    text += f"\n*Letzte Aktualisierung: {TODAY} — {len(new_prompts)} Prompts importiert*\n"

    if not DRY_RUN:
        CREDITS_FILE.write_text(text, encoding="utf-8")


# ── Hauptprogramm ────────────────────────────────────────────

def main():
    print("=== Lyra Prompts: Multi-Source Import ===")
    print(f"    Dataset: {DATASET} ({TOTAL_ROWS} Prompts)")
    print(f"    Max: {MAX_PROMPTS}")
    print(f"    Dry Run: {DRY_RUN}")
    if CATEGORY_FILTER:
        print(f"    Kategorie-Filter: {CATEGORY_FILTER}")
    print()

    # 1. Tracking laden
    print("[1/5] Lade Import-Historie...")
    imported_data = load_imported()
    known_hashes = set(imported_data.get("hashes", []))
    print(f"      {len(known_hashes)} bereits importiert")

    # 2. Bestehende Hashes laden
    print("[2/5] Lade bestehende Prompts...")
    existing_hashes = get_existing_hashes()
    all_known = known_hashes | existing_hashes
    print(f"      {len(existing_hashes)} bestehende Prompts")

    # 3. Prompts holen und kategorisieren
    print("[3/5] Hole Prompts von Hugging Face...")
    import random
    random.seed(TODAY)

    batch_size = 100
    max_offset = TOTAL_ROWS - batch_size
    # 30 zufaellige Stellen im Dataset samplen
    offsets = sorted(random.sample(range(0, max_offset), 30))

    candidates = {cat: [] for cat in CATEGORY_RULES}
    skipped_quality = 0
    skipped_nocat = 0
    skipped_dup = 0

    for offset in offsets:
        try:
            batch = fetch_prompts(offset, batch_size)
        except Exception as e:
            print(f"      Warnung: Offset {offset} fehlgeschlagen: {e}")
            continue

        for p in batch:
            text = p["text"]
            h = prompt_hash(text)

            if h in all_known:
                skipped_dup += 1
                continue

            if not quality_check(text):
                skipped_quality += 1
                continue

            cat = detect_category(text)
            if not cat:
                skipped_nocat += 1
                continue

            if CATEGORY_FILTER and cat != CATEGORY_FILTER:
                continue

            candidates[cat].append({
                "text": text,
                "hash": h,
                "source_dataset": p["source_dataset"],
            })
            all_known.add(h)

    total_candidates = sum(len(v) for v in candidates.values())
    print(f"      {total_candidates} Kandidaten gefunden")
    print(f"      Uebersprungen: {skipped_dup} Duplikate, {skipped_quality} Qualitaet, {skipped_nocat} ohne Kategorie")

    # 4. Gleichmaessig auf Kategorien verteilen
    print("[4/5] Verteile auf Kategorien...")
    per_cat = max(2, MAX_PROMPTS // len(CATEGORY_RULES))
    selected = []

    for cat in sorted(candidates.keys()):
        cat_list = candidates[cat][:per_cat]
        for p in cat_list:
            p["category"] = cat
            selected.append(p)

    # Auffuellen wenn noetig
    if len(selected) < MAX_PROMPTS:
        for cat in candidates:
            remaining = candidates[cat][per_cat:]
            for p in remaining:
                if len(selected) >= MAX_PROMPTS:
                    break
                p["category"] = cat
                selected.append(p)

    selected = selected[:MAX_PROMPTS]

    cat_summary = {}
    for p in selected:
        cat_summary[p["category"]] = cat_summary.get(p["category"], 0) + 1
    for cat, count in sorted(cat_summary.items()):
        print(f"      {CAT_DISPLAY.get(cat, cat)}: {count}")

    if not selected:
        print("\n[5/5] Keine neuen Prompts gefunden.")
        print(f"\nFertig! 0 neue Prompts importiert.")
        return 0

    # 5. Dateien erstellen
    print(f"\n[5/5] Erstelle {len(selected)} Prompt-Dateien...")
    next_id = get_next_id()
    new_prompts = []

    for p in selected:
        title = extract_title(p["text"])
        tags = generate_tags(p["text"])
        create_prompt_file(
            next_id, title, p["text"], p["category"], tags, p["source_dataset"]
        )
        slug = slugify(title)
        filename = f"{next_id:03d}-{slug}.md"

        new_prompts.append({
            "id": next_id,
            "title": title,
            "category": p["category"],
            "filename": filename,
            "hash": p["hash"],
        })

        known_hashes.add(p["hash"])
        print(f"      + #{next_id:03d} {title[:45]} -> {p['category']}")
        next_id += 1

    # 6. CREDITS.md und Tracking
    if new_prompts and not DRY_RUN:
        update_credits(new_prompts, next_id)
        imported_data["hashes"] = sorted(known_hashes)
        imported_data["last_run"] = TODAY
        imported_data["last_count"] = len(new_prompts)
        imported_data["total_imported"] = imported_data.get("total_imported", 0) + len(new_prompts)
        save_imported(imported_data)

        log = {
            "imported_count": len(new_prompts),
            "categories": cat_summary,
            "date": TODAY,
            "dry_run": DRY_RUN,
        }
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        LOG_FILE.write_text(json.dumps(log, indent=2), encoding="utf-8")

    print(f"\nFertig! {len(new_prompts)} neue Prompts importiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
