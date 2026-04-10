#!/usr/bin/env python3
"""
Lyra Prompts Sortierskript — Keyword/Anti-Word basierte Kategorisierung
Analysiert alle Prompts und verschiebt falsch einsortierte Dateien.

Usage:
  python3 sort-prompts.py --dry-run    # Nur Report, keine Änderungen
  python3 sort-prompts.py --execute    # Tatsächlich verschieben + Frontmatter fix
"""

import os
import re
import sys
import shutil
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).parent / "kategorien"

# ─── KATEGORIE-ORDNER → Anzeigename ─────────────────────────────────
CAT_DISPLAY = {
    "alltag-leben": "Alltag & Leben",
    "beruf-karriere": "Beruf & Karriere",
    "bildbearbeitung-visualisierung": "Bildbearbeitung & KI-Visualisierung",
    "gesundheit-wohlbefinden": "Gesundheit & Wohlbefinden",
    "kommunikation-beziehungen": "Kommunikation & Beziehungen",
    "kreativitaet-freizeit": "Kreativitaet & Freizeit",
    "lernen-wachstum": "Lernen & Wachstum",
    "pro": "Pro — Premium",
    "spezielle-situationen": "Spezielle Situationen",
    "technik-alltag": "Technik & Alltag",
}

# ─── KEYWORD-REGELWERK ──────────────────────────────────────────────
# Jede Kategorie hat:
#   keywords: Wörter die FÜR diese Kategorie sprechen (Gewicht: +2 pro Treffer)
#   strong:   Starke Signale die fast sicher diese Kategorie bedeuten (+5)
#   anti:     Wörter die GEGEN diese Kategorie sprechen (-3 pro Treffer)

RULES = {
    "alltag-leben": {
        "strong": [
            "kochen", "rezept", "recipe", "haushalt", "putzen", "cleaning",
            "einkauf", "grocery", "haustier", "pet", "babysitter", "meal prep",
            "küche", "kitchen", "backen", "baking", "wohnung", "apartment",
            "renovier", "garten", "garden", "food critic", "chef", "personal shopper",
            "personal stylist", "restaurant", "budget tracker", "recipe finder",
            "automobile", "car mechanic", "travel guide", "reiseführer",
        ],
        "keywords": [
            "alltag", "daily", "haushalt", "household", "kochen", "cook",
            "rezept", "recipe", "essen", "food", "trinken", "drink",
            "einkauf", "shopping", "mode", "fashion", "kleidung", "clothes",
            "wohnung", "wohnen", "umzug", "moving", "miete", "rent",
            "tier", "animal", "pet", "hund", "katze", "garten",
            "reise", "travel", "urlaub", "vacation", "auto", "car",
            "familie", "family", "kinder", "children", "eltern", "parent",
            "geburtstag", "birthday", "hochzeit", "wedding", "feiern",
            "organisation", "planung", "planning", "routine",
            "stylist", "shopper", "decorator", "florist",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "algorithm",
            "machine learning", "neural", "database", "server", "docker",
            "kubernetes", "framework", "deploy", "git", "devops",
            "marketing", "seo", "startup", "investor", "pitch",
            "midjourney", "dall-e", "stable diffusion", "sdxl",
            "meditation", "therapie", "psycholog", "workout",
        ],
    },
    "beruf-karriere": {
        "strong": [
            "bewerbung", "job interview", "vorstellungsgespräch", "lebenslauf",
            "resume", "cover letter", "recruiter", "career counsel", "career coach",
            "salary", "gehalt", "startup idea", "ceo", "cto", "cfo",
            "product manager", "project manager", "accountant", "financial analyst",
            "investment manager", "real estate agent", "salesperson",
            "business plan", "geschäftsplan", "freelancer",
        ],
        "keywords": [
            "bewerbung", "karriere", "career", "job", "beruf", "profession",
            "gehalt", "salary", "interview", "recruiter", "manager",
            "leadership", "führung", "mitarbeiter", "employee", "team",
            "projekt", "management", "startup", "gründung", "unternehmen",
            "firma", "company", "business", "executive", "strategie",
            "meeting", "präsentation", "presentation", "pitch", "investor",
            "verkauf", "sales", "freelancer", "selbständig", "büro", "office",
            "arbeit", "work", "professional", "hire", "employ",
            "consultant", "lawyer", "anwalt", "logistik", "logistician",
            "kanban", "agile", "scrum", "pricing",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "code",
            "midjourney", "dall-e", "stable diffusion", "sdxl",
            "fitness", "workout", "meditation", "kochen", "rezept",
            "bild", "image", "photo", "portrait", "render",
        ],
    },
    "bildbearbeitung-visualisierung": {
        "strong": [
            "midjourney", "dall-e", "stable diffusion", "sdxl", "flux",
            "portrait", "illustration", "3d render", "cinematic",
            "photography style", "diorama", "double exposure",
            "watercolor", "oil painting", "digital art", "concept art",
            "anime style", "hyperrealistic", "photorealistic",
            "bokeh", "lens", "camera", "isometric", "poster design",
            "food image", "product shot", "wallpaper", "aesthetic",
            "visual style", "art style", "image prompt",
            "botanical illustration", "vintage illustration",
            "comic style", "comic stil", "marvel", "superhero art",
        ],
        "keywords": [
            "bild", "image", "photo", "art", "visual", "portrait",
            "illustration", "design", "3d", "render", "cinematic",
            "photography", "painting", "draw", "sketch", "style",
            "aesthetic", "camera", "lens", "lighting", "composition",
            "color palette", "texture", "poster", "wallpaper",
            "anime", "cartoon", "realistic", "4k", "8k", "hdr",
            "landscape", "fashion photo", "miniature", "diorama",
            "exploded view", "urban", "vintage", "retro",
            "surreal", "fantasy art", "sci-fi art",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "code",
            "programming", "develop", "build a", "create a web",
            "create an app", "implement", "function", "class",
            "database", "sql", "server", "deploy", "framework",
            "bewerbung", "karriere", "fitness", "meditation",
            "three.js", "canvas api", "react", "angular", "vue",
        ],
    },
    "gesundheit-wohlbefinden": {
        "strong": [
            "fitness", "workout", "personal trainer", "ernährung", "nutrition",
            "diät", "diet", "kalorien", "calorie", "yoga", "meditation",
            "achtsamkeit", "mindfulness", "mental health", "psycholog",
            "therapie", "therapy", "stress", "burnout", "schlaf", "sleep",
            "wellness", "arzt", "doctor", "dentist", "krankheit", "disease",
            "symptom", "medizin", "medicine", "healing", "heilung",
            "self-care", "selbstfürsorge", "ayurveda", "hypnotherap",
            "nutritionist", "dietitian", "health metric",
        ],
        "keywords": [
            "gesundheit", "health", "fitness", "sport", "training",
            "exercise", "übung", "ernährung", "abnehmen", "gewicht",
            "weight", "mental", "psyche", "wohlbefinden", "wellbeing",
            "schmerz", "pain", "heilung", "recovery", "prävention",
            "prevention", "habit tracker", "diabetes", "blutdruck",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "code",
            "programming", "develop", "build a", "create a web",
            "seo", "marketing", "business", "bewerbung", "karriere",
            "midjourney", "dall-e", "stable diffusion",
            "pomodoro", "kanban", "project manage",
        ],
    },
    "kommunikation-beziehungen": {
        "strong": [
            "beziehung", "relationship", "partner", "freundschaft",
            "konflikt", "conflict", "verhandlung", "negotiation",
            "rhetorik", "rhetoric", "debate", "debater", "speech",
            "public speaking", "elocution", "motivational speak",
            "motivational coach", "social media manager",
            "social media influencer", "linkedin", "ghostwriter",
            "branding strategist", "seo specialist", "advertiser",
            "content creator", "journalist", "commentariat",
        ],
        "keywords": [
            "kommunikation", "communication", "gespräch", "conversation",
            "dialog", "beziehung", "relationship", "empathie", "empathy",
            "feedback", "email", "brief", "letter", "nachricht", "message",
            "social media", "netzwerk", "network", "influencer",
            "content", "blog", "newsletter", "seo", "marketing",
            "werbung", "advertising", "branding", "public relation",
            "smalltalk", "networking", "überzeugung", "persuasion",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "code",
            "programming", "develop", "build a", "create a web",
            "fitness", "meditation", "kochen", "rezept",
            "midjourney", "dall-e", "stable diffusion",
            "bewerbung", "resume", "cover letter", "lebenslauf",
        ],
    },
    "kreativitaet-freizeit": {
        "strong": [
            "storyteller", "story", "geschichten", "novelist", "roman",
            "screenwriter", "drehbuch", "poet", "gedicht", "poem",
            "rapper", "composer", "songwriter", "comedian", "stand-up",
            "magician", "ascii art", "text adventure", "game",
            "quiz", "rätsel", "puzzle", "trivia", "brettspiel",
            "movie critic", "film critic", "music", "song",
            "diy", "basteln", "hobby", "makeup artist",
            "interior decorator", "florist", "artist advisor",
            "aphorism", "football commentator",
        ],
        "keywords": [
            "kreativ", "creative", "geschichte", "story", "schreiben",
            "writing", "roman", "novel", "gedicht", "poem", "poetry",
            "song", "musik", "music", "lied", "rap", "comedy", "humor",
            "witz", "joke", "spiel", "game", "quiz", "rätsel", "puzzle",
            "hobby", "basteln", "diy", "kunst", "art", "film", "movie",
            "serie", "buch", "book", "theater", "abenteuer", "adventure",
            "fantasy", "science fiction", "charakter", "character",
            "plot", "roleplay", "fiktion", "fiction",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "code",
            "programming", "database", "server", "deploy",
            "bewerbung", "karriere", "marketing", "seo",
            "fitness", "workout", "meditation",
            "midjourney", "dall-e", "stable diffusion", "sdxl",
            "cinematic", "hyperrealistic", "photorealistic",
        ],
    },
    "lernen-wachstum": {
        "strong": [
            "teacher", "lehrer", "tutor", "professor", "education",
            "school", "schule", "university", "universität", "studium",
            "course", "kurs", "tutorial", "language tutor", "translator",
            "übersetzer", "grammar", "grammatik", "vocabulary", "vokabel",
            "math", "mathematik", "physik", "physics", "chemie", "chemistry",
            "biolog", "histor", "philosophy", "philosophie",
            "exam", "prüfung", "homework", "hausaufgabe",
            "learning", "teaching", "curriculum",
        ],
        "keywords": [
            "lernen", "learn", "bildung", "education", "wissen", "knowledge",
            "forschung", "research", "wissenschaft", "science",
            "sprache", "language", "übersetzen", "translate",
            "analyse", "analysis", "critical thinking", "denken",
            "skill", "fähigkeit", "weiterbildung", "zertifikat",
            "roadmap", "prompt generator", "ai model", "llm",
        ],
        "anti": [
            "midjourney", "dall-e", "stable diffusion", "sdxl",
            "kochen", "rezept", "recipe", "cook", "food",
            "fitness", "workout", "meditation",
            "bewerbung", "karriere",
        ],
    },
    "spezielle-situationen": {
        "strong": [
            "notfall", "emergency", "krise", "crisis", "legal",
            "rechtlich", "anwalt", "lawyer", "gericht", "court",
            "versicherung", "insurance", "beschwerde", "complaint",
            "auswandern", "immigration", "emigration", "todesfall",
            "trauer", "grief", "scheidung", "divorce", "trennung",
            "unfall", "accident", "erste hilfe", "first aid",
            "mobbing", "bullying", "diskriminierung", "discrimination",
            "fallacy finder", "historian", "astrologer",
            "emergency response", "talent coach",
        ],
        "keywords": [
            "notfall", "emergency", "krise", "crisis", "recht", "legal",
            "gericht", "court", "versicherung", "insurance",
            "beschwerde", "complaint", "auswandern", "immigration",
            "trauer", "grief", "scheidung", "divorce",
            "sicherheit", "safety", "betrug", "fraud",
            "ethik", "ethics", "moral", "dilemma",
            "swot", "risk", "political",
        ],
        "anti": [
            "python", "javascript", "html", "css", "api", "code",
            "midjourney", "dall-e", "stable diffusion",
            "kochen", "rezept", "fitness", "workout",
        ],
    },
    "technik-alltag": {
        "strong": [
            "python", "javascript", "typescript", "java", "c++", "rust",
            "golang", "html", "css", "react", "angular", "vue", "node",
            "api", "rest", "graphql", "database", "sql", "nosql",
            "server", "cloud", "aws", "azure", "docker", "kubernetes",
            "git", "devops", "ci/cd", "algorithm", "data structure",
            "machine learning", "neural network", "deep learning",
            "automation", "terminal", "linux", "shell", "regex",
            "cyber security", "encryption", "blockchain", "web develop",
            "software", "developer", "engineer", "framework",
            "three.js", "canvas", "tensorflow", "pytorch",
            "excel sheet", "sql terminal", "smart domain",
            "tech reviewer", "tech writer", "it expert", "it architect",
        ],
        "keywords": [
            "code", "programming", "coding", "script", "debug", "test",
            "deploy", "security", "hacking", "web", "app", "software",
            "backend", "frontend", "fullstack", "compiler", "interpreter",
            "browser", "extension", "plugin", "cli", "command line",
            "data", "analytics", "scraping", "crawler",
            "image editor", "video editor",  # tools, not art
        ],
        "anti": [
            "kochen", "rezept", "recipe", "cook", "food",
            "fitness", "meditation", "yoga", "wellness",
            "beziehung", "relationship", "partner",
            "midjourney", "dall-e", "stable diffusion", "sdxl",
            "portrait", "cinematic", "hyperrealistic", "photorealistic",
            "oil painting", "watercolor", "illustration style",
        ],
    },
}

# ─── PRO wird nicht umsortiert (manuell kuratiert) ──────────────────
# Pro-Prompts bleiben wo sie sind.


def read_frontmatter(filepath):
    """Liest Frontmatter und ersten Teil des Prompt-Body."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read(4000)  # Nur erste 4KB lesen
    except Exception:
        return None, ""

    fm = {}
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        for line in fm_match.group(1).split("\n"):
            m = re.match(r'^([^:]+):\s*(.+)$', line)
            if m:
                key = m.group(1).strip()
                val = m.group(2).strip().strip('"').strip("'")
                if val.startswith("[") and val.endswith("]"):
                    val = [x.strip().strip('"').strip("'")
                           for x in val[1:-1].split(",") if x.strip()]
                fm[key] = val

    body = content[fm_match.end():] if fm_match else content
    return fm, body.lower()


def score_category(text, cat_key):
    """Berechnet Score für eine Kategorie basierend auf Keywords."""
    if cat_key == "pro" or cat_key not in RULES:
        return -999

    rules = RULES[cat_key]
    score = 0
    text_lower = text.lower()

    for word in rules.get("strong", []):
        if word.lower() in text_lower:
            score += 5

    for word in rules.get("keywords", []):
        if word.lower() in text_lower:
            score += 2

    for word in rules.get("anti", []):
        if word.lower() in text_lower:
            score -= 3

    return score


def fix_frontmatter_kategorie(filepath, new_cat_folder):
    """Aktualisiert die kategorie im Frontmatter."""
    new_display = CAT_DISPLAY.get(new_cat_folder, new_cat_folder)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return False

    # Ersetze kategorie-Zeile
    new_content = re.sub(
        r'^(kategorie:\s*).*$',
        f'kategorie: "{new_display}"',
        content,
        count=1,
        flags=re.MULTILINE
    )

    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def analyze_all():
    """Analysiert alle Prompts und gibt Verschiebe-Vorschläge zurück."""
    moves = []  # (filepath, current_cat, suggested_cat, score_diff, title)
    stats = defaultdict(int)
    errors = []

    for cat_folder in sorted(BASE.iterdir()):
        if not cat_folder.is_dir():
            continue
        cat_key = cat_folder.name

        # Pro-Prompts nicht anfassen
        if cat_key == "pro":
            continue

        for md_file in sorted(cat_folder.glob("*.md")):
            stats["total"] += 1
            fm, body = read_frontmatter(md_file)
            if fm is None:
                errors.append(str(md_file))
                continue

            title = fm.get("titel", md_file.stem)
            if isinstance(title, list):
                title = " ".join(title)
            tags = fm.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]

            # Gesamttext für Scoring: Titel + Tags + Body
            search_text = f"{title} {' '.join(tags)} {body}"

            # Score für jede Kategorie berechnen
            scores = {}
            for candidate in RULES:
                scores[candidate] = score_category(search_text, candidate)

            current_score = scores.get(cat_key, 0)
            best_cat = max(scores, key=scores.get)
            best_score = scores[best_cat]

            # Nur verschieben wenn:
            # 1. Beste Kategorie != aktuelle
            # 2. Score-Differenz signifikant (mind. 6 Punkte)
            # 3. Bester Score ist positiv
            if best_cat != cat_key and best_score > current_score and (best_score - current_score) >= 6 and best_score > 0:
                moves.append((
                    md_file,
                    cat_key,
                    best_cat,
                    best_score - current_score,
                    title,
                    {k: v for k, v in sorted(scores.items(), key=lambda x: -x[1])[:3]}
                ))
                stats["to_move"] += 1
            else:
                stats["ok"] += 1

    return moves, stats, errors


def print_report(moves, stats, errors):
    """Druckt einen übersichtlichen Report."""
    print("=" * 70)
    print("  LYRA PROMPTS — SORTIER-REPORT")
    print("=" * 70)
    print(f"\n  Gesamt analysiert:  {stats['total']}")
    print(f"  Korrekt einsortiert: {stats['ok']}")
    print(f"  Falsch einsortiert:  {stats['to_move']}")
    if errors:
        print(f"  Fehler beim Lesen:   {len(errors)}")
    print()

    # Gruppiere nach Verschiebungsrichtung
    by_direction = defaultdict(list)
    for filepath, current, suggested, diff, title, scores in moves:
        by_direction[f"{current} → {suggested}"].append(
            (filepath.name, title, diff, scores)
        )

    for direction in sorted(by_direction, key=lambda d: -len(by_direction[d])):
        items = by_direction[direction]
        print(f"\n{'─' * 60}")
        print(f"  {direction}  ({len(items)} Prompts)")
        print(f"{'─' * 60}")
        for fname, title, diff, scores in sorted(items, key=lambda x: -x[2])[:20]:
            print(f"  [{diff:+d}] {title[:50]}")
            print(f"        Datei: {fname}")
            top3 = ", ".join(f"{k}={v}" for k, v in list(scores.items())[:3])
            print(f"        Scores: {top3}")
        if len(items) > 20:
            print(f"  ... und {len(items) - 20} weitere")

    # Zusammenfassung der Bewegungen
    print(f"\n{'=' * 70}")
    print("  ZUSAMMENFASSUNG DER VERSCHIEBUNGEN")
    print(f"{'=' * 70}")
    move_summary = defaultdict(lambda: defaultdict(int))
    for _, current, suggested, _, _, _ in moves:
        move_summary[current][suggested] += 1

    for source in sorted(move_summary):
        for target in sorted(move_summary[source], key=lambda t: -move_summary[source][t]):
            count = move_summary[source][target]
            print(f"  {source} → {target}: {count}")

    print(f"\n  TOTAL: {stats['to_move']} Prompts werden verschoben")
    print()


def execute_moves(moves):
    """Führt die tatsächlichen Verschiebungen durch."""
    moved = 0
    failed = 0

    for filepath, current_cat, new_cat, diff, title, _ in moves:
        new_dir = BASE / new_cat
        new_path = new_dir / filepath.name

        # Namenskollision vermeiden
        if new_path.exists():
            stem = filepath.stem
            suffix = filepath.suffix
            counter = 2
            while new_path.exists():
                new_path = new_dir / f"{stem}-{counter}{suffix}"
                counter += 1

        try:
            shutil.move(str(filepath), str(new_path))
            fix_frontmatter_kategorie(new_path, new_cat)
            moved += 1
        except Exception as e:
            print(f"  FEHLER: {filepath.name}: {e}")
            failed += 1

    print(f"\n  Verschoben: {moved}")
    print(f"  Fehler:     {failed}")
    return moved


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ("--dry-run", "--execute"):
        print("Usage:")
        print("  python3 sort-prompts.py --dry-run    # Nur Report")
        print("  python3 sort-prompts.py --execute    # Verschieben + Frontmatter fix")
        sys.exit(1)

    mode = sys.argv[1]

    print("\nAnalysiere alle Prompts...")
    moves, stats, errors = analyze_all()
    print_report(moves, stats, errors)

    if mode == "--execute":
        if not moves:
            print("Keine Verschiebungen nötig.")
            return

        print(f"\n  {len(moves)} Prompts werden jetzt verschoben...")
        count = execute_moves(moves)
        print(f"\n  Fertig! {count} Prompts neu sortiert.")
    else:
        print("  (Dry-Run — keine Änderungen. Mit --execute ausführen)")


if __name__ == "__main__":
    main()
