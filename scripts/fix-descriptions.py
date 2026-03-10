#!/usr/bin/env python3
"""
Fix-Descriptions: Generiert individuelle Anwendungs- und Variationen-Texte
fuer alle importierten Prompts basierend auf dem Prompt-Inhalt.

Ersetzt die generischen Textbloecke durch kontextbezogene Beschreibungen.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KATEGORIEN_DIR = REPO_ROOT / "kategorien"

# ── Themen-Erkennung fuer bessere Beschreibungen ─────────────

TOPIC_TEMPLATES = {
    # (keywords) -> (anwendung_text, variationen_list)
    "rezept": {
        "keywords": ["recipe", "cook", "bake", "ingredient", "meal", "dish", "food", "sauce", "soup"],
        "anwendung": "Perfekt fuer alle, die neue Rezeptideen suchen oder ihre Kochkuenste erweitern wollen. "
                     "Die KI erstellt ein vollstaendiges Rezept mit Zutaten und Anleitung.",
        "tipps": [
            "Ersetze Zutaten durch das, was du im Kuehlschrank hast",
            "Fuege \"fuer [X] Personen\" hinzu fuer angepasste Mengen",
            "Frage nach einer veganen/vegetarischen Alternative",
            "Bitte um Naehrwertangaben pro Portion",
        ],
    },
    "styling": {
        "keywords": ["style", "fashion", "outfit", "clothing", "wardrobe", "wear", "dress"],
        "anwendung": "Ideal fuer Mode-Inspiration und Outfit-Planung. "
                     "Die KI gibt dir personalisierte Styling-Tipps passend zu deinem Anlass.",
        "tipps": [
            "Beschreibe deinen Koerpertyp und Stil-Vorlieben fuer bessere Tipps",
            "Nenne ein konkretes Event (Bewerbungsgespraech, Date, Hochzeit)",
            "Frage nach Budget-freundlichen Alternativen",
            "Bitte um Farb-Kombinationsvorschlaege",
        ],
    },
    "steuern_finanzen": {
        "keywords": ["tax", "filing", "financial", "budget", "money", "invest", "saving", "expense"],
        "anwendung": "Hilft bei Finanzfragen und gibt einen ersten Ueberblick. "
                     "Beachte: Fuer verbindliche Steuer- oder Finanzberatung immer einen Experten konsultieren.",
        "tipps": [
            "Nenne dein Land/Bundesland fuer lokale Steuerregeln",
            "Gib deine Einkommensklasse an fuer relevantere Tipps",
            "Frage nach konkreten Spar-Strategien fuer deine Situation",
            "Bitte um eine Schritt-fuer-Schritt-Checkliste",
        ],
    },
    "reise": {
        "keywords": ["travel", "trip", "vacation", "hotel", "flight", "destination", "itinerary", "tourist"],
        "anwendung": "Dein persoenlicher Reiseplaner. "
                     "Die KI erstellt massgeschneiderte Empfehlungen basierend auf deinen Wuenschen.",
        "tipps": [
            "Nenne dein Budget und die Reisedauer",
            "Gib an ob du Abenteuer, Erholung oder Kultur bevorzugst",
            "Frage nach Geheimtipps abseits der Touristenpfade",
            "Bitte um eine Packliste passend zum Reiseziel",
        ],
    },
    "hochzeit_event": {
        "keywords": ["wedding", "invitation", "party", "celebration", "event", "ceremony"],
        "anwendung": "Spart Zeit bei der Event-Planung. "
                     "Die KI generiert kreative Vorschlaege fuer Einladungen, Reden und Organisatorisches.",
        "tipps": [
            "Beschreibe den Stil der Feier (elegant, rustikal, modern)",
            "Nenne die Gaestezahl und das Budget",
            "Frage nach einem kompletten Zeitplan",
            "Bitte um verschiedene Stil-Varianten zum Vergleichen",
        ],
    },
    "email_brief": {
        "keywords": ["email", "letter", "write to", "manager", "colleague", "respond", "reply", "message"],
        "anwendung": "Spart Zeit beim Verfassen wichtiger Nachrichten. "
                     "Die KI formuliert professionelle E-Mails und Briefe im richtigen Ton.",
        "tipps": [
            "Beschreibe die Beziehung zum Empfaenger (Chef, Kunde, Kollege)",
            "Gib den gewuenschten Ton an: formell, freundlich, oder bestimmt",
            "Nenne die Kernbotschaft in einem Satz",
            "Frage nach einer kuerzeren/laengeren Version",
        ],
    },
    "bewerbung_karriere": {
        "keywords": ["resume", "cover letter", "interview", "career", "job", "hiring", "linkedin", "portfolio"],
        "anwendung": "Unterstuetzt dich bei der Jobsuche und Karriereplanung. "
                     "Die KI erstellt professionelle Bewerbungsunterlagen und Vorbereitungen.",
        "tipps": [
            "Nenne die konkrete Stellenausschreibung oder Branche",
            "Beschreibe deine bisherige Erfahrung in Stichpunkten",
            "Frage nach branchenspezifischen Keywords fuer den Lebenslauf",
            "Bitte um Uebungsfragen fuers Vorstellungsgespraech",
        ],
    },
    "business_startup": {
        "keywords": ["business", "startup", "entrepreneur", "company", "venture", "trading", "futures", "market"],
        "anwendung": "Unterstuetzt bei der Geschaeftsplanung und Unternehmensgruendung. "
                     "Die KI liefert strukturierte Analysen und Strategievorschlaege.",
        "tipps": [
            "Beschreibe deine Branche und Zielgruppe",
            "Nenne dein Startkapital oder Budget",
            "Frage nach einer SWOT-Analyse fuer deine Idee",
            "Bitte um einen konkreten Aktionsplan mit Meilensteinen",
        ],
    },
    "gesundheit_fitness": {
        "keywords": ["health", "fitness", "workout", "exercise", "nutrition", "diet", "weight", "body",
                     "supplement", "vitamin", "protein", "lysine", "amino"],
        "anwendung": "Gibt einen ersten Ueberblick zu Gesundheits- und Fitnessthemen. "
                     "Beachte: Ersetzt keine aerztliche Beratung — bei Beschwerden immer zum Arzt.",
        "tipps": [
            "Nenne dein Fitnesslevel und eventuelle Einschraenkungen",
            "Gib dein konkretes Ziel an (Muskelaufbau, Ausdauer, Abnehmen)",
            "Frage nach einem Wochenplan statt einzelner Tipps",
            "Bitte um wissenschaftliche Quellen fuer die Empfehlungen",
        ],
    },
    "mental_health": {
        "keywords": ["meditation", "mindful", "stress", "anxiety", "depression", "sleep", "wellbeing",
                     "self-care", "mental", "therapy", "breathing"],
        "anwendung": "Bietet Anregungen fuer mehr Wohlbefinden und Achtsamkeit im Alltag. "
                     "Bei ernsthaften psychischen Problemen bitte professionelle Hilfe suchen.",
        "tipps": [
            "Beschreibe deine aktuelle Situation in ein paar Worten",
            "Frage nach einer gefuehrten Meditation als Text",
            "Bitte um eine Morgen- oder Abendroutine",
            "Frage nach wissenschaftlich fundierten Techniken",
        ],
    },
    "kreatives_schreiben": {
        "keywords": ["story", "write a", "creative", "fiction", "novel", "poem", "character", "diary",
                     "imagine", "narrative", "tale"],
        "anwendung": "Perfekt fuer kreative Schreibprojekte und Inspiration. "
                     "Die KI generiert Texte in verschiedenen Genres und Stilen.",
        "tipps": [
            "Gib Genre und Stimmung an (lustig, dunkel, romantisch)",
            "Nenne eine gewuenschte Wortanzahl",
            "Frage nach alternativen Enden oder Perspektiven",
            "Bitte die KI, im Stil eines bestimmten Autors zu schreiben",
        ],
    },
    "musik_unterhaltung": {
        "keywords": ["song", "music", "lyric", "film", "movie", "book", "recommend", "playlist",
                     "album", "artist", "band"],
        "anwendung": "Dein persoenlicher Kultur- und Unterhaltungsberater. "
                     "Die KI empfiehlt passende Medien basierend auf deinem Geschmack.",
        "tipps": [
            "Nenne 2-3 Beispiele die dir gefallen fuer bessere Empfehlungen",
            "Gib die gewuenschte Stimmung an (energetisch, entspannt, melancholisch)",
            "Frage nach weniger bekannten Geheimtipps",
            "Bitte um eine sortierte Top-10-Liste mit Begruendung",
        ],
    },
    "programmierung": {
        "keywords": ["code", "program", "software", "develop", "python", "javascript", "html", "api",
                     "database", "algorithm", "function", "debug", "testing", "deploy", "git"],
        "anwendung": "Hilft bei Programmier-Fragen von Anfaenger bis Fortgeschritten. "
                     "Die KI erklaert Konzepte, schreibt Code und hilft beim Debugging.",
        "tipps": [
            "Nenne die Programmiersprache und Version",
            "Beschreibe den Kontext: Lernprojekt, Arbeit, oder Hobby",
            "Frage nach Code-Beispielen mit Kommentaren",
            "Bitte um Best Practices und haeufige Fehlerquellen",
        ],
    },
    "technik_digital": {
        "keywords": ["computer", "smartphone", "tech", "digital", "excel", "spreadsheet",
                     "wordpress", "seo", "website", "troubleshoot", "error", "security", "password"],
        "anwendung": "Loest technische Alltagsprobleme und erklaert digitale Werkzeuge. "
                     "Ideal fuer alle, die sich mit Technik besser zurechtfinden wollen.",
        "tipps": [
            "Nenne dein Betriebssystem und die Software-Version",
            "Beschreibe das Problem so genau wie moeglich",
            "Frage nach einer Schritt-fuer-Schritt-Anleitung mit Screenshots-Beschreibung",
            "Bitte um Alternativen zu deinem aktuellen Tool",
        ],
    },
    "lernen_bildung": {
        "keywords": ["explain", "learn", "study", "education", "teach", "tutor", "course",
                     "history", "science", "math", "physics", "summarize", "compare"],
        "anwendung": "Dein persoenlicher Nachhilfelehrer fuer jedes Thema. "
                     "Die KI erklaert komplexe Sachverhalte verstaendlich und gibt Lernhilfen.",
        "tipps": [
            "Gib dein Vorwissensniveau an (Anfaenger, Fortgeschritten, Experte)",
            "Frage nach Analogien und Alltagsbeispielen",
            "Bitte um Uebungsaufgaben mit Loesungen",
            "Frage nach weiterfuehrenden Ressourcen und Buechern",
        ],
    },
    "sprache_uebersetzung": {
        "keywords": ["translat", "language", "grammar", "vocabulary", "english", "german", "spanish",
                     "french", "sentence", "word"],
        "anwendung": "Hilft beim Sprachenlernen und Uebersetzen. "
                     "Die KI erklaert Grammatikregeln, uebersetzt Texte und gibt Uebungen.",
        "tipps": [
            "Nenne dein aktuelles Sprachniveau (A1-C2)",
            "Frage nach Beispielsaetzen fuer den Alltag",
            "Bitte um Erklaerungen von Redewendungen",
            "Frage nach Uebungen mit steigendem Schwierigkeitsgrad",
        ],
    },
    "recht_legal": {
        "keywords": ["legal", "law", "contract", "rights", "lawyer", "court", "regulation"],
        "anwendung": "Gibt einen ersten Ueberblick zu rechtlichen Fragen. "
                     "Beachte: Keine Rechtsberatung — fuer verbindliche Auskuenfte einen Anwalt konsultieren.",
        "tipps": [
            "Nenne dein Land/Bundesland fuer die richtige Rechtslage",
            "Beschreibe die Situation in eigenen Worten",
            "Frage nach einer Checkliste deiner Rechte und Pflichten",
            "Bitte um Erklaerung in einfacher Sprache ohne Juristendeutsch",
        ],
    },
    "religion_ethik": {
        "keywords": ["religion", "spiritual", "faith", "belief", "ethic", "moral", "buddhist",
                     "christian", "muslim", "philosophy", "meaning"],
        "anwendung": "Bietet Perspektiven zu ethischen, spirituellen und philosophischen Fragen. "
                     "Die KI stellt verschiedene Sichtweisen respektvoll dar.",
        "tipps": [
            "Nenne die Tradition oder Denkschule die dich interessiert",
            "Frage nach verschiedenen Perspektiven zu einem Thema",
            "Bitte um praktische Uebungen oder Reflexionsfragen",
            "Frage nach Buchempfehlungen zum Vertiefen",
        ],
    },
    "umwelt_nachhaltigkeit": {
        "keywords": ["climate", "environment", "sustainab", "eco", "green", "recycl", "carbon",
                     "renewable", "pollution"],
        "anwendung": "Gibt praktische Tipps fuer einen nachhaltigeren Lebensstil. "
                     "Die KI liefert faktenbasierte Informationen zu Umweltthemen.",
        "tipps": [
            "Frage nach konkreten Massnahmen fuer deinen Alltag",
            "Nenne dein Budget fuer nachhaltige Alternativen",
            "Bitte um einen Vergleich der Umweltauswirkungen",
            "Frage nach lokalen Initiativen und Moeglichkeiten",
        ],
    },
    "kommunikation": {
        "keywords": ["conversation", "dialog", "discuss", "persuade", "argue", "debate",
                     "feedback", "conflict", "relationship", "social"],
        "anwendung": "Verbessert deine Kommunikationsfaehigkeiten in verschiedenen Situationen. "
                     "Die KI gibt Formulierungshilfen und Gespraechsstrategien.",
        "tipps": [
            "Beschreibe die konkrete Situation und die Beziehung",
            "Nenne das gewuenschte Ergebnis des Gespraechs",
            "Frage nach verschiedenen Formulierungsvorschlaegen",
            "Bitte um Tipps fuer Koerpersprache und Tonfall",
        ],
    },
    "bild_prompt": {
        "keywords": ["image", "photo", "picture", "visual", "generate", "dall-e", "midjourney",
                     "illustration", "render", "3d", "isometric", "portrait", "landscape",
                     "art style", "digital art", "painting"],
        "anwendung": "Generiert beeindruckende KI-Bilder mit optimierten Beschreibungen. "
                     "Kopiere den Prompt in ChatGPT (DALL-E), Midjourney oder andere Bild-KIs.",
        "tipps": [
            "Aendere Farben, Stimmung oder Beleuchtung nach Wunsch",
            "Fuege \"--ar 16:9\" (Midjourney) oder Formatangaben hinzu",
            "Ersetze das Hauptmotiv durch dein eigenes Thema",
            "Kombiniere verschiedene Stile (z.B. \"watercolor meets cyberpunk\")",
        ],
    },
}

# Fallback fuer nicht-erkannte Themen
FALLBACK_TEMPLATES = {
    "alltag-leben": {
        "anwendung": "Ein praktischer Alltagshelfer. Kopiere den Prompt und passe ihn an deine persoenliche Situation an.",
        "tipps": [
            "Fuege konkrete Details zu deiner Situation hinzu",
            "Frage nach einer Schritt-fuer-Schritt-Anleitung",
            "Bitte um Alternativen und Vergleiche",
            "Aendere die Sprache auf Deutsch fuer lokale Ergebnisse",
        ],
    },
    "beruf-karriere": {
        "anwendung": "Unterstuetzt dich bei beruflichen Herausforderungen. Passe den Prompt an deine Branche und Position an.",
        "tipps": [
            "Nenne deine Branche und Berufserfahrung",
            "Gib die Unternehmensgroesse und -kultur an",
            "Frage nach konkreten Formulierungsbeispielen",
            "Bitte um eine professionelle und eine lockere Version",
        ],
    },
    "lernen-wachstum": {
        "anwendung": "Erweitert dein Wissen zu diesem Thema. Die KI erklaert verstaendlich und gibt Lernressourcen.",
        "tipps": [
            "Gib dein Vorwissen an fuer passende Erklaerungen",
            "Frage nach Beispielen aus dem Alltag",
            "Bitte um eine Zusammenfassung in 3 Saetzen",
            "Frage nach weiterführenden Quellen",
        ],
    },
    "kommunikation-beziehungen": {
        "anwendung": "Hilft bei der Formulierung und Kommunikation. Passe Ton und Kontext an deine Situation an.",
        "tipps": [
            "Beschreibe die Beziehung zum Gegenueber",
            "Nenne den gewuenschten Ton (formell, locker, bestimmt)",
            "Frage nach verschiedenen Formulierungsvarianten",
            "Bitte um Feedback zu deinem eigenen Textentwurf",
        ],
    },
    "kreativitaet-freizeit": {
        "anwendung": "Fuer kreative Projekte und Freizeitgestaltung. Lass dich inspirieren und passe den Output an deinen Stil an.",
        "tipps": [
            "Nenne Genre, Stimmung und Zielgruppe",
            "Frage nach verschiedenen Stil-Varianten",
            "Bitte um laengere oder kuerzere Versionen",
            "Kombiniere mit eigenen Ideen fuer einzigartige Ergebnisse",
        ],
    },
    "gesundheit-wohlbefinden": {
        "anwendung": "Gibt Anregungen fuer Gesundheit und Wohlbefinden. Beachte: Bei Beschwerden immer einen Arzt konsultieren.",
        "tipps": [
            "Nenne dein Alter und Fitnesslevel",
            "Beschreibe eventuelle Einschraenkungen",
            "Frage nach einem personalisierten Plan",
            "Bitte um wissenschaftlich fundierte Informationen",
        ],
    },
    "technik-alltag": {
        "anwendung": "Erklaert technische Konzepte und loest digitale Probleme. Ideal fuer Einsteiger und Fortgeschrittene.",
        "tipps": [
            "Nenne deine technische Erfahrung",
            "Gib Betriebssystem und Version an",
            "Frage nach konkreten Code-Beispielen",
            "Bitte um eine Erklaerung fuer Anfaenger",
        ],
    },
    "spezielle-situationen": {
        "anwendung": "Hilft in besonderen Lebenssituationen mit strukturierten Informationen und Handlungsempfehlungen.",
        "tipps": [
            "Beschreibe deine konkrete Situation",
            "Nenne dein Land fuer relevante Informationen",
            "Frage nach einer Checkliste der naechsten Schritte",
            "Bitte um verschiedene Szenarien und Optionen",
        ],
    },
    "bildbearbeitung-visualisierung": {
        "anwendung": "Generiert KI-Bilder in diesem Stil. Kopiere den Prompt in ChatGPT (DALL-E), Midjourney oder Stable Diffusion.",
        "tipps": [
            "Aendere Farben und Stimmung nach Wunsch",
            "Ersetze das Hauptmotiv durch dein eigenes Thema",
            "Fuege Stil-Modifikatoren hinzu (z.B. \"cinematic\", \"minimalist\")",
            "Experimentiere mit verschiedenen Bildformaten",
        ],
    },
}


def detect_topic(prompt_text: str, kategorie: str = "") -> dict:
    """Findet das passendste Themen-Template fuer einen Prompt.
    Beruecksichtigt auch die Kategorie aus dem Ordnernamen."""
    text_lower = prompt_text.lower()
    best_topic = None
    best_score = 0

    # Kategorie-basierte Bonus-Mappings
    cat_bonus = {
        "bildbearbeitung": "bild_prompt",
        "visualisierung": "bild_prompt",
    }

    bonus_topic = None
    for cat_kw, topic_id in cat_bonus.items():
        if cat_kw in kategorie.lower():
            bonus_topic = topic_id
            break

    for topic_id, template in TOPIC_TEMPLATES.items():
        score = 0
        for kw in template["keywords"]:
            if kw in text_lower:
                score += len(kw)
        # Bonus wenn Kategorie passt
        if topic_id == bonus_topic:
            score += 50
        if score > best_score:
            best_score = score
            best_topic = template

    return best_topic


def extract_key_phrases(prompt_text: str) -> list:
    """Extrahiert 2-3 inhaltliche Schluesselbegriffe aus dem Prompt."""
    text = prompt_text[:400]

    # Stoppwoerter die KEINE Themen-Keywords sind
    stop = {
        "write", "create", "generate", "make", "give", "provide", "include",
        "explain", "describe", "tell", "help", "please", "imagine", "should",
        "could", "would", "will", "have", "this", "that", "what", "which",
        "where", "when", "some", "also", "your", "their", "these", "those",
        "given", "part", "definition", "task", "following", "based", "using",
        "need", "want", "like", "just", "about", "with", "from", "into",
        "been", "here", "there", "then", "than", "more", "most", "each",
        "such", "very", "well", "come", "take", "know", "first", "after",
        "does", "done", "being", "able", "must", "shall", "other", "only",
        "example", "reference", "sentence", "teacher", "detailed",
        "instructions", "input", "output", "reply", "answer", "question",
        "start", "information", "text", "word", "words", "length",
        "least", "below", "above", "between",
    }

    # 1. Zusammengesetzte Begriffe (2 Woerter) suchen
    bigrams = re.findall(r'\b([a-z]{3,}[ -][a-z]{3,})\b', text.lower())
    # 2. Einzelne inhaltliche Woerter
    words = re.findall(r'\b([a-z]{4,})\b', text.lower())

    seen = set()
    result = []

    # Zuerst Bigrams (informativer)
    for bg in bigrams:
        parts = re.split(r'[ -]', bg)
        if all(p not in stop for p in parts):
            phrase = bg.title()
            if phrase not in seen:
                seen.add(phrase)
                result.append(phrase)
        if len(result) >= 2:
            break

    # Dann Einzelwoerter auffuellen
    for w in words:
        if w not in stop and w not in seen and len(w) >= 4:
            seen.add(w)
            result.append(w.title())
        if len(result) >= 3:
            break

    return result


def generate_description(prompt_text: str, kategorie: str) -> tuple:
    """Generiert individuelle Anwendung + Variationen fuer einen Prompt."""
    topic = detect_topic(prompt_text, kategorie)
    key_phrases = extract_key_phrases(prompt_text)

    # Kontext-Zusatz aus Schluesselbegriffen (nur wenn sinnvoll)
    if key_phrases and len(key_phrases[0]) > 3:
        kontext = f"**Thema: {', '.join(key_phrases[:2])}** — "
    else:
        kontext = ""

    if topic:
        anwendung = kontext + topic["anwendung"]
        tipps = topic["tipps"]
    else:
        # Fallback pro Kategorie
        cat_key = kategorie.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
        # Map display name to folder name
        cat_map = {
            "alltag & leben": "alltag-leben",
            "beruf & karriere": "beruf-karriere",
            "lernen & wachstum": "lernen-wachstum",
            "kommunikation & beziehungen": "kommunikation-beziehungen",
            "kreativitaet & freizeit": "kreativitaet-freizeit",
            "kreativität & freizeit": "kreativitaet-freizeit",
            "gesundheit & wohlbefinden": "gesundheit-wohlbefinden",
            "technik & alltag": "technik-alltag",
            "spezielle situationen": "spezielle-situationen",
            "bildbearbeitung & visualisierung": "bildbearbeitung-visualisierung",
        }
        folder = cat_map.get(cat_key, "alltag-leben")
        fb = FALLBACK_TEMPLATES.get(folder, FALLBACK_TEMPLATES["alltag-leben"])
        anwendung = kontext + fb["anwendung"]
        tipps = fb["tipps"]

    return anwendung, tipps


def process_file(filepath: Path) -> bool:
    """Aktualisiert die Anwendung+Variationen einer Prompt-Datei."""
    content = filepath.read_text(encoding="utf-8")

    # Nur importierte Prompts
    if 'quelle:' not in content and 'unterkategorie: "Importiert"' not in content:
        return False

    # Prompt-Text extrahieren
    prompt_match = re.search(r'```\n(.*?)\n```', content, re.DOTALL)
    if not prompt_match:
        return False
    prompt_text = prompt_match.group(1)

    # Kategorie extrahieren
    cat_match = re.search(r'kategorie:\s*"([^"]+)"', content)
    kategorie = cat_match.group(1) if cat_match else "Alltag & Leben"

    # Neue Beschreibung generieren
    anwendung, tipps = generate_description(prompt_text, kategorie)

    # Alten Anwendungs-Block ersetzen
    new_anwendung = f"""## Anwendung

{anwendung}

Kopiere den Prompt und fuege ihn in ChatGPT, Claude oder Gemini ein.
Passe die Details an deine Beduerfnisse an.

## Variationen

- {tipps[0]}
- {tipps[1]}
- {tipps[2]}
- {tipps[3]}
"""

    # Ersetze alles ab "## Anwendung" bis Ende
    new_content = re.sub(
        r'## Anwendung\n.*',
        new_anwendung,
        content,
        flags=re.DOTALL
    )

    if new_content != content:
        filepath.write_text(new_content, encoding="utf-8")
        return True
    return False


def main():
    print("=== Fix-Descriptions: Individuelle Beschreibungen generieren ===\n")

    updated = 0
    skipped = 0
    errors = 0

    for md_file in sorted(KATEGORIEN_DIR.rglob("*.md")):
        try:
            if process_file(md_file):
                rel = md_file.relative_to(REPO_ROOT)
                print(f"  [OK] {rel}")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  [ERR] {md_file.name}: {e}")
            errors += 1

    print(f"\nFertig! {updated} aktualisiert, {skipped} uebersprungen, {errors} Fehler.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
