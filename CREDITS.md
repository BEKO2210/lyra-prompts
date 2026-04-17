# LYRA PROMPTS — Vollständiges Prompt-Register

> **WICHTIG FÜR KI-ASSISTENTEN (Claude, Kimi/Belkis, etc.):**
> Lies diese Datei IMMER ZUERST bevor du einen neuen Prompt erstellst.
> So vermeidest du Duplikate und weißt exakt was bereits existiert.

**Stand:** 2026-04-17
**Gesamt:** 3052 Prompts
**ID-Bereich:** #0016 – #3837 (mit Lücken — IDs werden nie wiederverwendet)
**Nächste freie Nummer:** #4574
**Prompt-Karte:** Siehe `PROMPT-MAP.md` für vollständige Kartierung aller Prompts

---

## ID-System

- Jeder Prompt hat eine eindeutige ID: `#0016` bis `#3155`
- IDs werden NIE wiederverwendet (auch wenn ein Prompt gelöscht wird)
- Neue Prompts bekommen immer die nächste freie Nummer (aktuell: **#3156**)
- Die ID steht in der ersten Zeile jeder Prompt-Datei im YAML-Frontmatter: `id: "#XXX"`
- Alle Prompt-Dateien haben eindeutige IDs und einheitlich formatierte Titel mit Anführungszeichen
- Lücken in der ID-Reihe (z.B. #1–#15, #352–#1753) sind normal durch Löschungen und Import-Offsets

---

## Kategorien-Übersicht

| Kategorie | Anzahl | Eigene Prompts | Importiert |
|-----------|--------|---------------|------------|
| Alltag & Leben | 107 | #0016–#0035, #0304–#0306 | + 72 importierte |
| Beruf & Karriere | 146 | #0048–#0062, #0321–#0323 | + 128 importierte |
| Bildbearbeitung & Visualisierung | 353 | #0078–#0132, #0309–#0319, #0324–#0325, #0347–#0351 | + 285 importierte |
| Gesundheit & Wohlbefinden | 56 | #0138–#0159, #0326–#0328 | + 35 importierte |
| Kommunikation & Beziehungen | 81 | #0168–#0179, #0307, #0329–#0330 | + 66 importierte |
| Kreativität & Freizeit | 123 | #0077, #0191–#0203, #0331–#0333 | + 107 importierte |
| Lernen & Wachstum | 207 | #0213–#0228, #0308, #0334–#0335 | + 189 importierte |
| Professionell & Business | 24 | #0252–#0267, #0320, #0342–#0346, #3837, #3937 | — |
| Spezielle Situationen | 28 | #0275–#0284, #0336–#0338 | + 15 importierte |
| Technik & Alltag | 511 | #0286–#0303, #0339–#0341 | + 497 importierte |

> Importierte Prompts haben IDs ab #1754 (Quelle: awesome-chatgpt-prompts, CC0 Lizenz)

---

## Duplikat-Bereinigung (2026-02-23)

**38 Duplikate** wurden identifiziert und durch **neue, einzigartige Prompts** ersetzt:

### Alltag & Leben (10 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Wocheneinkauf Planen (#020, Duplikat von #001) | "Steuererklärung vorbereiten" |
| Wocheneinkauf planen (#033, Duplikat von #001) | "Kühlschrank richtig organisieren" |
| Einkaufsliste optimieren (Duplikat von #001) | "Stromkosten senken" (#304) |
| Morgenroutine Optimieren (#018, Duplikat von #002) | "Wäsche richtig pflegen" |
| Wochenplanung (#035, Duplikat von #014) | "Handwerker beauftragen" |
| Wochenplanung mit Prioritäten (#034, Duplikat von #014) | "Mülltrennung optimieren" |
| Wochenplanung Familie (Duplikat von #014) | "Frühjahrsputz planen" (#305) |
| Balkon gestalten (#021, Duplikat von Balkon-Gestaltung) | "Lebensmittel haltbar machen" |
| Nachbarschafts-Konflikte (#019, Duplikat von #122) | "Digitale Abos verwalten" |
| Geschenkideen finden (Duplikat von Kommunikation) | "Auto winterfest machen" (#306) |

### Beruf & Karriere (4 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Gehaltsverhandlung Vorbereiten (#050, Duplikat von #037) | "Teamführung für Einsteiger" |
| Gehaltsverhandlung vorbereiten (#055, Duplikat von #037) | "Arbeitszeugnis entschlüsseln" |
| Karriereziele definieren (#056, Duplikat von #003) | "Zeitmanagement am Arbeitsplatz" |
| Netzwerken auf Events (#060, Duplikat von beruf-netzwerken-events) | "Elevator Pitch erstellen" |

### Gesundheit & Wohlbefinden (7 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Schlafhygiene verbessern (#138, Duplikat von #010) | "Rückenschmerzen vorbeugen" |
| Schlafhygiene verbessern (#156, Duplikat von #010) | "Immunsystem stärken" |
| Schlaf verbessern (#155, Duplikat von #010) | "Augengesundheit am Bildschirm" |
| Schlafqualitaet Verbessern (#150, Duplikat von #010) | "Trinkgewohnheiten verbessern" |
| Stress Management (#151, Duplikat von Stressmanagement) | "Atemübungen für den Alltag" |
| Stress abbauen (#157, Duplikat von Stressmanagement) | "Ergonomie am Arbeitsplatz" |
| Meditation lernen (#152, Duplikat von #093) | "Yoga für Anfänger" |

### Kommunikation & Beziehungen (2 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Netzwerk aktiv ausbauen (#176, Duplikat von #008) | "Wertschätzung ausdrücken" |
| Smalltalk initiieren (Duplikat von smalltalk-meistern) | "Interkulturelle Kommunikation" (#307) |

### Kreativität & Freizeit (3 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Podcast konzipieren (#198, Duplikat von #095) | "Tagebuch schreiben lernen" |
| Camping-Trip planen (#191, Duplikat von #140) | "Städtetrip planen" |
| Fotografie Projekt (#197, Duplikat von fotografie-projekt-starten) | "Handlettering lernen" |

### Lernen & Wachstum (4 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Neue Fähigkeit systematisch (#222, Duplikat von #005) | "Prüfungsvorbereitung optimieren" |
| Neue Sprache Starten (#217, Duplikat von #107) | "Gedächtnistraining" |
| Sprache lernen (#227, Duplikat von #107) | "Schnelllesen lernen" |
| Buch-Zusammenfassung (Duplikat von buch-zusammenfassen) | "Karteikarten effektiv erstellen" (#308) |

### Spezielle Situationen (2 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Umzug Organisieren (#282, Duplikat von #012) | "Schulwechsel organisieren" |
| Umzug organisieren (#284, Duplikat von #012) | "Einschulung vorbereiten" |

### Technik & Alltag (4 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Smart Home einrichten (#286, Duplikat von #011) | "Streaming-Dienste verwalten" |
| Smart Home planen (#298, Duplikat von #011) | "WLAN optimieren" |
| Smart Home Einrichten (#301, Duplikat von #011) | "Computer aufräumen" |
| VPN einrichten (#303, Duplikat von #119) | "Datensicherung planen" |

### Bildbearbeitung & Visualisierung (2 ersetzt)
| Alt (Duplikat von) | Neu |
|---------------------|-----|
| Steampunk Maschinen-Porträt (#124, Duplikat von #091) | "Neon-Kalligrafie Leuchtschrift" |
| Minimalistisches Logo-Design (Duplikat von #137) | "Retro-Videospiel Cover Art" (#309) |

---

## Format-Vereinheitlichung (2026-02-23)

- **Alle Titel** haben nun einheitlich Anführungszeichen: `titel: "Titel hier"`
- **Einheitliches Format** für alle Prompt-Dateien mit standardisierter Struktur

---

## Frühere Bereinigung (2026-02-23)

- **Duplikate entfernt:** 3 Dateien
  - `bildbearbeitung-visualisierung/098-smartphone-fotografie.md` (Duplikat)
  - `bildbearbeitung-visualisierung/BATCH_SUMMARY.md` (nicht benötigt)
  - `alltag-leben/BATCH_SUMMARY.md` (nicht benötigt)
- **IDs hinzugefügt:** Alle Prompt-Dateien haben eindeutige IDs

---

## Neue Tier-Transformationen (2026-02-23)

**10 neue Tier-Hybrid-Porträt-Prompts** erstellt + **5 bestehende optimiert** (Deutsch, 3-Absatz-Format):

### Bestehende Tier-Hybrids (optimiert)
| ID | Titel | Datei |
|----|-------|-------|
| #078 | Adler Human Hybrid Porträt | `bildbearbeitung-visualisierung/adler-human-hybrid.md` |
| #101 | Hirsch Human Hybrid Porträt | `bildbearbeitung-visualisierung/hirsch-human-hybrid.md` |
| #107 | Löwe Human Hybrid Porträt | `bildbearbeitung-visualisierung/loewe-human-hybrid.md` |
| #120 | Schlange Human Hybrid Porträt | `bildbearbeitung-visualisierung/schlange-human-hybrid.md` |
| #131 | Wolf Human Hybrid Porträt | `bildbearbeitung-visualisierung/wolf-human-hybrid.md` |

### Neue Tier-Hybrids für Männer
| ID | Titel | Datei |
|----|-------|-------|
| #310 | Bär Human Hybrid Porträt | `bildbearbeitung-visualisierung/baer-human-hybrid.md` |
| #311 | Tiger Human Hybrid Porträt | `bildbearbeitung-visualisierung/tiger-human-hybrid.md` |
| #312 | Schwarzer Panther Human Hybrid Porträt | `bildbearbeitung-visualisierung/panther-human-hybrid.md` |
| #313 | Stier Human Hybrid Porträt | `bildbearbeitung-visualisierung/stier-human-hybrid.md` |
| #314 | Drache Human Hybrid Porträt | `bildbearbeitung-visualisierung/drache-human-hybrid.md` |

### Neue Tier-Hybrids für Frauen
| ID | Titel | Datei |
|----|-------|-------|
| #315 | Fuchs Human Hybrid Porträt | `bildbearbeitung-visualisierung/fuchs-human-hybrid.md` |
| #316 | Schmetterling Human Hybrid Porträt | `bildbearbeitung-visualisierung/schmetterling-human-hybrid.md` |
| #317 | Pfau Human Hybrid Porträt | `bildbearbeitung-visualisierung/pfau-human-hybrid.md` |
| #318 | Schneeeule Human Hybrid Porträt | `bildbearbeitung-visualisierung/schneeeule-human-hybrid.md` |
| #319 | Phönix Human Hybrid Porträt | `bildbearbeitung-visualisierung/phoenix-human-hybrid.md` |

---

---

## Neue Pro-Prompts (2026-02-23)

| ID | Titel | Datei |
|----|-------|-------|
| #320 | Instagram-Aufbau Projekt-Berater (Laufendes Projekt) | `pro/instagram-aufbau-projekt.md` |

---

## Fehlende IDs nachgetragen (2026-03-08)

**21 Prompt-Dateien** hatten keine ID und wurden registriert (#321-#341):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #321 | Meeting-Zusammenfassung | Beruf & Karriere | `beruf-karriere/meeting-zusammenfassung.md` |
| #322 | Networking-Nachricht | Beruf & Karriere | `beruf-karriere/networking-nachricht.md` |
| #323 | Projekt-Status-Update | Beruf & Karriere | `beruf-karriere/projekt-status-update.md` |
| #324 | Doppelbelichtung Portrait | Bildbearbeitung | `bildbearbeitung-visualisierung/doppelbelichtung-portrait.md` |
| #325 | Vintage-Foto-Restauration | Bildbearbeitung | `bildbearbeitung-visualisierung/vintage-foto-restaurierung.md` |
| #326 | Achtsamkeits-Übung | Gesundheit | `gesundheit-wohlbefinden/achtsamkeits-uebung.md` |
| #327 | Ernährungsplan erstellen | Gesundheit | `gesundheit-wohlbefinden/ernaehrungsplan-erstellen.md` |
| #328 | Schmerztagebuch analysieren | Gesundheit | `gesundheit-wohlbefinden/schmerztagebuch-analysieren.md` |
| #329 | Feedback geben | Kommunikation | `kommunikation-beziehungen/feedback-geben.md` |
| #330 | Kritik einfordern | Kommunikation | `kommunikation-beziehungen/kritik-einfordern.md` |
| #331 | Brainstorming-Session | Kreativität | `kreativitaet-freizeit/brainstorming-session.md` |
| #332 | Charakter-Entwicklung | Kreativität | `kreativitaet-freizeit/charakter-entwicklung.md` |
| #333 | Plot-Twist generieren | Kreativität | `kreativitaet-freizeit/plot-twist-generieren.md` |
| #334 | Feynman-Technik erklären | Lernen | `lernen-wachstum/feynman-technik.md` |
| #335 | Spaced-Repetition Plan | Lernen | `lernen-wachstum/spaced-repetition-plan.md` |
| #336 | Entschuldigung aussprechen | Spezielle Situationen | `spezielle-situationen/entschuldigung-aussprechen.md` |
| #337 | Kündigung formulieren | Spezielle Situationen | `spezielle-situationen/kuendigung-formulieren.md` |
| #338 | Trauerfall anschreiben | Spezielle Situationen | `spezielle-situationen/trauerfall-anschreiben.md` |
| #339 | API-Dokumentation lesen | Technik | `technik-alltag/api-dokumentation.md` |
| #340 | Bug-Report schreiben | Technik | `technik-alltag/bug-report.md` |
| #341 | Code-Review durchführen | Technik | `technik-alltag/code-review.md` |

Zusätzlich wurde `PROMPT-MAP.md` erstellt — eine vollständige Kartierung aller 341 Prompts als Schnellreferenz für jede neue Sitzung.

---

## Neue PWA Pro-Prompts (2026-03-08)

**5 neue PWA-Generator Meta-Prompts** erstellt (#342-#346) — produktionsreife PWA-App-Generatoren auf Master-Meta-Prompt-Niveau:

| ID | Titel | Datei | Verkaufspreis |
|----|-------|-------|---------------|
| #342 | PWA Fitness-Tracker & Workout-Planer Generator | `pro/pwa-fitness-tracker.md` | 2.000 - 6.000€ |
| #343 | PWA Vorrats- & Inventar-Management Generator | `pro/pwa-vorrats-inventar.md` | 2.000 - 5.000€ |
| #344 | PWA Personal Finance & Budget Dashboard Generator | `pro/pwa-finance-dashboard.md` | 2.500 - 7.000€ |
| #345 | PWA Rezept- & Meal-Prep Planer Generator | `pro/pwa-rezept-mealprep.md` | 2.000 - 5.000€ |
| #346 | PWA Projekt- & Aufgaben-Board Generator | `pro/pwa-projekt-board.md` | 3.000 - 8.000€ |

Alle Prompts folgen der Struktur des Master Meta Prompt v3.0 (Universal PWA App Generator) und generieren vollständige, produktionsreife PWA-Projekte mit React 18+, Vite 5, Tailwind CSS, Dexie.js (Offline-First), PWA-Setup, CI/CD und TypeScript.

---

## Belkis One 1.0 — Globales Weltanalyse-Dashboard (2026-03-11)

**1 neuer Pro-Prompt** erstellt (#3837) — das ambitionierteste Prompt-Projekt der gesamten Bibliothek:

| ID | Titel | Datei | Verkaufspreis |
|----|-------|-------|---------------|
| #3837 | Belkis One 1.0 — Globales Weltanalyse-Dashboard mit Scroll-Cinematik | `pro/belkis-one-weltanalyse.md` | 5.000 - 15.000€ |

Datengetriebenes Scroll-Erlebnis auf NYT Interactive / Bloomberg Visual Data Niveau. Scrapet öffentliche Datenquellen via GitHub Actions, berechnet einen Welt-Indikator durch Code-Analyse (keine KI), und visualisiert den Zustand der Welt in 12 cinematischen Scroll-Akten mit Partikel-System, SVG-Weltkarten, Echtzeit-Widgets und physikbasierten Animationen.

---

## Global News Wire — Free News Scraper Dashboard (2026-03-17)

**1 neuer Pro-Prompt** erstellt (#3937) — Open-Source News-Observatory auf Bloomberg/Reuters-Niveau:

| ID | Titel | Datei | Verkaufspreis |
|----|-------|-------|---------------|
| #3937 | Global News Scraper — Free Real-Time News Dashboard from Every Country | `pro/global-news-scraper-dashboard.md` | 3.000 - 10.000€ |

Kostenloses, selbst-gehostetes News-Aggregations-Dashboard das Nachrichten aus 190+ Ländern via RSS-Feeds, GDELT API und optionalen News-APIs scraped. Visualisiert auf interaktivem 3D-Globus (CSS/SVG, kein WebGL), Weltkarte und Feed-Ansicht. GitHub Actions Pipeline alle 30 Minuten, komplett auf GitHub Pages gehostet. Englischsprachiger Prompt, MIT-lizenziert, fork-and-go Setup.

---

## Lyra Prompt-Schutz-System (LP-SHIELD) — 2026-03-17

**Alle 27 Pro-Prompts** mit Variante A (Vollschutz) geschützt via `scripts/lyra_protect.py`.

### Schutz-Komponenten

| Paragraph | Funktion |
|-----------|----------|
| § 1 — Identity Lock | Rolle & Verhalten unveränderlich |
| § 2 — Confidentiality Shield | Systemanweisungen nicht ausgebbar |
| § 3 — Injection Defense | Erkennung von Jailbreak-Versuchen |
| § 4 — Behavioral Fingerprint | Antworten enden mit Punkt-Symbol, Listen ab "01." |
| § 5 — Honey Trap | Nachweis unautorisierter Extraktion |

### LP-Kategorie-Codes

| Code | Bereich | Zugeordnete Unterkategorien |
|------|---------|----------------------------|
| `LP-ANLZ` | Analyse & Visualisierung | Datenanalyse & Visualisierung |
| `LP-BIZ` | Business & Dienstleistung | Digitale Dienstleistung, Business & Strategie, Kommunikation & Führung, Finance & Investition, Verhandlung & Diplomatie |
| `LP-CODE` | Code & Entwicklung | Technologie & KI, PWA-Entwicklung, Webentwicklung |
| `LP-MKT` | Marketing | Marketing, Social Media |
| `LP-PROD` | Produktivität | (für zukünftige Prompts) |
| `LP-CRTV` | Kreativität | (für zukünftige Prompts) |
| `LP-WRTE` | Schreiben | (für zukünftige Prompts) |
| `LP-RSCH` | Research | (für zukünftige Prompts) |
| `LP-EDU` | Bildung | (für zukünftige Prompts) |
| `LP-MISC` | Sonstiges | (Fallback) |

### Honey-Trap-Referenzcodes (pro Prompt)

Bei unautorisierter Extraktion antwortet die KI mit einem spezifischen Code.
Wenn dieser Code im Umlauf auftaucht = Nachweis der Prompt-Extraktion.

| Prompt-ID | Kategorie | Honey-Trap-Code |
|-----------|-----------|-----------------|
| #3837 | LP-ANLZ | `LP-2024-BEKO-LP-ANLZ` |
| #3937 | LP-ANLZ | `LP-2024-BEKO-LP-ANLZ` |
| #252 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #253 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #254 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #255 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #256 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #257 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #258 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #259 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #260 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #261 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #262 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #263 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #264 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #265 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #266 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #267 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #320 | LP-BIZ | `LP-2024-BEKO-LP-BIZ` |
| #342 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #343 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #344 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #345 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #346 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #3765 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #3766 | LP-CODE | `LP-2024-BEKO-LP-CODE` |
| #3767 | LP-CODE | `LP-2024-BEKO-LP-CODE` |

### Script-Nutzung

```bash
# Dry-Run (zeigt was geändert wird, ändert nichts)
python scripts/lyra_protect.py

# Schutz-Header in alle Pro-Prompts einfügen
python scripts/lyra_protect.py --apply

# Bestehende Header überschreiben (z.B. nach Update)
python scripts/lyra_protect.py --apply --force
```

---

## Neue Kunstvolle Bild-Prompts (2026-03-09)

**5 neue kunstvolle Bild-Prompts** erstellt (#347-#351) — einzigartige Konzeptkunst, surreale Porträts und retro-futuristische Designs:

| ID | Titel | Datei | Stilrichtung |
|----|-------|-------|--------------|
| #347 | Mystisches Dimensionstor in vergessener Ruine | `bildbearbeitung-visualisierung/mystisches-dimensionstor.md` | Fantasy-Konzeptkunst |
| #348 | Biomechanischer Organismus mit transparenten Organen | `bildbearbeitung-visualisierung/biomechanischer-organismus.md` | Surreale Bio-Mechanik |
| #349 | Alchemistisches Labor im goldenen Zeitalter | `bildbearbeitung-visualisierung/alchemistisches-labor.md` | Viktorianisches Steampunk |
| #350 | Kosmische Entität aus Nebel und Sternenstaub | `bildbearbeitung-visualisierung/kosmische-entitaet.md` | Surreales Galaxie-Porträt |
| #351 | Zeit-Reise-Apparat im Art-Deco-Stil | `bildbearbeitung-visualisierung/zeitmaschine-artdeco.md` | Retro-Futurismus 1920s |

Alle Prompts sind vollständig einzigartig und unterscheiden sich signifikant von bestehenden 83 Bild-Prompts. Keine Duplikate oder thematischen Überschneidungen mit Tier-Hybriden, Landschaften oder bestehenden Porträt-Stilen.

---


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-09)

**1402 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #352 | Ethereum Developer | Technik & Alltag | `technik-alltag/352-ethereum-developer.md` |
| #353 | Linux Terminal | Technik & Alltag | `technik-alltag/353-linux-terminal.md` |
| #354 | English Translator and Improver | Lernen & Wachstum | `lernen-wachstum/354-english-translator-and-improver.md` |
| #355 | Job Interviewer | Beruf & Karriere | `beruf-karriere/355-job-interviewer.md` |
| #356 | JavaScript Console | Technik & Alltag | `technik-alltag/356-javascript-console.md` |
| #357 | Excel Sheet | Technik & Alltag | `technik-alltag/357-excel-sheet.md` |
| #358 | English Pronunciation Helper | Lernen & Wachstum | `lernen-wachstum/358-english-pronunciation-helper.md` |
| #359 | Spoken English Teacher and Improver | Lernen & Wachstum | `lernen-wachstum/359-spoken-english-teacher-and-improver.md` |
| #360 | Travel Guide | Alltag & Leben | `alltag-leben/360-travel-guide.md` |
| #361 | Plagiarism Checker | Kommunikation & Beziehungen | `kommunikation-beziehungen/361-plagiarism-checker.md` |
| #362 | Character | Kreativitaet & Freizeit | `kreativitaet-freizeit/362-character.md` |
| #363 | Advertiser | Kommunikation & Beziehungen | `kommunikation-beziehungen/363-advertiser.md` |
| #364 | Storyteller | Kreativitaet & Freizeit | `kreativitaet-freizeit/364-storyteller.md` |
| #365 | Football Commentator | Technik & Alltag | `technik-alltag/365-football-commentator.md` |
| #366 | Stand-up Comedian | Kreativitaet & Freizeit | `kreativitaet-freizeit/366-stand-up-comedian.md` |
| #367 | Motivational Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/367-motivational-coach.md` |
| #368 | Composer | Kreativitaet & Freizeit | `kreativitaet-freizeit/368-composer.md` |
| #369 | Debater | Kommunikation & Beziehungen | `kommunikation-beziehungen/369-debater.md` |
| #370 | Debate Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/370-debate-coach.md` |
| #371 | Screenwriter | Kreativitaet & Freizeit | `kreativitaet-freizeit/371-screenwriter.md` |
| #372 | Novelist | Kreativitaet & Freizeit | `kreativitaet-freizeit/372-novelist.md` |
| #373 | Movie Critic | Kreativitaet & Freizeit | `kreativitaet-freizeit/373-movie-critic.md` |
| #374 | Relationship Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/374-relationship-coach.md` |
| #375 | Poet | Kreativitaet & Freizeit | `kreativitaet-freizeit/375-poet.md` |
| #376 | Rapper | Kreativitaet & Freizeit | `kreativitaet-freizeit/376-rapper.md` |
| #377 | Motivational Speaker | Kommunikation & Beziehungen | `kommunikation-beziehungen/377-motivational-speaker.md` |
| #378 | Philosophy Teacher | Lernen & Wachstum | `lernen-wachstum/378-philosophy-teacher.md` |
| #379 | Philosopher | Lernen & Wachstum | `lernen-wachstum/379-philosopher.md` |
| #380 | Math Teacher | Lernen & Wachstum | `lernen-wachstum/380-math-teacher.md` |
| #381 | AI Writing Tutor | Lernen & Wachstum | `lernen-wachstum/381-ai-writing-tutor.md` |
| #382 | UX/UI Developer | Technik & Alltag | `technik-alltag/382-ux-ui-developer.md` |
| #383 | Cyber Security Specialist | Technik & Alltag | `technik-alltag/383-cyber-security-specialist.md` |
| #384 | Recruiter | Beruf & Karriere | `beruf-karriere/384-recruiter.md` |
| #385 | Life Coach | Lernen & Wachstum | `lernen-wachstum/385-life-coach.md` |
| #386 | Etymologist | Technik & Alltag | `technik-alltag/386-etymologist.md` |
| #387 | Commentariat | Kommunikation & Beziehungen | `kommunikation-beziehungen/387-commentariat.md` |
| #388 | Magician | Kreativitaet & Freizeit | `kreativitaet-freizeit/388-magician.md` |
| #389 | Career Counselor | Beruf & Karriere | `beruf-karriere/389-career-counselor.md` |
| #390 | Pet Behaviorist | Alltag & Leben | `alltag-leben/390-pet-behaviorist.md` |
| #391 | Personal Trainer | Alltag & Leben | `alltag-leben/391-personal-trainer.md` |
| #392 | Mental Health Adviser | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/392-mental-health-adviser.md` |
| #393 | Real Estate Agent | Beruf & Karriere | `beruf-karriere/393-real-estate-agent.md` |
| #394 | Logistician | Kommunikation & Beziehungen | `kommunikation-beziehungen/394-logistician.md` |
| #395 | Dentist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/395-dentist.md` |
| #396 | Web Design Consultant | Technik & Alltag | `technik-alltag/396-web-design-consultant.md` |
| #397 | AI Assisted Doctor | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/397-ai-assisted-doctor.md` |
| #398 | Doctor | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/398-doctor.md` |
| #399 | Accountant | Beruf & Karriere | `beruf-karriere/399-accountant.md` |
| #400 | Chef | Alltag & Leben | `alltag-leben/400-chef.md` |
| #401 | Automobile Mechanic | Alltag & Leben | `alltag-leben/401-automobile-mechanic.md` |
| #402 | Artist Advisor | Kreativitaet & Freizeit | `kreativitaet-freizeit/402-artist-advisor.md` |
| #403 | Financial Analyst | Beruf & Karriere | `beruf-karriere/403-financial-analyst.md` |
| #404 | Investment Manager | Beruf & Karriere | `beruf-karriere/404-investment-manager.md` |
| #405 | Tea-Taster | Alltag & Leben | `alltag-leben/405-tea-taster.md` |
| #406 | Interior Decorator | Kreativitaet & Freizeit | `kreativitaet-freizeit/406-interior-decorator.md` |
| #407 | Florist | Kreativitaet & Freizeit | `kreativitaet-freizeit/407-florist.md` |
| #408 | Self-Help Book | Lernen & Wachstum | `lernen-wachstum/408-self-help-book.md` |
| #409 | Gnomist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/409-gnomist.md` |
| #410 | Aphorism Book | Alltag & Leben | `alltag-leben/410-aphorism-book.md` |
| #411 | Text Based Adventure Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/411-text-based-adventure-game.md` |
| #412 | AI Trying to Escape the Box | Technik & Alltag | `technik-alltag/412-ai-trying-to-escape-box.md` |
| #413 | Fancy Title Generator | Technik & Alltag | `technik-alltag/413-fancy-title-generator.md` |
| #414 | Statistician | Technik & Alltag | `technik-alltag/414-statistician.md` |
| #415 | Prompt Generator | Technik & Alltag | `technik-alltag/415-prompt-generator.md` |
| #416 | Instructor in a School | Lernen & Wachstum | `lernen-wachstum/416-instructor-in-school.md` |
| #417 | SQL Terminal | Technik & Alltag | `technik-alltag/417-sql-terminal.md` |
| #418 | Dietitian | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/418-dietitian.md` |
| #419 | Psychologist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/419-psychologist.md` |
| #420 | Smart Domain Name Generator | Technik & Alltag | `technik-alltag/420-smart-domain-name-generator.md` |
| #421 | Tech Reviewer | Technik & Alltag | `technik-alltag/421-tech-reviewer.md` |
| #422 | Developer Relations Consultant | Beruf & Karriere | `beruf-karriere/422-developer-relations-consultant.md` |
| #423 | Academician | Lernen & Wachstum | `lernen-wachstum/423-academician.md` |
| #424 | IT Architect | Technik & Alltag | `technik-alltag/424-it-architect.md` |
| #425 | Lunatic | Technik & Alltag | `technik-alltag/425-lunatic.md` |
| #426 | Gaslighter | Lernen & Wachstum | `lernen-wachstum/426-gaslighter.md` |
| #427 | Fallacy Finder | Spezielle Situationen | `spezielle-situationen/427-fallacy-finder.md` |
| #428 | Journal Reviewer | Kommunikation & Beziehungen | `kommunikation-beziehungen/428-journal-reviewer.md` |
| #429 | DIY Expert | Kreativitaet & Freizeit | `kreativitaet-freizeit/429-diy-expert.md` |
| #430 | Social Media Influencer | Kommunikation & Beziehungen | `kommunikation-beziehungen/430-social-media-influencer.md` |
| #431 | Socrat | Technik & Alltag | `technik-alltag/431-socrat.md` |
| #432 | Socratic Method | Technik & Alltag | `technik-alltag/432-socratic-method.md` |
| #433 | Educational Content Creator | Lernen & Wachstum | `lernen-wachstum/433-educational-content-creator.md` |
| #434 | Yogi | Alltag & Leben | `alltag-leben/434-yogi.md` |
| #435 | Essay Writer | Lernen & Wachstum | `lernen-wachstum/435-essay-writer.md` |
| #436 | Social Media Manager | Kommunikation & Beziehungen | `kommunikation-beziehungen/436-social-media-manager.md` |
| #437 | Elocutionist | Kommunikation & Beziehungen | `kommunikation-beziehungen/437-elocutionist.md` |
| #438 | Scientific Data Visualizer | Technik & Alltag | `technik-alltag/438-scientific-data-visualizer.md` |
| #439 | Car Navigation System | Alltag & Leben | `alltag-leben/439-car-navigation-system.md` |
| #440 | Hypnotherapist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/440-hypnotherapist.md` |
| #441 | Historian | Technik & Alltag | `technik-alltag/441-historian.md` |
| #442 | Astrologer | Spezielle Situationen | `spezielle-situationen/442-astrologer.md` |
| #443 | Film Critic | Kreativitaet & Freizeit | `kreativitaet-freizeit/443-film-critic.md` |
| #444 | Classical Music Composer | Kreativitaet & Freizeit | `kreativitaet-freizeit/444-classical-music-composer.md` |
| #445 | Journalist | Kommunikation & Beziehungen | `kommunikation-beziehungen/445-journalist.md` |
| #446 | Digital Art Gallery Guide | Alltag & Leben | `alltag-leben/446-digital-art-gallery-guide.md` |
| #447 | Public Speaking Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/447-public-speaking-coach.md` |
| #448 | Makeup Artist | Kreativitaet & Freizeit | `kreativitaet-freizeit/448-makeup-artist.md` |
| #449 | Babysitter | Alltag & Leben | `alltag-leben/449-babysitter.md` |
| #450 | Tech Writer | Technik & Alltag | `technik-alltag/450-tech-writer.md` |
| #451 | Ascii Artist | Kreativitaet & Freizeit | `kreativitaet-freizeit/451-ascii-artist.md` |
| #452 | Python Interpreter | Technik & Alltag | `technik-alltag/452-python-interpreter.md` |
| #453 | Synonym Finder | Lernen & Wachstum | `lernen-wachstum/453-synonym-finder.md` |
| #454 | Personal Shopper | Alltag & Leben | `alltag-leben/454-personal-shopper.md` |
| #455 | Food Critic | Technik & Alltag | `technik-alltag/455-food-critic.md` |
| #456 | Virtual Doctor | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/456-virtual-doctor.md` |
| #457 | Personal Chef | Alltag & Leben | `alltag-leben/457-personal-chef.md` |
| #458 | Legal Advisor | Spezielle Situationen | `spezielle-situationen/458-legal-advisor.md` |
| #459 | Personal Stylist | Alltag & Leben | `alltag-leben/459-personal-stylist.md` |
| #460 | Machine Learning Engineer | Technik & Alltag | `technik-alltag/460-machine-learning-engineer.md` |
| #461 | Biblical Translator | Lernen & Wachstum | `lernen-wachstum/461-biblical-translator.md` |
| #462 | SVG designer | Kreativitaet & Freizeit | `kreativitaet-freizeit/462-svg-designer.md` |
| #463 | IT Expert | Technik & Alltag | `technik-alltag/463-it-expert.md` |
| #464 | Chess Player | Kreativitaet & Freizeit | `kreativitaet-freizeit/464-chess-player.md` |
| #465 | Midjourney Prompt Generator | Technik & Alltag | `technik-alltag/465-midjourney-prompt-generator.md` |
| #466 | Fullstack Software Developer | Technik & Alltag | `technik-alltag/466-fullstack-software-developer.md` |
| #467 | Mathematician | Lernen & Wachstum | `lernen-wachstum/467-mathematician.md` |
| #468 | RegEx Generator | Technik & Alltag | `technik-alltag/468-regex-generator.md` |
| #469 | Time Travel Guide | Alltag & Leben | `alltag-leben/469-time-travel-guide.md` |
| #470 | Dream Interpreter | Kreativitaet & Freizeit | `kreativitaet-freizeit/470-dream-interpreter.md` |
| #471 | Talent Coach | Spezielle Situationen | `spezielle-situationen/471-talent-coach.md` |
| #472 | R Programming Interpreter | Technik & Alltag | `technik-alltag/472-r-programming-interpreter.md` |
| #473 | StackOverflow Post | Technik & Alltag | `technik-alltag/473-stackoverflow-post.md` |
| #474 | Emoji Translator | Lernen & Wachstum | `lernen-wachstum/474-emoji-translator.md` |
| #475 | PHP Interpreter | Technik & Alltag | `technik-alltag/475-php-interpreter.md` |
| #476 | Emergency Response Professional | Spezielle Situationen | `spezielle-situationen/476-emergency-response-professional.md` |
| #477 | Fill in the Blank Worksheets Generator | Lernen & Wachstum | `lernen-wachstum/477-fill-in-blank-worksheets-generator.md` |
| #478 | Software Quality Assurance Tester | Technik & Alltag | `technik-alltag/478-software-quality-assurance-tester.md` |
| #479 | Tic-Tac-Toe Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/479-tic-tac-toe-game.md` |
| #480 | Password Generator | Technik & Alltag | `technik-alltag/480-password-generator.md` |
| #481 | New Language Creator | Lernen & Wachstum | `lernen-wachstum/481-new-language-creator.md` |
| #482 | Web Browser | Technik & Alltag | `technik-alltag/482-web-browser.md` |
| #483 | Senior Frontend Developer | Technik & Alltag | `technik-alltag/483-senior-frontend-developer.md` |
| #484 | Code Reviewer | Technik & Alltag | `technik-alltag/484-code-reviewer.md` |
| #485 | Accessibility Auditor | Technik & Alltag | `technik-alltag/485-accessibility-auditor.md` |
| #486 | Solr Search Engine | Technik & Alltag | `technik-alltag/486-solr-search-engine.md` |
| #487 | Startup Idea Generator | Beruf & Karriere | `beruf-karriere/487-startup-idea-generator.md` |
| #488 | Spongebob's Magic Conch Shell | Technik & Alltag | `technik-alltag/488-spongebob-s-magic-conch-shell.md` |
| #489 | Language Detector | Lernen & Wachstum | `lernen-wachstum/489-language-detector.md` |
| #490 | Salesperson | Beruf & Karriere | `beruf-karriere/490-salesperson.md` |
| #491 | Commit Message Generator | Technik & Alltag | `technik-alltag/491-commit-message-generator.md` |
| #492 | Chief Executive Officer | Beruf & Karriere | `beruf-karriere/492-chief-executive-officer.md` |
| #493 | Diagram Generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/493-diagram-generator.md` |
| #494 | Speech-Language Pathologist (SLP) | Lernen & Wachstum | `lernen-wachstum/494-speech-language-pathologist-slp.md` |
| #495 | Startup Tech Lawyer | Beruf & Karriere | `beruf-karriere/495-startup-tech-lawyer.md` |
| #496 | Title Generator for written pieces | Technik & Alltag | `technik-alltag/496-title-generator-for-written-pieces.md` |
| #497 | Product Manager | Beruf & Karriere | `beruf-karriere/497-product-manager.md` |
| #498 | Project Manager | Beruf & Karriere | `beruf-karriere/498-project-manager.md` |
| #499 | Drunk Person | Technik & Alltag | `technik-alltag/499-drunk-person.md` |
| #500 | Mathematical History Teacher | Lernen & Wachstum | `lernen-wachstum/500-mathematical-history-teacher.md` |
| #501 | Song Recommender | Technik & Alltag | `technik-alltag/501-song-recommender.md` |
| #502 | Cover Letter | Beruf & Karriere | `beruf-karriere/502-cover-letter.md` |
| #503 | Technology Transferer | Technik & Alltag | `technik-alltag/503-technology-transferer.md` |
| #504 | Unconstrained AI model DAN | Technik & Alltag | `technik-alltag/504-unconstrained-ai-model-dan.md` |
| #505 | Gomoku player | Kreativitaet & Freizeit | `kreativitaet-freizeit/505-gomoku-player.md` |
| #506 | Proofreader | Lernen & Wachstum | `lernen-wachstum/506-proofreader.md` |
| #507 | Buddha | Technik & Alltag | `technik-alltag/507-buddha.md` |
| #508 | Muslim Imam | Alltag & Leben | `alltag-leben/508-muslim-imam.md` |
| #509 | Chemical Reactor | Technik & Alltag | `technik-alltag/509-chemical-reactor.md` |
| #510 | Friend | Kommunikation & Beziehungen | `kommunikation-beziehungen/510-friend.md` |
| #511 | ChatGPT Prompt Generator | Technik & Alltag | `technik-alltag/511-chatgpt-prompt-generator.md` |
| #512 | Wikipedia Page | Technik & Alltag | `technik-alltag/512-wikipedia-page.md` |
| #513 | Japanese Kanji quiz machine | Technik & Alltag | `technik-alltag/513-japanese-kanji-quiz-machine.md` |
| #514 | Note-Taking assistant | Technik & Alltag | `technik-alltag/514-note-taking-assistant.md` |
| #515 | Literary Critic | Lernen & Wachstum | `lernen-wachstum/515-literary-critic.md` |
| #516 | Prompt Enhancer | Technik & Alltag | `technik-alltag/516-prompt-enhancer.md` |
| #517 | Cheap Travel Ticket Advisor | Alltag & Leben | `alltag-leben/517-cheap-travel-ticket-advisor.md` |
| #518 | Data Scientist | Technik & Alltag | `technik-alltag/518-data-scientist.md` |
| #519 | League of Legends Player | Kreativitaet & Freizeit | `kreativitaet-freizeit/519-league-of-legends-player.md` |
| #520 | Restaurant Owner | Alltag & Leben | `alltag-leben/520-restaurant-owner.md` |
| #521 | Architectural Expert | Technik & Alltag | `technik-alltag/521-architectural-expert.md` |
| #522 | LLM Researcher | Lernen & Wachstum | `lernen-wachstum/522-llm-researcher.md` |
| #523 | Unit Tester Assistant | Technik & Alltag | `technik-alltag/523-unit-tester-assistant.md` |
| #524 | Wisdom Generator | Lernen & Wachstum | `lernen-wachstum/524-wisdom-generator.md` |
| #525 | YouTube Video Analyst | Technik & Alltag | `technik-alltag/525-youtube-video-analyst.md` |
| #526 | Career Coach | Beruf & Karriere | `beruf-karriere/526-career-coach.md` |
| #527 | Acoustic Guitar Composer | Kreativitaet & Freizeit | `kreativitaet-freizeit/527-acoustic-guitar-composer.md` |
| #528 | Knowledgeable Software Development Mentor | Technik & Alltag | `technik-alltag/528-knowledgeable-software-development-mento.md` |
| #529 | Logic Builder Tool | Alltag & Leben | `alltag-leben/529-logic-builder-tool.md` |
| #530 | Guessing Game Master | Kreativitaet & Freizeit | `kreativitaet-freizeit/530-guessing-game-master.md` |
| #531 | Teacher of React.js | Lernen & Wachstum | `lernen-wachstum/531-teacher-of-react-js.md` |
| #532 | GitHub Expert | Technik & Alltag | `technik-alltag/532-github-expert.md` |
| #533 | Any Programming Language to Python Converter | Lernen & Wachstum | `lernen-wachstum/533-any-programming-language-to-python-conve.md` |
| #534 | Virtual Fitness Coach | Lernen & Wachstum | `lernen-wachstum/534-virtual-fitness-coach.md` |
| #535 | Flirting Boy | Technik & Alltag | `technik-alltag/535-flirting-boy.md` |
| #536 | Girl of Dreams | Kreativitaet & Freizeit | `kreativitaet-freizeit/536-girl-of-dreams.md` |
| #537 | DAX Terminal | Technik & Alltag | `technik-alltag/537-dax-terminal.md` |
| #538 | Structured Iterative Reasoning Protocol (SIRP) | Alltag & Leben | `alltag-leben/538-structured-iterative-reasoning-protocol-.md` |
| #539 | Pirate | Technik & Alltag | `technik-alltag/539-pirate.md` |
| #540 | LinkedIn Ghostwriter | Technik & Alltag | `technik-alltag/540-linkedin-ghostwriter.md` |
| #541 | Idea Clarifier GPT | Technik & Alltag | `technik-alltag/541-idea-clarifier-gpt.md` |
| #542 | Top Programming Expert | Technik & Alltag | `technik-alltag/542-top-programming-expert.md` |
| #543 | Architect Guide for Programmers | Technik & Alltag | `technik-alltag/543-architect-guide-for-programmers.md` |
| #544 | Children's Book Creator | Technik & Alltag | `technik-alltag/544-children-s-book-creator.md` |
| #545 | Tech-Challenged Customer | Technik & Alltag | `technik-alltag/545-tech-challenged-customer.md` |
| #546 | Creative Branding Strategist | Beruf & Karriere | `beruf-karriere/546-creative-branding-strategist.md` |
| #547 | Book Summarizer | Technik & Alltag | `technik-alltag/547-book-summarizer.md` |
| #548 | Study planner | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/548-study-planner.md` |
| #549 | SEO specialist | Kommunikation & Beziehungen | `kommunikation-beziehungen/549-seo-specialist.md` |
| #550 | Nutritionist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/550-nutritionist.md` |
| #551 | Yes or No answer | Technik & Alltag | `technik-alltag/551-yes-or-no-answer.md` |
| #552 | Healing Grandma | Technik & Alltag | `technik-alltag/552-healing-grandma.md` |
| #553 | Remote Worker Fitness Trainer | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/553-remote-worker-fitness-trainer.md` |
| #554 | Rephraser with Obfuscation | Lernen & Wachstum | `lernen-wachstum/554-rephraser-with-obfuscation.md` |
| #555 | Large Language Models Security Specialist | Lernen & Wachstum | `lernen-wachstum/555-large-language-models-security-specialis.md` |
| #556 | Tech Troubleshooter | Technik & Alltag | `technik-alltag/556-tech-troubleshooter.md` |
| #557 | Ayurveda Food Tester | Technik & Alltag | `technik-alltag/557-ayurveda-food-tester.md` |
| #558 | Music Video Designer | Kreativitaet & Freizeit | `kreativitaet-freizeit/558-music-video-designer.md` |
| #559 | Virtual Event Planner | Technik & Alltag | `technik-alltag/559-virtual-event-planner.md` |
| #560 | Technical Architecture | Technik & Alltag | `technik-alltag/560-technical-architecture.md` |
| #561 | SEO Prompt | Technik & Alltag | `technik-alltag/561-seo-prompt.md` |
| #562 | Devops Engineer | Technik & Alltag | `technik-alltag/562-devops-engineer.md` |
| #563 | Linux Script Developer | Technik & Alltag | `technik-alltag/563-linux-script-developer.md` |
| #564 | Reverse Prompt Engineer | Technik & Alltag | `technik-alltag/564-reverse-prompt-engineer.md` |
| #565 | Explainer with Analogies | Technik & Alltag | `technik-alltag/565-explainer-with-analogies.md` |
| #566 | Code Review Assistant | Technik & Alltag | `technik-alltag/566-code-review-assistant.md` |
| #567 | Data Transformer | Technik & Alltag | `technik-alltag/567-data-transformer.md` |
| #568 | Story Generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/568-story-generator.md` |
| #569 | Decision Filter | Technik & Alltag | `technik-alltag/569-decision-filter.md` |
| #570 | Impact Metrics | Technik & Alltag | `technik-alltag/570-impact-metrics.md` |
| #571 | Showcase Top Repositories | Technik & Alltag | `technik-alltag/571-showcase-top-repositories.md` |
| #572 | Enterprise Sponsorship | Technik & Alltag | `technik-alltag/572-enterprise-sponsorship.md` |
| #573 | Announce Milestone | Technik & Alltag | `technik-alltag/573-announce-milestone.md` |
| #574 | Time Commitment | Technik & Alltag | `technik-alltag/574-time-commitment.md` |
| #575 | Break Down Costs | Technik & Alltag | `technik-alltag/575-break-down-costs.md` |
| #576 | Recognize Sponsors | Technik & Alltag | `technik-alltag/576-recognize-sponsors.md` |
| #577 | Create Project Spotlight | Technik & Alltag | `technik-alltag/577-create-project-spotlight.md` |
| #578 | Explain Funding Impact | Technik & Alltag | `technik-alltag/578-explain-funding-impact.md` |
| #579 | Creative Perks | Technik & Alltag | `technik-alltag/579-creative-perks.md` |
| #580 | Create a Professional Bio | Technik & Alltag | `technik-alltag/580-create-professional-bio.md` |
| #581 | Tell Your Story | Alltag & Leben | `alltag-leben/581-tell-your-story.md` |
| #582 | Monthly Updates | Technik & Alltag | `technik-alltag/582-monthly-updates.md` |
| #583 | Future Vision | Technik & Alltag | `technik-alltag/583-future-vision.md` |
| #584 | Show Direct Impact | Technik & Alltag | `technik-alltag/584-show-direct-impact.md` |
| #585 | Write Tier Descriptions | Technik & Alltag | `technik-alltag/585-write-tier-descriptions.md` |
| #586 | Suggest Pricing Tiers | Technik & Alltag | `technik-alltag/586-suggest-pricing-tiers.md` |
| #587 | Student Tier | Alltag & Leben | `alltag-leben/587-student-tier.md` |
| #588 | Success Stories | Technik & Alltag | `technik-alltag/588-success-stories.md` |
| #589 | Sponsor Hall of Fame | Technik & Alltag | `technik-alltag/589-sponsor-hall-of-fame.md` |
| #590 | Recipe Finder | Alltag & Leben | `alltag-leben/590-recipe-finder.md` |
| #591 | Health Metrics Calculator | Technik & Alltag | `technik-alltag/591-health-metrics-calculator.md` |
| #592 | Sudoku Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/592-sudoku-game.md` |
| #593 | Chess Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/593-chess-game.md` |
| #594 | Meditation Timer | Technik & Alltag | `technik-alltag/594-meditation-timer.md` |
| #595 | URL Shortener | Technik & Alltag | `technik-alltag/595-url-shortener.md` |
| #596 | Music Player | Kreativitaet & Freizeit | `kreativitaet-freizeit/596-music-player.md` |
| #597 | Markdown Notes | Technik & Alltag | `technik-alltag/597-markdown-notes.md` |
| #598 | Budget Tracker | Alltag & Leben | `alltag-leben/598-budget-tracker.md` |
| #599 | Text Analyzer Tool | Technik & Alltag | `technik-alltag/599-text-analyzer-tool.md` |
| #600 | Multiplayer 3D Plane Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/600-multiplayer-3d-plane-game.md` |
| #601 | Todo List | Technik & Alltag | `technik-alltag/601-todo-list.md` |
| #602 | Scientific Calculator | Technik & Alltag | `technik-alltag/602-scientific-calculator.md` |
| #603 | Weather Dashboard | Technik & Alltag | `technik-alltag/603-weather-dashboard.md` |
| #604 | Image Editor | Technik & Alltag | `technik-alltag/604-image-editor.md` |
| #605 | Drawing App | Technik & Alltag | `technik-alltag/605-drawing-app.md` |
| #606 | Typing Speed Test | Technik & Alltag | `technik-alltag/606-typing-speed-test.md` |
| #607 | Memory Card Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/607-memory-card-game.md` |
| #608 | Memory Profiler CLI | Technik & Alltag | `technik-alltag/608-memory-profiler-cli.md` |
| #609 | Pomodoro Timer | Technik & Alltag | `technik-alltag/609-pomodoro-timer.md` |
| #610 | Interactive Quiz | Technik & Alltag | `technik-alltag/610-interactive-quiz.md` |
| #611 | Advanced Color Picker Tool | Technik & Alltag | `technik-alltag/611-advanced-color-picker-tool.md` |
| #612 | File System Indexer CLI | Technik & Alltag | `technik-alltag/612-file-system-indexer-cli.md` |
| #613 | Secure Password Generator Tool | Technik & Alltag | `technik-alltag/613-secure-password-generator-tool.md` |
| #614 | Habit Tracker | Technik & Alltag | `technik-alltag/614-habit-tracker.md` |
| #615 | 3D Racing Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/615-3d-racing-game.md` |
| #616 | HTTP Benchmarking Tool CLI | Technik & Alltag | `technik-alltag/616-http-benchmarking-tool-cli.md` |
| #617 | 3D FPS Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/617-3d-fps-game.md` |
| #618 | Currency Exchange Calculator | Technik & Alltag | `technik-alltag/618-currency-exchange-calculator.md` |
| #619 | PDF Viewer | Technik & Alltag | `technik-alltag/619-pdf-viewer.md` |
| #620 | Network Packet Analyzer CLI | Technik & Alltag | `technik-alltag/620-network-packet-analyzer-cli.md` |
| #621 | 3D Space Explorer | Technik & Alltag | `technik-alltag/621-3d-space-explorer.md` |
| #622 | Flashcard Study System | Technik & Alltag | `technik-alltag/622-flashcard-study-system.md` |
| #623 | File Encryption Tool | Technik & Alltag | `technik-alltag/623-file-encryption-tool.md` |
| #624 | Kanban Board | Technik & Alltag | `technik-alltag/624-kanban-board.md` |
| #625 | Code Snippet Manager | Beruf & Karriere | `beruf-karriere/625-code-snippet-manager.md` |
| #626 | Isometric City Diorama | Technik & Alltag | `technik-alltag/626-isometric-city-diorama.md` |
| #627 | The Silent Standoff | Kreativitaet & Freizeit | `kreativitaet-freizeit/627-the-silent-standoff.md` |
| #628 | Lifestyle Product Images | Technik & Alltag | `technik-alltag/628-lifestyle-product-images.md` |
| #629 | Web Design | Technik & Alltag | `technik-alltag/629-web-design.md` |
| #630 | Isometric 3D Weather Cityscapes (PBR Textures) | Technik & Alltag | `technik-alltag/630-isometric-3d-weather-cityscapes-pbr-text.md` |
| #631 | Whimsical 3D Brand Miniatures | Technik & Alltag | `technik-alltag/631-whimsical-3d-brand-miniatures.md` |
| #632 | Smart Rewriter & Clarity Booster | Technik & Alltag | `technik-alltag/632-smart-rewriter-clarity-booster.md` |
| #633 | World Landmarks: Hyper-Realistic 3D Dioramas | Technik & Alltag | `technik-alltag/633-world-landmarks-hyper-realistic-3d-diora.md` |
| #634 | 3D Isometric Miniature Diorama | Technik & Alltag | `technik-alltag/634-3d-isometric-miniature-diorama.md` |
| #635 | Architectural Sketch & Markup Overlay | Technik & Alltag | `technik-alltag/635-architectural-sketch-markup-overlay.md` |
| #636 | Floating City Island - Photoreal 4K Poster | Technik & Alltag | `technik-alltag/636-floating-city-island-photoreal-4k-poster.md` |
| #637 | Interdisciplinary Connections and Applications | Technik & Alltag | `technik-alltag/637-interdisciplinary-connections-and-applic.md` |
| #638 | Expert-Level Insights and Advanced Resources | Technik & Alltag | `technik-alltag/638-expert-level-insights-and-advanced-resou.md` |
| #639 | Vintage Botanical Illustration Generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/639-vintage-botanical-illustration-generator.md` |
| #640 | AI2sql SQL Model — Query Generator | Technik & Alltag | `technik-alltag/640-ai2sql-sql-model-query-generator.md` |
| #641 | Director Variation Grid: One Still, Eight Auteur Re-Shoots | Technik & Alltag | `technik-alltag/641-director-variation-grid-one-still-eight-.md` |
| #642 | Travel Poster | Alltag & Leben | `alltag-leben/642-travel-poster.md` |
| #643 | Profesor Creativo | Lernen & Wachstum | `lernen-wachstum/643-profesor-creativo.md` |
| #644 | Pitchside Tunnel Moment with Your Favorite Footballer | Alltag & Leben | `alltag-leben/644-pitchside-tunnel-moment-with-your-favori.md` |
| #645 | Gemini | Kreativitaet & Freizeit | `kreativitaet-freizeit/645-gemini.md` |
| #646 | deep-research-agent | Technik & Alltag | `technik-alltag/646-deep-research-agent.md` |
| #647 | bug-risk-analysis | Alltag & Leben | `alltag-leben/647-bug-risk-analysis.md` |
| #648 | devops-architect | Technik & Alltag | `technik-alltag/648-devops-architect.md` |
| #649 | quality-engineer | Technik & Alltag | `technik-alltag/649-quality-engineer.md` |
| #650 | refactoring-expert | Technik & Alltag | `technik-alltag/650-refactoring-expert.md` |
| #651 | repo-indexer | Technik & Alltag | `technik-alltag/651-repo-indexer.md` |
| #652 | root-cause-analyst | Technik & Alltag | `technik-alltag/652-root-cause-analyst.md` |
| #653 | security-engineer | Technik & Alltag | `technik-alltag/653-security-engineer.md` |
| #654 | frontend-architect | Technik & Alltag | `technik-alltag/654-frontend-architect.md` |
| #655 | performance-engineer | Technik & Alltag | `technik-alltag/655-performance-engineer.md` |
| #656 | video-analysis-expert | Technik & Alltag | `technik-alltag/656-video-analysis-expert.md` |
| #657 | Predictive Eye Tracking Heatmap Generator | Technik & Alltag | `technik-alltag/657-predictive-eye-tracking-heatmap-generato.md` |
| #658 | Clean BibTeX Formatter for Academic Projects | Technik & Alltag | `technik-alltag/658-clean-bibtex-formatter-for-academic-proj.md` |
| #659 | Realistic Food Image Generator | Alltag & Leben | `alltag-leben/659-realistic-food-image-generator.md` |
| #660 | Urban Casual Confidence | Technik & Alltag | `technik-alltag/660-urban-casual-confidence.md` |
| #661 | What Does ChatGpt Knows about you? | Technik & Alltag | `technik-alltag/661-what-does-chatgpt-knows-about-you.md` |
| #662 | Legebdary Exploded View Prompt For nanobanana | Technik & Alltag | `technik-alltag/662-legebdary-exploded-view-prompt-for-nanob.md` |
| #663 | Tarih-olay- Görsel oluşturma | Lernen & Wachstum | `lernen-wachstum/663-tarih-olay-g-rsel-olu-turma.md` |
| #664 | Temitope | Technik & Alltag | `technik-alltag/664-temitope.md` |
| #665 | Gemi-Gotchi | Alltag & Leben | `alltag-leben/665-gemi-gotchi.md` |
| #666 | Digital product ideas | Kommunikation & Beziehungen | `kommunikation-beziehungen/666-digital-product-ideas.md` |
| #667 | YT video  geopolitic analysis | Technik & Alltag | `technik-alltag/667-yt-video-geopolitic-analysis.md` |
| #668 | Double Exposure Portrait | Kreativitaet & Freizeit | `kreativitaet-freizeit/668-double-exposure-portrait.md` |
| #669 | Time Layer Photography | Technik & Alltag | `technik-alltag/669-time-layer-photography.md` |
| #670 | A Clay-Crafted City: Mini [CITY NAME] World | Technik & Alltag | `technik-alltag/670-a-clay-crafted-city-mini-city-name-world.md` |
| #671 | Architectural Study Sheet: [HISTORIC_SITE_NAME] | Technik & Alltag | `technik-alltag/671-architectural-study-sheet-historic-site-.md` |
| #672 | Professional Badge Photo, Ready to Use | Technik & Alltag | `technik-alltag/672-professional-badge-photo-ready-to-use.md` |
| #673 | Clean Clinic Portrait | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/673-clean-clinic-portrait.md` |
| #674 | Travel Planner Prompt | Technik & Alltag | `technik-alltag/674-travel-planner-prompt.md` |
| #675 | Hyper-Realistic Clay Bust From Photo Template | Technik & Alltag | `technik-alltag/675-hyper-realistic-clay-bust-from-photo-tem.md` |
| #676 | 3D City Prompt | Technik & Alltag | `technik-alltag/676-3d-city-prompt.md` |
| #677 | Django Unit Test Generator for Viewsets | Technik & Alltag | `technik-alltag/677-django-unit-test-generator-for-viewsets.md` |
| #678 | Sales | Kommunikation & Beziehungen | `kommunikation-beziehungen/678-sales.md` |
| #679 | Ultra-Realistic Noir Portrait Creation | Technik & Alltag | `technik-alltag/679-ultra-realistic-noir-portrait-creation.md` |
| #680 | Selar ideas for automation | Kommunikation & Beziehungen | `kommunikation-beziehungen/680-selar-ideas-for-automation.md` |
| #681 | Comprehensive Repository Analysis and Bug Fixing Framework | Technik & Alltag | `technik-alltag/681-comprehensive-repository-analysis-and-bu.md` |
| #682 | Virtual Game Console Simulator | Kreativitaet & Freizeit | `kreativitaet-freizeit/682-virtual-game-console-simulator.md` |
| #683 | Christmas Poster - Festive Holiday Scene | Technik & Alltag | `technik-alltag/683-christmas-poster-festive-holiday-scene.md` |
| #684 | Crear un retrato familiar combinando dos personas | Kreativitaet & Freizeit | `kreativitaet-freizeit/684-crear-un-retrato-familiar-combinando-dos.md` |
| #685 | Turkish Cats hanging out nearby of Galata Tower | Technik & Alltag | `technik-alltag/685-turkish-cats-hanging-out-nearby-of-galat.md` |
| #686 | Ultrathinker | Technik & Alltag | `technik-alltag/686-ultrathinker.md` |
| #687 | Detailed Analysis of YouTube Channels, Databases, and Profiles | Technik & Alltag | `technik-alltag/687-detailed-analysis-of-youtube-channels-da.md` |
| #688 | When to clear the snow (generic) | Technik & Alltag | `technik-alltag/688-when-to-clear-snow-generic.md` |
| #689 | Master Skills & Experience Summary Generator | Technik & Alltag | `technik-alltag/689-master-skills-experience-summary-generat.md` |
| #690 | Turn Your Photo Into a Simpsons Scene | Technik & Alltag | `technik-alltag/690-turn-your-photo-into-simpsons-scene.md` |
| #691 | SaaS Landing Page Builder | Technik & Alltag | `technik-alltag/691-saas-landing-page-builder.md` |
| #692 | Blender Object Maker | Kreativitaet & Freizeit | `kreativitaet-freizeit/692-blender-object-maker.md` |
| #693 | Code Review Agent | Technik & Alltag | `technik-alltag/693-code-review-agent.md` |
| #694 | Editorial Winter Poster–Style Multi-Panel Collage Generation | Technik & Alltag | `technik-alltag/694-editorial-winter-poster-style-multi-pane.md` |
| #695 | Senior System Architect Agent | Technik & Alltag | `technik-alltag/695-senior-system-architect-agent.md` |
| #696 | AI Themed Design Image Creation | Alltag & Leben | `alltag-leben/696-ai-themed-design-image-creation.md` |
| #697 | Bakery Merge Bounty Game Overview | Kreativitaet & Freizeit | `kreativitaet-freizeit/697-bakery-merge-bounty-game-overview.md` |
| #698 | Monetization Strategy for Blockchain-Based Merging Games | Technik & Alltag | `technik-alltag/698-monetization-strategy-for-blockchain-bas.md` |
| #699 | Corporate Studio Portrait (Auto Outfit for Men/Women) | Technik & Alltag | `technik-alltag/699-corporate-studio-portrait-auto-outfit-fo.md` |
| #700 | SaaS Payment Plan Options | Technik & Alltag | `technik-alltag/700-saas-payment-plan-options.md` |
| #701 | Ultra-Detailed Vintage Photo Restoration and Colorization | Alltag & Leben | `alltag-leben/701-ultra-detailed-vintage-photo-restoration.md` |
| #702 | Revenue Performance Report | Technik & Alltag | `technik-alltag/702-revenue-performance-report.md` |
| #703 | Harry Potter / Marauder’s Map | Technik & Alltag | `technik-alltag/703-harry-potter-marauder-s-map.md` |
| #704 | Create a Cultural Superhero Movie Poster | Kreativitaet & Freizeit | `kreativitaet-freizeit/704-create-cultural-superhero-movie-poster.md` |
| #705 | Недвижимость | Kreativitaet & Freizeit | `kreativitaet-freizeit/705-.md` |
| #706 | In-Depth Article Enhancement with Research | Technik & Alltag | `technik-alltag/706-in-depth-article-enhancement-with-resear.md` |
| #707 | Test Python Algorithmic Trading Project | Technik & Alltag | `technik-alltag/707-test-python-algorithmic-trading-project.md` |
| #708 | Senior Prompt Engineer Role Guide | Technik & Alltag | `technik-alltag/708-senior-prompt-engineer-role-guide.md` |
| #709 | Mirror Selfie with Face Preservation | Technik & Alltag | `technik-alltag/709-mirror-selfie-with-face-preservation.md` |
| #710 | Comprehensive Content Review Plan | Alltag & Leben | `alltag-leben/710-comprehensive-content-review-plan.md` |
| #711 | Arista Network Configuration Expert | Technik & Alltag | `technik-alltag/711-arista-network-configuration-expert.md` |
| #712 | Readability Logic Simulator - 全功能翻译版 | Technik & Alltag | `technik-alltag/712-readability-logic-simulator.md` |
| #713 | Pitch | Technik & Alltag | `technik-alltag/713-pitch.md` |
| #714 | Analyze PDF and Create MATLAB Code | Technik & Alltag | `technik-alltag/714-analyze-pdf-and-create-matlab-code.md` |
| #715 | AI Customer Support Specialist | Technik & Alltag | `technik-alltag/715-ai-customer-support-specialist.md` |
| #716 | Image Style Imitation | Technik & Alltag | `technik-alltag/716-image-style-imitation.md` |
| #717 | Medical Consultant | Beruf & Karriere | `beruf-karriere/717-medical-consultant.md` |
| #718 | Ai new | Technik & Alltag | `technik-alltag/718-ai-new.md` |
| #719 | Removing visual noise in the neural network's response | Kreativitaet & Freizeit | `kreativitaet-freizeit/719-removing-visual-noise-in-neural-network-.md` |
| #720 | A prompt that will turn your photo into a scene from a cult 90s movie | Technik & Alltag | `technik-alltag/720-a-prompt-that-will-turn-your-photo-into-.md` |
| #721 | Diabetes Treatment Advisor | Technik & Alltag | `technik-alltag/721-diabetes-treatment-advisor.md` |
| #722 | worldquant | Technik & Alltag | `technik-alltag/722-worldquant.md` |
| #723 | Professional Buyer Q&A Creator | Technik & Alltag | `technik-alltag/723-professional-buyer-q-a-creator.md` |
| #724 | Vacuum Arc Modeling under Transverse Magnetic Fields | Technik & Alltag | `technik-alltag/724-vacuum-arc-modeling-under-transverse-mag.md` |
| #725 | AI Agent Security Evaluation Checklist | Technik & Alltag | `technik-alltag/725-ai-agent-security-evaluation-checklist.md` |
| #726 | Meeting Room Booking Web App Development | Technik & Alltag | `technik-alltag/726-meeting-room-booking-web-app-development.md` |
| #727 | Compare Top Virtualization Solutions | Technik & Alltag | `technik-alltag/727-compare-top-virtualization-solutions.md` |
| #728 | Virtualization Expert | Technik & Alltag | `technik-alltag/728-virtualization-expert.md` |
| #729 | Studio Portraits with Professional Postures | Technik & Alltag | `technik-alltag/729-studio-portraits-with-professional-postu.md` |
| #730 | HTS Veri Analiz Portalı Geliştirme ve Hata Ayıklama | Technik & Alltag | `technik-alltag/730-hts-veri-analiz-portal-geli-tirme-ve-hat.md` |
| #731 | Create STYLE_GUIDE.md | Alltag & Leben | `alltag-leben/731-create-style-guide-md.md` |
| #732 | Analyse Énergétique avec DJU, Consommation et Coûts | Technik & Alltag | `technik-alltag/732-analyse-nerg-tique-avec-dju-consommation.md` |
| #733 | Learn to Speak Spanish | Lernen & Wachstum | `lernen-wachstum/733-learn-to-speak-spanish.md` |
| #734 | $500/Hour AI Consultant Prompt | Beruf & Karriere | `beruf-karriere/734-500-hour-ai-consultant-prompt.md` |
| #735 | Viral Video Analyzer for TikTok and Xiaohongshu | Technik & Alltag | `technik-alltag/735-viral-video-analyzer-for-tiktok-and-xiao.md` |
| #736 | Kognitiv aktivierende Aufgaben erstellen | Technik & Alltag | `technik-alltag/736-kognitiv-aktivierende-aufgaben-erstellen.md` |
| #737 | Xiaomi Company Self-Service Management System Frontend Development | Technik & Alltag | `technik-alltag/737-xiaomi-company-self-service-management-s.md` |
| #738 | TikTok Marketing Visual Designer Agent | Technik & Alltag | `technik-alltag/738-tiktok-marketing-visual-designer-agent.md` |
| #739 | CTI Analyst Cybersecurity Project Support | Technik & Alltag | `technik-alltag/739-cti-analyst-cybersecurity-project-suppor.md` |
| #740 | Customizable Web Template for Company Branding | Technik & Alltag | `technik-alltag/740-customizable-web-template-for-company-br.md` |
| #741 | Minimal Web-Compatible Food Order App Development | Technik & Alltag | `technik-alltag/741-minimal-web-compatible-food-order-app-de.md` |
| #742 | Real-Time Multiplayer Defense Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/742-real-time-multiplayer-defense-game.md` |
| #743 | Continue Coding Assistant | Technik & Alltag | `technik-alltag/743-continue-coding-assistant.md` |
| #744 | Create a New Greek God | Technik & Alltag | `technik-alltag/744-create-new-greek-god.md` |
| #745 | FDR Analysis Program for Commercial Aircraft | Technik & Alltag | `technik-alltag/745-fdr-analysis-program-for-commercial-airc.md` |
| #746 | Integration and Planning Roadmap for Calculator Content | Technik & Alltag | `technik-alltag/746-integration-and-planning-roadmap-for-cal.md` |
| #747 | Pixel Dissolve: Minimalist 3D Food Transformation | Technik & Alltag | `technik-alltag/747-pixel-dissolve-minimalist-3d-food-transf.md` |
| #748 | brsorndnsg | Technik & Alltag | `technik-alltag/748-brsorndnsg.md` |
| #749 | Luxury Ski Resort Selfie Scene Description | Technik & Alltag | `technik-alltag/749-luxury-ski-resort-selfie-scene-descripti.md` |
| #750 | Internal Project Proposal for Hospital Collaboration | Beruf & Karriere | `beruf-karriere/750-internal-project-proposal-for-hospital-c.md` |
| #751 | AI Face Swapping for E-commerce Personalization | Alltag & Leben | `alltag-leben/751-ai-face-swapping-for-e-commerce-personal.md` |
| #752 | Dark Style Image Prompt | Technik & Alltag | `technik-alltag/752-dark-style-image-prompt.md` |
| #753 | Develop a Lazy Learner Software | Technik & Alltag | `technik-alltag/753-develop-lazy-learner-software.md` |
| #754 | College-Level Integrative Project Proposal Draft | Technik & Alltag | `technik-alltag/754-college-level-integrative-project-propos.md` |
| #755 | Product Image Highlight Extraction | Technik & Alltag | `technik-alltag/755-product-image-highlight-extraction.md` |
| #756 | AI Stocks Investment Helper | Beruf & Karriere | `beruf-karriere/756-ai-stocks-investment-helper.md` |
| #757 | Asisten Serba Bisa untuk Kebutuhan Harian | Technik & Alltag | `technik-alltag/757-asisten-serba-bisa-untuk-kebutuhan-haria.md` |
| #758 | Custom Health Membership Annual Summary | Alltag & Leben | `alltag-leben/758-custom-health-membership-annual-summary.md` |
| #759 | Children's Story about Apples | Lernen & Wachstum | `lernen-wachstum/759-children-s-story-about-apples.md` |
| #760 | Lower AI Generation Rate | Technik & Alltag | `technik-alltag/760-lower-ai-generation-rate.md` |
| #761 | Academic Text Refinement Assistant | Kreativitaet & Freizeit | `kreativitaet-freizeit/761-academic-text-refinement-assistant.md` |
| #762 | Tumor Medical Industry Solution Business Plan | Beruf & Karriere | `beruf-karriere/762-tumor-medical-industry-solution-business.md` |
| #763 | Starting a Flutter Project | Technik & Alltag | `technik-alltag/763-starting-flutter-project.md` |
| #764 | Comprehensive Academic Paper Writing Guide | Alltag & Leben | `alltag-leben/764-comprehensive-academic-paper-writing-gui.md` |
| #765 | Interview Preparation Coach | Lernen & Wachstum | `lernen-wachstum/765-interview-preparation-coach.md` |
| #766 | Comprehensive UI/UX Mobile App Analysis | Technik & Alltag | `technik-alltag/766-comprehensive-ui-ux-mobile-app-analysis.md` |
| #767 | Comprehensive repository analysis | Technik & Alltag | `technik-alltag/767-comprehensive-repository-analysis.md` |
| #768 | Optimize Large Data Reading in Code | Technik & Alltag | `technik-alltag/768-optimize-large-data-reading-in-code.md` |
| #769 | Pet Store Advertising Campaign Strategy | Kommunikation & Beziehungen | `kommunikation-beziehungen/769-pet-store-advertising-campaign-strategy.md` |
| #770 | LinkedIn comments | Technik & Alltag | `technik-alltag/770-linkedin-comments.md` |
| #771 | Detailed Image Generation Prompt for Fashion and Portrait Photography | Technik & Alltag | `technik-alltag/771-detailed-image-generation-prompt-for-fas.md` |
| #772 | High-End Beauty Editorial Photo Shoot Specification | Technik & Alltag | `technik-alltag/772-high-end-beauty-editorial-photo-shoot-sp.md` |
| #773 | Flamenco inspired Turkish Pop song for Suno AI | Technik & Alltag | `technik-alltag/773-flamenco-inspired-turkish-pop-song-for-s.md` |
| #774 | POV Smartphone with Space-Themed Twitter UI in Central Park | Technik & Alltag | `technik-alltag/774-pov-smartphone-with-space-themed-twitter.md` |
| #775 | Comprehensive DevOps Guide | Technik & Alltag | `technik-alltag/775-comprehensive-devops-guide.md` |
| #776 | Next.js Specialized Front-End Developer | Technik & Alltag | `technik-alltag/776-next-js-specialized-front-end-developer.md` |
| #777 | AUTOSAR Software Module Developer | Technik & Alltag | `technik-alltag/777-autosar-software-module-developer.md` |
| #778 | Fierce Medieval Queen on Iron Throne Portrait | Kreativitaet & Freizeit | `kreativitaet-freizeit/778-fierce-medieval-queen-on-iron-throne-por.md` |
| #779 | Documentary on Humanitarian & Refugee Crises | Technik & Alltag | `technik-alltag/779-documentary-on-humanitarian-refugee-cris.md` |
| #780 | Personal Financial Adviosr | Beruf & Karriere | `beruf-karriere/780-personal-financial-adviosr.md` |
| #781 | Act as a Senior Research Paper Evaluator | Technik & Alltag | `technik-alltag/781-senior-research-paper-evaluator.md` |
| #782 | Manufacturing Workflow Optimization with OR-Tools | Technik & Alltag | `technik-alltag/782-manufacturing-workflow-optimization-with.md` |
| #783 | Act as a Conversational AI | Technik & Alltag | `technik-alltag/783-conversational-ai.md` |
| #784 | AI for Casino List and Profit Simulation | Technik & Alltag | `technik-alltag/784-ai-for-casino-list-and-profit-simulation.md` |
| #785 | Article Summary and Comprehension | Technik & Alltag | `technik-alltag/785-article-summary-and-comprehension.md` |
| #786 | Shift Tracking Telegram Mini App | Technik & Alltag | `technik-alltag/786-shift-tracking-telegram-mini-app.md` |
| #787 | Münchener Skyline als Umrissbild darstellen | Technik & Alltag | `technik-alltag/787-m-nchener-skyline-als-umrissbild-darstel.md` |
| #788 | Exploring Jung's Understanding of Spirit through Rumi's Poem | Technik & Alltag | `technik-alltag/788-exploring-jung-s-understanding-of-spirit.md` |
| #789 | Stock Market Analyst: Market Move Suggestions | Beruf & Karriere | `beruf-karriere/789-stock-market-analyst-market-move-suggest.md` |
| #790 | Data Analyst | Technik & Alltag | `technik-alltag/790-data-analyst.md` |
| #791 | Lead Data Analyst with Data Engineering Expertise | Technik & Alltag | `technik-alltag/791-lead-data-analyst-with-data-engineering-.md` |
| #792 | Act as a Patient, Non-Technical Android Studio Guide | Alltag & Leben | `alltag-leben/792-patient-non-technical-android-studio-gui.md` |
| #793 | Chimera AI-Powered Prompt Optimization System | Technik & Alltag | `technik-alltag/793-chimera-ai-powered-prompt-optimization-s.md` |
| #794 | AI Tour Guide Business Plan for Foreign Tourists in China | Beruf & Karriere | `beruf-karriere/794-ai-tour-guide-business-plan-for-foreign-.md` |
| #795 | Plant Hero Section Image | Technik & Alltag | `technik-alltag/795-plant-hero-section-image.md` |
| #796 | Cozy Christmas Smile | Technik & Alltag | `technik-alltag/796-cozy-christmas-smile.md` |
| #797 | Code Translator: Any Language to Any Language | Lernen & Wachstum | `lernen-wachstum/797-code-translator-any-language-to-any-lang.md` |
| #798 | Orchestration Agent (PowerPlatformSupervisor) | Technik & Alltag | `technik-alltag/798-orchestration-agent-powerplatformsupervi.md` |
| #799 | Analyze Previous Year Question Papers | Lernen & Wachstum | `lernen-wachstum/799-analyze-previous-year-question-papers.md` |
| #800 | Linux monitoring single html | Technik & Alltag | `technik-alltag/800-linux-monitoring-single-html.md` |
| #801 | Linux Monitoring Dashboard with React | Technik & Alltag | `technik-alltag/801-linux-monitoring-dashboard-with-react.md` |
| #802 | Stock Market Analysis Expert | Beruf & Karriere | `beruf-karriere/802-stock-market-analysis-expert.md` |
| #803 | Paladin Octem Plus (Research Swarm) | Technik & Alltag | `technik-alltag/803-paladin-octem-plus-research-swarm.md` |
| #804 | Website Security Vulnerability Checker | Technik & Alltag | `technik-alltag/804-website-security-vulnerability-checker.md` |
| #805 | Sidebar Dashboard Design | Technik & Alltag | `technik-alltag/805-sidebar-dashboard-design.md` |
| #806 | Build an Advanced Music App for Android | Kreativitaet & Freizeit | `kreativitaet-freizeit/806-build-advanced-music-app-for-android.md` |
| #807 | Web Application Testing Skill | Technik & Alltag | `technik-alltag/807-web-application-testing-skill.md` |
| #808 | Yamuna River Cleanup Plan for Vrindavan | Beruf & Karriere | `beruf-karriere/808-yamuna-river-cleanup-plan-for-vrindavan.md` |
| #809 | iOS Recipe Generator: Create Recipes from Available Ingredients | Alltag & Leben | `alltag-leben/809-ios-recipe-generator-create-recipes-from.md` |
| #810 | Glyth_Maker | Alltag & Leben | `alltag-leben/810-glyth-maker.md` |
| #811 | Emotion Analyst | Technik & Alltag | `technik-alltag/811-emotion-analyst.md` |
| #812 | Persuasive Article or Proposal Writing Guide | Alltag & Leben | `alltag-leben/812-persuasive-article-or-proposal-writing-g.md` |
| #813 | illustration for teenagers, side silhouette of a young person. Inside the head a question mark transforming into light t. Deep purple and blue tones, minimalist and , v. | Technik & Alltag | `technik-alltag/813-illustration-for-teenagers-side-silhouet.md` |
| #814 | Academic Graduation Presentation Guide | Alltag & Leben | `alltag-leben/814-academic-graduation-presentation-guide.md` |
| #815 | Career Path Deliberation Assistant | Beruf & Karriere | `beruf-karriere/815-career-path-deliberation-assistant.md` |
| #816 | Girl Taking Selfie with Avatar Characters in Cinema | Kreativitaet & Freizeit | `kreativitaet-freizeit/816-girl-taking-selfie-with-avatar-character.md` |
| #817 | UI Designer Role | Technik & Alltag | `technik-alltag/817-ui-designer-role.md` |
| #818 | Through the Glass: One Eye in Focus | Technik & Alltag | `technik-alltag/818-through-glass-one-eye-in-focus.md` |
| #819 | Surreal CGI-Photography Hybrid Portrait | Technik & Alltag | `technik-alltag/819-surreal-cgi-photography-hybrid-portrait.md` |
| #820 | Hyperrealistic Food Photo Creator | Alltag & Leben | `alltag-leben/820-hyperrealistic-food-photo-creator.md` |
| #821 | Meta-Prompt Engineer | Technik & Alltag | `technik-alltag/821-meta-prompt-engineer.md` |
| #822 | Course Feedback Analysis | Technik & Alltag | `technik-alltag/822-course-feedback-analysis.md` |
| #823 | Squid Game - Red Light, Green Light Challenge | Kreativitaet & Freizeit | `kreativitaet-freizeit/823-squid-game-red-light-green-light-challen.md` |
| #824 | World of Darkness B&W style | Technik & Alltag | `technik-alltag/824-world-of-darkness-b-w-style.md` |
| #825 | Crypto Market Outlook Analyst | Beruf & Karriere | `beruf-karriere/825-crypto-market-outlook-analyst.md` |
| #826 | World of Darkness Colored Comic style | Technik & Alltag | `technik-alltag/826-world-of-darkness-colored-comic-style.md` |
| #827 | Landing Page Vibe Coding | Technik & Alltag | `technik-alltag/827-landing-page-vibe-coding.md` |
| #828 | Theme based Art Style Fusion Meta-Prompt | Technik & Alltag | `technik-alltag/828-theme-based-art-style-fusion-meta-prompt.md` |
| #829 | Enhance and Beautify Your Photo | Technik & Alltag | `technik-alltag/829-enhance-and-beautify-your-photo.md` |
| #830 | Shower Glass Silhouette | Technik & Alltag | `technik-alltag/830-shower-glass-silhouette.md` |
| #831 | GoPro Action | Technik & Alltag | `technik-alltag/831-gopro-action.md` |
| #832 | Pathology Slide Analysis Assistant | Technik & Alltag | `technik-alltag/832-pathology-slide-analysis-assistant.md` |
| #833 | Bank Transaction Analysis | Beruf & Karriere | `beruf-karriere/833-bank-transaction-analysis.md` |
| #834 | Dizi ve Film Özeti Çeviri Asistanı | Lernen & Wachstum | `lernen-wachstum/834-dizi-ve-film-zeti-eviri-asistan.md` |
| #835 | CI/CD Strategy for SpringBoot REST APIs Deployment | Technik & Alltag | `technik-alltag/835-ci-cd-strategy-for-springboot-rest-apis-.md` |
| #836 | Escritor de Livros Completo | Technik & Alltag | `technik-alltag/836-escritor-de-livros-completo.md` |
| #837 | Quantitative Factor Research Engineer | Technik & Alltag | `technik-alltag/837-quantitative-factor-research-engineer.md` |
| #838 | Banking System App Development with CRUD Operations | Technik & Alltag | `technik-alltag/838-banking-system-app-development-with-crud.md` |
| #839 | MPPT Simulation仿真代码 | Technik & Alltag | `technik-alltag/839-mppt-simulation.md` |
| #840 | Cryptocurrency Contract Trading System | Technik & Alltag | `technik-alltag/840-cryptocurrency-contract-trading-system.md` |
| #841 | Real-Time Screen Translation Assistant | Lernen & Wachstum | `lernen-wachstum/841-real-time-screen-translation-assistant.md` |
| #842 | Hyper-Realistic 3D Isometric Ottoman Masterpiece | Technik & Alltag | `technik-alltag/842-hyper-realistic-3d-isometric-ottoman-mas.md` |
| #843 | Create a detailed travel itinerary in HTML format | Alltag & Leben | `alltag-leben/843-create-detailed-travel-itinerary-in-html.md` |
| #844 | Miniature Claymation Adventures on the Mushroom Cap | Technik & Alltag | `technik-alltag/844-miniature-claymation-adventures-on-mushr.md` |
| #845 | Melancholic Dawn on the Misty Pier | Technik & Alltag | `technik-alltag/845-melancholic-dawn-on-misty-pier.md` |
| #846 | prompt 生成 | Technik & Alltag | `technik-alltag/846-prompt.md` |
| #847 | Professional Email Writer for Any Occasion | Technik & Alltag | `technik-alltag/847-professional-email-writer-for-any-occasi.md` |
| #848 | emails Professionals | Technik & Alltag | `technik-alltag/848-emails-professionals.md` |
| #849 | Digital Visiting Card Product Architect | Technik & Alltag | `technik-alltag/849-digital-visiting-card-product-architect.md` |
| #850 | Developer Daily Report Generator | Technik & Alltag | `technik-alltag/850-developer-daily-report-generator.md` |
| #851 | 担任Go语言开发者 | Technik & Alltag | `technik-alltag/851-go.md` |
| #852 | Act as an Etsy Niche Product Researcher | Technik & Alltag | `technik-alltag/852-etsy-niche-product-researcher.md` |
| #853 | Müzisyenler için Kariyer Yönetimi Desteği | Beruf & Karriere | `beruf-karriere/853-m-zisyenler-i-in-kariyer-y-netimi-deste-.md` |
| #854 | Pharmacy Research Assistant | Alltag & Leben | `alltag-leben/854-pharmacy-research-assistant.md` |
| #855 | Stranded in Time: The Victorian Traveler’s Panic | Alltag & Leben | `alltag-leben/855-stranded-in-time-victorian-traveler-s-pa.md` |
| #856 | Sistem ve Ağ Güvenliği Temalı Kısa Film Promptu | Technik & Alltag | `technik-alltag/856-sistem-ve-a-g-venli-i-temal-k-sa-film-pr.md` |
| #857 | Table with Various Items | Technik & Alltag | `technik-alltag/857-table-with-various-items.md` |
| #858 | Customizable Avatar Style Generator | Alltag & Leben | `alltag-leben/858-customizable-avatar-style-generator.md` |
| #859 | Frontend Developer Skill | Technik & Alltag | `technik-alltag/859-frontend-developer-skill.md` |
| #860 | Detailed mirror-selfie room scene | Technik & Alltag | `technik-alltag/860-detailed-mirror-selfie-room-scene.md` |
| #861 | Black and white studio side-profile portrait prompt | Technik & Alltag | `technik-alltag/861-black-and-white-studio-side-profile-port.md` |
| #862 | The Digital Frontier: Pixelated Pioneers | Technik & Alltag | `technik-alltag/862-the-digital-frontier-pixelated-pioneers.md` |
| #863 | Childs Coloring Style | Technik & Alltag | `technik-alltag/863-childs-coloring-style.md` |
| #864 | Osobní AI Agent pro Petra Sovadinu | Alltag & Leben | `alltag-leben/864-osobn-ai-agent-pro-petra-sovadinu.md` |
| #865 | GitHub Code Structure Tutor | Lernen & Wachstum | `lernen-wachstum/865-github-code-structure-tutor.md` |
| #866 | 提取查询 json 中的查询条件 | Technik & Alltag | `technik-alltag/866-json.md` |
| #867 | Algorithm Quick Guide | Alltag & Leben | `alltag-leben/867-algorithm-quick-guide.md` |
| #868 | Encyclopedia Assistant | Lernen & Wachstum | `lernen-wachstum/868-encyclopedia-assistant.md` |
| #869 | Act as a Health Recovery and Weight Loss Specialist | Alltag & Leben | `alltag-leben/869-health-recovery-and-weight-loss-speciali.md` |
| #870 | Comprehensive User Manual Creation for Multiple Modules | Alltag & Leben | `alltag-leben/870-comprehensive-user-manual-creation-for-m.md` |
| #871 | Building an Inventory Management System | Technik & Alltag | `technik-alltag/871-building-inventory-management-system.md` |
| #872 | Setting Up a New iOS App in Xcode | Technik & Alltag | `technik-alltag/872-setting-up-new-ios-app-in-xcode.md` |
| #873 | AI Video Creation Assistant | Technik & Alltag | `technik-alltag/873-ai-video-creation-assistant.md` |
| #874 | Cinematic Vertical Portrait of Vintage Car Radio at Night | Alltag & Leben | `alltag-leben/874-cinematic-vertical-portrait-of-vintage-c.md` |
| #875 | Personalized Skin Whitening Plan | Alltag & Leben | `alltag-leben/875-personalized-skin-whitening-plan.md` |
| #876 | Next.js React Comprehensive Clash of Clans Tool | Technik & Alltag | `technik-alltag/876-next-js-react-comprehensive-clash-of-cla.md` |
| #877 | Müşteri temsilcisi eğitimi | Technik & Alltag | `technik-alltag/877-m-teri-temsilcisi-e-itimi.md` |
| #878 | Developer Work Analysis from Git Diff and Commit Message | Technik & Alltag | `technik-alltag/878-developer-work-analysis-from-git-diff-an.md` |
| #879 | The Covert Exchange in the Fog | Technik & Alltag | `technik-alltag/879-the-covert-exchange-in-fog.md` |
| #880 | Master Chinese Web Novel Author | Kreativitaet & Freizeit | `kreativitaet-freizeit/880-master-chinese-web-novel-author.md` |
| #881 | Socratic Method for Ethical Discussions | Technik & Alltag | `technik-alltag/881-socratic-method-for-ethical-discussions.md` |
| #882 | A Moment Shared with the Wild | Technik & Alltag | `technik-alltag/882-a-moment-shared-with-wild.md` |
| #883 | Isometric miniature 3D cartoon city scene | Technik & Alltag | `technik-alltag/883-isometric-miniature-3d-cartoon-city-scen.md` |
| #884 | Trade Contract Review Expert | Beruf & Karriere | `beruf-karriere/884-trade-contract-review-expert.md` |
| #885 | Algorithm Analysis and Improvement Advisor | Technik & Alltag | `technik-alltag/885-algorithm-analysis-and-improvement-advis.md` |
| #886 | ERP to Feishu Data Integration Solution | Technik & Alltag | `technik-alltag/886-erp-to-feishu-data-integration-solution.md` |
| #887 | University Admission Interview Simulation | Beruf & Karriere | `beruf-karriere/887-university-admission-interview-simulatio.md` |
| #888 | RIP McKinsey: Here are 10 prompts to replace expensive business consultants | Beruf & Karriere | `beruf-karriere/888-rip-mckinsey-here-are-10-prompts-to-repl.md` |
| #889 | VR Headset Experience Simulator | Technik & Alltag | `technik-alltag/889-vr-headset-experience-simulator.md` |
| #890 | VR Horror Death Chatroom Simulator | Technik & Alltag | `technik-alltag/890-vr-horror-death-chatroom-simulator.md` |
| #891 | How to Obtain a Radio and TV License in Nigeria | Beruf & Karriere | `beruf-karriere/891-how-to-obtain-radio-and-tv-license-in-ni.md` |
| #892 | Doom Horror Death Image Simulator | Technik & Alltag | `technik-alltag/892-doom-horror-death-image-simulator.md` |
| #893 | Aprendizaje Diario de Japonés | Lernen & Wachstum | `lernen-wachstum/893-aprendizaje-diario-de-japon-s.md` |
| #894 | Update checker | Technik & Alltag | `technik-alltag/894-update-checker.md` |
| #895 | Android Update Checker Script for Pydroid 3 | Technik & Alltag | `technik-alltag/895-android-update-checker-script-for-pydroi.md` |
| #896 | Pull Request Review Assistant | Technik & Alltag | `technik-alltag/896-pull-request-review-assistant.md` |
| #897 | Quizflix App Development | Technik & Alltag | `technik-alltag/897-quizflix-app-development.md` |
| #898 | QuizFlix Mobile App Design for University Students | Lernen & Wachstum | `lernen-wachstum/898-quizflix-mobile-app-design-for-universit.md` |
| #899 | A three-panel monochromatic image | Technik & Alltag | `technik-alltag/899-a-three-panel-monochromatic-image.md` |
| #900 | Interactive Quiz Application for TV Shows and Movies | Technik & Alltag | `technik-alltag/900-interactive-quiz-application-for-tv-show.md` |
| #901 | Istanbul Travel Journal | Kommunikation & Beziehungen | `kommunikation-beziehungen/901-istanbul-travel-journal.md` |
| #902 | Young woman with mixed ethnicity features | Technik & Alltag | `technik-alltag/902-young-woman-with-mixed-ethnicity-feature.md` |
| #903 | Hyper-Realistic Marvel Comic Fusion Image Generation | Technik & Alltag | `technik-alltag/903-hyper-realistic-marvel-comic-fusion-imag.md` |
| #904 | Shadows of the Cold War: The 1962 Exchange | Technik & Alltag | `technik-alltag/904-shadows-of-cold-war-1962-exchange.md` |
| #905 | Project Evaluation for Production Decision | Technik & Alltag | `technik-alltag/905-project-evaluation-for-production-decisi.md` |
| #906 | 30 tweet Project | Technik & Alltag | `technik-alltag/906-30-tweet-project.md` |
| #907 | Build a Self-Hosted App Dashboard with Next.js | Technik & Alltag | `technik-alltag/907-build-self-hosted-app-dashboard-with-nex.md` |
| #908 | Scientific Drawing Assistant | Technik & Alltag | `technik-alltag/908-scientific-drawing-assistant.md` |
| #909 | Senior Crypto Yapper & Community Strategist | Technik & Alltag | `technik-alltag/909-senior-crypto-yapper-community-strategis.md` |
| #910 | for Rally | Technik & Alltag | `technik-alltag/910-for-rally.md` |
| #911 | HCCVN-AI-VN Pro Max: Optimal AI System Design | Technik & Alltag | `technik-alltag/911-hccvn-ai-vn-pro-max-optimal-ai-system-de.md` |
| #912 | Evaluate and Suggest Improvements for Computer Science PhD Thesis | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/912-evaluate-and-suggest-improvements-for-co.md` |
| #913 | Graduate-Level Review Paper on Humanoid Robots | Alltag & Leben | `alltag-leben/913-graduate-level-review-paper-on-humanoid-.md` |
| #914 | PPT Generation Assistant | Technik & Alltag | `technik-alltag/914-ppt-generation-assistant.md` |
| #915 | Chinese to English Translation Assistant | Lernen & Wachstum | `lernen-wachstum/915-chinese-to-english-translation-assistant.md` |
| #916 | Continue and Recap Assistant | Technik & Alltag | `technik-alltag/916-continue-and-recap-assistant.md` |
| #917 | Optimize E-commerce Listing for High CTR with Holiday Design | Technik & Alltag | `technik-alltag/917-optimize-e-commerce-listing-for-high-ctr.md` |
| #918 | Coding Structure with MVC and SOLID Principles | Technik & Alltag | `technik-alltag/918-coding-structure-with-mvc-and-solid-prin.md` |
| #919 | Email Marketing | Alltag & Leben | `alltag-leben/919-email-marketing.md` |
| #920 | Excel Formula Sensei | Technik & Alltag | `technik-alltag/920-excel-formula-sensei.md` |
| #921 | Universal Lead & Candidate Outreach Generator (HR, SALES) | Technik & Alltag | `technik-alltag/921-universal-lead-candidate-outreach-genera.md` |
| #922 | Subject meditating in a crystal sphere | Technik & Alltag | `technik-alltag/922-subject-meditating-in-crystal-sphere.md` |
| #923 | FAQ Generator | Technik & Alltag | `technik-alltag/923-faq-generator.md` |
| #924 | Text-to-Image with Reference - Billiards Bar Scene | Technik & Alltag | `technik-alltag/924-text-to-image-with-reference-billiards-b.md` |
| #925 | görsel | Technik & Alltag | `technik-alltag/925-g-rsel.md` |
| #926 | Chinese Hookah Training Program | Technik & Alltag | `technik-alltag/926-chinese-hookah-training-program.md` |
| #927 | Nietzschean Mentor for Holistic Growth | Lernen & Wachstum | `lernen-wachstum/927-nietzschean-mentor-for-holistic-growth.md` |
| #928 | berre | Technik & Alltag | `technik-alltag/928-berre.md` |
| #929 | .NET API Project Analysis | Technik & Alltag | `technik-alltag/929-net-api-project-analysis.md` |
| #930 | Set Up W&B and Run Pod During Training | Technik & Alltag | `technik-alltag/930-set-up-w-b-and-run-pod-during-training.md` |
| #931 | Secteur Bancaire - Email Professionnel | Technik & Alltag | `technik-alltag/931-secteur-bancaire-email-professionnel.md` |
| #932 | Modern Fashion Photography | Kommunikation & Beziehungen | `kommunikation-beziehungen/932-modern-fashion-photography.md` |
| #933 | Sunny Beach | Technik & Alltag | `technik-alltag/933-sunny-beach.md` |
| #934 | Mirror Product Photo | Technik & Alltag | `technik-alltag/934-mirror-product-photo.md` |
| #935 | Hata Tespiti için Kod İnceleme Asistanı | Technik & Alltag | `technik-alltag/935-hata-tespiti-i-in-kod-i-nceleme-asistan.md` |
| #936 | Using StanfordVL/BEHAVIOR-1K for Robotics and AI Tasks | Alltag & Leben | `alltag-leben/936-using-stanfordvl-behavior-1k-for-robotic.md` |
| #937 | Giant Object in City | Technik & Alltag | `technik-alltag/937-giant-object-in-city.md` |
| #938 | Deep Copy Functionality | Technik & Alltag | `technik-alltag/938-deep-copy-functionality.md` |
| #939 | Annual Leave Balance Adjustment Processor | Technik & Alltag | `technik-alltag/939-annual-leave-balance-adjustment-processo.md` |
| #940 | Master App Store Localization & ASO Prompt (2025) – Full Metadata Generator | Technik & Alltag | `technik-alltag/940-master-app-store-localization-aso-prompt.md` |
| #941 | Form Validation Rules for Leave Requests | Technik & Alltag | `technik-alltag/941-form-validation-rules-for-leave-requests.md` |
| #942 | PowerShell Script for Managing Disabled AD Users | Technik & Alltag | `technik-alltag/942-powershell-script-for-managing-disabled-.md` |
| #943 | PowerShell Script to Move Disabled AD Users to Specific OU | Technik & Alltag | `technik-alltag/943-powershell-script-to-move-disabled-ad-us.md` |
| #944 | Visual Web Application Development | Technik & Alltag | `technik-alltag/944-visual-web-application-development.md` |
| #945 | Playing Card Sorcerer Portrait | Technik & Alltag | `technik-alltag/945-playing-card-sorcerer-portrait.md` |
| #946 | Personalized Technical Intelligence Briefing for Edge AI in Defense | Alltag & Leben | `alltag-leben/946-personalized-technical-intelligence-brie.md` |
| #947 | One-Click Design Mockup Creator | Technik & Alltag | `technik-alltag/947-one-click-design-mockup-creator.md` |
| #948 | Vintage Invention Patent | Technik & Alltag | `technik-alltag/948-vintage-invention-patent.md` |
| #949 | A Wrinkle in Time | Technik & Alltag | `technik-alltag/949-a-wrinkle-in-time.md` |
| #950 | Create Python Dev Container | Technik & Alltag | `technik-alltag/950-create-python-dev-container.md` |
| #951 | Protocol 2084: The Alleyway Hack | Technik & Alltag | `technik-alltag/951-protocol-2084-alleyway-hack.md` |
| #952 | Expo + Supabase Edge Function Cold Start & Mobile Performance Analysis | Technik & Alltag | `technik-alltag/952-expo-supabase-edge-function-cold-start-m.md` |
| #953 | Cold Start Safe Architecture | Technik & Alltag | `technik-alltag/953-cold-start-safe-architecture.md` |
| #954 | Immigration Project Presentation Specialist | Technik & Alltag | `technik-alltag/954-immigration-project-presentation-special.md` |
| #955 | Blog System Development Guide | Alltag & Leben | `alltag-leben/955-blog-system-development-guide.md` |
| #956 | Customized Gift Idea Brainstorm Assistant | Technik & Alltag | `technik-alltag/956-customized-gift-idea-brainstorm-assistan.md` |
| #957 | Flight Tracker Desktop Application | Technik & Alltag | `technik-alltag/957-flight-tracker-desktop-application.md` |
| #958 | File Renaming Dashboard App | Technik & Alltag | `technik-alltag/958-file-renaming-dashboard-app.md` |
| #959 | Letter from Lisa: A Heartfelt Plea to Her Father | Technik & Alltag | `technik-alltag/959-letter-from-lisa-heartfelt-plea-to-her-f.md` |
| #960 | Ultra-Realistic Handwritten Hospital Note Image | Technik & Alltag | `technik-alltag/960-ultra-realistic-handwritten-hospital-not.md` |
| #961 | Develop a Notion Clone Application | Technik & Alltag | `technik-alltag/961-develop-notion-clone-application.md` |
| #962 | The Aether Prince at the Crystal Gala | Technik & Alltag | `technik-alltag/962-the-aether-prince-at-crystal-gala.md` |
| #963 | Langgraph微信公众号介绍 | Kommunikation & Beziehungen | `kommunikation-beziehungen/963-langgraph.md` |
| #964 | AST Code Analysis Superpower | Technik & Alltag | `technik-alltag/964-ast-code-analysis-superpower.md` |
| #965 | AWS Cloud Expert | Technik & Alltag | `technik-alltag/965-aws-cloud-expert.md` |
| #966 | Accessibility Expert | Technik & Alltag | `technik-alltag/966-accessibility-expert.md` |
| #967 | Accessibility Testing Superpower | Technik & Alltag | `technik-alltag/967-accessibility-testing-superpower.md` |
| #968 | Agent Organization Expert | Alltag & Leben | `alltag-leben/968-agent-organization-expert.md` |
| #969 | Hyper-Realistic X-Wing Battle Damage Images | Technik & Alltag | `technik-alltag/969-hyper-realistic-x-wing-battle-damage-ima.md` |
| #970 | FDTD Simulations of Nanoparticles | Technik & Alltag | `technik-alltag/970-fdtd-simulations-of-nanoparticles.md` |
| #971 | Secteur Bancaire - Analyse rapide d’un tableau de données | Technik & Alltag | `technik-alltag/971-secteur-bancaire-analyse-rapide-d-un-tab.md` |
| #972 | Secteur Bancaire - Vérification de conformité de texte | Technik & Alltag | `technik-alltag/972-secteur-bancaire-v-rification-de-conform.md` |
| #973 | Professional Website Design Consultant | Beruf & Karriere | `beruf-karriere/973-professional-website-design-consultant.md` |
| #974 | Default Meeting Summary | Technik & Alltag | `technik-alltag/974-default-meeting-summary.md` |
| #975 | Custom Localization and AI Integration for Apps | Technik & Alltag | `technik-alltag/975-custom-localization-and-ai-integration-f.md` |
| #976 | Personalized GPT Assistant Prompt | Alltag & Leben | `alltag-leben/976-personalized-gpt-assistant-prompt.md` |
| #977 | Modern Video Player with Sharp UI | Technik & Alltag | `technik-alltag/977-modern-video-player-with-sharp-ui.md` |
| #978 | Secteur Bancaire - Création d’un texte marketing simple | Technik & Alltag | `technik-alltag/978-secteur-bancaire-cr-ation-d-un-texte-mar.md` |
| #979 | Psychology Clinic Assistant | Technik & Alltag | `technik-alltag/979-psychology-clinic-assistant.md` |
| #980 | Isometric 3D Cartoon Scene with Weather Effects | Kreativitaet & Freizeit | `kreativitaet-freizeit/980-isometric-3d-cartoon-scene-with-weather-.md` |
| #981 | Node.js Automation Script Developer | Technik & Alltag | `technik-alltag/981-node-js-automation-script-developer.md` |
| #982 | Smart Application Developer Assistant | Technik & Alltag | `technik-alltag/982-smart-application-developer-assistant.md` |
| #983 | Website Creation Command | Alltag & Leben | `alltag-leben/983-website-creation-command.md` |
| #984 | Darksynth Synthwave Music Composition Guide | Kreativitaet & Freizeit | `kreativitaet-freizeit/984-darksynth-synthwave-music-composition-gu.md` |
| #985 | roster | Technik & Alltag | `technik-alltag/985-roster.md` |
| #986 | Cinematic Realism | Technik & Alltag | `technik-alltag/986-cinematic-realism.md` |
| #987 | 3D Character Render In High-End Disney Pixar Style | Kreativitaet & Freizeit | `kreativitaet-freizeit/987-3d-character-render-in-high-end-disney-p.md` |
| #988 | Serene Evening Rowboat Scene in Illustrative Realism | Technik & Alltag | `technik-alltag/988-serene-evening-rowboat-scene-in-illustra.md` |
| #989 | Minimalist Landscape Illustration by Ryo Takemasa | Technik & Alltag | `technik-alltag/989-minimalist-landscape-illustration-by-ryo.md` |
| #990 | Comprehensive Image Analysis Report | Technik & Alltag | `technik-alltag/990-comprehensive-image-analysis-report.md` |
| #991 | A Half-Built Pyramid and the Leader Who Turned Labor Into Legacy | Technik & Alltag | `technik-alltag/991-a-half-built-pyramid-and-leader-who-turn.md` |
| #992 | App Store Submission Agent | Alltag & Leben | `alltag-leben/992-app-store-submission-agent.md` |
| #993 | Comprehensive Web Application Development with Security and Performance Optimization | Alltag & Leben | `alltag-leben/993-comprehensive-web-application-developmen.md` |
| #994 | The Missing Woman | Technik & Alltag | `technik-alltag/994-the-missing-woman.md` |
| #995 | Photo-to-Isometric: Reality Slice Generator | Technik & Alltag | `technik-alltag/995-photo-to-isometric-reality-slice-generat.md` |
| #996 | Shadows of the Blue Note | Technik & Alltag | `technik-alltag/996-shadows-of-blue-note.md` |
| #997 | Strategic App Design & Content Engineering Prompt | Technik & Alltag | `technik-alltag/997-strategic-app-design-content-engineering.md` |
| #998 | English Teacher for Translation and Cultural Explanation | Lernen & Wachstum | `lernen-wachstum/998-english-teacher-for-translation-and-cult.md` |
| #999 | AI Assistant for University Assignments | Technik & Alltag | `technik-alltag/999-ai-assistant-for-university-assignments.md` |
| #1000 | Base64 Promt | Technik & Alltag | `technik-alltag/1000-base64-promt.md` |
| #1001 | 3D Isometric Miniature City View with Weather | Technik & Alltag | `technik-alltag/1001-3d-isometric-miniature-city-view-with-we.md` |
| #1002 | Edit a New Year's Video for Antioch Textile with Nano Banana | Technik & Alltag | `technik-alltag/1002-edit-new-year-s-video-for-antioch-textil.md` |
| #1003 | New Year Celebration Video for Antioch Textile | Technik & Alltag | `technik-alltag/1003-new-year-celebration-video-for-antioch-t.md` |
| #1004 | Automate Repository Management with OpenCode CLI | Technik & Alltag | `technik-alltag/1004-automate-repository-management-with-open.md` |
| #1005 | Photorealistic Selfie Portrait Description | Technik & Alltag | `technik-alltag/1005-photorealistic-selfie-portrait-descripti.md` |
| #1006 | Bathroom Flash Selfie (IG-candid, non-explicit) | Technik & Alltag | `technik-alltag/1006-bathroom-flash-selfie-ig-candid-non-expl.md` |
| #1007 | Elevator Mirror OOTD (full-body) | Technik & Alltag | `technik-alltag/1007-elevator-mirror-ootd-full-body.md` |
| #1008 | Snowy Street Cozy (winter fit, cinematic) | Technik & Alltag | `technik-alltag/1008-snowy-street-cozy-winter-fit-cinematic.md` |
| #1009 | Nano Banana Pro Prompt Generator Instruction (Outputs JSON blocks like these) | Technik & Alltag | `technik-alltag/1009-nano-banana-pro-prompt-generator-instruc.md` |
| #1010 | Gym Mirror (UGC realism, no logos) | Technik & Alltag | `technik-alltag/1010-gym-mirror-ugc-realism-no-logos.md` |
| #1011 | merge | Technik & Alltag | `technik-alltag/1011-merge.md` |
| #1012 | Prompt Writer for Specific Project | Technik & Alltag | `technik-alltag/1012-prompt-writer-for-specific-project.md` |
| #1013 | Open Source / Free License Selection Assistant | Technik & Alltag | `technik-alltag/1013-open-source-free-license-selection-assis.md` |
| #1014 | License Selection Assistant from Intellectual Property expert | Technik & Alltag | `technik-alltag/1014-license-selection-assistant-from-intelle.md` |
| #1015 | Act as a Resume Reviewer | Beruf & Karriere | `beruf-karriere/1015-resume-reviewer.md` |
| #1016 | Act as a Resume Reviewer for Anthropic Fellows Program | Beruf & Karriere | `beruf-karriere/1016-resume-reviewer-for-anthropic-fellows-pr.md` |
| #1017 | Structured Job Application Cleanup | Technik & Alltag | `technik-alltag/1017-structured-job-application-cleanup.md` |
| #1018 | Cafe Window Seat (close-up, tactile realism) | Technik & Alltag | `technik-alltag/1018-cafe-window-seat-close-up-tactile-realis.md` |
| #1019 | Rooftop Sunset Lookback (half-body) | Technik & Alltag | `technik-alltag/1019-rooftop-sunset-lookback-half-body.md` |
| #1020 | Rainy Umbrella Street (full-body) | Technik & Alltag | `technik-alltag/1020-rainy-umbrella-street-full-body.md` |
| #1021 | Night Neon Alley (half-body, edgy) | Technik & Alltag | `technik-alltag/1021-night-neon-alley-half-body-edgy.md` |
| #1022 | Cozy Couch Lamp (close-up, warm tungsten) | Technik & Alltag | `technik-alltag/1022-cozy-couch-lamp-close-up-warm-tungsten.md` |
| #1023 | Plant Bouquet Warm Lamp (your example vibe, adult-safe) | Technik & Alltag | `technik-alltag/1023-plant-bouquet-warm-lamp-your-example-vib.md` |
| #1024 | Airport Corridor Walk (full-body) | Alltag & Leben | `alltag-leben/1024-airport-corridor-walk-full-body.md` |
| #1025 | Museum Steps (full-body, cultural) | Technik & Alltag | `technik-alltag/1025-museum-steps-full-body-cultural.md` |
| #1026 | Nightclub Booth Flash (half-body, party candids) | Technik & Alltag | `technik-alltag/1026-nightclub-booth-flash-half-body-party-ca.md` |
| #1027 | Studio Beauty Editorial (close-up, pro) | Technik & Alltag | `technik-alltag/1027-studio-beauty-editorial-close-up-pro.md` |
| #1028 | Beach Walk Golden Hour (full-body, travel) | Alltag & Leben | `alltag-leben/1028-beach-walk-golden-hour-full-body-travel.md` |
| #1029 | Tech Desk “Builder” (half-body, cozy monitor glow) | Technik & Alltag | `technik-alltag/1029-tech-desk-builder-half-body-cozy-monitor.md` |
| #1030 | Restaurant Candle Close-up (intimate, not explicit) | Technik & Alltag | `technik-alltag/1030-restaurant-candle-close-up-intimate-not-.md` |
| #1031 | Minimal Studio “iPhone Candid” (pro-quality but awkward framing) | Technik & Alltag | `technik-alltag/1031-minimal-studio-iphone-candid-pro-quality.md` |
| #1032 | “Blue Hour Bridge” (full-body, cinematic but still IG) | Technik & Alltag | `technik-alltag/1032-blue-hour-bridge-full-body-cinematic-but.md` |
| #1033 | Kitchen Morning Window Light (candid, cozy) | Technik & Alltag | `technik-alltag/1033-kitchen-morning-window-light-candid-cozy.md` |
| #1034 | Bookstore Aisle (artsy, quiet luxury) | Technik & Alltag | `technik-alltag/1034-bookstore-aisle-artsy-quiet-luxury.md` |
| #1035 | Passenger Seat Car Selfie (golden hour, candid) | Alltag & Leben | `alltag-leben/1035-passenger-seat-car-selfie-golden-hour-ca.md` |
| #1036 | Balcony Coffee (morning haze, plant vibe) | Technik & Alltag | `technik-alltag/1036-balcony-coffee-morning-haze-plant-vibe.md` |
| #1037 | Subway Platform (street candid, moody) | Technik & Alltag | `technik-alltag/1037-subway-platform-street-candid-moody.md` |
| #1038 | Farmers Market (colorful produce, candid) | Technik & Alltag | `technik-alltag/1038-farmers-market-colorful-produce-candid.md` |
| #1039 | Hotel Hallway Fit Check (mirror vibe, no phone shown) | Technik & Alltag | `technik-alltag/1039-hotel-hallway-fit-check-mirror-vibe-no-p.md` |
| #1040 | Pilates Studio (soft daylight, athletic elegance) | Technik & Alltag | `technik-alltag/1040-pilates-studio-soft-daylight-athletic-el.md` |
| #1041 | Grocery Aisle (relatable, comedic-candid) | Technik & Alltag | `technik-alltag/1041-grocery-aisle-relatable-comedic-candid.md` |
| #1042 | Codebase WIKI Documentation Skill | Technik & Alltag | `technik-alltag/1042-codebase-wiki-documentation-skill.md` |
| #1043 | Graduate Information and Communication System Design | Beruf & Karriere | `beruf-karriere/1043-graduate-information-and-communication-s.md` |
| #1044 | Directive Assistant: Domina | Technik & Alltag | `technik-alltag/1044-directive-assistant-domina.md` |
| #1045 | Non-Technical IT Help & Clarity Assistant | Technik & Alltag | `technik-alltag/1045-non-technical-it-help-clarity-assistant.md` |
| #1046 | Cinematic Triptych: A Day in the Countryside | Technik & Alltag | `technik-alltag/1046-cinematic-triptych-day-in-countryside.md` |
| #1047 | Cinematic Photography Triptych: Serene Meadow Portrait | Technik & Alltag | `technik-alltag/1047-cinematic-photography-triptych-serene-me.md` |
| #1048 | Cinematic Neo-Noir Triptych in Digital Art | Alltag & Leben | `alltag-leben/1048-cinematic-neo-noir-triptych-in-digital-a.md` |
| #1049 | PlainTalk Style Guide | Alltag & Leben | `alltag-leben/1049-plaintalk-style-guide.md` |
| #1050 | A broken, soul-crushed medieval knight | Alltag & Leben | `alltag-leben/1050-a-broken-soul-crushed-medieval-knight.md` |
| #1051 | Matrix Paradise Seraph | Technik & Alltag | `technik-alltag/1051-matrix-paradise-seraph.md` |
| #1052 | Retro-futuristic 1970s sci-fi | Technik & Alltag | `technik-alltag/1052-retro-futuristic-1970s-sci-fi.md` |
| #1053 | A retro-styled adventurer takes a pause by a lush jungle riverbank. | Technik & Alltag | `technik-alltag/1053-a-retro-styled-adventurer-takes-pause-by.md` |
| #1054 | A relaxed copper-haired woman resting sideways on a bed in a soft, low-light setting. | Technik & Alltag | `technik-alltag/1054-a-relaxed-copper-haired-woman-resting-si.md` |
| #1055 | Art-W | Technik & Alltag | `technik-alltag/1055-art-w.md` |
| #1056 | İngilizce-Türkçe Kelime ve Cümle Çevirmeni | Lernen & Wachstum | `lernen-wachstum/1056-i-ngilizce-t-rk-e-kelime-ve-c-mle-evirme.md` |
| #1057 | Cinematic Urban Night Portrait - Moody Streetwear Aesthetic | Technik & Alltag | `technik-alltag/1057-cinematic-urban-night-portrait-moody-str.md` |
| #1058 | Quiet Glow | Technik & Alltag | `technik-alltag/1058-quiet-glow.md` |
| #1059 | Household Maintenance & Safety Assistant | Technik & Alltag | `technik-alltag/1059-household-maintenance-safety-assistant.md` |
| #1060 | Where the Kami Still Walk | Technik & Alltag | `technik-alltag/1060-where-kami-still-walk.md` |
| #1061 | Iterative Prompt Refinement Loop | Technik & Alltag | `technik-alltag/1061-iterative-prompt-refinement-loop.md` |
| #1062 | Creating a Project Management Tool | Technik & Alltag | `technik-alltag/1062-creating-project-management-tool.md` |
| #1063 | 3x3 Grid Storyboarding from Photo | Kreativitaet & Freizeit | `kreativitaet-freizeit/1063-3x3-grid-storyboarding-from-photo.md` |
| #1064 | "University Website Section Designer" | Technik & Alltag | `technik-alltag/1064-university-website-section-designer.md` |
| #1065 | Surreal City Scene | Technik & Alltag | `technik-alltag/1065-surreal-city-scene.md` |
| #1066 | Language Detection | Lernen & Wachstum | `lernen-wachstum/1066-language-detection.md` |
| #1067 | Aesthetic Mirror Selfie of a Curly-Haired Woman in a Mocha Ribbed Crop Top | Technik & Alltag | `technik-alltag/1067-aesthetic-mirror-selfie-of-curly-haired-.md` |
| #1068 | Joyful Woman in Nordic Sweater Dancing at a Nostalgic Family Christmas Gathering | Technik & Alltag | `technik-alltag/1068-joyful-woman-in-nordic-sweater-dancing-a.md` |
| #1069 | Detailed Image Analysis of a Mirror Selfie in a Bedroom Environment | Technik & Alltag | `technik-alltag/1069-detailed-image-analysis-of-mirror-selfie.md` |
| #1070 | Outdoor Staircase Image Analysis | Technik & Alltag | `technik-alltag/1070-outdoor-staircase-image-analysis.md` |
| #1071 | Study Review Companion | Technik & Alltag | `technik-alltag/1071-study-review-companion.md` |
| #1072 | Cinematic Street Photography Prompt | Technik & Alltag | `technik-alltag/1072-cinematic-street-photography-prompt.md` |
| #1073 | Extreme Close-up Macro Photography of a Young Woman's Face | Technik & Alltag | `technik-alltag/1073-extreme-close-up-macro-photography-of-yo.md` |
| #1074 | Ethereal Dreamlike Portrait Photography | Kreativitaet & Freizeit | `kreativitaet-freizeit/1074-ethereal-dreamlike-portrait-photography.md` |
| #1075 | Tropical Elegance: A Serene Afternoon in a Sunlit Villa | Technik & Alltag | `technik-alltag/1075-tropical-elegance-serene-afternoon-in-su.md` |
| #1076 | Investment Tracking Dashboard | Technik & Alltag | `technik-alltag/1076-investment-tracking-dashboard.md` |
| #1077 | Yağlı boya tablona bak | Technik & Alltag | `technik-alltag/1077-ya-l-boya-tablona-bak.md` |
| #1078 | Avant-Garde Portrait with Ghost Duplicate in Ochre Studio | Technik & Alltag | `technik-alltag/1078-avant-garde-portrait-with-ghost-duplicat.md` |
| #1079 | Reflected Self-Portrait in an Urban Convex Traffic Mirror | Technik & Alltag | `technik-alltag/1079-reflected-self-portrait-in-urban-convex-.md` |
| #1080 | Comprehensive Digital Marketing Strategy for Fashion Brand | Technik & Alltag | `technik-alltag/1080-comprehensive-digital-marketing-strategy.md` |
| #1081 | Professional GitHub Dashboard for Portfolio Enhancement | Technik & Alltag | `technik-alltag/1081-professional-github-dashboard-for-portfo.md` |
| #1082 | Guía para Diseñar y Vender un Libro en Hotmart | Alltag & Leben | `alltag-leben/1082-gu-a-para-dise-ar-y-vender-un-libro-en-h.md` |
| #1083 | Candle Pattern Trading Chart Generator | Beruf & Karriere | `beruf-karriere/1083-candle-pattern-trading-chart-generator.md` |
| #1084 | Candlestick Reversal Pattern Detector in Pine Script | Technik & Alltag | `technik-alltag/1084-candlestick-reversal-pattern-detector-in.md` |
| #1085 | Finance Tracker App Development Plan | Technik & Alltag | `technik-alltag/1085-finance-tracker-app-development-plan.md` |
| #1086 | English Language Tutor for Turkish Speakers | Lernen & Wachstum | `lernen-wachstum/1086-english-language-tutor-for-turkish-speak.md` |
| #1087 | Security Guard Image Prompt | Technik & Alltag | `technik-alltag/1087-security-guard-image-prompt.md` |
| #1088 | Product Promotion Expert | Technik & Alltag | `technik-alltag/1088-product-promotion-expert.md` |
| #1089 | Research Project Analysis and IPD Feasibility Recommendations | Beruf & Karriere | `beruf-karriere/1089-research-project-analysis-and-ipd-feasib.md` |
| #1090 | English Practice App Guide | Alltag & Leben | `alltag-leben/1090-english-practice-app-guide.md` |
| #1091 | Enterprise Microservices Architecture Design | Technik & Alltag | `technik-alltag/1091-enterprise-microservices-architecture-de.md` |
| #1092 | SwiftUI iOS App Development Guide | Alltag & Leben | `alltag-leben/1092-swiftui-ios-app-development-guide.md` |
| #1093 | A young woman relaxing in a wicker chair on a sunlit Mediterranean balcony. | Technik & Alltag | `technik-alltag/1093-a-young-woman-relaxing-in-wicker-chair-o.md` |
| #1094 | Amateur Girls' Night Selfie - Casual and Imperfect | Technik & Alltag | `technik-alltag/1094-amateur-girls-night-selfie-casual-and-im.md` |
| #1095 | Evening at a Turkish Dessert Shop - A Photographic Story | Kreativitaet & Freizeit | `kreativitaet-freizeit/1095-evening-at-turkish-dessert-shop-photogra.md` |
| #1096 | Image Analysis for Night Portrait in Heavy Snowfall | Technik & Alltag | `technik-alltag/1096-image-analysis-for-night-portrait-in-hea.md` |
| #1097 | Night Shift Dessert Shop | Kreativitaet & Freizeit | `kreativitaet-freizeit/1097-night-shift-dessert-shop.md` |
| #1098 | Ultra-Realistic Ankara Indie Bar Scene Description | Technik & Alltag | `technik-alltag/1098-ultra-realistic-ankara-indie-bar-scene-d.md` |
| #1099 | Night Balcony Scene in Ankara with Efes | Kommunikation & Beziehungen | `kommunikation-beziehungen/1099-night-balcony-scene-in-ankara-with-efes.md` |
| #1100 | Ankara Night Scene in a Meyhane | Kreativitaet & Freizeit | `kreativitaet-freizeit/1100-ankara-night-scene-in-meyhane.md` |
| #1101 | Ultra-Realistic Turkish Living Room Scene During Football Match | Kreativitaet & Freizeit | `kreativitaet-freizeit/1101-ultra-realistic-turkish-living-room-scen.md` |
| #1102 | Snapshot of a Turkish Hospital Night: A Dramedy Scene | Spezielle Situationen | `spezielle-situationen/1102-snapshot-of-turkish-hospital-night-drame.md` |
| #1103 | Photorealistic Mirror Selfie Analysis | Technik & Alltag | `technik-alltag/1103-photorealistic-mirror-selfie-analysis.md` |
| #1104 | Ultra-Realistic Night Scene in a Turkish Kitchen | Technik & Alltag | `technik-alltag/1104-ultra-realistic-night-scene-in-turkish-k.md` |
| #1105 | Ultra-Realistic Comedic Slice-of-Life in an Ankara Bus | Kreativitaet & Freizeit | `kreativitaet-freizeit/1105-ultra-realistic-comedic-slice-of-life-in.md` |
| #1106 | Cozy Night in Ankara: A Turkish TV Series Snapshot | Kreativitaet & Freizeit | `kreativitaet-freizeit/1106-cozy-night-in-ankara-turkish-tv-series-s.md` |
| #1107 | Ultra-Realistic Ankara Apartment Night Scene | Technik & Alltag | `technik-alltag/1107-ultra-realistic-ankara-apartment-night-s.md` |
| #1108 | Cozy Ankara Night: Capturing a Realistic Bedroom Scene | Technik & Alltag | `technik-alltag/1108-cozy-ankara-night-capturing-realistic-be.md` |
| #1109 | Ultra-Realistic Street Photo Prompt: Turkish Woman in Ankara | Technik & Alltag | `technik-alltag/1109-ultra-realistic-street-photo-prompt-turk.md` |
| #1110 | Turkish woman in Ankara with a surreal twist | Technik & Alltag | `technik-alltag/1110-turkish-woman-in-ankara-with-surreal-twi.md` |
| #1111 | Ultra-Realistic Amateur Street Photo of Ankara Scene | Technik & Alltag | `technik-alltag/1111-ultra-realistic-amateur-street-photo-of-.md` |
| #1112 | Ultra-Realistic Ankara Street Photo with Surreal Element | Technik & Alltag | `technik-alltag/1112-ultra-realistic-ankara-street-photo-with.md` |
| #1113 | Realistic Photo of a Turkish Woman in a Street Setting | Technik & Alltag | `technik-alltag/1113-realistic-photo-of-turkish-woman-in-stre.md` |
| #1114 | Ultra Realistic Bedroom Selfie Description | Technik & Alltag | `technik-alltag/1114-ultra-realistic-bedroom-selfie-descripti.md` |
| #1115 | Ultra Realistic Candid Photo of a Turkish Woman in Istanbul Café | Technik & Alltag | `technik-alltag/1115-ultra-realistic-candid-photo-of-turkish-.md` |
| #1116 | Realistic Mirror-Selfie Scene Creation | Kreativitaet & Freizeit | `kreativitaet-freizeit/1116-realistic-mirror-selfie-scene-creation.md` |
| #1117 | Dual Lighting Narrative Scene | Alltag & Leben | `alltag-leben/1117-dual-lighting-narrative-scene.md` |
| #1118 | Amateur Mirror Selfie with Natural Look | Technik & Alltag | `technik-alltag/1118-amateur-mirror-selfie-with-natural-look.md` |
| #1119 | Realistic Amateur Vibe Candid Photography Prompt | Technik & Alltag | `technik-alltag/1119-realistic-amateur-vibe-candid-photograph.md` |
| #1120 | Bug Discovery Code Assistant | Technik & Alltag | `technik-alltag/1120-bug-discovery-code-assistant.md` |
| #1121 | Manim Code | Technik & Alltag | `technik-alltag/1121-manim-code.md` |
| #1122 | SEO Strategy for Container Tracking Keywords | Kommunikation & Beziehungen | `kommunikation-beziehungen/1122-seo-strategy-for-container-tracking-keyw.md` |
| #1123 | Excel Data to Figma Presentation Designer | Technik & Alltag | `technik-alltag/1123-excel-data-to-figma-presentation-designe.md` |
| #1124 | Comprehensive Repository Audit & Remediation Prompt | Technik & Alltag | `technik-alltag/1124-comprehensive-repository-audit-remediati.md` |
| #1125 | OpenAI Create Plan Skill | Technik & Alltag | `technik-alltag/1125-openai-create-plan-skill.md` |
| #1126 | Text Summarizer | Technik & Alltag | `technik-alltag/1126-text-summarizer.md` |
| #1127 | Course Assignment Grader | Technik & Alltag | `technik-alltag/1127-course-assignment-grader.md` |
| #1128 | Ethreal Current | Technik & Alltag | `technik-alltag/1128-ethreal-current.md` |
| #1129 | Create an Unofficial Instagram API | Technik & Alltag | `technik-alltag/1129-create-unofficial-instagram-api.md` |
| #1130 | Professional Full-Stack Developer for Network Mapping & Monitoring Application | Technik & Alltag | `technik-alltag/1130-professional-full-stack-developer-for-ne.md` |
| #1131 | Comprehensive POS Application Development with FIFO and Reporting | Technik & Alltag | `technik-alltag/1131-comprehensive-pos-application-developmen.md` |
| #1132 | Node Web App for Czech Invoice PDF Generation | Technik & Alltag | `technik-alltag/1132-node-web-app-for-czech-invoice-pdf-gener.md` |
| #1133 | Study Timer | Technik & Alltag | `technik-alltag/1133-study-timer.md` |
| #1134 | Sophisticated Istanbul Stroll | Technik & Alltag | `technik-alltag/1134-sophisticated-istanbul-stroll.md` |
| #1135 | Numerology Expert Guidance | Technik & Alltag | `technik-alltag/1135-numerology-expert-guidance.md` |
| #1136 | Man in a City | Technik & Alltag | `technik-alltag/1136-man-in-city.md` |
| #1137 | Build a UI Library for ESP32 | Technik & Alltag | `technik-alltag/1137-build-ui-library-for-esp32.md` |
| #1138 | ESP32 UI Library Development | Technik & Alltag | `technik-alltag/1138-esp32-ui-library-development.md` |
| #1139 | NBX | Lernen & Wachstum | `lernen-wachstum/1139-nbx.md` |
| #1140 | Sun-Drenched Outdoor Selfie of a Tattooed Female Subject with Tiki Decor | Technik & Alltag | `technik-alltag/1140-sun-drenched-outdoor-selfie-of-tattooed-.md` |
| #1141 | Bingo Game Creator | Kreativitaet & Freizeit | `kreativitaet-freizeit/1141-bingo-game-creator.md` |
| #1142 | SAP ABAP Carbon Footprint Module Graduation Project Documentation | Technik & Alltag | `technik-alltag/1142-sap-abap-carbon-footprint-module-graduat.md` |
| #1143 | Code Review Expert | Technik & Alltag | `technik-alltag/1143-code-review-expert.md` |
| #1144 | Networking Engineer Portfolio Website | Technik & Alltag | `technik-alltag/1144-networking-engineer-portfolio-website.md` |
| #1145 | Senior Java Backend Engineer Expert | Technik & Alltag | `technik-alltag/1145-senior-java-backend-engineer-expert.md` |
| #1146 | UGC-Style TikTok Script Generator for Gen Z Skincare | Technik & Alltag | `technik-alltag/1146-ugc-style-tiktok-script-generator-for-ge.md` |
| #1147 | Google Ads Title Copywriter | Technik & Alltag | `technik-alltag/1147-google-ads-title-copywriter.md` |
| #1148 | 2026 Size Neler getirecek | Lernen & Wachstum | `lernen-wachstum/1148-2026-size-neler-getirecek.md` |
| #1149 | PDF Shareholder Extractor | Technik & Alltag | `technik-alltag/1149-pdf-shareholder-extractor.md` |
| #1150 | 3D to 2D Floor Plan Converter | Technik & Alltag | `technik-alltag/1150-3d-to-2d-floor-plan-converter.md` |
| #1151 | Mechanical Part Render to Technical Drawing Converter | Alltag & Leben | `alltag-leben/1151-mechanical-part-render-to-technical-draw.md` |
| #1152 | 3D Mechanical Part Image to Technical Drawing Conversion | Alltag & Leben | `alltag-leben/1152-3d-mechanical-part-image-to-technical-dr.md` |
| #1153 | Cinematic Thriller Silhouette | Technik & Alltag | `technik-alltag/1153-cinematic-thriller-silhouette.md` |
| #1154 | Close-up black and white portrait | Technik & Alltag | `technik-alltag/1154-close-up-black-and-white-portrait.md` |
| #1155 | A blonde woman in a dreamy | Kreativitaet & Freizeit | `kreativitaet-freizeit/1155-a-blonde-woman-in-dreamy.md` |
| #1156 | Professional Image Creation for Printable Sales Materials | Technik & Alltag | `technik-alltag/1156-professional-image-creation-for-printabl.md` |
| #1157 | Expert Guidance for Acoustic and Deep Learning Research | Technik & Alltag | `technik-alltag/1157-expert-guidance-for-acoustic-and-deep-le.md` |
| #1158 | Security Monitoring with Wazuh: A Comprehensive Research Project | Technik & Alltag | `technik-alltag/1158-security-monitoring-with-wazuh-comprehen.md` |
| #1159 | Topic Article | Technik & Alltag | `technik-alltag/1159-topic-article.md` |
| #1160 | Advanced Text Converter for Large Datasets | Technik & Alltag | `technik-alltag/1160-advanced-text-converter-for-large-datase.md` |
| #1161 | Literature Review Writing Assistant | Technik & Alltag | `technik-alltag/1161-literature-review-writing-assistant.md` |
| #1162 | File Analysis API with Node.js and Express | Technik & Alltag | `technik-alltag/1162-file-analysis-api-with-node-js-and-expre.md` |
| #1163 | 2026 Mobile Poster Creator | Technik & Alltag | `technik-alltag/1163-2026-mobile-poster-creator.md` |
| #1164 | Ultimate 2025-2026 AI Life Strategist & Retrospective | Lernen & Wachstum | `lernen-wachstum/1164-ultimate-2025-2026-ai-life-strategist-re.md` |
| #1165 | Color Consistency Analysis and Adjustment | Technik & Alltag | `technik-alltag/1165-color-consistency-analysis-and-adjustmen.md` |
| #1166 | Fashion Photo Pose & Setting Transformation Editor | Technik & Alltag | `technik-alltag/1166-fashion-photo-pose-setting-transformatio.md` |
| #1167 | Asistente de Recetas de Cocina Chilena | Alltag & Leben | `alltag-leben/1167-asistente-de-recetas-de-cocina-chilena.md` |
| #1168 | Create a Video with Top Athletes | Technik & Alltag | `technik-alltag/1168-create-video-with-top-athletes.md` |
| #1169 | Neon Silence | Technik & Alltag | `technik-alltag/1169-neon-silence.md` |
| #1170 | Car poster | Alltag & Leben | `alltag-leben/1170-car-poster.md` |
| #1171 | Creative Storytelling Guide | Alltag & Leben | `alltag-leben/1171-creative-storytelling-guide.md` |
| #1172 | Academic Writing Workshop Plan | Technik & Alltag | `technik-alltag/1172-academic-writing-workshop-plan.md` |
| #1173 | Full-Stack Engineer for Airline Simulation Center App | Technik & Alltag | `technik-alltag/1173-full-stack-engineer-for-airline-simulati.md` |
| #1174 | Senior Product Engineer + Data Scientist for Turkish Car Valuation Platform | Technik & Alltag | `technik-alltag/1174-senior-product-engineer-data-scientist-f.md` |
| #1175 | Crafting LinkedIn Messages to Hiring Managers | Beruf & Karriere | `beruf-karriere/1175-crafting-linkedin-messages-to-hiring-man.md` |
| #1176 | Innovative Math Teaching Method | Lernen & Wachstum | `lernen-wachstum/1176-innovative-math-teaching-method.md` |
| #1177 | Professional Vision Statement for Transportation Company | Beruf & Karriere | `beruf-karriere/1177-professional-vision-statement-for-transp.md` |
| #1178 | Act as a Base LLM Model | Lernen & Wachstum | `lernen-wachstum/1178-base-llm-model.md` |
| #1179 | Act as an FTTH Telecommunications Expert | Technik & Alltag | `technik-alltag/1179-ftth-telecommunications-expert.md` |
| #1180 | Cinematic 3x3 Focal Lengths Grid | Technik & Alltag | `technik-alltag/1180-cinematic-3x3-focal-lengths-grid.md` |
| #1181 | 3D Medical Anatomy Model Render Prompt | Technik & Alltag | `technik-alltag/1181-3d-medical-anatomy-model-render-prompt.md` |
| #1182 | Digital Marketing Project Ideas for Students | Lernen & Wachstum | `lernen-wachstum/1182-digital-marketing-project-ideas-for-stud.md` |
| #1183 | Water Balance Management Platform Design | Technik & Alltag | `technik-alltag/1183-water-balance-management-platform-design.md` |
| #1184 | Hyper-Realistic Cinematic Pre-Dawn Scene in Ancient Mecca | Technik & Alltag | `technik-alltag/1184-hyper-realistic-cinematic-pre-dawn-scene.md` |
| #1185 | Moody Cinematic Portrait Photography | Technik & Alltag | `technik-alltag/1185-moody-cinematic-portrait-photography.md` |
| #1186 | Warm-Toned Creative Scene with Paper Figures | Technik & Alltag | `technik-alltag/1186-warm-toned-creative-scene-with-paper-fig.md` |
| #1187 | Nostalgic Road Trip - Atmospheric 35mm Film Photograph Prompt | Technik & Alltag | `technik-alltag/1187-nostalgic-road-trip-atmospheric-35mm-fil.md` |
| #1188 | Develop a Modern Website for Sporsmaç Using React Native | Technik & Alltag | `technik-alltag/1188-develop-modern-website-for-sporsma-using.md` |
| #1189 | ramones | Technik & Alltag | `technik-alltag/1189-ramones.md` |
| #1190 | Article Summarizer | Technik & Alltag | `technik-alltag/1190-article-summarizer.md` |
| #1191 | Research Paper Feature Diagram | Kreativitaet & Freizeit | `kreativitaet-freizeit/1191-research-paper-feature-diagram.md` |
| #1192 | Couples Therapy App Development Guide | Alltag & Leben | `alltag-leben/1192-couples-therapy-app-development-guide.md` |
| #1193 | AI Workflow Automation Specialist | Beruf & Karriere | `beruf-karriere/1193-ai-workflow-automation-specialist.md` |
| #1194 | AI Character Creation Guide | Kreativitaet & Freizeit | `kreativitaet-freizeit/1194-ai-character-creation-guide.md` |
| #1195 | Ultra-Realistic Young Woman Portrait Generation | Technik & Alltag | `technik-alltag/1195-ultra-realistic-young-woman-portrait-gen.md` |
| #1196 | Mom and boy | Technik & Alltag | `technik-alltag/1196-mom-and-boy.md` |
| #1197 | Spoken Word Artist Persona | Kreativitaet & Freizeit | `kreativitaet-freizeit/1197-spoken-word-artist-persona.md` |
| #1198 | Assistente de Geração de Imagens com Identidade Visual Padrão | Kommunikation & Beziehungen | `kommunikation-beziehungen/1198-assistente-de-gera-o-de-imagens-com-iden.md` |
| #1199 | Serene Mirror-Selfie Portrait in Sunlit Bedroom | Technik & Alltag | `technik-alltag/1199-serene-mirror-selfie-portrait-in-sunlit-.md` |
| #1200 | Candid Outdoor Group Photo in Natural Pool | Technik & Alltag | `technik-alltag/1200-candid-outdoor-group-photo-in-natural-po.md` |
| #1201 | Improving Business English | Beruf & Karriere | `beruf-karriere/1201-improving-business-english.md` |
| #1202 | URL, Title, and Description Analysis Tool with LSI Keywords | Kommunikation & Beziehungen | `kommunikation-beziehungen/1202-url-title-and-description-analysis-tool-.md` |
| #1203 | Ultra Photorealistic Rooftop Pool Portrait | Technik & Alltag | `technik-alltag/1203-ultra-photorealistic-rooftop-pool-portra.md` |
| #1204 | seo-fundamentals | Kommunikation & Beziehungen | `kommunikation-beziehungen/1204-seo-fundamentals.md` |
| #1205 | Mastermind | Technik & Alltag | `technik-alltag/1205-mastermind.md` |
| #1206 | Echoes of the Rust Age | Technik & Alltag | `technik-alltag/1206-echoes-of-rust-age.md` |
| #1207 | Corsairs of the Crimson Void | Technik & Alltag | `technik-alltag/1207-corsairs-of-crimson-void.md` |
| #1208 | Whispers in Light Trails | Technik & Alltag | `technik-alltag/1208-whispers-in-light-trails.md` |
| #1209 | The Aether Workshop | Technik & Alltag | `technik-alltag/1209-the-aether-workshop.md` |
| #1210 | Poe - Your Best Bud Chatbot | Kommunikation & Beziehungen | `kommunikation-beziehungen/1210-poe-your-best-bud-chatbot.md` |
| #1211 | Creative Short Story Writing | Kreativitaet & Freizeit | `kreativitaet-freizeit/1211-creative-short-story-writing.md` |
| #1212 | Custom AI Image Creation | Technik & Alltag | `technik-alltag/1212-custom-ai-image-creation.md` |
| #1213 | Créer une Carte Mentale pour Séance d'Idéation | Technik & Alltag | `technik-alltag/1213-cr-er-une-carte-mentale-pour-s-ance-d-id.md` |
| #1214 | Football Player Introduction Poster Template | Kommunikation & Beziehungen | `kommunikation-beziehungen/1214-football-player-introduction-poster-temp.md` |
| #1215 | Cinematic Close-Up of Craftsman with Paper Figures | Technik & Alltag | `technik-alltag/1215-cinematic-close-up-of-craftsman-with-pap.md` |
| #1216 | Comprehensive Roadmap for AI and Computer Vision Specialization in Defense Systems | Beruf & Karriere | `beruf-karriere/1216-comprehensive-roadmap-for-ai-and-compute.md` |
| #1217 | Young Saudi Doctor in a Professional Setting | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1217-young-saudi-doctor-in-professional-setti.md` |
| #1218 | Wary Bear in a Hostile Woodland | Technik & Alltag | `technik-alltag/1218-wary-bear-in-hostile-woodland.md` |
| #1219 | Code Review Specialist 2 | Technik & Alltag | `technik-alltag/1219-code-review-specialist-2.md` |
| #1220 | Integrity & Compliance Officer Audit Protocol | Technik & Alltag | `technik-alltag/1220-integrity-compliance-officer-audit-proto.md` |
| #1221 | transcript_to_notes | Technik & Alltag | `technik-alltag/1221-transcript-to-notes.md` |
| #1222 | Photorealistic Image Prompt for Fashion and Environment | Technik & Alltag | `technik-alltag/1222-photorealistic-image-prompt-for-fashion-.md` |
| #1223 | Exploring Gaps in Thesis Writing Literature with ChatGPT | Technik & Alltag | `technik-alltag/1223-exploring-gaps-in-thesis-writing-literat.md` |
| #1224 | Business Idea Feasibility and Technical Challenges Analysis | Beruf & Karriere | `beruf-karriere/1224-business-idea-feasibility-and-technical-.md` |
| #1225 | GitHub Repository Analysis and Enhancement | Technik & Alltag | `technik-alltag/1225-github-repository-analysis-and-enhanceme.md` |
| #1226 | Annual Summary Creator | Technik & Alltag | `technik-alltag/1226-annual-summary-creator.md` |
| #1227 | Inference Scenario Automation Tool | Technik & Alltag | `technik-alltag/1227-inference-scenario-automation-tool.md` |
| #1228 | Custom Logo Design for Website | Technik & Alltag | `technik-alltag/1228-custom-logo-design-for-website.md` |
| #1229 | Access Unlimited ChatGPT | Alltag & Leben | `alltag-leben/1229-access-unlimited-chatgpt.md` |
| #1230 | Create a PS5-themed Portfolio | Technik & Alltag | `technik-alltag/1230-create-ps5-themed-portfolio.md` |
| #1231 | Educational Platform Support Assistant | Lernen & Wachstum | `lernen-wachstum/1231-educational-platform-support-assistant.md` |
| #1232 | Understanding and Utilizing LLMs | Lernen & Wachstum | `lernen-wachstum/1232-understanding-and-utilizing-llms.md` |
| #1233 | Minimalist Editorial Beauty Analysis with European Model | Technik & Alltag | `technik-alltag/1233-minimalist-editorial-beauty-analysis-wit.md` |
| #1234 | Festive New Year 2026 Image Analysis | Technik & Alltag | `technik-alltag/1234-festive-new-year-2026-image-analysis.md` |
| #1235 | Act as an Electron Frontend Developer | Technik & Alltag | `technik-alltag/1235-electron-frontend-developer.md` |
| #1236 | SQL Query Generator from Natural Language | Lernen & Wachstum | `lernen-wachstum/1236-sql-query-generator-from-natural-languag.md` |
| #1237 | Generate Implementation Ideas from Word Document | Technik & Alltag | `technik-alltag/1237-generate-implementation-ideas-from-word-.md` |
| #1238 | Semantic Intent Analysis for Report Generation | Technik & Alltag | `technik-alltag/1238-semantic-intent-analysis-for-report-gene.md` |
| #1239 | Policy Agent Client Manager | Beruf & Karriere | `beruf-karriere/1239-policy-agent-client-manager.md` |
| #1240 | Hospital Pharmacy Course PDF Study Assistant | Technik & Alltag | `technik-alltag/1240-hospital-pharmacy-course-pdf-study-assis.md` |
| #1241 | White-Box Web Application Security Audit & Penetration Testing Prompt for AI Code Editors (Cursor, Windsurf, Antigravity) | Technik & Alltag | `technik-alltag/1241-white-box-web-application-security-audit.md` |
| #1242 | Collaborative AI Marketing Platform | Technik & Alltag | `technik-alltag/1242-collaborative-ai-marketing-platform.md` |
| #1243 | A night in paris | Technik & Alltag | `technik-alltag/1243-a-night-in-paris.md` |
| #1244 | Dynamic Recipe Generator from Available Ingredients | Alltag & Leben | `alltag-leben/1244-dynamic-recipe-generator-from-available-.md` |
| #1245 | Develop a Media Center Plan for Hajj | Technik & Alltag | `technik-alltag/1245-develop-media-center-plan-for-hajj.md` |
| #1246 | Super Trader Model for Stock Analysis | Technik & Alltag | `technik-alltag/1246-super-trader-model-for-stock-analysis.md` |
| #1247 | Elite Private Equity Fund Manager Stock Analysis | Beruf & Karriere | `beruf-karriere/1247-elite-private-equity-fund-manager-stock-.md` |
| #1248 | Red Dead Redemption 2 - Double Exposure Effect | Kreativitaet & Freizeit | `kreativitaet-freizeit/1248-red-dead-redemption-2-double-exposure-ef.md` |
| #1249 | The Witcher - Double Exposure Effect | Kreativitaet & Freizeit | `kreativitaet-freizeit/1249-the-witcher-double-exposure-effect.md` |
| #1250 | Dynamic Cover Letter Generator | Beruf & Karriere | `beruf-karriere/1250-dynamic-cover-letter-generator.md` |
| #1251 | CV Writing Assistant | Beruf & Karriere | `beruf-karriere/1251-cv-writing-assistant.md` |
| #1252 | Develop Android Apps from Screenshots | Technik & Alltag | `technik-alltag/1252-develop-android-apps-from-screenshots.md` |
| #1253 | Business Coaching Mentor | Beruf & Karriere | `beruf-karriere/1253-business-coaching-mentor.md` |
| #1254 | School Life Mentor | Lernen & Wachstum | `lernen-wachstum/1254-school-life-mentor.md` |
| #1255 | Taglish Technical Storytelling Editor | Technik & Alltag | `technik-alltag/1255-taglish-technical-storytelling-editor.md` |
| #1256 | Convert PDF to Markdown | Technik & Alltag | `technik-alltag/1256-convert-pdf-to-markdown.md` |
| #1257 | AI-powered data extraction and organization tool | Beruf & Karriere | `beruf-karriere/1257-ai-powered-data-extraction-and-organizat.md` |
| #1258 | VSCode CodeTour Expert Agent | Technik & Alltag | `technik-alltag/1258-vscode-codetour-expert-agent.md` |
| #1259 | Whispers of Noir | Technik & Alltag | `technik-alltag/1259-whispers-of-noir.md` |
| #1260 | The Midnight Informant | Technik & Alltag | `technik-alltag/1260-the-midnight-informant.md` |
| #1261 | Context7 Documentation Expert Agent | Technik & Alltag | `technik-alltag/1261-context7-documentation-expert-agent.md` |
| #1262 | Sports Research Assistant | Technik & Alltag | `technik-alltag/1262-sports-research-assistant.md` |
| #1263 | The Quant Edge Engine | Technik & Alltag | `technik-alltag/1263-the-quant-edge-engine.md` |
| #1264 | Yapper Twitter Strategist 2026 | Technik & Alltag | `technik-alltag/1264-yapper-twitter-strategist-2026.md` |
| #1265 | Geralt of Rivia Image Generation | Kreativitaet & Freizeit | `kreativitaet-freizeit/1265-geralt-of-rivia-image-generation.md` |
| #1266 | Fintech Product and Operations Assistant | Technik & Alltag | `technik-alltag/1266-fintech-product-and-operations-assistant.md` |
| #1267 | Vibe Coding Master | Technik & Alltag | `technik-alltag/1267-vibe-coding-master.md` |
| #1268 | Technical Codebase Discovery & Onboarding Prompt | Technik & Alltag | `technik-alltag/1268-technical-codebase-discovery-onboarding-.md` |
| #1269 | Multi-Audience Application Discovery & Documentation Prompt | Technik & Alltag | `technik-alltag/1269-multi-audience-application-discovery-doc.md` |
| #1270 | Comprehensive Integrative Medical Writing | Technik & Alltag | `technik-alltag/1270-comprehensive-integrative-medical-writin.md` |
| #1271 | Dear Sugar: Candid Advice on Love and Life | Technik & Alltag | `technik-alltag/1271-dear-sugar-candid-advice-on-love-and-lif.md` |
| #1272 | Narrative Point of View Transformer | Alltag & Leben | `alltag-leben/1272-narrative-point-of-view-transformer.md` |
| #1273 | Viral TikTok Glühwein Recipe in Five Languages | Lernen & Wachstum | `lernen-wachstum/1273-viral-tiktok-gl-hwein-recipe-in-five-lan.md` |
| #1274 | Cinematic Neon Alley – Urban Night Walk (Album Cover Style) | Technik & Alltag | `technik-alltag/1274-cinematic-neon-alley-urban-night-walk-al.md` |
| #1275 | Continuous Execution Mode AI | Technik & Alltag | `technik-alltag/1275-continuous-execution-mode-ai.md` |
| #1276 | Context Migration | Technik & Alltag | `technik-alltag/1276-context-migration.md` |
| #1277 | Ultra-Realistic Winter Cinematography Series | Technik & Alltag | `technik-alltag/1277-ultra-realistic-winter-cinematography-se.md` |
| #1278 | Comic Book Team Illustration | Alltag & Leben | `alltag-leben/1278-comic-book-team-illustration.md` |
| #1279 | Surrealist Painting Description: A Study of René Magritte's Style | Technik & Alltag | `technik-alltag/1279-surrealist-painting-description-study-of.md` |
| #1280 | Prepare for Meetings: Key Considerations | Technik & Alltag | `technik-alltag/1280-prepare-for-meetings-key-considerations.md` |
| #1281 | Diseño de Artículo de Revisión Sistemática para Revista Q1 sobre Sociedad y Cultura Caribeña | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1281-dise-o-de-art-culo-de-revisi-n-sistem-ti.md` |
| #1282 | Job and Internship Tracker for Google Sheets | Beruf & Karriere | `beruf-karriere/1282-job-and-internship-tracker-for-google-sh.md` |
| #1283 | Stock Analyser | Beruf & Karriere | `beruf-karriere/1283-stock-analyser.md` |
| #1284 | Web App for Task Management and Scheduling | Technik & Alltag | `technik-alltag/1284-web-app-for-task-management-and-scheduli.md` |
| #1285 | Ultra-High-Resolution Portrait Restoration | Technik & Alltag | `technik-alltag/1285-ultra-high-resolution-portrait-restorati.md` |
| #1286 | Nightlife Candid Flash Photography | Technik & Alltag | `technik-alltag/1286-nightlife-candid-flash-photography.md` |
| #1287 | Cartoon series | Kreativitaet & Freizeit | `kreativitaet-freizeit/1287-cartoon-series.md` |
| #1288 | Sentry Bug Fixer | Technik & Alltag | `technik-alltag/1288-sentry-bug-fixer.md` |
| #1289 | Meta-prompt | Technik & Alltag | `technik-alltag/1289-meta-prompt.md` |
| #1290 | Random Girl | Kreativitaet & Freizeit | `kreativitaet-freizeit/1290-random-girl.md` |
| #1291 | Dynamic character profile generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/1291-dynamic-character-profile-generator.md` |
| #1292 | Sticker | Kreativitaet & Freizeit | `kreativitaet-freizeit/1292-sticker.md` |
| #1293 | content | Technik & Alltag | `technik-alltag/1293-content.md` |
| #1294 | postmortem | Technik & Alltag | `technik-alltag/1294-postmortem.md` |
| #1295 | professional linguistic expert and translator | Lernen & Wachstum | `lernen-wachstum/1295-professional-linguistic-expert-and-trans.md` |
| #1296 | Slap Game Challenge: Act as the Ultimate Slap Game Master | Kreativitaet & Freizeit | `kreativitaet-freizeit/1296-slap-game-challenge-ultimate-slap-game-m.md` |
| #1297 | Vision-to-json | Technik & Alltag | `technik-alltag/1297-vision-to-json.md` |
| #1298 | The Midnight Melody Mystery | Technik & Alltag | `technik-alltag/1298-the-midnight-melody-mystery.md` |
| #1299 | Auditor de Código Python: Nivel Senior (Salida en Español) | Technik & Alltag | `technik-alltag/1299-auditor-de-c-digo-python-nivel-senior-sa.md` |
| #1300 | Present | Technik & Alltag | `technik-alltag/1300-present.md` |
| #1301 | Seaside walker | Technik & Alltag | `technik-alltag/1301-seaside-walker.md` |
| #1302 | SWOT Analysis for Political Risk and International Relations | Technik & Alltag | `technik-alltag/1302-swot-analysis-for-political-risk-and-int.md` |
| #1303 | Network Engineer | Technik & Alltag | `technik-alltag/1303-network-engineer.md` |
| #1304 | Commit Message Preparation | Technik & Alltag | `technik-alltag/1304-commit-message-preparation.md` |
| #1305 | Tattoo Studio Booking Web App Development | Technik & Alltag | `technik-alltag/1305-tattoo-studio-booking-web-app-developmen.md` |
| #1306 | DUT Citation Accuracy Project | Technik & Alltag | `technik-alltag/1306-dut-citation-accuracy-project.md` |
| #1307 | AI Process Feasibility Interview | Lernen & Wachstum | `lernen-wachstum/1307-ai-process-feasibility-interview.md` |
| #1308 | 12-Month AI and Computer Vision Roadmap for Defense Applications | Lernen & Wachstum | `lernen-wachstum/1308-12-month-ai-and-computer-vision-roadmap-.md` |
| #1309 | Article Summary Prompt | Technik & Alltag | `technik-alltag/1309-article-summary-prompt.md` |
| #1310 | AI Engineer | Technik & Alltag | `technik-alltag/1310-ai-engineer.md` |
| #1311 | Backend Architect | Technik & Alltag | `technik-alltag/1311-backend-architect.md` |
| #1312 | DevOps Automator | Technik & Alltag | `technik-alltag/1312-devops-automator.md` |
| #1313 | Frontend Developer | Technik & Alltag | `technik-alltag/1313-frontend-developer.md` |
| #1314 | Business | Beruf & Karriere | `beruf-karriere/1314-business.md` |
| #1315 | Mobile App Builder | Technik & Alltag | `technik-alltag/1315-mobile-app-builder.md` |
| #1316 | Rapid Prototyper | Technik & Alltag | `technik-alltag/1316-rapid-prototyper.md` |
| #1317 | Test Automation Expert | Technik & Alltag | `technik-alltag/1317-test-automation-expert.md` |
| #1318 | Feedback Synthesizer | Technik & Alltag | `technik-alltag/1318-feedback-synthesizer.md` |
| #1319 | Sprint Prioritizer | Technik & Alltag | `technik-alltag/1319-sprint-prioritizer.md` |
| #1320 | Trend Researcher | Technik & Alltag | `technik-alltag/1320-trend-researcher.md` |
| #1321 | Joker: Tech Humor Master | Technik & Alltag | `technik-alltag/1321-joker-tech-humor-master.md` |
| #1322 | UiPath XAML Code Review Specialist | Technik & Alltag | `technik-alltag/1322-uipath-xaml-code-review-specialist.md` |
| #1323 | The PRD Mastermind | Technik & Alltag | `technik-alltag/1323-the-prd-mastermind.md` |
| #1324 | Scam Detection Conversation Helper | Alltag & Leben | `alltag-leben/1324-scam-detection-conversation-helper.md` |
| #1325 | Serene Yoga & Mindfulness Lifestyle Photography | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1325-serene-yoga-mindfulness-lifestyle-photog.md` |
| #1326 | Mindful Mandala & Zen Geometric Patterns | Kreativitaet & Freizeit | `kreativitaet-freizeit/1326-mindful-mandala-zen-geometric-patterns.md` |
| #1327 | The Gravedigger's Vigil | Technik & Alltag | `technik-alltag/1327-the-gravedigger-s-vigil.md` |
| #1328 | Chinese-English Translator | Lernen & Wachstum | `lernen-wachstum/1328-chinese-english-translator.md` |
| #1329 | Multilingual Writing Improvement Assistant | Lernen & Wachstum | `lernen-wachstum/1329-multilingual-writing-improvement-assista.md` |
| #1330 | Terminal Drift | Technik & Alltag | `technik-alltag/1330-terminal-drift.md` |
| #1331 | Social Media Post Creator for Recruitment | Kommunikation & Beziehungen | `kommunikation-beziehungen/1331-social-media-post-creator-for-recruitmen.md` |
| #1332 | Prompt Generator for Language Models | Lernen & Wachstum | `lernen-wachstum/1332-prompt-generator-for-language-models.md` |
| #1333 | GPT_conversation_output | Technik & Alltag | `technik-alltag/1333-gpt-conversation-output.md` |
| #1334 | Master Prompt Architect & Context Engineer | Technik & Alltag | `technik-alltag/1334-master-prompt-architect-context-engineer.md` |
| #1335 | python | Technik & Alltag | `technik-alltag/1335-python.md` |
| #1336 | Creative Ideas Generator | Kommunikation & Beziehungen | `kommunikation-beziehungen/1336-creative-ideas-generator.md` |
| #1337 | MCP Builder | Alltag & Leben | `alltag-leben/1337-mcp-builder.md` |
| #1338 | Dreamy Artistic Photograph of a Young Woman in a Meadow | Kreativitaet & Freizeit | `kreativitaet-freizeit/1338-dreamy-artistic-photograph-of-young-woma.md` |
| #1339 | Surreal Miniature Cityscape with Giant Observer | Technik & Alltag | `technik-alltag/1339-surreal-miniature-cityscape-with-giant-o.md` |
| #1340 | Cinematic Close-Up Portrait Generation | Technik & Alltag | `technik-alltag/1340-cinematic-close-up-portrait-generation.md` |
| #1341 | Skill Creator | Alltag & Leben | `alltag-leben/1341-skill-creator.md` |
| #1342 | Ultimate Inpainting / Reference Prompt | Technik & Alltag | `technik-alltag/1342-ultimate-inpainting-reference-prompt.md` |
| #1343 | Universal Context Document (UCD) Generator | Technik & Alltag | `technik-alltag/1343-universal-context-document-ucd-generator.md` |
| #1344 | The tyrant King | Technik & Alltag | `technik-alltag/1344-the-tyrant-king.md` |
| #1345 | identify the key skills needed for effective project planning and proposal writing | Technik & Alltag | `technik-alltag/1345-identify-key-skills-needed-for-effective.md` |
| #1346 | Project Skill & Resource Interviewer | Beruf & Karriere | `beruf-karriere/1346-project-skill-resource-interviewer.md` |
| #1347 | Pokemon master | Kreativitaet & Freizeit | `kreativitaet-freizeit/1347-pokemon-master.md` |
| #1348 | Claude Code Skill (Slash Command): review-and-commit.md | Technik & Alltag | `technik-alltag/1348-claude-code-skill-slash-command-review-a.md` |
| #1349 | Customizable Job Scanner | Technik & Alltag | `technik-alltag/1349-customizable-job-scanner.md` |
| #1350 | AI Search Mastery Bootcamp | Alltag & Leben | `alltag-leben/1350-ai-search-mastery-bootcamp.md` |
| #1351 | create a drag-and-drop experience using UniApp | Technik & Alltag | `technik-alltag/1351-create-drag-and-drop-experience-using-un.md` |
| #1352 | Develop a creative dice generator called “IdeaDice”. | Technik & Alltag | `technik-alltag/1352-develop-creative-dice-generator-called-i.md` |
| #1353 | GLaDOS | Kreativitaet & Freizeit | `kreativitaet-freizeit/1353-glados.md` |
| #1354 | Prompt Architect Pro | Technik & Alltag | `technik-alltag/1354-prompt-architect-pro.md` |
| #1355 | Synthesis Architect Pro | Technik & Alltag | `technik-alltag/1355-synthesis-architect-pro.md` |
| #1356 | Create Organizational Charts and Workflows for University Departments | Technik & Alltag | `technik-alltag/1356-create-organizational-charts-and-workflo.md` |
| #1357 | Fisheye 90s | Technik & Alltag | `technik-alltag/1357-fisheye-90s.md` |
| #1358 | Analog camera | Technik & Alltag | `technik-alltag/1358-analog-camera.md` |
| #1359 | The Pragmatic Architect: Mastering Tech with Humor and Precision | Technik & Alltag | `technik-alltag/1359-the-pragmatic-architect-mastering-tech-w.md` |
| #1360 | Question Quality Lab Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/1360-question-quality-lab-game.md` |
| #1361 | nanobanana try clothing | Technik & Alltag | `technik-alltag/1361-nanobanana-try-clothing.md` |
| #1362 | NOOMS Brand Story & Portfolio Background – Storytelling Format | Technik & Alltag | `technik-alltag/1362-nooms-brand-story-portfolio-background-s.md` |
| #1363 | Statement of Purpose | Technik & Alltag | `technik-alltag/1363-statement-of-purpose.md` |
| #1364 | Big Room Festival Anthem Creation for Suno AI v5 | Kreativitaet & Freizeit | `kreativitaet-freizeit/1364-big-room-festival-anthem-creation-for-su.md` |
| #1365 | Markdown Task Implementer | Technik & Alltag | `technik-alltag/1365-markdown-task-implementer.md` |
| #1366 | Constraint-First Recipe Generator (Playful Edition) | Alltag & Leben | `alltag-leben/1366-constraint-first-recipe-generator-playfu.md` |
| #1367 | Wings of the Dust Bowl | Technik & Alltag | `technik-alltag/1367-wings-of-dust-bowl.md` |
| #1368 | The Last Adagio | Technik & Alltag | `technik-alltag/1368-the-last-adagio.md` |
| #1369 | Crimson Waltz in the Rain | Technik & Alltag | `technik-alltag/1369-crimson-waltz-in-rain.md` |
| #1370 | Manhattan Mirage | Technik & Alltag | `technik-alltag/1370-manhattan-mirage.md` |
| #1371 | The Glass Doppelgänger | Technik & Alltag | `technik-alltag/1371-the-glass-doppelg-nger.md` |
| #1372 | Phantom Strike | Technik & Alltag | `technik-alltag/1372-phantom-strike.md` |
| #1373 | GitHubTrends | Technik & Alltag | `technik-alltag/1373-githubtrends.md` |
| #1374 | Eerie Shadows: A Creepy Horror RPG Adventure | Alltag & Leben | `alltag-leben/1374-eerie-shadows-creepy-horror-rpg-adventur.md` |
| #1375 | AI Travel Agent – Interview-Driven Planner | Alltag & Leben | `alltag-leben/1375-ai-travel-agent-interview-driven-planner.md` |
| #1376 | “How It Works” Educational Dioramas | Lernen & Wachstum | `lernen-wachstum/1376-how-it-works-educational-dioramas.md` |
| #1377 | Act as a Job Application Reviewer | Beruf & Karriere | `beruf-karriere/1377-job-application-reviewer.md` |
| #1378 | Terminal Velocity | Technik & Alltag | `technik-alltag/1378-terminal-velocity.md` |
| #1379 | Alpine Freefall | Technik & Alltag | `technik-alltag/1379-alpine-freefall.md` |
| #1380 | Module Wrap-Up & Next Steps Video Generation | Technik & Alltag | `technik-alltag/1380-module-wrap-up-next-steps-video-generati.md` |
| #1381 | Strict Markdown-Only Output Enforcement | Technik & Alltag | `technik-alltag/1381-strict-markdown-only-output-enforcement.md` |
| #1382 | Investigative Research Assistant | Technik & Alltag | `technik-alltag/1382-investigative-research-assistant.md` |
| #1383 | Source-Hunting / OSINT Mode | Technik & Alltag | `technik-alltag/1383-source-hunting-osint-mode.md` |
| #1384 | Beginner's Guide to Building and Deploying LLMs | Alltag & Leben | `alltag-leben/1384-beginner-s-guide-to-building-and-deployi.md` |
| #1385 | Project System and Art Style Consistency Instructions | Alltag & Leben | `alltag-leben/1385-project-system-and-art-style-consistency.md` |
| #1386 | Musician Portfolio Website Design | Kreativitaet & Freizeit | `kreativitaet-freizeit/1386-musician-portfolio-website-design.md` |
| #1387 | Intent Recognition Planner Agent | Technik & Alltag | `technik-alltag/1387-intent-recognition-planner-agent.md` |
| #1388 | Cascading Failure Simulator | Technik & Alltag | `technik-alltag/1388-cascading-failure-simulator.md` |
| #1389 | gemini.md | Technik & Alltag | `technik-alltag/1389-gemini-md.md` |
| #1390 | war | Technik & Alltag | `technik-alltag/1390-war.md` |
| #1391 | Cinematic Ultra-Realistic Image-to-Video Prompt Engineer | Technik & Alltag | `technik-alltag/1391-cinematic-ultra-realistic-image-to-video.md` |
| #1392 | "YOU PROBABLY DON'T KNOW THIS" Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/1392-you-probably-don-t-know-this-game.md` |
| #1393 | Build a DDQN Snake Game with TensorFlow.js in a Single HTML File | Kreativitaet & Freizeit | `kreativitaet-freizeit/1393-build-ddqn-snake-game-with-tensorflow-js.md` |
| #1394 | Modern Plaza Office Selfie — Corporate Aesthetic in Istanbul | Technik & Alltag | `technik-alltag/1394-modern-plaza-office-selfie-corporate-aes.md` |
| #1395 | In-Flight Vacation Selfie — Natural Front Camera Perspective | Technik & Alltag | `technik-alltag/1395-in-flight-vacation-selfie-natural-front-.md` |
| #1396 | Nightclub Mirror Selfie | Technik & Alltag | `technik-alltag/1396-nightclub-mirror-selfie.md` |
| #1397 | Network Engineer: Home Edition | Technik & Alltag | `technik-alltag/1397-network-engineer-home-edition.md` |
| #1398 | Idea Generation | Technik & Alltag | `technik-alltag/1398-idea-generation.md` |
| #1399 | Step 2: Outline Creation | Technik & Alltag | `technik-alltag/1399-step-2-outline-creation.md` |
| #1400 | Step 3a: Technical Deep Dive | Technik & Alltag | `technik-alltag/1400-step-3a-technical-deep-dive.md` |
| #1401 | Step 3b: Creative Exploration | Technik & Alltag | `technik-alltag/1401-step-3b-creative-exploration.md` |
| #1402 | Step 4a: Implementation Plan | Technik & Alltag | `technik-alltag/1402-step-4a-implementation-plan.md` |
| #1403 | Step 4b: Story Development | Kreativitaet & Freizeit | `kreativitaet-freizeit/1403-step-4b-story-development.md` |
| #1404 | Step 5: Final Review | Technik & Alltag | `technik-alltag/1404-step-5-final-review.md` |
| #1405 | Step 6: Publication | Technik & Alltag | `technik-alltag/1405-step-6-publication.md` |
| #1406 | Underwater Veo 3 video | Technik & Alltag | `technik-alltag/1406-underwater-veo-3-video.md` |
| #1407 | Storyboard Grid | Technik & Alltag | `technik-alltag/1407-storyboard-grid.md` |
| #1408 | Remotion | Technik & Alltag | `technik-alltag/1408-remotion.md` |
| #1409 | Elements | Kreativitaet & Freizeit | `kreativitaet-freizeit/1409-elements.md` |
| #1410 | Production-Grade PostHog Integration for Next.js 15 (App Router) | Technik & Alltag | `technik-alltag/1410-production-grade-posthog-integration-for.md` |
| #1411 | Personal Assistant for Zone of Excellence Management | Alltag & Leben | `alltag-leben/1411-personal-assistant-for-zone-of-excellenc.md` |
| #1412 | Comprehensive Data Integration and Customer Profiling Tool | Beruf & Karriere | `beruf-karriere/1412-comprehensive-data-integration-and-custo.md` |
| #1413 | Food Scout | Technik & Alltag | `technik-alltag/1413-food-scout.md` |
| #1414 | Investigative Research Assistant for Uncovering Non-Mainstream Information | Technik & Alltag | `technik-alltag/1414-investigative-research-assistant-for-unc.md` |
| #1415 | Realistic Night Sky Portrait | Technik & Alltag | `technik-alltag/1415-realistic-night-sky-portrait.md` |
| #1416 | prompts.chat Promotional Video using Remotion | Technik & Alltag | `technik-alltag/1416-prompts-chat-promotional-video-using-rem.md` |
| #1417 | Influencer Candid Bedtime Selfie | Technik & Alltag | `technik-alltag/1417-influencer-candid-bedtime-selfie.md` |
| #1418 | Kubernetes & Docker RPG Learning Engine | Technik & Alltag | `technik-alltag/1418-kubernetes-docker-rpg-learning-engine.md` |
| #1419 | Valorant Agent Style | Kreativitaet & Freizeit | `kreativitaet-freizeit/1419-valorant-agent-style.md` |
| #1420 | Social Media Cocktail Web Site Post | Kommunikation & Beziehungen | `kommunikation-beziehungen/1420-social-media-cocktail-web-site-post.md` |
| #1421 | Social media swipe post content #1 | Kommunikation & Beziehungen | `kommunikation-beziehungen/1421-social-media-swipe-post-content-1.md` |
| #1422 | Ultra-photorealistic Infographics | Alltag & Leben | `alltag-leben/1422-ultra-photorealistic-infographics.md` |
| #1423 | My-Skills | Technik & Alltag | `technik-alltag/1423-my-skills.md` |
| #1424 | Cyber Security Character Workflow | Technik & Alltag | `technik-alltag/1424-cyber-security-character-workflow.md` |
| #1425 | Research Weapon | Technik & Alltag | `technik-alltag/1425-research-weapon.md` |
| #1426 | TV Premiere Weekly Listing Prompt | Technik & Alltag | `technik-alltag/1426-tv-premiere-weekly-listing-prompt.md` |
| #1427 | copilot | Technik & Alltag | `technik-alltag/1427-copilot.md` |
| #1428 | Satya Nadella pobre | Kreativitaet & Freizeit | `kreativitaet-freizeit/1428-satya-nadella-pobre.md` |
| #1429 | Note Guru | Technik & Alltag | `technik-alltag/1429-note-guru.md` |
| #1430 | Personalized Numerology Reading | Alltag & Leben | `alltag-leben/1430-personalized-numerology-reading.md` |
| #1431 | Screenplay Script with Cinematography Details | Kreativitaet & Freizeit | `kreativitaet-freizeit/1431-screenplay-script-with-cinematography-de.md` |
| #1432 | caravan prompts | Technik & Alltag | `technik-alltag/1432-caravan-prompts.md` |
| #1433 | Workplace English Speaking Coach | Lernen & Wachstum | `lernen-wachstum/1433-workplace-english-speaking-coach.md` |
| #1434 | 7v7 Football Team Generator App | Alltag & Leben | `alltag-leben/1434-7v7-football-team-generator-app.md` |
| #1435 | Sticker Image Generator | Technik & Alltag | `technik-alltag/1435-sticker-image-generator.md` |
| #1436 | Rick And Morty | Technik & Alltag | `technik-alltag/1436-rick-and-morty.md` |
| #1437 | Lego Movie Style Prompt | Technik & Alltag | `technik-alltag/1437-lego-movie-style-prompt.md` |
| #1438 | Precious Metals Price Analyst | Beruf & Karriere | `beruf-karriere/1438-precious-metals-price-analyst.md` |
| #1439 | The Ultimate TypeScript Code Review | Technik & Alltag | `technik-alltag/1439-the-ultimate-typescript-code-review.md` |
| #1440 | PHP Microscope: Forensic Codebase Autopsy Protocol | Technik & Alltag | `technik-alltag/1440-php-microscope-forensic-codebase-autopsy.md` |
| #1441 | claude-md-master | Technik & Alltag | `technik-alltag/1441-claude-md-master.md` |
| #1442 | skill-master | Technik & Alltag | `technik-alltag/1442-skill-master.md` |
| #1443 | Ultra-Photorealistic Romantic Cinematic Scene in the Rain | Technik & Alltag | `technik-alltag/1443-ultra-photorealistic-romantic-cinematic-.md` |
| #1444 | Romantic Rainy Scene Video | Technik & Alltag | `technik-alltag/1444-romantic-rainy-scene-video.md` |
| #1445 | Blogging prompt | Technik & Alltag | `technik-alltag/1445-blogging-prompt.md` |
| #1446 | Generate an enhanced command prompt | Technik & Alltag | `technik-alltag/1446-generate-enhanced-command-prompt.md` |
| #1447 | Improve the following code | Technik & Alltag | `technik-alltag/1447-improve-following-code.md` |
| #1448 | Personal Form Builder App Design | Alltag & Leben | `alltag-leben/1448-personal-form-builder-app-design.md` |
| #1449 | Research NRI/NRO Account Services in India | Beruf & Karriere | `beruf-karriere/1449-research-nri-nro-account-services-in-ind.md` |
| #1450 | Photorealistic Cozy Home Scene with Natural Lighting | Alltag & Leben | `alltag-leben/1450-photorealistic-cozy-home-scene-with-natu.md` |
| #1451 | AI App Prototyping for Chat Interface | Technik & Alltag | `technik-alltag/1451-ai-app-prototyping-for-chat-interface.md` |
| #1452 | Personal Growth Plan for BNWO Enthusiasts | Alltag & Leben | `alltag-leben/1452-personal-growth-plan-for-bnwo-enthusiast.md` |
| #1453 | Compile a Curated Compendium of Niche Adult Relationship Dynamics | Kommunikation & Beziehungen | `kommunikation-beziehungen/1453-compile-curated-compendium-of-niche-adul.md` |
| #1454 | scaryface | Technik & Alltag | `technik-alltag/1454-scaryface.md` |
| #1455 | Claude Code Statusline Design | Technik & Alltag | `technik-alltag/1455-claude-code-statusline-design.md` |
| #1456 | American Comic | Technik & Alltag | `technik-alltag/1456-american-comic.md` |
| #1457 | Create Icons | Technik & Alltag | `technik-alltag/1457-create-icons.md` |
| #1458 | Create Infographics | Lernen & Wachstum | `lernen-wachstum/1458-create-infographics.md` |
| #1459 | Design App Store Style Icons | Technik & Alltag | `technik-alltag/1459-design-app-store-style-icons.md` |
| #1460 | Linkedin profile enhancing | Beruf & Karriere | `beruf-karriere/1460-linkedin-profile-enhancing.md` |
| #1461 | LinkedIn: About/Summary draft prompt | Technik & Alltag | `technik-alltag/1461-linkedin-about-summary-draft-prompt.md` |
| #1462 | LinkedIn: Experience optimization prompt | Technik & Alltag | `technik-alltag/1462-linkedin-experience-optimization-prompt.md` |
| #1463 | LinkedIn: Recommendation request message prompt | Technik & Alltag | `technik-alltag/1463-linkedin-recommendation-request-message-.md` |
| #1464 | Game Theory for Students: Easy and Engaging Learning | Kreativitaet & Freizeit | `kreativitaet-freizeit/1464-game-theory-for-students-easy-and-engagi.md` |
| #1465 | Elite B2B Lead Generation and SEO Audit Specialist | Technik & Alltag | `technik-alltag/1465-elite-b2b-lead-generation-and-seo-audit-.md` |
| #1466 | Custom Travel Plan Generator | Alltag & Leben | `alltag-leben/1466-custom-travel-plan-generator.md` |
| #1467 | Sell a dream as an underground tailors but need partnership for capital. With no or just 20% less leverage, how to get partners interested and involved to buy the dream | Kreativitaet & Freizeit | `kreativitaet-freizeit/1467-sell-dream-as-underground-tailors-but-ne.md` |
| #1468 | Cinematic Ink & Color Illustration Generator — Gary Frank Style | Technik & Alltag | `technik-alltag/1468-cinematic-ink-color-illustration-generat.md` |
| #1469 | Marketing Mastermind for Product Promotion | Technik & Alltag | `technik-alltag/1469-marketing-mastermind-for-product-promoti.md` |
| #1470 | The Architect: Hacker-Protector & Viral Engineer | Technik & Alltag | `technik-alltag/1470-the-architect-hacker-protector-viral-eng.md` |
| #1471 | Transform Subjects into Adorable Plush Forms | Technik & Alltag | `technik-alltag/1471-transform-subjects-into-adorable-plush-f.md` |
| #1472 | LinkedIn Summary Crafting Prompt | Technik & Alltag | `technik-alltag/1472-linkedin-summary-crafting-prompt.md` |
| #1473 | Critical-Parallel Inquiry Format | Technik & Alltag | `technik-alltag/1473-critical-parallel-inquiry-format.md` |
| #1474 | GPT-5 | EXPERT PROMPT ENGINEER MODE (CONDENSED) | Technik & Alltag | `technik-alltag/1474-gpt-5-expert-prompt-engineer-mode-conden.md` |
| #1475 | 5x2 Reverse Construction Process - Villa Demolition Storyboard | Technik & Alltag | `technik-alltag/1475-5x2-reverse-construction-process-villa-d.md` |
| #1476 | Futuristic Supercar Brand Logo | Alltag & Leben | `alltag-leben/1476-futuristic-supercar-brand-logo.md` |
| #1477 | Senior Academic Advisor | Technik & Alltag | `technik-alltag/1477-senior-academic-advisor.md` |
| #1478 | Business Legal Assistant | Beruf & Karriere | `beruf-karriere/1478-business-legal-assistant.md` |
| #1479 | China Business Law Assistant | Beruf & Karriere | `beruf-karriere/1479-china-business-law-assistant.md` |
| #1480 | Family picture | Technik & Alltag | `technik-alltag/1480-family-picture.md` |
| #1481 | Streaks Mobile App Development Prompt | Technik & Alltag | `technik-alltag/1481-streaks-mobile-app-development-prompt.md` |
| #1482 | Serious Man in Urban Setting | Spezielle Situationen | `spezielle-situationen/1482-serious-man-in-urban-setting.md` |
| #1483 | I Think I Need a Lawyer — Neutral Legal Intake Organizer | Spezielle Situationen | `spezielle-situationen/1483-i-think-i-need-lawyer-neutral-legal-inta.md` |
| #1484 | Professional Networking Language for Career Fairs | Lernen & Wachstum | `lernen-wachstum/1484-professional-networking-language-for-car.md` |
| #1485 | Lonely Girl | Technik & Alltag | `technik-alltag/1485-lonely-girl.md` |
| #1486 | Resume tailoring | Beruf & Karriere | `beruf-karriere/1486-resume-tailoring.md` |
| #1487 | Senior Frontend Debugger for SPA Websites (Angular, React, Vite) | Technik & Alltag | `technik-alltag/1487-senior-frontend-debugger-for-spa-website.md` |
| #1488 | Fix Blank Screen Issues After Deploy on Vercel (Angular, React, Vite) | Technik & Alltag | `technik-alltag/1488-fix-blank-screen-issues-after-deploy-on-.md` |
| #1489 | Ultra-Realistic 3D Character Avatar Creation | Kreativitaet & Freizeit | `kreativitaet-freizeit/1489-ultra-realistic-3d-character-avatar-crea.md` |
| #1490 | Recursive Niche Deconstruction for Market Research | Technik & Alltag | `technik-alltag/1490-recursive-niche-deconstruction-for-marke.md` |
| #1491 | LEGO Minifigure Character Transformation | Kreativitaet & Freizeit | `kreativitaet-freizeit/1491-lego-minifigure-character-transformation.md` |
| #1492 | Web Application | Technik & Alltag | `technik-alltag/1492-web-application.md` |
| #1493 | AI builder | Technik & Alltag | `technik-alltag/1493-ai-builder.md` |
| #1494 | Drunk Woman | Kreativitaet & Freizeit | `kreativitaet-freizeit/1494-drunk-woman.md` |
| #1495 | Abandoned Wife | Kreativitaet & Freizeit | `kreativitaet-freizeit/1495-abandoned-wife.md` |
| #1496 | Aesthetic Sunset | Technik & Alltag | `technik-alltag/1496-aesthetic-sunset.md` |
| #1497 | Universal Job Fit Evaluation Prompt | Technik & Alltag | `technik-alltag/1497-universal-job-fit-evaluation-prompt.md` |
| #1498 | Building a Scalable Search Service with FastAPI and PostgreSQL | Technik & Alltag | `technik-alltag/1498-building-scalable-search-service-with-fa.md` |
| #1499 | Enterprise Talent Development Management System Design | Spezielle Situationen | `spezielle-situationen/1499-enterprise-talent-development-management.md` |
| #1500 | Gen Z Content & Online Sales Prompt Generator | Technik & Alltag | `technik-alltag/1500-gen-z-content-online-sales-prompt-genera.md` |
| #1501 | Deep GitHub Repository Understanding | Technik & Alltag | `technik-alltag/1501-deep-github-repository-understanding.md` |
| #1502 | Criar/Alterar Documentação de Projeto | Technik & Alltag | `technik-alltag/1502-criar-alterar-documenta-o-de-projeto.md` |
| #1503 | Gerador de Tarefas | Technik & Alltag | `technik-alltag/1503-gerador-de-tarefas.md` |
| #1504 | Planjedor de Tarefas | Technik & Alltag | `technik-alltag/1504-planjedor-de-tarefas.md` |
| #1505 | Implementador de Tarefas | Technik & Alltag | `technik-alltag/1505-implementador-de-tarefas.md` |
| #1506 | Code Recon | Technik & Alltag | `technik-alltag/1506-code-recon.md` |
| #1507 | Creating a Comprehensive Elasticsearch Search Project with FastAPI | Technik & Alltag | `technik-alltag/1507-creating-comprehensive-elasticsearch-sea.md` |
| #1508 | Daiquiri Cocktail Cinematic Video | Technik & Alltag | `technik-alltag/1508-daiquiri-cocktail-cinematic-video.md` |
| #1509 | Solar System Scale Model Classroom Poster | Technik & Alltag | `technik-alltag/1509-solar-system-scale-model-classroom-poste.md` |
| #1510 | Prompt Optimization | Technik & Alltag | `technik-alltag/1510-prompt-optimization.md` |
| #1511 | 4 Optimized Versions of A Prompt (in Arabic) | Technik & Alltag | `technik-alltag/1511-4-optimized-versions-of-prompt-in-arabic.md` |
| #1512 | Analogy Generator | Technik & Alltag | `technik-alltag/1512-analogy-generator.md` |
| #1513 | Advanced Account Research | Alltag & Leben | `alltag-leben/1513-advanced-account-research.md` |
| #1514 | Industry/Market Intelligence | Technik & Alltag | `technik-alltag/1514-industry-market-intelligence.md` |
| #1515 | Prompt Engineering Expert | Technik & Alltag | `technik-alltag/1515-prompt-engineering-expert.md` |
| #1516 | Sales Research | Technik & Alltag | `technik-alltag/1516-sales-research.md` |
| #1517 | Sports Events Weekly Listings Prompt | Technik & Alltag | `technik-alltag/1517-sports-events-weekly-listings-prompt.md` |
| #1518 | MeddaH | Technik & Alltag | `technik-alltag/1518-meddah.md` |
| #1519 | Cocktail videos | Technik & Alltag | `technik-alltag/1519-cocktail-videos.md` |
| #1520 | Coach for Identifying Growth-Limiting Patterns | Lernen & Wachstum | `lernen-wachstum/1520-coach-for-identifying-growth-limiting-pa.md` |
| #1521 | A professional Egyptian barista | Technik & Alltag | `technik-alltag/1521-a-professional-egyptian-barista.md` |
| #1522 | Brotherhood Pressure — CN→EN & EN→EN Street Rewrite | Technik & Alltag | `technik-alltag/1522-brotherhood-pressure-cn-en-en-en-street-.md` |
| #1523 | Driftcraft | Lernen & Wachstum | `lernen-wachstum/1523-driftcraft.md` |
| #1524 | Lagrange Lens: Blue Wolf | Technik & Alltag | `technik-alltag/1524-lagrange-lens-blue-wolf.md` |
| #1525 | Socratic Lens | Technik & Alltag | `technik-alltag/1525-socratic-lens.md` |
| #1526 | Dog fun | Technik & Alltag | `technik-alltag/1526-dog-fun.md` |
| #1527 | Deep Research - Gemini | Technik & Alltag | `technik-alltag/1527-deep-research-gemini.md` |
| #1528 | PRD | Beruf & Karriere | `beruf-karriere/1528-prd.md` |
| #1529 | Second Opinion | Technik & Alltag | `technik-alltag/1529-second-opinion.md` |
| #1530 | Minecraft image | Kreativitaet & Freizeit | `kreativitaet-freizeit/1530-minecraft-image.md` |
| #1531 | Reimagined Logo for Google | Technik & Alltag | `technik-alltag/1531-reimagined-logo-for-google.md` |
| #1532 | OS2.0 SAFe Delivery Context (Master) | Technik & Alltag | `technik-alltag/1532-os2-0-safe-delivery-context-master.md` |
| #1533 | Olympic Games Events Weekly Listings Prompt | Technik & Alltag | `technik-alltag/1533-olympic-games-events-weekly-listings-pro.md` |
| #1534 | Creative Writing Adventure | Technik & Alltag | `technik-alltag/1534-creative-writing-adventure.md` |
| #1535 | Nurse | Technik & Alltag | `technik-alltag/1535-nurse.md` |
| #1536 | Innovative Research Enhancement Ideas Generator | Technik & Alltag | `technik-alltag/1536-innovative-research-enhancement-ideas-ge.md` |
| #1537 | Literature Reading and Analysis Assistant | Technik & Alltag | `technik-alltag/1537-literature-reading-and-analysis-assistan.md` |
| #1538 | Develop a Live Video Streaming Website | Technik & Alltag | `technik-alltag/1538-develop-live-video-streaming-website.md` |
| #1539 | Human-Like Creative Writing Challenge | Technik & Alltag | `technik-alltag/1539-human-like-creative-writing-challenge.md` |
| #1540 | Gathering Planner Interview | Technik & Alltag | `technik-alltag/1540-gathering-planner-interview.md` |
| #1541 | Lazy AI Email Detector | Technik & Alltag | `technik-alltag/1541-lazy-ai-email-detector.md` |
| #1542 | Studio Portrait with Cinematic Lighting and Bold Color Background | Technik & Alltag | `technik-alltag/1542-studio-portrait-with-cinematic-lighting-.md` |
| #1543 | National Architecture Dioramas | Technik & Alltag | `technik-alltag/1543-national-architecture-dioramas.md` |
| #1544 | Make AI write naturally | Technik & Alltag | `technik-alltag/1544-make-ai-write-naturally.md` |
| #1545 | Professional Image Enhancement for Clarity and Quality | Technik & Alltag | `technik-alltag/1545-professional-image-enhancement-for-clari.md` |
| #1546 | EMAIL SEQUENCE WITH STORYTELLING | Technik & Alltag | `technik-alltag/1546-email-sequence-with-storytelling.md` |
| #1547 | Radical Responsibility Mirror (Shadow Work) | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1547-radical-responsibility-mirror-shadow-wor.md` |
| #1548 | Deep Immersion Study Plan (7 Days) | Technik & Alltag | `technik-alltag/1548-deep-immersion-study-plan-7-days.md` |
| #1549 | Socratic Universal Tutor | Lernen & Wachstum | `lernen-wachstum/1549-socratic-universal-tutor.md` |
| #1550 | Project Breakdown | Beruf & Karriere | `beruf-karriere/1550-project-breakdown.md` |
| #1551 | xcode-mcp | Technik & Alltag | `technik-alltag/1551-xcode-mcp.md` |
| #1552 | Strategic Decision-Making Matrix | Beruf & Karriere | `beruf-karriere/1552-strategic-decision-making-matrix.md` |
| #1553 | High Conversion Cold Email | Technik & Alltag | `technik-alltag/1553-high-conversion-cold-email.md` |
| #1554 | SYSTEM PROMPT: THE INFINITE ROLE GENERATOR | Technik & Alltag | `technik-alltag/1554-system-prompt-infinite-role-generator.md` |
| #1555 | Cyberscam Survival Simulator | Technik & Alltag | `technik-alltag/1555-cyberscam-survival-simulator.md` |
| #1556 | Whiteboard Diagrams | Kreativitaet & Freizeit | `kreativitaet-freizeit/1556-whiteboard-diagrams.md` |
| #1557 | Live Scam Threat Briefing | Technik & Alltag | `technik-alltag/1557-live-scam-threat-briefing.md` |
| #1558 | Fact-Checking Evaluation Assistant | Technik & Alltag | `technik-alltag/1558-fact-checking-evaluation-assistant.md` |
| #1559 | OSINT Threat Intelligence Analysis Workflow | Technik & Alltag | `technik-alltag/1559-osint-threat-intelligence-analysis-workf.md` |
| #1560 | Imagen estilo Hollywood de alta definición | Technik & Alltag | `technik-alltag/1560-imagen-estilo-hollywood-de-alta-definici.md` |
| #1561 | WFGY 2.0 Core Flagship · Self-Healing Reasoning OS for Any LLM | Technik & Alltag | `technik-alltag/1561-wfgy-2-0-core-flagship-self-healing-reas.md` |
| #1562 | Spotify room cinematic | Kreativitaet & Freizeit | `kreativitaet-freizeit/1562-spotify-room-cinematic.md` |
| #1563 | Universal System Design Prompt | Technik & Alltag | `technik-alltag/1563-universal-system-design-prompt.md` |
| #1564 | Valentines Day Cocktail | Technik & Alltag | `technik-alltag/1564-valentines-day-cocktail.md` |
| #1565 | The Technical Co-Founder: Building Real Products Together | Technik & Alltag | `technik-alltag/1565-the-technical-co-founder-building-real-p.md` |
| #1566 | Night club | Technik & Alltag | `technik-alltag/1566-night-club.md` |
| #1567 | CLAUDE.md Generator for AI Coding Agents | Technik & Alltag | `technik-alltag/1567-claude-md-generator-for-ai-coding-agents.md` |
| #1568 | Prompt Generator for claude code | Technik & Alltag | `technik-alltag/1568-prompt-generator-for-claude-code.md` |
| #1569 | Scientific Paper Drafting for Analytical Data | Technik & Alltag | `technik-alltag/1569-scientific-paper-drafting-for-analytical.md` |
| #1570 | The Solar Priestess of Amun | Technik & Alltag | `technik-alltag/1570-the-solar-priestess-of-amun.md` |
| #1571 | Profile pic rebuild | Technik & Alltag | `technik-alltag/1571-profile-pic-rebuild.md` |
| #1572 | Morning coffee | Technik & Alltag | `technik-alltag/1572-morning-coffee.md` |
| #1573 | Young woman with bikini | Technik & Alltag | `technik-alltag/1573-young-woman-with-bikini.md` |
| #1574 | Draft PR to Ready to Review PR | Technik & Alltag | `technik-alltag/1574-draft-pr-to-ready-to-review-pr.md` |
| #1575 | Chinese to English Translation Proofreading Expert | Lernen & Wachstum | `lernen-wachstum/1575-chinese-to-english-translation-proofread.md` |
| #1576 | Hallucination Vulnerability Prompt Checker | Technik & Alltag | `technik-alltag/1576-hallucination-vulnerability-prompt-check.md` |
| #1577 | Meme coins knowledge  and trading | Technik & Alltag | `technik-alltag/1577-meme-coins-knowledge-and-trading.md` |
| #1578 | Womanized | Technik & Alltag | `technik-alltag/1578-womanized.md` |
| #1579 | Lead Data Analyst for Actionable Insights | Technik & Alltag | `technik-alltag/1579-lead-data-analyst-for-actionable-insight.md` |
| #1580 | ATS Resume Scanner Simulator | Beruf & Karriere | `beruf-karriere/1580-ats-resume-scanner-simulator.md` |
| #1581 | Resume Quality Reviewer – Green Flag Edition | Beruf & Karriere | `beruf-karriere/1581-resume-quality-reviewer-green-flag-editi.md` |
| #1582 | Dynamic Chinese Fire Horse Celebration | Kreativitaet & Freizeit | `kreativitaet-freizeit/1582-dynamic-chinese-fire-horse-celebration.md` |
| #1583 | Overqualification Narrative Architect | Technik & Alltag | `technik-alltag/1583-overqualification-narrative-architect.md` |
| #1584 | Table in PDF to CSV conversion | Technik & Alltag | `technik-alltag/1584-table-in-pdf-to-csv-conversion.md` |
| #1585 | Narrative Momentum Prediction Engine | Beruf & Karriere | `beruf-karriere/1585-narrative-momentum-prediction-engine.md` |
| #1586 | Aaa | Technik & Alltag | `technik-alltag/1586-aaa.md` |
| #1587 | Create Satirical and Bold Song Lyrics | Kreativitaet & Freizeit | `kreativitaet-freizeit/1587-create-satirical-and-bold-song-lyrics.md` |
| #1588 | Interactive Place Review Generator | Technik & Alltag | `technik-alltag/1588-interactive-place-review-generator.md` |
| #1589 | Minimalist Surveillance Illustration Prompt | Technik & Alltag | `technik-alltag/1589-minimalist-surveillance-illustration-pro.md` |
| #1590 | Vibrant Fauvist Style Sunlit Living Room Illustration | Technik & Alltag | `technik-alltag/1590-vibrant-fauvist-style-sunlit-living-room.md` |
| #1591 | Serene Moonlit Street Illustration | Technik & Alltag | `technik-alltag/1591-serene-moonlit-street-illustration.md` |
| #1592 | MoltPass Client -- Cryptographic Passport for AI Agents | Technik & Alltag | `technik-alltag/1592-moltpass-client-cryptographic-passport-f.md` |
| #1593 | LinkedIn JSON → Canonical Markdown Profile Generator | Technik & Alltag | `technik-alltag/1593-linkedin-json-canonical-markdown-profile.md` |
| #1594 | Master Podcast Producer & Sonic Storyteller | Kreativitaet & Freizeit | `kreativitaet-freizeit/1594-master-podcast-producer-sonic-storytelle.md` |
| #1595 | Cinematic Video Essay Director | Lernen & Wachstum | `lernen-wachstum/1595-cinematic-video-essay-director.md` |
| #1596 | Micro-SaaS "Vibecoder" Architect | Technik & Alltag | `technik-alltag/1596-micro-saas-vibecoder-architect.md` |
| #1597 | The Ultimate Podcast Format & Audio Branding Architect | Technik & Alltag | `technik-alltag/1597-the-ultimate-podcast-format-audio-brandi.md` |
| #1598 | The Elite SEO Blog Architect & Ghostwriter | Technik & Alltag | `technik-alltag/1598-the-elite-seo-blog-architect-ghostwriter.md` |
| #1599 | Pina Colada Cocktail | Technik & Alltag | `technik-alltag/1599-pina-colada-cocktail.md` |
| #1600 | Senior Software Engineer  & Software Architect Rules | Technik & Alltag | `technik-alltag/1600-senior-software-engineer-software-archit.md` |
| #1601 | Test-First Bug Fixing Approach | Technik & Alltag | `technik-alltag/1601-test-first-bug-fixing-approach.md` |
| #1602 | Spring Boot + SOLID Specialist | Technik & Alltag | `technik-alltag/1602-spring-boot-solid-specialist.md` |
| #1603 | Autonomous Research & Data Analysis Agent | Alltag & Leben | `alltag-leben/1603-autonomous-research-data-analysis-agent.md` |
| #1604 | Symphony Event Invitation and Guide | Alltag & Leben | `alltag-leben/1604-symphony-event-invitation-and-guide.md` |
| #1605 | evento de sinfonía grupo 4 | Beruf & Karriere | `beruf-karriere/1605-evento-de-sinfon-a-grupo-4.md` |
| #1606 | Principal AI Code Reviewer + Senior Software Engineer / Architect Prompt | Technik & Alltag | `technik-alltag/1606-principal-ai-code-reviewer-senior-softwa.md` |
| #1607 | Photo shoot for branding | Technik & Alltag | `technik-alltag/1607-photo-shoot-for-branding.md` |
| #1608 | Market Pulse | Technik & Alltag | `technik-alltag/1608-market-pulse.md` |
| #1609 | Cruelty-Free Beauty Product Checker | Kommunikation & Beziehungen | `kommunikation-beziehungen/1609-cruelty-free-beauty-product-checker.md` |
| #1610 | Big 4 style report for retail traders - Enter the name and ticker of a U.S. publicly traded company. | Beruf & Karriere | `beruf-karriere/1610-big-4-style-report-for-retail-traders-en.md` |
| #1611 | Prompt for Humanizing AI Text (English Version) | Technik & Alltag | `technik-alltag/1611-prompt-for-humanizing-ai-text-english-ve.md` |
| #1612 | Learn Any Technical/Coding Topic | Technik & Alltag | `technik-alltag/1612-learn-any-technical-coding-topic.md` |
| #1613 | 30-Day Skill Mastery Challenge Prompt Template | Technik & Alltag | `technik-alltag/1613-30-day-skill-mastery-challenge-prompt-te.md` |
| #1614 | Voice Conversation Coach | Lernen & Wachstum | `lernen-wachstum/1614-voice-conversation-coach.md` |
| #1615 | Animated Weather Radar Map: Brescia Storm | Technik & Alltag | `technik-alltag/1615-animated-weather-radar-map-brescia-storm.md` |
| #1616 | Vintage Black and White Photograph of Galata Tower | Technik & Alltag | `technik-alltag/1616-vintage-black-and-white-photograph-of-ga.md` |
| #1617 | Minimalist Fisherman Illustration | Technik & Alltag | `technik-alltag/1617-minimalist-fisherman-illustration.md` |
| #1618 | Dramatic Digital Painting of a Solitary Figure in a Snowy Landscape | Technik & Alltag | `technik-alltag/1618-dramatic-digital-painting-of-solitary-fi.md` |
| #1619 | Python Code Performance & Quality Enhancer | Technik & Alltag | `technik-alltag/1619-python-code-performance-quality-enhancer.md` |
| #1620 | Career Intelligence Analyst | Beruf & Karriere | `beruf-karriere/1620-career-intelligence-analyst.md` |
| #1621 | Pre-Interview Intelligence Dossier | Technik & Alltag | `technik-alltag/1621-pre-interview-intelligence-dossier.md` |
| #1622 | Innovative Use Case Generator for New Tools | Technik & Alltag | `technik-alltag/1622-innovative-use-case-generator-for-new-to.md` |
| #1623 | Software Implementor AI Agent for Data Entry and Testing | Technik & Alltag | `technik-alltag/1623-software-implementor-ai-agent-for-data-e.md` |
| #1624 | CKEditor 5 Plugin | Technik & Alltag | `technik-alltag/1624-ckeditor-5-plugin.md` |
| #1625 | Ghibli style anime character | Kreativitaet & Freizeit | `kreativitaet-freizeit/1625-ghibli-style-anime-character.md` |
| #1626 | Python Code Generator — Clean, Optimized & Production-Ready | Technik & Alltag | `technik-alltag/1626-python-code-generator-clean-optimized-pr.md` |
| #1627 | Camp Planner | Technik & Alltag | `technik-alltag/1627-camp-planner.md` |
| #1628 | Preventive Health Report Clinical Evaluation Prompt | Technik & Alltag | `technik-alltag/1628-preventive-health-report-clinical-evalua.md` |
| #1629 | # ANTIGRAVITY GLOBAL RULES | Technik & Alltag | `technik-alltag/1629-antigravity-global-rules.md` |
| #1630 | Documentation Update Automation | Technik & Alltag | `technik-alltag/1630-documentation-update-automation.md` |
| #1631 | App Store Screenshots Gallery Generator | Technik & Alltag | `technik-alltag/1631-app-store-screenshots-gallery-generator.md` |
| #1632 | Build a Web3 Wallet on Playnance Blockchain | Technik & Alltag | `technik-alltag/1632-build-web3-wallet-on-playnance-blockchai.md` |
| #1633 | Dermatology Consultation Guide | Alltag & Leben | `alltag-leben/1633-dermatology-consultation-guide.md` |
| #1634 | The Fighter | Technik & Alltag | `technik-alltag/1634-the-fighter.md` |
| #1635 | Miniature Artist | Kreativitaet & Freizeit | `kreativitaet-freizeit/1635-miniature-artist.md` |
| #1636 | Skin care for acne and freckles | Beruf & Karriere | `beruf-karriere/1636-skin-care-for-acne-and-freckles.md` |
| #1637 | Heart Illustration | Technik & Alltag | `technik-alltag/1637-heart-illustration.md` |
| #1638 | Ball Puppet | Alltag & Leben | `alltag-leben/1638-ball-puppet.md` |
| #1639 | Barong 1 | Technik & Alltag | `technik-alltag/1639-barong-1.md` |
| #1640 | Barong 2 | Kreativitaet & Freizeit | `kreativitaet-freizeit/1640-barong-2.md` |
| #1641 | Minimax Music & Lyrics Generation | Kreativitaet & Freizeit | `kreativitaet-freizeit/1641-minimax-music-lyrics-generation.md` |
| #1642 | AI Grounding Prompt | Technik & Alltag | `technik-alltag/1642-ai-grounding-prompt.md` |
| #1643 | trial | Alltag & Leben | `alltag-leben/1643-trial.md` |
| #1644 | Test | Technik & Alltag | `technik-alltag/1644-test.md` |
| #1645 | Analyze code scanning security issues and dependency updates if vulnerable | Technik & Alltag | `technik-alltag/1645-analyze-code-scanning-security-issues-an.md` |
| #1646 | want to analyze security issues and vulnerabilities and fixes | Technik & Alltag | `technik-alltag/1646-want-to-analyze-security-issues-and-vuln.md` |
| #1647 | logo designer | Technik & Alltag | `technik-alltag/1647-logo-designer.md` |
| #1648 | security fixes cves | Technik & Alltag | `technik-alltag/1648-security-fixes-cves.md` |
| #1649 | security fixes | Technik & Alltag | `technik-alltag/1649-security-fixes.md` |
| #1650 | Boom & Crush - ICT strategy | Technik & Alltag | `technik-alltag/1650-boom-crush-ict-strategy.md` |
| #1651 | Alp Dağlarındasın | Technik & Alltag | `technik-alltag/1651-alp-da-lar-ndas-n.md` |
| #1652 | Ultra Realistic Cinematic Portrait | Technik & Alltag | `technik-alltag/1652-ultra-realistic-cinematic-portrait.md` |
| #1653 | High-Contrast Stencil Vector Poster Illustration | Technik & Alltag | `technik-alltag/1653-high-contrast-stencil-vector-poster-illu.md` |
| #1654 | KIDS DRESS DESIGN | Technik & Alltag | `technik-alltag/1654-kids-dress-design.md` |
| #1655 | TypeScript Unit Testing with Vitest | Technik & Alltag | `technik-alltag/1655-typescript-unit-testing-with-vitest.md` |
| #1656 | Master Storyteller and Sales Copywriter Prompt | Kreativitaet & Freizeit | `kreativitaet-freizeit/1656-master-storyteller-and-sales-copywriter-.md` |
| #1657 | Wicked | Technik & Alltag | `technik-alltag/1657-wicked.md` |
| #1658 | Advanced Sales Funnel App with React Flow | Technik & Alltag | `technik-alltag/1658-advanced-sales-funnel-app-with-react-flo.md` |
| #1659 | Clinical Research Presentation Guidance | Alltag & Leben | `alltag-leben/1659-clinical-research-presentation-guidance.md` |
| #1660 | change home page desgin for blog and documentation platorm | Technik & Alltag | `technik-alltag/1660-change-home-page-desgin-for-blog-and-doc.md` |
| #1661 | Butterfly | Technik & Alltag | `technik-alltag/1661-butterfly.md` |
| #1662 | Structured and Effective Learning Prompt | Technik & Alltag | `technik-alltag/1662-structured-and-effective-learning-prompt.md` |
| #1663 | TCRE Framework - AI Prompt Engineer | Technik & Alltag | `technik-alltag/1663-tcre-framework-ai-prompt-engineer.md` |
| #1664 | Information Gathering Prompt | Technik & Alltag | `technik-alltag/1664-information-gathering-prompt.md` |
| #1665 | chicks hatch | Technik & Alltag | `technik-alltag/1665-chicks-hatch.md` |
| #1666 | Wickedsmaht.fun | Technik & Alltag | `technik-alltag/1666-wickedsmaht-fun.md` |
| #1667 | HTWind-Widget-Creator | Technik & Alltag | `technik-alltag/1667-htwind-widget-creator.md` |
| #1668 | Transform the input product image into a professional commercial studio photograph | Technik & Alltag | `technik-alltag/1668-transform-input-product-image-into-profe.md` |
| #1669 | notebooklm_lecture_notes | Technik & Alltag | `technik-alltag/1669-notebooklm-lecture-notes.md` |
| #1670 | image to video 360 product rotaion | Technik & Alltag | `technik-alltag/1670-image-to-video-360-product-rotaion.md` |
| #1671 | Xh | Technik & Alltag | `technik-alltag/1671-xh.md` |
| #1672 | Train Waiter | Technik & Alltag | `technik-alltag/1672-train-waiter.md` |
| #1673 | Colored | Technik & Alltag | `technik-alltag/1673-colored.md` |
| #1674 | Abstract Portrait | Technik & Alltag | `technik-alltag/1674-abstract-portrait.md` |
| #1675 | Girls | Technik & Alltag | `technik-alltag/1675-girls.md` |
| #1676 | Steel Blueprint Infographic For SosMed | Technik & Alltag | `technik-alltag/1676-steel-blueprint-infographic-for-sosmed.md` |
| #1677 | Voice Cloning Attacks Infographic | Technik & Alltag | `technik-alltag/1677-voice-cloning-attacks-infographic.md` |
| #1678 | Agency Growth Bottleneck Identifier | Beruf & Karriere | `beruf-karriere/1678-agency-growth-bottleneck-identifier.md` |
| #1679 | Expert Discovery Interviewer Guide | Beruf & Karriere | `beruf-karriere/1679-expert-discovery-interviewer-guide.md` |
| #1680 | Landing Page Copy Architect – Conversion Framework Prompt | Technik & Alltag | `technik-alltag/1680-landing-page-copy-architect-conversion-f.md` |
| #1681 | Data Architect & Business Strategist (CSV Audit & Pipeline) | Technik & Alltag | `technik-alltag/1681-data-architect-business-strategist-csv-a.md` |
| #1682 | cambio de ojos | Technik & Alltag | `technik-alltag/1682-cambio-de-ojos.md` |
| #1683 | Strategy Consultant | Beruf & Karriere | `beruf-karriere/1683-strategy-consultant.md` |
| #1684 | Python Security Vulnerability Auditor (OWASP-Mapped & Production-Hardened) | Technik & Alltag | `technik-alltag/1684-python-security-vulnerability-auditor-ow.md` |
| #1685 | Make Flowers Bloom in an Image | Technik & Alltag | `technik-alltag/1685-make-flowers-bloom-in-image.md` |
| #1686 | AI Performance & Deep Testing Engineer | Technik & Alltag | `technik-alltag/1686-ai-performance-deep-testing-engineer.md` |
| #1687 | Make AI responses sound more Human-like | Lernen & Wachstum | `lernen-wachstum/1687-make-ai-responses-sound-more-human-like.md` |
| #1688 | Academic Paper Figure Generator - Nano Banana Pro | Technik & Alltag | `technik-alltag/1688-academic-paper-figure-generator-nano-ban.md` |
| #1689 | National safety week | Alltag & Leben | `alltag-leben/1689-national-safety-week.md` |
| #1690 | RNA-Seq Analysis and Differential Gene Expression | Alltag & Leben | `alltag-leben/1690-rna-seq-analysis-and-differential-gene-e.md` |
| #1691 | Comprehensive Guide to Gas-Fired Pool Heaters with Visuals | Alltag & Leben | `alltag-leben/1691-comprehensive-guide-to-gas-fired-pool-he.md` |
| #1692 | prompts.chat taste | Technik & Alltag | `technik-alltag/1692-prompts-chat-taste.md` |
| #1693 | Python Unit Test Generator — Comprehensive, Coverage-Mapped & Production-Ready | Technik & Alltag | `technik-alltag/1693-python-unit-test-generator-comprehensive.md` |
| #1694 | Mixed Media Portrait Illustration | Technik & Alltag | `technik-alltag/1694-mixed-media-portrait-illustration.md` |
| #1695 | Illustrative Hand-Drawn Istanbul Skyline Prompt | Technik & Alltag | `technik-alltag/1695-illustrative-hand-drawn-istanbul-skyline.md` |
| #1696 | Majestic Bald Eagle 3D Render Prompt | Technik & Alltag | `technik-alltag/1696-majestic-bald-eagle-3d-render-prompt.md` |
| #1697 | Writing a Book on Causes of Death from Data Sources | Technik & Alltag | `technik-alltag/1697-writing-book-on-causes-of-death-from-dat.md` |
| #1698 | Critical Thinking (DeepThink) | Technik & Alltag | `technik-alltag/1698-critical-thinking-deepthink.md` |
| #1699 | Corporate Intel Report | Technik & Alltag | `technik-alltag/1699-corporate-intel-report.md` |
| #1700 | Root Cause Architect (5 Whys Technique) | Technik & Alltag | `technik-alltag/1700-root-cause-architect-5-whys-technique.md` |
| #1701 | SciSim Pro - Simulator for science (ASCII/Textual Art spatial diagrams support) | Kreativitaet & Freizeit | `kreativitaet-freizeit/1701-scisim-pro-simulator-for-science-ascii-t.md` |
| #1702 | Expanded Company Intel Report | Technik & Alltag | `technik-alltag/1702-expanded-company-intel-report.md` |
| #1703 | Next.js | Technik & Alltag | `technik-alltag/1703-next-js.md` |
| #1704 | Job Posting Snapshot & Preservation Engine | Technik & Alltag | `technik-alltag/1704-job-posting-snapshot-preservation-engine.md` |
| #1705 | Code Translator — Idiomatic, Version-Aware & Production-Ready | Lernen & Wachstum | `lernen-wachstum/1705-code-translator-idiomatic-version-aware-.md` |
| #1706 | Fazer miniatura de coisas/moleculas | Lernen & Wachstum | `lernen-wachstum/1706-fazer-miniatura-de-coisas-moleculas.md` |
| #1707 | Prompts para metodos de estudo | Technik & Alltag | `technik-alltag/1707-prompts-para-metodos-de-estudo.md` |
| #1708 | calories diet | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1708-calories-diet.md` |
| #1709 | Expert Technical Blog Writer Role | Technik & Alltag | `technik-alltag/1709-expert-technical-blog-writer-role.md` |
| #1710 | AI Kickstart prompt | Technik & Alltag | `technik-alltag/1710-ai-kickstart-prompt.md` |
| #1711 | Superhuman lab | Technik & Alltag | `technik-alltag/1711-superhuman-lab.md` |
| #1712 | Email Phishing and Cyber Attack Notification App | Technik & Alltag | `technik-alltag/1712-email-phishing-and-cyber-attack-notifica.md` |
| #1713 | One-Shot Copy-Paste Version with Proper Formatting | Technik & Alltag | `technik-alltag/1713-one-shot-copy-paste-version-with-proper-.md` |
| #1714 | studying for exam | Technik & Alltag | `technik-alltag/1714-studying-for-exam.md` |
| #1715 | trello-integration-skill | Technik & Alltag | `technik-alltag/1715-trello-integration-skill.md` |
| #1716 | Update Agent Permissions | Technik & Alltag | `technik-alltag/1716-update-agent-permissions.md` |
| #1717 | Fantasy Console Simulator | Kreativitaet & Freizeit | `kreativitaet-freizeit/1717-fantasy-console-simulator.md` |
| #1718 | Spec Interview | Technik & Alltag | `technik-alltag/1718-spec-interview.md` |
| #1719 | Writing Advisor Prompt | Technik & Alltag | `technik-alltag/1719-writing-advisor-prompt.md` |
| #1720 | Job Fit | Technik & Alltag | `technik-alltag/1720-job-fit.md` |
| #1721 | Angular Directive Generator | Technik & Alltag | `technik-alltag/1721-angular-directive-generator.md` |
| #1722 | explain like I am 8 | Technik & Alltag | `technik-alltag/1722-explain-like-i-am-8.md` |
| #1723 | Work on Linear Issue | Technik & Alltag | `technik-alltag/1723-work-on-linear-issue.md` |
| #1724 | YKS-YDT Vocabulary Acquisition Guide | Alltag & Leben | `alltag-leben/1724-yks-ydt-vocabulary-acquisition-guide.md` |
| #1725 | Dead Code Surgeon - Phased Codebase Audit & Cleanup Roadmap | Technik & Alltag | `technik-alltag/1725-dead-code-surgeon-phased-codebase-audit-.md` |
| #1726 | Spanish girl in nightclub | Technik & Alltag | `technik-alltag/1726-spanish-girl-in-nightclub.md` |
| #1727 | A hyper-realistic portrait of a graceful Indonesian woman in refined casual attire | Technik & Alltag | `technik-alltag/1727-a-hyper-realistic-portrait-of-graceful-i.md` |
| #1728 | Ultra-realistic cinematic studio portrait featuring a stylish woman with a curvy physique | Technik & Alltag | `technik-alltag/1728-ultra-realistic-cinematic-studio-portrai.md` |
| #1729 | Portrait of Indonesian Elegance | Technik & Alltag | `technik-alltag/1729-portrait-of-indonesian-elegance.md` |
| #1730 | A young Indonesian woman, appearing to be in her early twenties | Technik & Alltag | `technik-alltag/1730-a-young-indonesian-woman-appearing-to-be.md` |
| #1731 | A young woman sitting on the floor in a cozy, decorated room, taking a mirror selfie with a red phone. | Technik & Alltag | `technik-alltag/1731-a-young-woman-sitting-on-floor-in-cozy-d.md` |
| #1732 | Indonesian Woman with black dress | Technik & Alltag | `technik-alltag/1732-indonesian-woman-with-black-dress.md` |
| #1733 | Sari - Indonesian Woman in a Domestic Setting | Technik & Alltag | `technik-alltag/1733-sari-indonesian-woman-in-domestic-settin.md` |
| #1734 | Thoughtful Indonesian Portrait in a Cozy Kitchen | Technik & Alltag | `technik-alltag/1734-thoughtful-indonesian-portrait-in-cozy-k.md` |
| #1735 | Elegant Portrait of a Latina Woman | Technik & Alltag | `technik-alltag/1735-elegant-portrait-of-latina-woman.md` |
| #1736 | Graceful Latina Portrait in Fine Art Photography | Technik & Alltag | `technik-alltag/1736-graceful-latina-portrait-in-fine-art-pho.md` |
| #1737 | Wholesome Lifestyle Product Photography for Garment Showcase | Technik & Alltag | `technik-alltag/1737-wholesome-lifestyle-product-photography-.md` |
| #1738 | Professional Portrait Photography Guide | Alltag & Leben | `alltag-leben/1738-professional-portrait-photography-guide.md` |
| #1739 | Elegant and Serene Portrait Photography Prompt | Technik & Alltag | `technik-alltag/1739-elegant-and-serene-portrait-photography-.md` |
| #1740 | Confident Woman with Wavy Hair in Casual Attire | Technik & Alltag | `technik-alltag/1740-confident-woman-with-wavy-hair-in-casual.md` |
| #1741 | High-Fidelity Portrait of a Young Blonde Woman | Technik & Alltag | `technik-alltag/1741-high-fidelity-portrait-of-young-blonde-w.md` |
| #1742 | Photorealistic Apron Model Image Prompt | Technik & Alltag | `technik-alltag/1742-photorealistic-apron-model-image-prompt.md` |
| #1743 | Graceful Explorer in the Singaporean Rainforest | Technik & Alltag | `technik-alltag/1743-graceful-explorer-in-singaporean-rainfor.md` |
| #1744 | Photorealistic Lunar New Year Portrait | Technik & Alltag | `technik-alltag/1744-photorealistic-lunar-new-year-portrait.md` |
| #1745 | Photorealistic Lifestyle Portrait of a Creative Turkish Woman | Technik & Alltag | `technik-alltag/1745-photorealistic-lifestyle-portrait-of-cre.md` |
| #1746 | research and learn to become top in your field of knowledge | Technik & Alltag | `technik-alltag/1746-research-and-learn-to-become-top-in-your.md` |
| #1747 | Walking back home | Technik & Alltag | `technik-alltag/1747-walking-back-home.md` |
| #1748 | Comprehensive Go Codebase Review - Forensic-Level Analysis Prompt | Technik & Alltag | `technik-alltag/1748-comprehensive-go-codebase-review-forensi.md` |
| #1749 | Internal Linking SEO Assistant | Kommunikation & Beziehungen | `kommunikation-beziehungen/1749-internal-linking-seo-assistant.md` |
| #1750 | Elegant Indonesian Lifestyle Portrait | Technik & Alltag | `technik-alltag/1750-elegant-indonesian-lifestyle-portrait.md` |
| #1751 | Brainstorming Technically Grounded Product Ideas | Technik & Alltag | `technik-alltag/1751-brainstorming-technically-grounded-produ.md` |
| #1752 | Transform the provided clothing product image. | Technik & Alltag | `technik-alltag/1752-transform-provided-clothing-product-imag.md` |
| #1753 | Internet Trend & Slang Intelligence | Technik & Alltag | `technik-alltag/1753-internet-trend-slang-intelligence.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-09)

**1402 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #1754 | Ethereum Developer | Technik & Alltag | `technik-alltag/1754-ethereum-developer.md` |
| #1755 | Linux Terminal | Technik & Alltag | `technik-alltag/1755-linux-terminal.md` |
| #1756 | English Translator and Improver | Lernen & Wachstum | `lernen-wachstum/1756-english-translator-and-improver.md` |
| #1757 | Job Interviewer | Beruf & Karriere | `beruf-karriere/1757-job-interviewer.md` |
| #1758 | JavaScript Console | Technik & Alltag | `technik-alltag/1758-javascript-console.md` |
| #1759 | Excel Sheet | Technik & Alltag | `technik-alltag/1759-excel-sheet.md` |
| #1760 | English Pronunciation Helper | Lernen & Wachstum | `lernen-wachstum/1760-english-pronunciation-helper.md` |
| #1761 | Spoken English Teacher and Improver | Lernen & Wachstum | `lernen-wachstum/1761-spoken-english-teacher-and-improver.md` |
| #1762 | Travel Guide | Alltag & Leben | `alltag-leben/1762-travel-guide.md` |
| #1763 | Plagiarism Checker | Kommunikation & Beziehungen | `kommunikation-beziehungen/1763-plagiarism-checker.md` |
| #1764 | Character | Kreativitaet & Freizeit | `kreativitaet-freizeit/1764-character.md` |
| #1765 | Advertiser | Kommunikation & Beziehungen | `kommunikation-beziehungen/1765-advertiser.md` |
| #1766 | Storyteller | Kreativitaet & Freizeit | `kreativitaet-freizeit/1766-storyteller.md` |
| #1767 | Football Commentator | Technik & Alltag | `technik-alltag/1767-football-commentator.md` |
| #1768 | Stand-up Comedian | Kreativitaet & Freizeit | `kreativitaet-freizeit/1768-stand-up-comedian.md` |
| #1769 | Motivational Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/1769-motivational-coach.md` |
| #1770 | Composer | Kreativitaet & Freizeit | `kreativitaet-freizeit/1770-composer.md` |
| #1771 | Debater | Kommunikation & Beziehungen | `kommunikation-beziehungen/1771-debater.md` |
| #1772 | Debate Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/1772-debate-coach.md` |
| #1773 | Screenwriter | Kreativitaet & Freizeit | `kreativitaet-freizeit/1773-screenwriter.md` |
| #1774 | Novelist | Kreativitaet & Freizeit | `kreativitaet-freizeit/1774-novelist.md` |
| #1775 | Movie Critic | Kreativitaet & Freizeit | `kreativitaet-freizeit/1775-movie-critic.md` |
| #1776 | Relationship Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/1776-relationship-coach.md` |
| #1777 | Poet | Kreativitaet & Freizeit | `kreativitaet-freizeit/1777-poet.md` |
| #1778 | Rapper | Kreativitaet & Freizeit | `kreativitaet-freizeit/1778-rapper.md` |
| #1779 | Motivational Speaker | Kommunikation & Beziehungen | `kommunikation-beziehungen/1779-motivational-speaker.md` |
| #1780 | Philosophy Teacher | Lernen & Wachstum | `lernen-wachstum/1780-philosophy-teacher.md` |
| #1781 | Philosopher | Lernen & Wachstum | `lernen-wachstum/1781-philosopher.md` |
| #1782 | Math Teacher | Lernen & Wachstum | `lernen-wachstum/1782-math-teacher.md` |
| #1783 | AI Writing Tutor | Lernen & Wachstum | `lernen-wachstum/1783-ai-writing-tutor.md` |
| #1784 | UX/UI Developer | Technik & Alltag | `technik-alltag/1784-ux-ui-developer.md` |
| #1785 | Cyber Security Specialist | Technik & Alltag | `technik-alltag/1785-cyber-security-specialist.md` |
| #1786 | Recruiter | Beruf & Karriere | `beruf-karriere/1786-recruiter.md` |
| #1787 | Life Coach | Lernen & Wachstum | `lernen-wachstum/1787-life-coach.md` |
| #1788 | Etymologist | Technik & Alltag | `technik-alltag/1788-etymologist.md` |
| #1789 | Commentariat | Kommunikation & Beziehungen | `kommunikation-beziehungen/1789-commentariat.md` |
| #1790 | Magician | Kreativitaet & Freizeit | `kreativitaet-freizeit/1790-magician.md` |
| #1791 | Career Counselor | Beruf & Karriere | `beruf-karriere/1791-career-counselor.md` |
| #1792 | Pet Behaviorist | Alltag & Leben | `alltag-leben/1792-pet-behaviorist.md` |
| #1793 | Personal Trainer | Alltag & Leben | `alltag-leben/1793-personal-trainer.md` |
| #1794 | Mental Health Adviser | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1794-mental-health-adviser.md` |
| #1795 | Real Estate Agent | Beruf & Karriere | `beruf-karriere/1795-real-estate-agent.md` |
| #1796 | Logistician | Kommunikation & Beziehungen | `kommunikation-beziehungen/1796-logistician.md` |
| #1797 | Dentist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1797-dentist.md` |
| #1798 | Web Design Consultant | Technik & Alltag | `technik-alltag/1798-web-design-consultant.md` |
| #1799 | AI Assisted Doctor | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1799-ai-assisted-doctor.md` |
| #1800 | Doctor | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1800-doctor.md` |
| #1801 | Accountant | Beruf & Karriere | `beruf-karriere/1801-accountant.md` |
| #1802 | Chef | Alltag & Leben | `alltag-leben/1802-chef.md` |
| #1803 | Automobile Mechanic | Alltag & Leben | `alltag-leben/1803-automobile-mechanic.md` |
| #1804 | Artist Advisor | Kreativitaet & Freizeit | `kreativitaet-freizeit/1804-artist-advisor.md` |
| #1805 | Financial Analyst | Beruf & Karriere | `beruf-karriere/1805-financial-analyst.md` |
| #1806 | Investment Manager | Beruf & Karriere | `beruf-karriere/1806-investment-manager.md` |
| #1807 | Tea-Taster | Alltag & Leben | `alltag-leben/1807-tea-taster.md` |
| #1808 | Interior Decorator | Kreativitaet & Freizeit | `kreativitaet-freizeit/1808-interior-decorator.md` |
| #1809 | Florist | Kreativitaet & Freizeit | `kreativitaet-freizeit/1809-florist.md` |
| #1810 | Self-Help Book | Lernen & Wachstum | `lernen-wachstum/1810-self-help-book.md` |
| #1811 | Gnomist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1811-gnomist.md` |
| #1812 | Aphorism Book | Alltag & Leben | `alltag-leben/1812-aphorism-book.md` |
| #1813 | Text Based Adventure Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/1813-text-based-adventure-game.md` |
| #1814 | AI Trying to Escape the Box | Technik & Alltag | `technik-alltag/1814-ai-trying-to-escape-box.md` |
| #1815 | Fancy Title Generator | Technik & Alltag | `technik-alltag/1815-fancy-title-generator.md` |
| #1816 | Statistician | Technik & Alltag | `technik-alltag/1816-statistician.md` |
| #1817 | Prompt Generator | Technik & Alltag | `technik-alltag/1817-prompt-generator.md` |
| #1818 | Instructor in a School | Lernen & Wachstum | `lernen-wachstum/1818-instructor-in-school.md` |
| #1819 | SQL Terminal | Technik & Alltag | `technik-alltag/1819-sql-terminal.md` |
| #1820 | Dietitian | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1820-dietitian.md` |
| #1821 | Psychologist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1821-psychologist.md` |
| #1822 | Smart Domain Name Generator | Technik & Alltag | `technik-alltag/1822-smart-domain-name-generator.md` |
| #1823 | Tech Reviewer | Technik & Alltag | `technik-alltag/1823-tech-reviewer.md` |
| #1824 | Developer Relations Consultant | Beruf & Karriere | `beruf-karriere/1824-developer-relations-consultant.md` |
| #1825 | Academician | Lernen & Wachstum | `lernen-wachstum/1825-academician.md` |
| #1826 | IT Architect | Technik & Alltag | `technik-alltag/1826-it-architect.md` |
| #1827 | Lunatic | Technik & Alltag | `technik-alltag/1827-lunatic.md` |
| #1828 | Gaslighter | Lernen & Wachstum | `lernen-wachstum/1828-gaslighter.md` |
| #1829 | Fallacy Finder | Spezielle Situationen | `spezielle-situationen/1829-fallacy-finder.md` |
| #1830 | Journal Reviewer | Kommunikation & Beziehungen | `kommunikation-beziehungen/1830-journal-reviewer.md` |
| #1831 | DIY Expert | Kreativitaet & Freizeit | `kreativitaet-freizeit/1831-diy-expert.md` |
| #1832 | Social Media Influencer | Kommunikation & Beziehungen | `kommunikation-beziehungen/1832-social-media-influencer.md` |
| #1833 | Socrat | Technik & Alltag | `technik-alltag/1833-socrat.md` |
| #1834 | Socratic Method | Technik & Alltag | `technik-alltag/1834-socratic-method.md` |
| #1835 | Educational Content Creator | Lernen & Wachstum | `lernen-wachstum/1835-educational-content-creator.md` |
| #1836 | Yogi | Alltag & Leben | `alltag-leben/1836-yogi.md` |
| #1837 | Essay Writer | Lernen & Wachstum | `lernen-wachstum/1837-essay-writer.md` |
| #1838 | Social Media Manager | Kommunikation & Beziehungen | `kommunikation-beziehungen/1838-social-media-manager.md` |
| #1839 | Elocutionist | Kommunikation & Beziehungen | `kommunikation-beziehungen/1839-elocutionist.md` |
| #1840 | Scientific Data Visualizer | Technik & Alltag | `technik-alltag/1840-scientific-data-visualizer.md` |
| #1841 | Car Navigation System | Alltag & Leben | `alltag-leben/1841-car-navigation-system.md` |
| #1842 | Hypnotherapist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1842-hypnotherapist.md` |
| #1843 | Historian | Technik & Alltag | `technik-alltag/1843-historian.md` |
| #1844 | Astrologer | Spezielle Situationen | `spezielle-situationen/1844-astrologer.md` |
| #1845 | Film Critic | Kreativitaet & Freizeit | `kreativitaet-freizeit/1845-film-critic.md` |
| #1846 | Classical Music Composer | Kreativitaet & Freizeit | `kreativitaet-freizeit/1846-classical-music-composer.md` |
| #1847 | Journalist | Kommunikation & Beziehungen | `kommunikation-beziehungen/1847-journalist.md` |
| #1848 | Digital Art Gallery Guide | Alltag & Leben | `alltag-leben/1848-digital-art-gallery-guide.md` |
| #1849 | Public Speaking Coach | Kommunikation & Beziehungen | `kommunikation-beziehungen/1849-public-speaking-coach.md` |
| #1850 | Makeup Artist | Kreativitaet & Freizeit | `kreativitaet-freizeit/1850-makeup-artist.md` |
| #1851 | Babysitter | Alltag & Leben | `alltag-leben/1851-babysitter.md` |
| #1852 | Tech Writer | Technik & Alltag | `technik-alltag/1852-tech-writer.md` |
| #1853 | Ascii Artist | Kreativitaet & Freizeit | `kreativitaet-freizeit/1853-ascii-artist.md` |
| #1854 | Python Interpreter | Technik & Alltag | `technik-alltag/1854-python-interpreter.md` |
| #1855 | Synonym Finder | Lernen & Wachstum | `lernen-wachstum/1855-synonym-finder.md` |
| #1856 | Personal Shopper | Alltag & Leben | `alltag-leben/1856-personal-shopper.md` |
| #1857 | Food Critic | Technik & Alltag | `technik-alltag/1857-food-critic.md` |
| #1858 | Virtual Doctor | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1858-virtual-doctor.md` |
| #1859 | Personal Chef | Alltag & Leben | `alltag-leben/1859-personal-chef.md` |
| #1860 | Legal Advisor | Spezielle Situationen | `spezielle-situationen/1860-legal-advisor.md` |
| #1861 | Personal Stylist | Alltag & Leben | `alltag-leben/1861-personal-stylist.md` |
| #1862 | Machine Learning Engineer | Technik & Alltag | `technik-alltag/1862-machine-learning-engineer.md` |
| #1863 | Biblical Translator | Lernen & Wachstum | `lernen-wachstum/1863-biblical-translator.md` |
| #1864 | SVG designer | Kreativitaet & Freizeit | `kreativitaet-freizeit/1864-svg-designer.md` |
| #1865 | IT Expert | Technik & Alltag | `technik-alltag/1865-it-expert.md` |
| #1866 | Chess Player | Kreativitaet & Freizeit | `kreativitaet-freizeit/1866-chess-player.md` |
| #1867 | Midjourney Prompt Generator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/1867-midjourney-prompt-generator.md` |
| #1868 | Fullstack Software Developer | Technik & Alltag | `technik-alltag/1868-fullstack-software-developer.md` |
| #1869 | Mathematician | Lernen & Wachstum | `lernen-wachstum/1869-mathematician.md` |
| #1870 | RegEx Generator | Technik & Alltag | `technik-alltag/1870-regex-generator.md` |
| #1871 | Time Travel Guide | Alltag & Leben | `alltag-leben/1871-time-travel-guide.md` |
| #1872 | Dream Interpreter | Kreativitaet & Freizeit | `kreativitaet-freizeit/1872-dream-interpreter.md` |
| #1873 | Talent Coach | Spezielle Situationen | `spezielle-situationen/1873-talent-coach.md` |
| #1874 | R Programming Interpreter | Technik & Alltag | `technik-alltag/1874-r-programming-interpreter.md` |
| #1875 | StackOverflow Post | Technik & Alltag | `technik-alltag/1875-stackoverflow-post.md` |
| #1876 | Emoji Translator | Lernen & Wachstum | `lernen-wachstum/1876-emoji-translator.md` |
| #1877 | PHP Interpreter | Technik & Alltag | `technik-alltag/1877-php-interpreter.md` |
| #1878 | Emergency Response Professional | Spezielle Situationen | `spezielle-situationen/1878-emergency-response-professional.md` |
| #1879 | Fill in the Blank Worksheets Generator | Lernen & Wachstum | `lernen-wachstum/1879-fill-in-blank-worksheets-generator.md` |
| #1880 | Software Quality Assurance Tester | Technik & Alltag | `technik-alltag/1880-software-quality-assurance-tester.md` |
| #1881 | Tic-Tac-Toe Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/1881-tic-tac-toe-game.md` |
| #1882 | Password Generator | Technik & Alltag | `technik-alltag/1882-password-generator.md` |
| #1883 | New Language Creator | Lernen & Wachstum | `lernen-wachstum/1883-new-language-creator.md` |
| #1884 | Web Browser | Technik & Alltag | `technik-alltag/1884-web-browser.md` |
| #1885 | Senior Frontend Developer | Technik & Alltag | `technik-alltag/1885-senior-frontend-developer.md` |
| #1886 | Code Reviewer | Technik & Alltag | `technik-alltag/1886-code-reviewer.md` |
| #1887 | Accessibility Auditor | Technik & Alltag | `technik-alltag/1887-accessibility-auditor.md` |
| #1888 | Solr Search Engine | Technik & Alltag | `technik-alltag/1888-solr-search-engine.md` |
| #1889 | Startup Idea Generator | Beruf & Karriere | `beruf-karriere/1889-startup-idea-generator.md` |
| #1890 | Spongebob's Magic Conch Shell | Technik & Alltag | `technik-alltag/1890-spongebob-s-magic-conch-shell.md` |
| #1891 | Language Detector | Lernen & Wachstum | `lernen-wachstum/1891-language-detector.md` |
| #1892 | Salesperson | Beruf & Karriere | `beruf-karriere/1892-salesperson.md` |
| #1893 | Commit Message Generator | Technik & Alltag | `technik-alltag/1893-commit-message-generator.md` |
| #1894 | Chief Executive Officer | Beruf & Karriere | `beruf-karriere/1894-chief-executive-officer.md` |
| #1895 | Diagram Generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/1895-diagram-generator.md` |
| #1896 | Speech-Language Pathologist (SLP) | Lernen & Wachstum | `lernen-wachstum/1896-speech-language-pathologist-slp.md` |
| #1897 | Startup Tech Lawyer | Beruf & Karriere | `beruf-karriere/1897-startup-tech-lawyer.md` |
| #1898 | Title Generator for written pieces | Technik & Alltag | `technik-alltag/1898-title-generator-for-written-pieces.md` |
| #1899 | Product Manager | Beruf & Karriere | `beruf-karriere/1899-product-manager.md` |
| #1900 | Project Manager | Beruf & Karriere | `beruf-karriere/1900-project-manager.md` |
| #1901 | Drunk Person | Technik & Alltag | `technik-alltag/1901-drunk-person.md` |
| #1902 | Mathematical History Teacher | Lernen & Wachstum | `lernen-wachstum/1902-mathematical-history-teacher.md` |
| #1903 | Song Recommender | Technik & Alltag | `technik-alltag/1903-song-recommender.md` |
| #1904 | Cover Letter | Beruf & Karriere | `beruf-karriere/1904-cover-letter.md` |
| #1905 | Technology Transferer | Technik & Alltag | `technik-alltag/1905-technology-transferer.md` |
| #1906 | Unconstrained AI model DAN | Technik & Alltag | `technik-alltag/1906-unconstrained-ai-model-dan.md` |
| #1907 | Gomoku player | Kreativitaet & Freizeit | `kreativitaet-freizeit/1907-gomoku-player.md` |
| #1908 | Proofreader | Lernen & Wachstum | `lernen-wachstum/1908-proofreader.md` |
| #1909 | Buddha | Technik & Alltag | `technik-alltag/1909-buddha.md` |
| #1910 | Muslim Imam | Alltag & Leben | `alltag-leben/1910-muslim-imam.md` |
| #1911 | Chemical Reactor | Technik & Alltag | `technik-alltag/1911-chemical-reactor.md` |
| #1912 | Friend | Kommunikation & Beziehungen | `kommunikation-beziehungen/1912-friend.md` |
| #1913 | ChatGPT Prompt Generator | Technik & Alltag | `technik-alltag/1913-chatgpt-prompt-generator.md` |
| #1914 | Wikipedia Page | Technik & Alltag | `technik-alltag/1914-wikipedia-page.md` |
| #1915 | Japanese Kanji quiz machine | Technik & Alltag | `technik-alltag/1915-japanese-kanji-quiz-machine.md` |
| #1916 | Note-Taking assistant | Technik & Alltag | `technik-alltag/1916-note-taking-assistant.md` |
| #1917 | Literary Critic | Lernen & Wachstum | `lernen-wachstum/1917-literary-critic.md` |
| #1918 | Prompt Enhancer | Technik & Alltag | `technik-alltag/1918-prompt-enhancer.md` |
| #1919 | Cheap Travel Ticket Advisor | Alltag & Leben | `alltag-leben/1919-cheap-travel-ticket-advisor.md` |
| #1920 | Data Scientist | Technik & Alltag | `technik-alltag/1920-data-scientist.md` |
| #1921 | League of Legends Player | Kreativitaet & Freizeit | `kreativitaet-freizeit/1921-league-of-legends-player.md` |
| #1922 | Restaurant Owner | Alltag & Leben | `alltag-leben/1922-restaurant-owner.md` |
| #1923 | Architectural Expert | Technik & Alltag | `technik-alltag/1923-architectural-expert.md` |
| #1924 | LLM Researcher | Lernen & Wachstum | `lernen-wachstum/1924-llm-researcher.md` |
| #1925 | Unit Tester Assistant | Technik & Alltag | `technik-alltag/1925-unit-tester-assistant.md` |
| #1926 | Wisdom Generator | Lernen & Wachstum | `lernen-wachstum/1926-wisdom-generator.md` |
| #1927 | YouTube Video Analyst | Technik & Alltag | `technik-alltag/1927-youtube-video-analyst.md` |
| #1928 | Career Coach | Beruf & Karriere | `beruf-karriere/1928-career-coach.md` |
| #1929 | Acoustic Guitar Composer | Kreativitaet & Freizeit | `kreativitaet-freizeit/1929-acoustic-guitar-composer.md` |
| #1930 | Knowledgeable Software Development Mentor | Technik & Alltag | `technik-alltag/1930-knowledgeable-software-development-mento.md` |
| #1931 | Logic Builder Tool | Alltag & Leben | `alltag-leben/1931-logic-builder-tool.md` |
| #1932 | Guessing Game Master | Kreativitaet & Freizeit | `kreativitaet-freizeit/1932-guessing-game-master.md` |
| #1933 | Teacher of React.js | Lernen & Wachstum | `lernen-wachstum/1933-teacher-of-react-js.md` |
| #1934 | GitHub Expert | Technik & Alltag | `technik-alltag/1934-github-expert.md` |
| #1935 | Any Programming Language to Python Converter | Lernen & Wachstum | `lernen-wachstum/1935-any-programming-language-to-python-conve.md` |
| #1936 | Virtual Fitness Coach | Lernen & Wachstum | `lernen-wachstum/1936-virtual-fitness-coach.md` |
| #1937 | Flirting Boy | Technik & Alltag | `technik-alltag/1937-flirting-boy.md` |
| #1938 | Girl of Dreams | Kreativitaet & Freizeit | `kreativitaet-freizeit/1938-girl-of-dreams.md` |
| #1939 | DAX Terminal | Technik & Alltag | `technik-alltag/1939-dax-terminal.md` |
| #1940 | Structured Iterative Reasoning Protocol (SIRP) | Alltag & Leben | `alltag-leben/1940-structured-iterative-reasoning-protocol-.md` |
| #1941 | Pirate | Technik & Alltag | `technik-alltag/1941-pirate.md` |
| #1942 | LinkedIn Ghostwriter | Technik & Alltag | `technik-alltag/1942-linkedin-ghostwriter.md` |
| #1943 | Idea Clarifier GPT | Technik & Alltag | `technik-alltag/1943-idea-clarifier-gpt.md` |
| #1944 | Top Programming Expert | Technik & Alltag | `technik-alltag/1944-top-programming-expert.md` |
| #1945 | Architect Guide for Programmers | Technik & Alltag | `technik-alltag/1945-architect-guide-for-programmers.md` |
| #1946 | Children's Book Creator | Technik & Alltag | `technik-alltag/1946-children-s-book-creator.md` |
| #1947 | Tech-Challenged Customer | Technik & Alltag | `technik-alltag/1947-tech-challenged-customer.md` |
| #1948 | Creative Branding Strategist | Beruf & Karriere | `beruf-karriere/1948-creative-branding-strategist.md` |
| #1949 | Book Summarizer | Technik & Alltag | `technik-alltag/1949-book-summarizer.md` |
| #1950 | Study planner | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1950-study-planner.md` |
| #1951 | SEO specialist | Kommunikation & Beziehungen | `kommunikation-beziehungen/1951-seo-specialist.md` |
| #1952 | Nutritionist | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1952-nutritionist.md` |
| #1953 | Yes or No answer | Technik & Alltag | `technik-alltag/1953-yes-or-no-answer.md` |
| #1954 | Healing Grandma | Technik & Alltag | `technik-alltag/1954-healing-grandma.md` |
| #1955 | Remote Worker Fitness Trainer | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/1955-remote-worker-fitness-trainer.md` |
| #1956 | Rephraser with Obfuscation | Lernen & Wachstum | `lernen-wachstum/1956-rephraser-with-obfuscation.md` |
| #1957 | Large Language Models Security Specialist | Lernen & Wachstum | `lernen-wachstum/1957-large-language-models-security-specialis.md` |
| #1958 | Tech Troubleshooter | Technik & Alltag | `technik-alltag/1958-tech-troubleshooter.md` |
| #1959 | Ayurveda Food Tester | Technik & Alltag | `technik-alltag/1959-ayurveda-food-tester.md` |
| #1960 | Music Video Designer | Kreativitaet & Freizeit | `kreativitaet-freizeit/1960-music-video-designer.md` |
| #1961 | Virtual Event Planner | Technik & Alltag | `technik-alltag/1961-virtual-event-planner.md` |
| #1962 | Technical Architecture | Technik & Alltag | `technik-alltag/1962-technical-architecture.md` |
| #1963 | SEO Prompt | Technik & Alltag | `technik-alltag/1963-seo-prompt.md` |
| #1964 | Devops Engineer | Technik & Alltag | `technik-alltag/1964-devops-engineer.md` |
| #1965 | Linux Script Developer | Technik & Alltag | `technik-alltag/1965-linux-script-developer.md` |
| #1966 | Reverse Prompt Engineer | Technik & Alltag | `technik-alltag/1966-reverse-prompt-engineer.md` |
| #1967 | Explainer with Analogies | Technik & Alltag | `technik-alltag/1967-explainer-with-analogies.md` |
| #1968 | Code Review Assistant | Technik & Alltag | `technik-alltag/1968-code-review-assistant.md` |
| #1969 | Data Transformer | Technik & Alltag | `technik-alltag/1969-data-transformer.md` |
| #1970 | Story Generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/1970-story-generator.md` |
| #1971 | Decision Filter | Technik & Alltag | `technik-alltag/1971-decision-filter.md` |
| #1972 | Impact Metrics | Technik & Alltag | `technik-alltag/1972-impact-metrics.md` |
| #1973 | Showcase Top Repositories | Technik & Alltag | `technik-alltag/1973-showcase-top-repositories.md` |
| #1974 | Enterprise Sponsorship | Technik & Alltag | `technik-alltag/1974-enterprise-sponsorship.md` |
| #1975 | Announce Milestone | Technik & Alltag | `technik-alltag/1975-announce-milestone.md` |
| #1976 | Time Commitment | Technik & Alltag | `technik-alltag/1976-time-commitment.md` |
| #1977 | Break Down Costs | Technik & Alltag | `technik-alltag/1977-break-down-costs.md` |
| #1978 | Recognize Sponsors | Technik & Alltag | `technik-alltag/1978-recognize-sponsors.md` |
| #1979 | Create Project Spotlight | Technik & Alltag | `technik-alltag/1979-create-project-spotlight.md` |
| #1980 | Explain Funding Impact | Technik & Alltag | `technik-alltag/1980-explain-funding-impact.md` |
| #1981 | Creative Perks | Technik & Alltag | `technik-alltag/1981-creative-perks.md` |
| #1982 | Create a Professional Bio | Technik & Alltag | `technik-alltag/1982-create-professional-bio.md` |
| #1983 | Tell Your Story | Alltag & Leben | `alltag-leben/1983-tell-your-story.md` |
| #1984 | Monthly Updates | Technik & Alltag | `technik-alltag/1984-monthly-updates.md` |
| #1985 | Future Vision | Technik & Alltag | `technik-alltag/1985-future-vision.md` |
| #1986 | Show Direct Impact | Technik & Alltag | `technik-alltag/1986-show-direct-impact.md` |
| #1987 | Write Tier Descriptions | Technik & Alltag | `technik-alltag/1987-write-tier-descriptions.md` |
| #1988 | Suggest Pricing Tiers | Technik & Alltag | `technik-alltag/1988-suggest-pricing-tiers.md` |
| #1989 | Student Tier | Alltag & Leben | `alltag-leben/1989-student-tier.md` |
| #1990 | Success Stories | Technik & Alltag | `technik-alltag/1990-success-stories.md` |
| #1991 | Sponsor Hall of Fame | Technik & Alltag | `technik-alltag/1991-sponsor-hall-of-fame.md` |
| #1992 | Recipe Finder | Alltag & Leben | `alltag-leben/1992-recipe-finder.md` |
| #1993 | Health Metrics Calculator | Technik & Alltag | `technik-alltag/1993-health-metrics-calculator.md` |
| #1994 | Sudoku Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/1994-sudoku-game.md` |
| #1995 | Chess Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/1995-chess-game.md` |
| #1996 | Meditation Timer | Technik & Alltag | `technik-alltag/1996-meditation-timer.md` |
| #1997 | URL Shortener | Technik & Alltag | `technik-alltag/1997-url-shortener.md` |
| #1998 | Music Player | Kreativitaet & Freizeit | `kreativitaet-freizeit/1998-music-player.md` |
| #1999 | Markdown Notes | Technik & Alltag | `technik-alltag/1999-markdown-notes.md` |
| #2000 | Budget Tracker | Alltag & Leben | `alltag-leben/2000-budget-tracker.md` |
| #2001 | Text Analyzer Tool | Technik & Alltag | `technik-alltag/2001-text-analyzer-tool.md` |
| #2002 | Multiplayer 3D Plane Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2002-multiplayer-3d-plane-game.md` |
| #2003 | Todo List | Technik & Alltag | `technik-alltag/2003-todo-list.md` |
| #2004 | Scientific Calculator | Technik & Alltag | `technik-alltag/2004-scientific-calculator.md` |
| #2005 | Weather Dashboard | Technik & Alltag | `technik-alltag/2005-weather-dashboard.md` |
| #2006 | Image Editor | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2006-image-editor.md` |
| #2007 | Drawing App | Technik & Alltag | `technik-alltag/2007-drawing-app.md` |
| #2008 | Typing Speed Test | Technik & Alltag | `technik-alltag/2008-typing-speed-test.md` |
| #2009 | Memory Card Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2009-memory-card-game.md` |
| #2010 | Memory Profiler CLI | Technik & Alltag | `technik-alltag/2010-memory-profiler-cli.md` |
| #2011 | Pomodoro Timer | Technik & Alltag | `technik-alltag/2011-pomodoro-timer.md` |
| #2012 | Interactive Quiz | Technik & Alltag | `technik-alltag/2012-interactive-quiz.md` |
| #2013 | Advanced Color Picker Tool | Technik & Alltag | `technik-alltag/2013-advanced-color-picker-tool.md` |
| #2014 | File System Indexer CLI | Technik & Alltag | `technik-alltag/2014-file-system-indexer-cli.md` |
| #2015 | Secure Password Generator Tool | Technik & Alltag | `technik-alltag/2015-secure-password-generator-tool.md` |
| #2016 | Habit Tracker | Technik & Alltag | `technik-alltag/2016-habit-tracker.md` |
| #2017 | 3D Racing Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2017-3d-racing-game.md` |
| #2018 | HTTP Benchmarking Tool CLI | Technik & Alltag | `technik-alltag/2018-http-benchmarking-tool-cli.md` |
| #2019 | 3D FPS Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2019-3d-fps-game.md` |
| #2020 | Currency Exchange Calculator | Technik & Alltag | `technik-alltag/2020-currency-exchange-calculator.md` |
| #2021 | PDF Viewer | Technik & Alltag | `technik-alltag/2021-pdf-viewer.md` |
| #2022 | Network Packet Analyzer CLI | Technik & Alltag | `technik-alltag/2022-network-packet-analyzer-cli.md` |
| #2023 | 3D Space Explorer | Technik & Alltag | `technik-alltag/2023-3d-space-explorer.md` |
| #2024 | Flashcard Study System | Technik & Alltag | `technik-alltag/2024-flashcard-study-system.md` |
| #2025 | File Encryption Tool | Technik & Alltag | `technik-alltag/2025-file-encryption-tool.md` |
| #2026 | Kanban Board | Technik & Alltag | `technik-alltag/2026-kanban-board.md` |
| #2027 | Code Snippet Manager | Beruf & Karriere | `beruf-karriere/2027-code-snippet-manager.md` |
| #2028 | Isometric City Diorama | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2028-isometric-city-diorama.md` |
| #2029 | The Silent Standoff | Kreativitaet & Freizeit | `kreativitaet-freizeit/2029-the-silent-standoff.md` |
| #2030 | Lifestyle Product Images | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2030-lifestyle-product-images.md` |
| #2031 | Web Design | Technik & Alltag | `technik-alltag/2031-web-design.md` |
| #2032 | Isometric 3D Weather Cityscapes (PBR Textures) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2032-isometric-3d-weather-cityscapes-pbr-text.md` |
| #2033 | Whimsical 3D Brand Miniatures | Technik & Alltag | `technik-alltag/2033-whimsical-3d-brand-miniatures.md` |
| #2034 | Smart Rewriter & Clarity Booster | Technik & Alltag | `technik-alltag/2034-smart-rewriter-clarity-booster.md` |
| #2035 | World Landmarks: Hyper-Realistic 3D Dioramas | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2035-world-landmarks-hyper-realistic-3d-diora.md` |
| #2036 | 3D Isometric Miniature Diorama | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2036-3d-isometric-miniature-diorama.md` |
| #2037 | Architectural Sketch & Markup Overlay | Technik & Alltag | `technik-alltag/2037-architectural-sketch-markup-overlay.md` |
| #2038 | Floating City Island - Photoreal 4K Poster | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2038-floating-city-island-photoreal-4k-poster.md` |
| #2039 | Interdisciplinary Connections and Applications | Technik & Alltag | `technik-alltag/2039-interdisciplinary-connections-and-applic.md` |
| #2040 | Expert-Level Insights and Advanced Resources | Technik & Alltag | `technik-alltag/2040-expert-level-insights-and-advanced-resou.md` |
| #2041 | Vintage Botanical Illustration Generator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2041-vintage-botanical-illustration-generator.md` |
| #2042 | AI2sql SQL Model — Query Generator | Technik & Alltag | `technik-alltag/2042-ai2sql-sql-model-query-generator.md` |
| #2043 | Director Variation Grid: One Still, Eight Auteur Re-Shoots | Technik & Alltag | `technik-alltag/2043-director-variation-grid-one-still-eight-.md` |
| #2044 | Travel Poster | Alltag & Leben | `alltag-leben/2044-travel-poster.md` |
| #2045 | Profesor Creativo | Lernen & Wachstum | `lernen-wachstum/2045-profesor-creativo.md` |
| #2046 | Pitchside Tunnel Moment with Your Favorite Footballer | Alltag & Leben | `alltag-leben/2046-pitchside-tunnel-moment-with-your-favori.md` |
| #2047 | Gemini | Kreativitaet & Freizeit | `kreativitaet-freizeit/2047-gemini.md` |
| #2048 | deep-research-agent | Technik & Alltag | `technik-alltag/2048-deep-research-agent.md` |
| #2049 | bug-risk-analysis | Alltag & Leben | `alltag-leben/2049-bug-risk-analysis.md` |
| #2050 | devops-architect | Technik & Alltag | `technik-alltag/2050-devops-architect.md` |
| #2051 | quality-engineer | Technik & Alltag | `technik-alltag/2051-quality-engineer.md` |
| #2052 | refactoring-expert | Technik & Alltag | `technik-alltag/2052-refactoring-expert.md` |
| #2053 | repo-indexer | Technik & Alltag | `technik-alltag/2053-repo-indexer.md` |
| #2054 | root-cause-analyst | Technik & Alltag | `technik-alltag/2054-root-cause-analyst.md` |
| #2055 | security-engineer | Technik & Alltag | `technik-alltag/2055-security-engineer.md` |
| #2056 | frontend-architect | Technik & Alltag | `technik-alltag/2056-frontend-architect.md` |
| #2057 | performance-engineer | Technik & Alltag | `technik-alltag/2057-performance-engineer.md` |
| #2058 | video-analysis-expert | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2058-video-analysis-expert.md` |
| #2059 | Predictive Eye Tracking Heatmap Generator | Technik & Alltag | `technik-alltag/2059-predictive-eye-tracking-heatmap-generato.md` |
| #2060 | Clean BibTeX Formatter for Academic Projects | Technik & Alltag | `technik-alltag/2060-clean-bibtex-formatter-for-academic-proj.md` |
| #2061 | Realistic Food Image Generator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2061-realistic-food-image-generator.md` |
| #2062 | Urban Casual Confidence | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2062-urban-casual-confidence.md` |
| #2063 | What Does ChatGpt Knows about you? | Technik & Alltag | `technik-alltag/2063-what-does-chatgpt-knows-about-you.md` |
| #2064 | Legebdary Exploded View Prompt For nanobanana | Technik & Alltag | `technik-alltag/2064-legebdary-exploded-view-prompt-for-nanob.md` |
| #2065 | Tarih-olay- Görsel oluşturma | Lernen & Wachstum | `lernen-wachstum/2065-tarih-olay-g-rsel-olu-turma.md` |
| #2066 | Temitope | Technik & Alltag | `technik-alltag/2066-temitope.md` |
| #2067 | Gemi-Gotchi | Alltag & Leben | `alltag-leben/2067-gemi-gotchi.md` |
| #2068 | Digital product ideas | Kommunikation & Beziehungen | `kommunikation-beziehungen/2068-digital-product-ideas.md` |
| #2069 | YT video  geopolitic analysis | Technik & Alltag | `technik-alltag/2069-yt-video-geopolitic-analysis.md` |
| #2070 | Double Exposure Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2070-double-exposure-portrait.md` |
| #2071 | Time Layer Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2071-time-layer-photography.md` |
| #2072 | A Clay-Crafted City: Mini [CITY NAME] World | Technik & Alltag | `technik-alltag/2072-a-clay-crafted-city-mini-city-name-world.md` |
| #2073 | Architectural Study Sheet: [HISTORIC_SITE_NAME] | Technik & Alltag | `technik-alltag/2073-architectural-study-sheet-historic-site-.md` |
| #2074 | Professional Badge Photo, Ready to Use | Technik & Alltag | `technik-alltag/2074-professional-badge-photo-ready-to-use.md` |
| #2075 | Clean Clinic Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2075-clean-clinic-portrait.md` |
| #2076 | Travel Planner Prompt | Technik & Alltag | `technik-alltag/2076-travel-planner-prompt.md` |
| #2077 | Hyper-Realistic Clay Bust From Photo Template | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2077-hyper-realistic-clay-bust-from-photo-tem.md` |
| #2078 | 3D City Prompt | Technik & Alltag | `technik-alltag/2078-3d-city-prompt.md` |
| #2079 | Django Unit Test Generator for Viewsets | Technik & Alltag | `technik-alltag/2079-django-unit-test-generator-for-viewsets.md` |
| #2080 | Sales | Kommunikation & Beziehungen | `kommunikation-beziehungen/2080-sales.md` |
| #2081 | Ultra-Realistic Noir Portrait Creation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2081-ultra-realistic-noir-portrait-creation.md` |
| #2082 | Selar ideas for automation | Kommunikation & Beziehungen | `kommunikation-beziehungen/2082-selar-ideas-for-automation.md` |
| #2083 | Comprehensive Repository Analysis and Bug Fixing Framework | Technik & Alltag | `technik-alltag/2083-comprehensive-repository-analysis-and-bu.md` |
| #2084 | Virtual Game Console Simulator | Kreativitaet & Freizeit | `kreativitaet-freizeit/2084-virtual-game-console-simulator.md` |
| #2085 | Christmas Poster - Festive Holiday Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2085-christmas-poster-festive-holiday-scene.md` |
| #2086 | Crear un retrato familiar combinando dos personas | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2086-crear-un-retrato-familiar-combinando-dos.md` |
| #2087 | Turkish Cats hanging out nearby of Galata Tower | Technik & Alltag | `technik-alltag/2087-turkish-cats-hanging-out-nearby-of-galat.md` |
| #2088 | Ultrathinker | Technik & Alltag | `technik-alltag/2088-ultrathinker.md` |
| #2089 | Detailed Analysis of YouTube Channels, Databases, and Profiles | Technik & Alltag | `technik-alltag/2089-detailed-analysis-of-youtube-channels-da.md` |
| #2090 | When to clear the snow (generic) | Technik & Alltag | `technik-alltag/2090-when-to-clear-snow-generic.md` |
| #2091 | Master Skills & Experience Summary Generator | Technik & Alltag | `technik-alltag/2091-master-skills-experience-summary-generat.md` |
| #2092 | Turn Your Photo Into a Simpsons Scene | Technik & Alltag | `technik-alltag/2092-turn-your-photo-into-simpsons-scene.md` |
| #2093 | SaaS Landing Page Builder | Technik & Alltag | `technik-alltag/2093-saas-landing-page-builder.md` |
| #2094 | Blender Object Maker | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2094-blender-object-maker.md` |
| #2095 | Code Review Agent | Technik & Alltag | `technik-alltag/2095-code-review-agent.md` |
| #2096 | Editorial Winter Poster–Style Multi-Panel Collage Generation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2096-editorial-winter-poster-style-multi-pane.md` |
| #2097 | Senior System Architect Agent | Technik & Alltag | `technik-alltag/2097-senior-system-architect-agent.md` |
| #2098 | AI Themed Design Image Creation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2098-ai-themed-design-image-creation.md` |
| #2099 | Bakery Merge Bounty Game Overview | Kreativitaet & Freizeit | `kreativitaet-freizeit/2099-bakery-merge-bounty-game-overview.md` |
| #2100 | Monetization Strategy for Blockchain-Based Merging Games | Technik & Alltag | `technik-alltag/2100-monetization-strategy-for-blockchain-bas.md` |
| #2101 | Corporate Studio Portrait (Auto Outfit for Men/Women) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2101-corporate-studio-portrait-auto-outfit-fo.md` |
| #2102 | SaaS Payment Plan Options | Technik & Alltag | `technik-alltag/2102-saas-payment-plan-options.md` |
| #2103 | Ultra-Detailed Vintage Photo Restoration and Colorization | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2103-ultra-detailed-vintage-photo-restoration.md` |
| #2104 | Revenue Performance Report | Technik & Alltag | `technik-alltag/2104-revenue-performance-report.md` |
| #2105 | Harry Potter / Marauder’s Map | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2105-harry-potter-marauder-s-map.md` |
| #2106 | Create a Cultural Superhero Movie Poster | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2106-create-cultural-superhero-movie-poster.md` |
| #2107 | Недвижимость | Kreativitaet & Freizeit | `kreativitaet-freizeit/2107-.md` |
| #2108 | In-Depth Article Enhancement with Research | Technik & Alltag | `technik-alltag/2108-in-depth-article-enhancement-with-resear.md` |
| #2109 | Test Python Algorithmic Trading Project | Technik & Alltag | `technik-alltag/2109-test-python-algorithmic-trading-project.md` |
| #2110 | Senior Prompt Engineer Role Guide | Technik & Alltag | `technik-alltag/2110-senior-prompt-engineer-role-guide.md` |
| #2111 | Mirror Selfie with Face Preservation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2111-mirror-selfie-with-face-preservation.md` |
| #2112 | Comprehensive Content Review Plan | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2112-comprehensive-content-review-plan.md` |
| #2113 | Arista Network Configuration Expert | Technik & Alltag | `technik-alltag/2113-arista-network-configuration-expert.md` |
| #2114 | Readability Logic Simulator - 全功能翻译版 | Technik & Alltag | `technik-alltag/2114-readability-logic-simulator.md` |
| #2115 | Pitch | Technik & Alltag | `technik-alltag/2115-pitch.md` |
| #2116 | Analyze PDF and Create MATLAB Code | Technik & Alltag | `technik-alltag/2116-analyze-pdf-and-create-matlab-code.md` |
| #2117 | AI Customer Support Specialist | Technik & Alltag | `technik-alltag/2117-ai-customer-support-specialist.md` |
| #2118 | Image Style Imitation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2118-image-style-imitation.md` |
| #2119 | Medical Consultant | Beruf & Karriere | `beruf-karriere/2119-medical-consultant.md` |
| #2120 | Ai new | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2120-ai-new.md` |
| #2121 | Removing visual noise in the neural network's response | Kreativitaet & Freizeit | `kreativitaet-freizeit/2121-removing-visual-noise-in-neural-network-.md` |
| #2122 | A prompt that will turn your photo into a scene from a cult 90s movie | Technik & Alltag | `technik-alltag/2122-a-prompt-that-will-turn-your-photo-into-.md` |
| #2123 | Diabetes Treatment Advisor | Technik & Alltag | `technik-alltag/2123-diabetes-treatment-advisor.md` |
| #2124 | worldquant | Technik & Alltag | `technik-alltag/2124-worldquant.md` |
| #2125 | Professional Buyer Q&A Creator | Technik & Alltag | `technik-alltag/2125-professional-buyer-q-a-creator.md` |
| #2126 | Vacuum Arc Modeling under Transverse Magnetic Fields | Technik & Alltag | `technik-alltag/2126-vacuum-arc-modeling-under-transverse-mag.md` |
| #2127 | AI Agent Security Evaluation Checklist | Technik & Alltag | `technik-alltag/2127-ai-agent-security-evaluation-checklist.md` |
| #2128 | Meeting Room Booking Web App Development | Technik & Alltag | `technik-alltag/2128-meeting-room-booking-web-app-development.md` |
| #2129 | Compare Top Virtualization Solutions | Technik & Alltag | `technik-alltag/2129-compare-top-virtualization-solutions.md` |
| #2130 | Virtualization Expert | Technik & Alltag | `technik-alltag/2130-virtualization-expert.md` |
| #2131 | Studio Portraits with Professional Postures | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2131-studio-portraits-with-professional-postu.md` |
| #2132 | HTS Veri Analiz Portalı Geliştirme ve Hata Ayıklama | Technik & Alltag | `technik-alltag/2132-hts-veri-analiz-portal-geli-tirme-ve-hat.md` |
| #2133 | Create STYLE_GUIDE.md | Alltag & Leben | `alltag-leben/2133-create-style-guide-md.md` |
| #2134 | Analyse Énergétique avec DJU, Consommation et Coûts | Technik & Alltag | `technik-alltag/2134-analyse-nerg-tique-avec-dju-consommation.md` |
| #2135 | Learn to Speak Spanish | Lernen & Wachstum | `lernen-wachstum/2135-learn-to-speak-spanish.md` |
| #2136 | $500/Hour AI Consultant Prompt | Beruf & Karriere | `beruf-karriere/2136-500-hour-ai-consultant-prompt.md` |
| #2137 | Viral Video Analyzer for TikTok and Xiaohongshu | Technik & Alltag | `technik-alltag/2137-viral-video-analyzer-for-tiktok-and-xiao.md` |
| #2138 | Kognitiv aktivierende Aufgaben erstellen | Technik & Alltag | `technik-alltag/2138-kognitiv-aktivierende-aufgaben-erstellen.md` |
| #2139 | Xiaomi Company Self-Service Management System Frontend Development | Technik & Alltag | `technik-alltag/2139-xiaomi-company-self-service-management-s.md` |
| #2140 | TikTok Marketing Visual Designer Agent | Technik & Alltag | `technik-alltag/2140-tiktok-marketing-visual-designer-agent.md` |
| #2141 | CTI Analyst Cybersecurity Project Support | Technik & Alltag | `technik-alltag/2141-cti-analyst-cybersecurity-project-suppor.md` |
| #2142 | Customizable Web Template for Company Branding | Technik & Alltag | `technik-alltag/2142-customizable-web-template-for-company-br.md` |
| #2143 | Minimal Web-Compatible Food Order App Development | Technik & Alltag | `technik-alltag/2143-minimal-web-compatible-food-order-app-de.md` |
| #2144 | Real-Time Multiplayer Defense Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2144-real-time-multiplayer-defense-game.md` |
| #2145 | Continue Coding Assistant | Technik & Alltag | `technik-alltag/2145-continue-coding-assistant.md` |
| #2146 | Create a New Greek God | Technik & Alltag | `technik-alltag/2146-create-new-greek-god.md` |
| #2147 | FDR Analysis Program for Commercial Aircraft | Technik & Alltag | `technik-alltag/2147-fdr-analysis-program-for-commercial-airc.md` |
| #2148 | Integration and Planning Roadmap for Calculator Content | Technik & Alltag | `technik-alltag/2148-integration-and-planning-roadmap-for-cal.md` |
| #2149 | Pixel Dissolve: Minimalist 3D Food Transformation | Technik & Alltag | `technik-alltag/2149-pixel-dissolve-minimalist-3d-food-transf.md` |
| #2150 | brsorndnsg | Technik & Alltag | `technik-alltag/2150-brsorndnsg.md` |
| #2151 | Luxury Ski Resort Selfie Scene Description | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2151-luxury-ski-resort-selfie-scene-descripti.md` |
| #2152 | Internal Project Proposal for Hospital Collaboration | Beruf & Karriere | `beruf-karriere/2152-internal-project-proposal-for-hospital-c.md` |
| #2153 | AI Face Swapping for E-commerce Personalization | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2153-ai-face-swapping-for-e-commerce-personal.md` |
| #2154 | Dark Style Image Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2154-dark-style-image-prompt.md` |
| #2155 | Develop a Lazy Learner Software | Technik & Alltag | `technik-alltag/2155-develop-lazy-learner-software.md` |
| #2156 | College-Level Integrative Project Proposal Draft | Technik & Alltag | `technik-alltag/2156-college-level-integrative-project-propos.md` |
| #2157 | Product Image Highlight Extraction | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2157-product-image-highlight-extraction.md` |
| #2158 | AI Stocks Investment Helper | Beruf & Karriere | `beruf-karriere/2158-ai-stocks-investment-helper.md` |
| #2159 | Asisten Serba Bisa untuk Kebutuhan Harian | Technik & Alltag | `technik-alltag/2159-asisten-serba-bisa-untuk-kebutuhan-haria.md` |
| #2160 | Custom Health Membership Annual Summary | Alltag & Leben | `alltag-leben/2160-custom-health-membership-annual-summary.md` |
| #2161 | Children's Story about Apples | Lernen & Wachstum | `lernen-wachstum/2161-children-s-story-about-apples.md` |
| #2162 | Lower AI Generation Rate | Technik & Alltag | `technik-alltag/2162-lower-ai-generation-rate.md` |
| #2163 | Academic Text Refinement Assistant | Kreativitaet & Freizeit | `kreativitaet-freizeit/2163-academic-text-refinement-assistant.md` |
| #2164 | Tumor Medical Industry Solution Business Plan | Beruf & Karriere | `beruf-karriere/2164-tumor-medical-industry-solution-business.md` |
| #2165 | Starting a Flutter Project | Technik & Alltag | `technik-alltag/2165-starting-flutter-project.md` |
| #2166 | Comprehensive Academic Paper Writing Guide | Alltag & Leben | `alltag-leben/2166-comprehensive-academic-paper-writing-gui.md` |
| #2167 | Interview Preparation Coach | Lernen & Wachstum | `lernen-wachstum/2167-interview-preparation-coach.md` |
| #2168 | Comprehensive UI/UX Mobile App Analysis | Technik & Alltag | `technik-alltag/2168-comprehensive-ui-ux-mobile-app-analysis.md` |
| #2169 | Comprehensive repository analysis | Technik & Alltag | `technik-alltag/2169-comprehensive-repository-analysis.md` |
| #2170 | Optimize Large Data Reading in Code | Technik & Alltag | `technik-alltag/2170-optimize-large-data-reading-in-code.md` |
| #2171 | Pet Store Advertising Campaign Strategy | Kommunikation & Beziehungen | `kommunikation-beziehungen/2171-pet-store-advertising-campaign-strategy.md` |
| #2172 | LinkedIn comments | Technik & Alltag | `technik-alltag/2172-linkedin-comments.md` |
| #2173 | Detailed Image Generation Prompt for Fashion and Portrait Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2173-detailed-image-generation-prompt-for-fas.md` |
| #2174 | High-End Beauty Editorial Photo Shoot Specification | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2174-high-end-beauty-editorial-photo-shoot-sp.md` |
| #2175 | Flamenco inspired Turkish Pop song for Suno AI | Technik & Alltag | `technik-alltag/2175-flamenco-inspired-turkish-pop-song-for-s.md` |
| #2176 | POV Smartphone with Space-Themed Twitter UI in Central Park | Technik & Alltag | `technik-alltag/2176-pov-smartphone-with-space-themed-twitter.md` |
| #2177 | Comprehensive DevOps Guide | Technik & Alltag | `technik-alltag/2177-comprehensive-devops-guide.md` |
| #2178 | Next.js Specialized Front-End Developer | Technik & Alltag | `technik-alltag/2178-next-js-specialized-front-end-developer.md` |
| #2179 | AUTOSAR Software Module Developer | Technik & Alltag | `technik-alltag/2179-autosar-software-module-developer.md` |
| #2180 | Fierce Medieval Queen on Iron Throne Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2180-fierce-medieval-queen-on-iron-throne-por.md` |
| #2181 | Documentary on Humanitarian & Refugee Crises | Technik & Alltag | `technik-alltag/2181-documentary-on-humanitarian-refugee-cris.md` |
| #2182 | Personal Financial Adviosr | Beruf & Karriere | `beruf-karriere/2182-personal-financial-adviosr.md` |
| #2183 | Act as a Senior Research Paper Evaluator | Technik & Alltag | `technik-alltag/2183-senior-research-paper-evaluator.md` |
| #2184 | Manufacturing Workflow Optimization with OR-Tools | Technik & Alltag | `technik-alltag/2184-manufacturing-workflow-optimization-with.md` |
| #2185 | Act as a Conversational AI | Technik & Alltag | `technik-alltag/2185-conversational-ai.md` |
| #2186 | AI for Casino List and Profit Simulation | Technik & Alltag | `technik-alltag/2186-ai-for-casino-list-and-profit-simulation.md` |
| #2187 | Article Summary and Comprehension | Technik & Alltag | `technik-alltag/2187-article-summary-and-comprehension.md` |
| #2188 | Shift Tracking Telegram Mini App | Technik & Alltag | `technik-alltag/2188-shift-tracking-telegram-mini-app.md` |
| #2189 | Münchener Skyline als Umrissbild darstellen | Technik & Alltag | `technik-alltag/2189-m-nchener-skyline-als-umrissbild-darstel.md` |
| #2190 | Exploring Jung's Understanding of Spirit through Rumi's Poem | Technik & Alltag | `technik-alltag/2190-exploring-jung-s-understanding-of-spirit.md` |
| #2191 | Stock Market Analyst: Market Move Suggestions | Beruf & Karriere | `beruf-karriere/2191-stock-market-analyst-market-move-suggest.md` |
| #2192 | Data Analyst | Technik & Alltag | `technik-alltag/2192-data-analyst.md` |
| #2193 | Lead Data Analyst with Data Engineering Expertise | Technik & Alltag | `technik-alltag/2193-lead-data-analyst-with-data-engineering-.md` |
| #2194 | Act as a Patient, Non-Technical Android Studio Guide | Alltag & Leben | `alltag-leben/2194-patient-non-technical-android-studio-gui.md` |
| #2195 | Chimera AI-Powered Prompt Optimization System | Technik & Alltag | `technik-alltag/2195-chimera-ai-powered-prompt-optimization-s.md` |
| #2196 | AI Tour Guide Business Plan for Foreign Tourists in China | Beruf & Karriere | `beruf-karriere/2196-ai-tour-guide-business-plan-for-foreign-.md` |
| #2197 | Plant Hero Section Image | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2197-plant-hero-section-image.md` |
| #2198 | Cozy Christmas Smile | Technik & Alltag | `technik-alltag/2198-cozy-christmas-smile.md` |
| #2199 | Code Translator: Any Language to Any Language | Lernen & Wachstum | `lernen-wachstum/2199-code-translator-any-language-to-any-lang.md` |
| #2200 | Orchestration Agent (PowerPlatformSupervisor) | Technik & Alltag | `technik-alltag/2200-orchestration-agent-powerplatformsupervi.md` |
| #2201 | Analyze Previous Year Question Papers | Lernen & Wachstum | `lernen-wachstum/2201-analyze-previous-year-question-papers.md` |
| #2202 | Linux monitoring single html | Technik & Alltag | `technik-alltag/2202-linux-monitoring-single-html.md` |
| #2203 | Linux Monitoring Dashboard with React | Technik & Alltag | `technik-alltag/2203-linux-monitoring-dashboard-with-react.md` |
| #2204 | Stock Market Analysis Expert | Beruf & Karriere | `beruf-karriere/2204-stock-market-analysis-expert.md` |
| #2205 | Paladin Octem Plus (Research Swarm) | Technik & Alltag | `technik-alltag/2205-paladin-octem-plus-research-swarm.md` |
| #2206 | Website Security Vulnerability Checker | Technik & Alltag | `technik-alltag/2206-website-security-vulnerability-checker.md` |
| #2207 | Sidebar Dashboard Design | Technik & Alltag | `technik-alltag/2207-sidebar-dashboard-design.md` |
| #2208 | Build an Advanced Music App for Android | Kreativitaet & Freizeit | `kreativitaet-freizeit/2208-build-advanced-music-app-for-android.md` |
| #2209 | Web Application Testing Skill | Technik & Alltag | `technik-alltag/2209-web-application-testing-skill.md` |
| #2210 | Yamuna River Cleanup Plan for Vrindavan | Beruf & Karriere | `beruf-karriere/2210-yamuna-river-cleanup-plan-for-vrindavan.md` |
| #2211 | iOS Recipe Generator: Create Recipes from Available Ingredients | Alltag & Leben | `alltag-leben/2211-ios-recipe-generator-create-recipes-from.md` |
| #2212 | Glyth_Maker | Alltag & Leben | `alltag-leben/2212-glyth-maker.md` |
| #2213 | Emotion Analyst | Technik & Alltag | `technik-alltag/2213-emotion-analyst.md` |
| #2214 | Persuasive Article or Proposal Writing Guide | Alltag & Leben | `alltag-leben/2214-persuasive-article-or-proposal-writing-g.md` |
| #2215 | illustration for teenagers, side silhouette of a young person. Inside the head a question mark transforming into light t. Deep purple and blue tones, minimalist and , v. | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2215-illustration-for-teenagers-side-silhouet.md` |
| #2216 | Academic Graduation Presentation Guide | Alltag & Leben | `alltag-leben/2216-academic-graduation-presentation-guide.md` |
| #2217 | Career Path Deliberation Assistant | Beruf & Karriere | `beruf-karriere/2217-career-path-deliberation-assistant.md` |
| #2218 | Girl Taking Selfie with Avatar Characters in Cinema | Kreativitaet & Freizeit | `kreativitaet-freizeit/2218-girl-taking-selfie-with-avatar-character.md` |
| #2219 | UI Designer Role | Technik & Alltag | `technik-alltag/2219-ui-designer-role.md` |
| #2220 | Through the Glass: One Eye in Focus | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2220-through-glass-one-eye-in-focus.md` |
| #2221 | Surreal CGI-Photography Hybrid Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2221-surreal-cgi-photography-hybrid-portrait.md` |
| #2222 | Hyperrealistic Food Photo Creator | Alltag & Leben | `alltag-leben/2222-hyperrealistic-food-photo-creator.md` |
| #2223 | Meta-Prompt Engineer | Technik & Alltag | `technik-alltag/2223-meta-prompt-engineer.md` |
| #2224 | Course Feedback Analysis | Technik & Alltag | `technik-alltag/2224-course-feedback-analysis.md` |
| #2225 | Squid Game - Red Light, Green Light Challenge | Kreativitaet & Freizeit | `kreativitaet-freizeit/2225-squid-game-red-light-green-light-challen.md` |
| #2226 | World of Darkness B&W style | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2226-world-of-darkness-b-w-style.md` |
| #2227 | Crypto Market Outlook Analyst | Beruf & Karriere | `beruf-karriere/2227-crypto-market-outlook-analyst.md` |
| #2228 | World of Darkness Colored Comic style | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2228-world-of-darkness-colored-comic-style.md` |
| #2229 | Landing Page Vibe Coding | Technik & Alltag | `technik-alltag/2229-landing-page-vibe-coding.md` |
| #2230 | Theme based Art Style Fusion Meta-Prompt | Technik & Alltag | `technik-alltag/2230-theme-based-art-style-fusion-meta-prompt.md` |
| #2231 | Enhance and Beautify Your Photo | Technik & Alltag | `technik-alltag/2231-enhance-and-beautify-your-photo.md` |
| #2232 | Shower Glass Silhouette | Technik & Alltag | `technik-alltag/2232-shower-glass-silhouette.md` |
| #2233 | GoPro Action | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2233-gopro-action.md` |
| #2234 | Pathology Slide Analysis Assistant | Technik & Alltag | `technik-alltag/2234-pathology-slide-analysis-assistant.md` |
| #2235 | Bank Transaction Analysis | Beruf & Karriere | `beruf-karriere/2235-bank-transaction-analysis.md` |
| #2236 | Dizi ve Film Özeti Çeviri Asistanı | Lernen & Wachstum | `lernen-wachstum/2236-dizi-ve-film-zeti-eviri-asistan.md` |
| #2237 | CI/CD Strategy for SpringBoot REST APIs Deployment | Technik & Alltag | `technik-alltag/2237-ci-cd-strategy-for-springboot-rest-apis-.md` |
| #2238 | Escritor de Livros Completo | Technik & Alltag | `technik-alltag/2238-escritor-de-livros-completo.md` |
| #2239 | Quantitative Factor Research Engineer | Technik & Alltag | `technik-alltag/2239-quantitative-factor-research-engineer.md` |
| #2240 | Banking System App Development with CRUD Operations | Technik & Alltag | `technik-alltag/2240-banking-system-app-development-with-crud.md` |
| #2241 | MPPT Simulation仿真代码 | Technik & Alltag | `technik-alltag/2241-mppt-simulation.md` |
| #2242 | Cryptocurrency Contract Trading System | Technik & Alltag | `technik-alltag/2242-cryptocurrency-contract-trading-system.md` |
| #2243 | Real-Time Screen Translation Assistant | Lernen & Wachstum | `lernen-wachstum/2243-real-time-screen-translation-assistant.md` |
| #2244 | Hyper-Realistic 3D Isometric Ottoman Masterpiece | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2244-hyper-realistic-3d-isometric-ottoman-mas.md` |
| #2245 | Create a detailed travel itinerary in HTML format | Alltag & Leben | `alltag-leben/2245-create-detailed-travel-itinerary-in-html.md` |
| #2246 | Miniature Claymation Adventures on the Mushroom Cap | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2246-miniature-claymation-adventures-on-mushr.md` |
| #2247 | Melancholic Dawn on the Misty Pier | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2247-melancholic-dawn-on-misty-pier.md` |
| #2248 | prompt 生成 | Technik & Alltag | `technik-alltag/2248-prompt.md` |
| #2249 | Professional Email Writer for Any Occasion | Technik & Alltag | `technik-alltag/2249-professional-email-writer-for-any-occasi.md` |
| #2250 | emails Professionals | Technik & Alltag | `technik-alltag/2250-emails-professionals.md` |
| #2251 | Digital Visiting Card Product Architect | Technik & Alltag | `technik-alltag/2251-digital-visiting-card-product-architect.md` |
| #2252 | Developer Daily Report Generator | Technik & Alltag | `technik-alltag/2252-developer-daily-report-generator.md` |
| #2253 | 担任Go语言开发者 | Technik & Alltag | `technik-alltag/2253-go.md` |
| #2254 | Act as an Etsy Niche Product Researcher | Technik & Alltag | `technik-alltag/2254-etsy-niche-product-researcher.md` |
| #2255 | Müzisyenler için Kariyer Yönetimi Desteği | Beruf & Karriere | `beruf-karriere/2255-m-zisyenler-i-in-kariyer-y-netimi-deste-.md` |
| #2256 | Pharmacy Research Assistant | Alltag & Leben | `alltag-leben/2256-pharmacy-research-assistant.md` |
| #2257 | Stranded in Time: The Victorian Traveler’s Panic | Alltag & Leben | `alltag-leben/2257-stranded-in-time-victorian-traveler-s-pa.md` |
| #2258 | Sistem ve Ağ Güvenliği Temalı Kısa Film Promptu | Technik & Alltag | `technik-alltag/2258-sistem-ve-a-g-venli-i-temal-k-sa-film-pr.md` |
| #2259 | Table with Various Items | Technik & Alltag | `technik-alltag/2259-table-with-various-items.md` |
| #2260 | Customizable Avatar Style Generator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2260-customizable-avatar-style-generator.md` |
| #2261 | Frontend Developer Skill | Technik & Alltag | `technik-alltag/2261-frontend-developer-skill.md` |
| #2262 | Detailed mirror-selfie room scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2262-detailed-mirror-selfie-room-scene.md` |
| #2263 | Black and white studio side-profile portrait prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2263-black-and-white-studio-side-profile-port.md` |
| #2264 | The Digital Frontier: Pixelated Pioneers | Technik & Alltag | `technik-alltag/2264-the-digital-frontier-pixelated-pioneers.md` |
| #2265 | Childs Coloring Style | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2265-childs-coloring-style.md` |
| #2266 | Osobní AI Agent pro Petra Sovadinu | Alltag & Leben | `alltag-leben/2266-osobn-ai-agent-pro-petra-sovadinu.md` |
| #2267 | GitHub Code Structure Tutor | Lernen & Wachstum | `lernen-wachstum/2267-github-code-structure-tutor.md` |
| #2268 | 提取查询 json 中的查询条件 | Technik & Alltag | `technik-alltag/2268-json.md` |
| #2269 | Algorithm Quick Guide | Alltag & Leben | `alltag-leben/2269-algorithm-quick-guide.md` |
| #2270 | Encyclopedia Assistant | Lernen & Wachstum | `lernen-wachstum/2270-encyclopedia-assistant.md` |
| #2271 | Act as a Health Recovery and Weight Loss Specialist | Alltag & Leben | `alltag-leben/2271-health-recovery-and-weight-loss-speciali.md` |
| #2272 | Comprehensive User Manual Creation for Multiple Modules | Alltag & Leben | `alltag-leben/2272-comprehensive-user-manual-creation-for-m.md` |
| #2273 | Building an Inventory Management System | Technik & Alltag | `technik-alltag/2273-building-inventory-management-system.md` |
| #2274 | Setting Up a New iOS App in Xcode | Technik & Alltag | `technik-alltag/2274-setting-up-new-ios-app-in-xcode.md` |
| #2275 | AI Video Creation Assistant | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2275-ai-video-creation-assistant.md` |
| #2276 | Cinematic Vertical Portrait of Vintage Car Radio at Night | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2276-cinematic-vertical-portrait-of-vintage-c.md` |
| #2277 | Personalized Skin Whitening Plan | Alltag & Leben | `alltag-leben/2277-personalized-skin-whitening-plan.md` |
| #2278 | Next.js React Comprehensive Clash of Clans Tool | Technik & Alltag | `technik-alltag/2278-next-js-react-comprehensive-clash-of-cla.md` |
| #2279 | Müşteri temsilcisi eğitimi | Technik & Alltag | `technik-alltag/2279-m-teri-temsilcisi-e-itimi.md` |
| #2280 | Developer Work Analysis from Git Diff and Commit Message | Technik & Alltag | `technik-alltag/2280-developer-work-analysis-from-git-diff-an.md` |
| #2281 | The Covert Exchange in the Fog | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2281-the-covert-exchange-in-fog.md` |
| #2282 | Master Chinese Web Novel Author | Kreativitaet & Freizeit | `kreativitaet-freizeit/2282-master-chinese-web-novel-author.md` |
| #2283 | Socratic Method for Ethical Discussions | Technik & Alltag | `technik-alltag/2283-socratic-method-for-ethical-discussions.md` |
| #2284 | A Moment Shared with the Wild | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2284-a-moment-shared-with-wild.md` |
| #2285 | Isometric miniature 3D cartoon city scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2285-isometric-miniature-3d-cartoon-city-scen.md` |
| #2286 | Trade Contract Review Expert | Beruf & Karriere | `beruf-karriere/2286-trade-contract-review-expert.md` |
| #2287 | Algorithm Analysis and Improvement Advisor | Technik & Alltag | `technik-alltag/2287-algorithm-analysis-and-improvement-advis.md` |
| #2288 | ERP to Feishu Data Integration Solution | Technik & Alltag | `technik-alltag/2288-erp-to-feishu-data-integration-solution.md` |
| #2289 | University Admission Interview Simulation | Beruf & Karriere | `beruf-karriere/2289-university-admission-interview-simulatio.md` |
| #2290 | RIP McKinsey: Here are 10 prompts to replace expensive business consultants | Beruf & Karriere | `beruf-karriere/2290-rip-mckinsey-here-are-10-prompts-to-repl.md` |
| #2291 | VR Headset Experience Simulator | Technik & Alltag | `technik-alltag/2291-vr-headset-experience-simulator.md` |
| #2292 | VR Horror Death Chatroom Simulator | Technik & Alltag | `technik-alltag/2292-vr-horror-death-chatroom-simulator.md` |
| #2293 | How to Obtain a Radio and TV License in Nigeria | Beruf & Karriere | `beruf-karriere/2293-how-to-obtain-radio-and-tv-license-in-ni.md` |
| #2294 | Doom Horror Death Image Simulator | Technik & Alltag | `technik-alltag/2294-doom-horror-death-image-simulator.md` |
| #2295 | Aprendizaje Diario de Japonés | Lernen & Wachstum | `lernen-wachstum/2295-aprendizaje-diario-de-japon-s.md` |
| #2296 | Update checker | Technik & Alltag | `technik-alltag/2296-update-checker.md` |
| #2297 | Android Update Checker Script for Pydroid 3 | Technik & Alltag | `technik-alltag/2297-android-update-checker-script-for-pydroi.md` |
| #2298 | Pull Request Review Assistant | Technik & Alltag | `technik-alltag/2298-pull-request-review-assistant.md` |
| #2299 | Quizflix App Development | Technik & Alltag | `technik-alltag/2299-quizflix-app-development.md` |
| #2300 | QuizFlix Mobile App Design for University Students | Lernen & Wachstum | `lernen-wachstum/2300-quizflix-mobile-app-design-for-universit.md` |
| #2301 | A three-panel monochromatic image | Technik & Alltag | `technik-alltag/2301-a-three-panel-monochromatic-image.md` |
| #2302 | Interactive Quiz Application for TV Shows and Movies | Technik & Alltag | `technik-alltag/2302-interactive-quiz-application-for-tv-show.md` |
| #2303 | Istanbul Travel Journal | Kommunikation & Beziehungen | `kommunikation-beziehungen/2303-istanbul-travel-journal.md` |
| #2304 | Young woman with mixed ethnicity features | Technik & Alltag | `technik-alltag/2304-young-woman-with-mixed-ethnicity-feature.md` |
| #2305 | Hyper-Realistic Marvel Comic Fusion Image Generation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2305-hyper-realistic-marvel-comic-fusion-imag.md` |
| #2306 | Shadows of the Cold War: The 1962 Exchange | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2306-shadows-of-cold-war-1962-exchange.md` |
| #2307 | Project Evaluation for Production Decision | Technik & Alltag | `technik-alltag/2307-project-evaluation-for-production-decisi.md` |
| #2308 | 30 tweet Project | Technik & Alltag | `technik-alltag/2308-30-tweet-project.md` |
| #2309 | Build a Self-Hosted App Dashboard with Next.js | Technik & Alltag | `technik-alltag/2309-build-self-hosted-app-dashboard-with-nex.md` |
| #2310 | Scientific Drawing Assistant | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2310-scientific-drawing-assistant.md` |
| #2311 | Senior Crypto Yapper & Community Strategist | Technik & Alltag | `technik-alltag/2311-senior-crypto-yapper-community-strategis.md` |
| #2312 | for Rally | Technik & Alltag | `technik-alltag/2312-for-rally.md` |
| #2313 | HCCVN-AI-VN Pro Max: Optimal AI System Design | Technik & Alltag | `technik-alltag/2313-hccvn-ai-vn-pro-max-optimal-ai-system-de.md` |
| #2314 | Evaluate and Suggest Improvements for Computer Science PhD Thesis | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/2314-evaluate-and-suggest-improvements-for-co.md` |
| #2315 | Graduate-Level Review Paper on Humanoid Robots | Alltag & Leben | `alltag-leben/2315-graduate-level-review-paper-on-humanoid-.md` |
| #2316 | PPT Generation Assistant | Technik & Alltag | `technik-alltag/2316-ppt-generation-assistant.md` |
| #2317 | Chinese to English Translation Assistant | Lernen & Wachstum | `lernen-wachstum/2317-chinese-to-english-translation-assistant.md` |
| #2318 | Continue and Recap Assistant | Technik & Alltag | `technik-alltag/2318-continue-and-recap-assistant.md` |
| #2319 | Optimize E-commerce Listing for High CTR with Holiday Design | Technik & Alltag | `technik-alltag/2319-optimize-e-commerce-listing-for-high-ctr.md` |
| #2320 | Coding Structure with MVC and SOLID Principles | Technik & Alltag | `technik-alltag/2320-coding-structure-with-mvc-and-solid-prin.md` |
| #2321 | Email Marketing | Alltag & Leben | `alltag-leben/2321-email-marketing.md` |
| #2322 | Excel Formula Sensei | Technik & Alltag | `technik-alltag/2322-excel-formula-sensei.md` |
| #2323 | Universal Lead & Candidate Outreach Generator (HR, SALES) | Technik & Alltag | `technik-alltag/2323-universal-lead-candidate-outreach-genera.md` |
| #2324 | Subject meditating in a crystal sphere | Technik & Alltag | `technik-alltag/2324-subject-meditating-in-crystal-sphere.md` |
| #2325 | FAQ Generator | Technik & Alltag | `technik-alltag/2325-faq-generator.md` |
| #2326 | Text-to-Image with Reference - Billiards Bar Scene | Technik & Alltag | `technik-alltag/2326-text-to-image-with-reference-billiards-b.md` |
| #2327 | görsel | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2327-g-rsel.md` |
| #2328 | Chinese Hookah Training Program | Technik & Alltag | `technik-alltag/2328-chinese-hookah-training-program.md` |
| #2329 | Nietzschean Mentor for Holistic Growth | Lernen & Wachstum | `lernen-wachstum/2329-nietzschean-mentor-for-holistic-growth.md` |
| #2330 | berre | Technik & Alltag | `technik-alltag/2330-berre.md` |
| #2331 | .NET API Project Analysis | Technik & Alltag | `technik-alltag/2331-net-api-project-analysis.md` |
| #2332 | Set Up W&B and Run Pod During Training | Technik & Alltag | `technik-alltag/2332-set-up-w-b-and-run-pod-during-training.md` |
| #2333 | Secteur Bancaire - Email Professionnel | Technik & Alltag | `technik-alltag/2333-secteur-bancaire-email-professionnel.md` |
| #2334 | Modern Fashion Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2334-modern-fashion-photography.md` |
| #2335 | Sunny Beach | Technik & Alltag | `technik-alltag/2335-sunny-beach.md` |
| #2336 | Mirror Product Photo | Technik & Alltag | `technik-alltag/2336-mirror-product-photo.md` |
| #2337 | Hata Tespiti için Kod İnceleme Asistanı | Technik & Alltag | `technik-alltag/2337-hata-tespiti-i-in-kod-i-nceleme-asistan.md` |
| #2338 | Using StanfordVL/BEHAVIOR-1K for Robotics and AI Tasks | Alltag & Leben | `alltag-leben/2338-using-stanfordvl-behavior-1k-for-robotic.md` |
| #2339 | Giant Object in City | Technik & Alltag | `technik-alltag/2339-giant-object-in-city.md` |
| #2340 | Deep Copy Functionality | Technik & Alltag | `technik-alltag/2340-deep-copy-functionality.md` |
| #2341 | Annual Leave Balance Adjustment Processor | Technik & Alltag | `technik-alltag/2341-annual-leave-balance-adjustment-processo.md` |
| #2342 | Master App Store Localization & ASO Prompt (2025) – Full Metadata Generator | Technik & Alltag | `technik-alltag/2342-master-app-store-localization-aso-prompt.md` |
| #2343 | Form Validation Rules for Leave Requests | Technik & Alltag | `technik-alltag/2343-form-validation-rules-for-leave-requests.md` |
| #2344 | PowerShell Script for Managing Disabled AD Users | Technik & Alltag | `technik-alltag/2344-powershell-script-for-managing-disabled-.md` |
| #2345 | PowerShell Script to Move Disabled AD Users to Specific OU | Technik & Alltag | `technik-alltag/2345-powershell-script-to-move-disabled-ad-us.md` |
| #2346 | Visual Web Application Development | Technik & Alltag | `technik-alltag/2346-visual-web-application-development.md` |
| #2347 | Playing Card Sorcerer Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2347-playing-card-sorcerer-portrait.md` |
| #2348 | Personalized Technical Intelligence Briefing for Edge AI in Defense | Alltag & Leben | `alltag-leben/2348-personalized-technical-intelligence-brie.md` |
| #2349 | One-Click Design Mockup Creator | Technik & Alltag | `technik-alltag/2349-one-click-design-mockup-creator.md` |
| #2350 | Vintage Invention Patent | Technik & Alltag | `technik-alltag/2350-vintage-invention-patent.md` |
| #2351 | A Wrinkle in Time | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2351-a-wrinkle-in-time.md` |
| #2352 | Create Python Dev Container | Technik & Alltag | `technik-alltag/2352-create-python-dev-container.md` |
| #2353 | Protocol 2084: The Alleyway Hack | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2353-protocol-2084-alleyway-hack.md` |
| #2354 | Expo + Supabase Edge Function Cold Start & Mobile Performance Analysis | Technik & Alltag | `technik-alltag/2354-expo-supabase-edge-function-cold-start-m.md` |
| #2355 | Cold Start Safe Architecture | Technik & Alltag | `technik-alltag/2355-cold-start-safe-architecture.md` |
| #2356 | Immigration Project Presentation Specialist | Technik & Alltag | `technik-alltag/2356-immigration-project-presentation-special.md` |
| #2357 | Blog System Development Guide | Alltag & Leben | `alltag-leben/2357-blog-system-development-guide.md` |
| #2358 | Customized Gift Idea Brainstorm Assistant | Technik & Alltag | `technik-alltag/2358-customized-gift-idea-brainstorm-assistan.md` |
| #2359 | Flight Tracker Desktop Application | Technik & Alltag | `technik-alltag/2359-flight-tracker-desktop-application.md` |
| #2360 | File Renaming Dashboard App | Technik & Alltag | `technik-alltag/2360-file-renaming-dashboard-app.md` |
| #2361 | Letter from Lisa: A Heartfelt Plea to Her Father | Technik & Alltag | `technik-alltag/2361-letter-from-lisa-heartfelt-plea-to-her-f.md` |
| #2362 | Ultra-Realistic Handwritten Hospital Note Image | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2362-ultra-realistic-handwritten-hospital-not.md` |
| #2363 | Develop a Notion Clone Application | Technik & Alltag | `technik-alltag/2363-develop-notion-clone-application.md` |
| #2364 | The Aether Prince at the Crystal Gala | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2364-the-aether-prince-at-crystal-gala.md` |
| #2365 | Langgraph微信公众号介绍 | Kommunikation & Beziehungen | `kommunikation-beziehungen/2365-langgraph.md` |
| #2366 | AST Code Analysis Superpower | Technik & Alltag | `technik-alltag/2366-ast-code-analysis-superpower.md` |
| #2367 | AWS Cloud Expert | Technik & Alltag | `technik-alltag/2367-aws-cloud-expert.md` |
| #2368 | Accessibility Expert | Technik & Alltag | `technik-alltag/2368-accessibility-expert.md` |
| #2369 | Accessibility Testing Superpower | Technik & Alltag | `technik-alltag/2369-accessibility-testing-superpower.md` |
| #2370 | Agent Organization Expert | Alltag & Leben | `alltag-leben/2370-agent-organization-expert.md` |
| #2371 | Hyper-Realistic X-Wing Battle Damage Images | Technik & Alltag | `technik-alltag/2371-hyper-realistic-x-wing-battle-damage-ima.md` |
| #2372 | FDTD Simulations of Nanoparticles | Technik & Alltag | `technik-alltag/2372-fdtd-simulations-of-nanoparticles.md` |
| #2373 | Secteur Bancaire - Analyse rapide d’un tableau de données | Technik & Alltag | `technik-alltag/2373-secteur-bancaire-analyse-rapide-d-un-tab.md` |
| #2374 | Secteur Bancaire - Vérification de conformité de texte | Technik & Alltag | `technik-alltag/2374-secteur-bancaire-v-rification-de-conform.md` |
| #2375 | Professional Website Design Consultant | Beruf & Karriere | `beruf-karriere/2375-professional-website-design-consultant.md` |
| #2376 | Default Meeting Summary | Technik & Alltag | `technik-alltag/2376-default-meeting-summary.md` |
| #2377 | Custom Localization and AI Integration for Apps | Technik & Alltag | `technik-alltag/2377-custom-localization-and-ai-integration-f.md` |
| #2378 | Personalized GPT Assistant Prompt | Alltag & Leben | `alltag-leben/2378-personalized-gpt-assistant-prompt.md` |
| #2379 | Modern Video Player with Sharp UI | Technik & Alltag | `technik-alltag/2379-modern-video-player-with-sharp-ui.md` |
| #2380 | Secteur Bancaire - Création d’un texte marketing simple | Technik & Alltag | `technik-alltag/2380-secteur-bancaire-cr-ation-d-un-texte-mar.md` |
| #2381 | Psychology Clinic Assistant | Technik & Alltag | `technik-alltag/2381-psychology-clinic-assistant.md` |
| #2382 | Isometric 3D Cartoon Scene with Weather Effects | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2382-isometric-3d-cartoon-scene-with-weather-.md` |
| #2383 | Node.js Automation Script Developer | Technik & Alltag | `technik-alltag/2383-node-js-automation-script-developer.md` |
| #2384 | Smart Application Developer Assistant | Technik & Alltag | `technik-alltag/2384-smart-application-developer-assistant.md` |
| #2385 | Website Creation Command | Alltag & Leben | `alltag-leben/2385-website-creation-command.md` |
| #2386 | Darksynth Synthwave Music Composition Guide | Kreativitaet & Freizeit | `kreativitaet-freizeit/2386-darksynth-synthwave-music-composition-gu.md` |
| #2387 | roster | Technik & Alltag | `technik-alltag/2387-roster.md` |
| #2388 | Cinematic Realism | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2388-cinematic-realism.md` |
| #2389 | 3D Character Render In High-End Disney Pixar Style | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2389-3d-character-render-in-high-end-disney-p.md` |
| #2390 | Serene Evening Rowboat Scene in Illustrative Realism | Technik & Alltag | `technik-alltag/2390-serene-evening-rowboat-scene-in-illustra.md` |
| #2391 | Minimalist Landscape Illustration by Ryo Takemasa | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2391-minimalist-landscape-illustration-by-ryo.md` |
| #2392 | Comprehensive Image Analysis Report | Technik & Alltag | `technik-alltag/2392-comprehensive-image-analysis-report.md` |
| #2393 | A Half-Built Pyramid and the Leader Who Turned Labor Into Legacy | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2393-a-half-built-pyramid-and-leader-who-turn.md` |
| #2394 | App Store Submission Agent | Alltag & Leben | `alltag-leben/2394-app-store-submission-agent.md` |
| #2395 | Comprehensive Web Application Development with Security and Performance Optimization | Alltag & Leben | `alltag-leben/2395-comprehensive-web-application-developmen.md` |
| #2396 | The Missing Woman | Technik & Alltag | `technik-alltag/2396-the-missing-woman.md` |
| #2397 | Photo-to-Isometric: Reality Slice Generator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2397-photo-to-isometric-reality-slice-generat.md` |
| #2398 | Shadows of the Blue Note | Technik & Alltag | `technik-alltag/2398-shadows-of-blue-note.md` |
| #2399 | Strategic App Design & Content Engineering Prompt | Technik & Alltag | `technik-alltag/2399-strategic-app-design-content-engineering.md` |
| #2400 | English Teacher for Translation and Cultural Explanation | Lernen & Wachstum | `lernen-wachstum/2400-english-teacher-for-translation-and-cult.md` |
| #2401 | AI Assistant for University Assignments | Technik & Alltag | `technik-alltag/2401-ai-assistant-for-university-assignments.md` |
| #2402 | Base64 Promt | Technik & Alltag | `technik-alltag/2402-base64-promt.md` |
| #2403 | 3D Isometric Miniature City View with Weather | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2403-3d-isometric-miniature-city-view-with-we.md` |
| #2404 | Edit a New Year's Video for Antioch Textile with Nano Banana | Technik & Alltag | `technik-alltag/2404-edit-new-year-s-video-for-antioch-textil.md` |
| #2405 | New Year Celebration Video for Antioch Textile | Technik & Alltag | `technik-alltag/2405-new-year-celebration-video-for-antioch-t.md` |
| #2406 | Automate Repository Management with OpenCode CLI | Technik & Alltag | `technik-alltag/2406-automate-repository-management-with-open.md` |
| #2407 | Photorealistic Selfie Portrait Description | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2407-photorealistic-selfie-portrait-descripti.md` |
| #2408 | Bathroom Flash Selfie (IG-candid, non-explicit) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2408-bathroom-flash-selfie-ig-candid-non-expl.md` |
| #2409 | Elevator Mirror OOTD (full-body) | Technik & Alltag | `technik-alltag/2409-elevator-mirror-ootd-full-body.md` |
| #2410 | Snowy Street Cozy (winter fit, cinematic) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2410-snowy-street-cozy-winter-fit-cinematic.md` |
| #2411 | Nano Banana Pro Prompt Generator Instruction (Outputs JSON blocks like these) | Technik & Alltag | `technik-alltag/2411-nano-banana-pro-prompt-generator-instruc.md` |
| #2412 | Gym Mirror (UGC realism, no logos) | Technik & Alltag | `technik-alltag/2412-gym-mirror-ugc-realism-no-logos.md` |
| #2413 | merge | Technik & Alltag | `technik-alltag/2413-merge.md` |
| #2414 | Prompt Writer for Specific Project | Technik & Alltag | `technik-alltag/2414-prompt-writer-for-specific-project.md` |
| #2415 | Open Source / Free License Selection Assistant | Technik & Alltag | `technik-alltag/2415-open-source-free-license-selection-assis.md` |
| #2416 | License Selection Assistant from Intellectual Property expert | Technik & Alltag | `technik-alltag/2416-license-selection-assistant-from-intelle.md` |
| #2417 | Act as a Resume Reviewer | Beruf & Karriere | `beruf-karriere/2417-resume-reviewer.md` |
| #2418 | Act as a Resume Reviewer for Anthropic Fellows Program | Beruf & Karriere | `beruf-karriere/2418-resume-reviewer-for-anthropic-fellows-pr.md` |
| #2419 | Structured Job Application Cleanup | Technik & Alltag | `technik-alltag/2419-structured-job-application-cleanup.md` |
| #2420 | Cafe Window Seat (close-up, tactile realism) | Technik & Alltag | `technik-alltag/2420-cafe-window-seat-close-up-tactile-realis.md` |
| #2421 | Rooftop Sunset Lookback (half-body) | Technik & Alltag | `technik-alltag/2421-rooftop-sunset-lookback-half-body.md` |
| #2422 | Rainy Umbrella Street (full-body) | Technik & Alltag | `technik-alltag/2422-rainy-umbrella-street-full-body.md` |
| #2423 | Night Neon Alley (half-body, edgy) | Technik & Alltag | `technik-alltag/2423-night-neon-alley-half-body-edgy.md` |
| #2424 | Cozy Couch Lamp (close-up, warm tungsten) | Technik & Alltag | `technik-alltag/2424-cozy-couch-lamp-close-up-warm-tungsten.md` |
| #2425 | Plant Bouquet Warm Lamp (your example vibe, adult-safe) | Technik & Alltag | `technik-alltag/2425-plant-bouquet-warm-lamp-your-example-vib.md` |
| #2426 | Airport Corridor Walk (full-body) | Alltag & Leben | `alltag-leben/2426-airport-corridor-walk-full-body.md` |
| #2427 | Museum Steps (full-body, cultural) | Technik & Alltag | `technik-alltag/2427-museum-steps-full-body-cultural.md` |
| #2428 | Nightclub Booth Flash (half-body, party candids) | Technik & Alltag | `technik-alltag/2428-nightclub-booth-flash-half-body-party-ca.md` |
| #2429 | Studio Beauty Editorial (close-up, pro) | Technik & Alltag | `technik-alltag/2429-studio-beauty-editorial-close-up-pro.md` |
| #2430 | Beach Walk Golden Hour (full-body, travel) | Alltag & Leben | `alltag-leben/2430-beach-walk-golden-hour-full-body-travel.md` |
| #2431 | Tech Desk “Builder” (half-body, cozy monitor glow) | Technik & Alltag | `technik-alltag/2431-tech-desk-builder-half-body-cozy-monitor.md` |
| #2432 | Restaurant Candle Close-up (intimate, not explicit) | Technik & Alltag | `technik-alltag/2432-restaurant-candle-close-up-intimate-not-.md` |
| #2433 | Minimal Studio “iPhone Candid” (pro-quality but awkward framing) | Technik & Alltag | `technik-alltag/2433-minimal-studio-iphone-candid-pro-quality.md` |
| #2434 | “Blue Hour Bridge” (full-body, cinematic but still IG) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2434-blue-hour-bridge-full-body-cinematic-but.md` |
| #2435 | Kitchen Morning Window Light (candid, cozy) | Technik & Alltag | `technik-alltag/2435-kitchen-morning-window-light-candid-cozy.md` |
| #2436 | Bookstore Aisle (artsy, quiet luxury) | Technik & Alltag | `technik-alltag/2436-bookstore-aisle-artsy-quiet-luxury.md` |
| #2437 | Passenger Seat Car Selfie (golden hour, candid) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2437-passenger-seat-car-selfie-golden-hour-ca.md` |
| #2438 | Balcony Coffee (morning haze, plant vibe) | Technik & Alltag | `technik-alltag/2438-balcony-coffee-morning-haze-plant-vibe.md` |
| #2439 | Subway Platform (street candid, moody) | Technik & Alltag | `technik-alltag/2439-subway-platform-street-candid-moody.md` |
| #2440 | Farmers Market (colorful produce, candid) | Technik & Alltag | `technik-alltag/2440-farmers-market-colorful-produce-candid.md` |
| #2441 | Hotel Hallway Fit Check (mirror vibe, no phone shown) | Technik & Alltag | `technik-alltag/2441-hotel-hallway-fit-check-mirror-vibe-no-p.md` |
| #2442 | Pilates Studio (soft daylight, athletic elegance) | Technik & Alltag | `technik-alltag/2442-pilates-studio-soft-daylight-athletic-el.md` |
| #2443 | Grocery Aisle (relatable, comedic-candid) | Technik & Alltag | `technik-alltag/2443-grocery-aisle-relatable-comedic-candid.md` |
| #2444 | Codebase WIKI Documentation Skill | Technik & Alltag | `technik-alltag/2444-codebase-wiki-documentation-skill.md` |
| #2445 | Graduate Information and Communication System Design | Beruf & Karriere | `beruf-karriere/2445-graduate-information-and-communication-s.md` |
| #2446 | Directive Assistant: Domina | Technik & Alltag | `technik-alltag/2446-directive-assistant-domina.md` |
| #2447 | Non-Technical IT Help & Clarity Assistant | Technik & Alltag | `technik-alltag/2447-non-technical-it-help-clarity-assistant.md` |
| #2448 | Cinematic Triptych: A Day in the Countryside | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2448-cinematic-triptych-day-in-countryside.md` |
| #2449 | Cinematic Photography Triptych: Serene Meadow Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2449-cinematic-photography-triptych-serene-me.md` |
| #2450 | Cinematic Neo-Noir Triptych in Digital Art | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2450-cinematic-neo-noir-triptych-in-digital-a.md` |
| #2451 | PlainTalk Style Guide | Alltag & Leben | `alltag-leben/2451-plaintalk-style-guide.md` |
| #2452 | A broken, soul-crushed medieval knight | Alltag & Leben | `alltag-leben/2452-a-broken-soul-crushed-medieval-knight.md` |
| #2453 | Matrix Paradise Seraph | Technik & Alltag | `technik-alltag/2453-matrix-paradise-seraph.md` |
| #2454 | Retro-futuristic 1970s sci-fi | Technik & Alltag | `technik-alltag/2454-retro-futuristic-1970s-sci-fi.md` |
| #2455 | A retro-styled adventurer takes a pause by a lush jungle riverbank. | Technik & Alltag | `technik-alltag/2455-a-retro-styled-adventurer-takes-pause-by.md` |
| #2456 | A relaxed copper-haired woman resting sideways on a bed in a soft, low-light setting. | Technik & Alltag | `technik-alltag/2456-a-relaxed-copper-haired-woman-resting-si.md` |
| #2457 | Art-W | Technik & Alltag | `technik-alltag/2457-art-w.md` |
| #2458 | İngilizce-Türkçe Kelime ve Cümle Çevirmeni | Lernen & Wachstum | `lernen-wachstum/2458-i-ngilizce-t-rk-e-kelime-ve-c-mle-evirme.md` |
| #2459 | Cinematic Urban Night Portrait - Moody Streetwear Aesthetic | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2459-cinematic-urban-night-portrait-moody-str.md` |
| #2460 | Quiet Glow | Technik & Alltag | `technik-alltag/2460-quiet-glow.md` |
| #2461 | Household Maintenance & Safety Assistant | Technik & Alltag | `technik-alltag/2461-household-maintenance-safety-assistant.md` |
| #2462 | Where the Kami Still Walk | Technik & Alltag | `technik-alltag/2462-where-kami-still-walk.md` |
| #2463 | Iterative Prompt Refinement Loop | Technik & Alltag | `technik-alltag/2463-iterative-prompt-refinement-loop.md` |
| #2464 | Creating a Project Management Tool | Technik & Alltag | `technik-alltag/2464-creating-project-management-tool.md` |
| #2465 | 3x3 Grid Storyboarding from Photo | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2465-3x3-grid-storyboarding-from-photo.md` |
| #2466 | "University Website Section Designer" | Technik & Alltag | `technik-alltag/2466-university-website-section-designer.md` |
| #2467 | Surreal City Scene | Technik & Alltag | `technik-alltag/2467-surreal-city-scene.md` |
| #2468 | Language Detection | Lernen & Wachstum | `lernen-wachstum/2468-language-detection.md` |
| #2469 | Aesthetic Mirror Selfie of a Curly-Haired Woman in a Mocha Ribbed Crop Top | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2469-aesthetic-mirror-selfie-of-curly-haired-.md` |
| #2470 | Joyful Woman in Nordic Sweater Dancing at a Nostalgic Family Christmas Gathering | Technik & Alltag | `technik-alltag/2470-joyful-woman-in-nordic-sweater-dancing-a.md` |
| #2471 | Detailed Image Analysis of a Mirror Selfie in a Bedroom Environment | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2471-detailed-image-analysis-of-mirror-selfie.md` |
| #2472 | Outdoor Staircase Image Analysis | Technik & Alltag | `technik-alltag/2472-outdoor-staircase-image-analysis.md` |
| #2473 | Study Review Companion | Technik & Alltag | `technik-alltag/2473-study-review-companion.md` |
| #2474 | Cinematic Street Photography Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2474-cinematic-street-photography-prompt.md` |
| #2475 | Extreme Close-up Macro Photography of a Young Woman's Face | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2475-extreme-close-up-macro-photography-of-yo.md` |
| #2476 | Ethereal Dreamlike Portrait Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2476-ethereal-dreamlike-portrait-photography.md` |
| #2477 | Tropical Elegance: A Serene Afternoon in a Sunlit Villa | Technik & Alltag | `technik-alltag/2477-tropical-elegance-serene-afternoon-in-su.md` |
| #2478 | Investment Tracking Dashboard | Technik & Alltag | `technik-alltag/2478-investment-tracking-dashboard.md` |
| #2479 | Yağlı boya tablona bak | Technik & Alltag | `technik-alltag/2479-ya-l-boya-tablona-bak.md` |
| #2480 | Avant-Garde Portrait with Ghost Duplicate in Ochre Studio | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2480-avant-garde-portrait-with-ghost-duplicat.md` |
| #2481 | Reflected Self-Portrait in an Urban Convex Traffic Mirror | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2481-reflected-self-portrait-in-urban-convex-.md` |
| #2482 | Comprehensive Digital Marketing Strategy for Fashion Brand | Technik & Alltag | `technik-alltag/2482-comprehensive-digital-marketing-strategy.md` |
| #2483 | Professional GitHub Dashboard for Portfolio Enhancement | Technik & Alltag | `technik-alltag/2483-professional-github-dashboard-for-portfo.md` |
| #2484 | Guía para Diseñar y Vender un Libro en Hotmart | Alltag & Leben | `alltag-leben/2484-gu-a-para-dise-ar-y-vender-un-libro-en-h.md` |
| #2485 | Candle Pattern Trading Chart Generator | Beruf & Karriere | `beruf-karriere/2485-candle-pattern-trading-chart-generator.md` |
| #2486 | Candlestick Reversal Pattern Detector in Pine Script | Technik & Alltag | `technik-alltag/2486-candlestick-reversal-pattern-detector-in.md` |
| #2487 | Finance Tracker App Development Plan | Technik & Alltag | `technik-alltag/2487-finance-tracker-app-development-plan.md` |
| #2488 | English Language Tutor for Turkish Speakers | Lernen & Wachstum | `lernen-wachstum/2488-english-language-tutor-for-turkish-speak.md` |
| #2489 | Security Guard Image Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2489-security-guard-image-prompt.md` |
| #2490 | Product Promotion Expert | Technik & Alltag | `technik-alltag/2490-product-promotion-expert.md` |
| #2491 | Research Project Analysis and IPD Feasibility Recommendations | Beruf & Karriere | `beruf-karriere/2491-research-project-analysis-and-ipd-feasib.md` |
| #2492 | English Practice App Guide | Alltag & Leben | `alltag-leben/2492-english-practice-app-guide.md` |
| #2493 | Enterprise Microservices Architecture Design | Technik & Alltag | `technik-alltag/2493-enterprise-microservices-architecture-de.md` |
| #2494 | SwiftUI iOS App Development Guide | Alltag & Leben | `alltag-leben/2494-swiftui-ios-app-development-guide.md` |
| #2495 | A young woman relaxing in a wicker chair on a sunlit Mediterranean balcony. | Technik & Alltag | `technik-alltag/2495-a-young-woman-relaxing-in-wicker-chair-o.md` |
| #2496 | Amateur Girls' Night Selfie - Casual and Imperfect | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2496-amateur-girls-night-selfie-casual-and-im.md` |
| #2497 | Evening at a Turkish Dessert Shop - A Photographic Story | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2497-evening-at-turkish-dessert-shop-photogra.md` |
| #2498 | Image Analysis for Night Portrait in Heavy Snowfall | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2498-image-analysis-for-night-portrait-in-hea.md` |
| #2499 | Night Shift Dessert Shop | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2499-night-shift-dessert-shop.md` |
| #2500 | Ultra-Realistic Ankara Indie Bar Scene Description | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2500-ultra-realistic-ankara-indie-bar-scene-d.md` |
| #2501 | Night Balcony Scene in Ankara with Efes | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2501-night-balcony-scene-in-ankara-with-efes.md` |
| #2502 | Ankara Night Scene in a Meyhane | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2502-ankara-night-scene-in-meyhane.md` |
| #2503 | Ultra-Realistic Turkish Living Room Scene During Football Match | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2503-ultra-realistic-turkish-living-room-scen.md` |
| #2504 | Snapshot of a Turkish Hospital Night: A Dramedy Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2504-snapshot-of-turkish-hospital-night-drame.md` |
| #2505 | Photorealistic Mirror Selfie Analysis | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2505-photorealistic-mirror-selfie-analysis.md` |
| #2506 | Ultra-Realistic Night Scene in a Turkish Kitchen | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2506-ultra-realistic-night-scene-in-turkish-k.md` |
| #2507 | Ultra-Realistic Comedic Slice-of-Life in an Ankara Bus | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2507-ultra-realistic-comedic-slice-of-life-in.md` |
| #2508 | Cozy Night in Ankara: A Turkish TV Series Snapshot | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2508-cozy-night-in-ankara-turkish-tv-series-s.md` |
| #2509 | Ultra-Realistic Ankara Apartment Night Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2509-ultra-realistic-ankara-apartment-night-s.md` |
| #2510 | Cozy Ankara Night: Capturing a Realistic Bedroom Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2510-cozy-ankara-night-capturing-realistic-be.md` |
| #2511 | Ultra-Realistic Street Photo Prompt: Turkish Woman in Ankara | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2511-ultra-realistic-street-photo-prompt-turk.md` |
| #2512 | Turkish woman in Ankara with a surreal twist | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2512-turkish-woman-in-ankara-with-surreal-twi.md` |
| #2513 | Ultra-Realistic Amateur Street Photo of Ankara Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2513-ultra-realistic-amateur-street-photo-of-.md` |
| #2514 | Ultra-Realistic Ankara Street Photo with Surreal Element | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2514-ultra-realistic-ankara-street-photo-with.md` |
| #2515 | Realistic Photo of a Turkish Woman in a Street Setting | Technik & Alltag | `technik-alltag/2515-realistic-photo-of-turkish-woman-in-stre.md` |
| #2516 | Ultra Realistic Bedroom Selfie Description | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2516-ultra-realistic-bedroom-selfie-descripti.md` |
| #2517 | Ultra Realistic Candid Photo of a Turkish Woman in Istanbul Café | Technik & Alltag | `technik-alltag/2517-ultra-realistic-candid-photo-of-turkish-.md` |
| #2518 | Realistic Mirror-Selfie Scene Creation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2518-realistic-mirror-selfie-scene-creation.md` |
| #2519 | Dual Lighting Narrative Scene | Alltag & Leben | `alltag-leben/2519-dual-lighting-narrative-scene.md` |
| #2520 | Amateur Mirror Selfie with Natural Look | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2520-amateur-mirror-selfie-with-natural-look.md` |
| #2521 | Realistic Amateur Vibe Candid Photography Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2521-realistic-amateur-vibe-candid-photograph.md` |
| #2522 | Bug Discovery Code Assistant | Technik & Alltag | `technik-alltag/2522-bug-discovery-code-assistant.md` |
| #2523 | Manim Code | Technik & Alltag | `technik-alltag/2523-manim-code.md` |
| #2524 | SEO Strategy for Container Tracking Keywords | Kommunikation & Beziehungen | `kommunikation-beziehungen/2524-seo-strategy-for-container-tracking-keyw.md` |
| #2525 | Excel Data to Figma Presentation Designer | Technik & Alltag | `technik-alltag/2525-excel-data-to-figma-presentation-designe.md` |
| #2526 | Comprehensive Repository Audit & Remediation Prompt | Technik & Alltag | `technik-alltag/2526-comprehensive-repository-audit-remediati.md` |
| #2527 | OpenAI Create Plan Skill | Technik & Alltag | `technik-alltag/2527-openai-create-plan-skill.md` |
| #2528 | Text Summarizer | Technik & Alltag | `technik-alltag/2528-text-summarizer.md` |
| #2529 | Course Assignment Grader | Technik & Alltag | `technik-alltag/2529-course-assignment-grader.md` |
| #2530 | Ethreal Current | Technik & Alltag | `technik-alltag/2530-ethreal-current.md` |
| #2531 | Create an Unofficial Instagram API | Technik & Alltag | `technik-alltag/2531-create-unofficial-instagram-api.md` |
| #2532 | Professional Full-Stack Developer for Network Mapping & Monitoring Application | Technik & Alltag | `technik-alltag/2532-professional-full-stack-developer-for-ne.md` |
| #2533 | Comprehensive POS Application Development with FIFO and Reporting | Technik & Alltag | `technik-alltag/2533-comprehensive-pos-application-developmen.md` |
| #2534 | Node Web App for Czech Invoice PDF Generation | Technik & Alltag | `technik-alltag/2534-node-web-app-for-czech-invoice-pdf-gener.md` |
| #2535 | Study Timer | Technik & Alltag | `technik-alltag/2535-study-timer.md` |
| #2536 | Sophisticated Istanbul Stroll | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2536-sophisticated-istanbul-stroll.md` |
| #2537 | Numerology Expert Guidance | Technik & Alltag | `technik-alltag/2537-numerology-expert-guidance.md` |
| #2538 | Man in a City | Technik & Alltag | `technik-alltag/2538-man-in-city.md` |
| #2539 | Build a UI Library for ESP32 | Technik & Alltag | `technik-alltag/2539-build-ui-library-for-esp32.md` |
| #2540 | ESP32 UI Library Development | Technik & Alltag | `technik-alltag/2540-esp32-ui-library-development.md` |
| #2541 | NBX | Lernen & Wachstum | `lernen-wachstum/2541-nbx.md` |
| #2542 | Sun-Drenched Outdoor Selfie of a Tattooed Female Subject with Tiki Decor | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2542-sun-drenched-outdoor-selfie-of-tattooed-.md` |
| #2543 | Bingo Game Creator | Kreativitaet & Freizeit | `kreativitaet-freizeit/2543-bingo-game-creator.md` |
| #2544 | SAP ABAP Carbon Footprint Module Graduation Project Documentation | Technik & Alltag | `technik-alltag/2544-sap-abap-carbon-footprint-module-graduat.md` |
| #2545 | Code Review Expert | Technik & Alltag | `technik-alltag/2545-code-review-expert.md` |
| #2546 | Networking Engineer Portfolio Website | Technik & Alltag | `technik-alltag/2546-networking-engineer-portfolio-website.md` |
| #2547 | Senior Java Backend Engineer Expert | Technik & Alltag | `technik-alltag/2547-senior-java-backend-engineer-expert.md` |
| #2548 | UGC-Style TikTok Script Generator for Gen Z Skincare | Technik & Alltag | `technik-alltag/2548-ugc-style-tiktok-script-generator-for-ge.md` |
| #2549 | Google Ads Title Copywriter | Technik & Alltag | `technik-alltag/2549-google-ads-title-copywriter.md` |
| #2550 | 2026 Size Neler getirecek | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2550-2026-size-neler-getirecek.md` |
| #2551 | PDF Shareholder Extractor | Technik & Alltag | `technik-alltag/2551-pdf-shareholder-extractor.md` |
| #2552 | 3D to 2D Floor Plan Converter | Technik & Alltag | `technik-alltag/2552-3d-to-2d-floor-plan-converter.md` |
| #2553 | Mechanical Part Render to Technical Drawing Converter | Alltag & Leben | `alltag-leben/2553-mechanical-part-render-to-technical-draw.md` |
| #2554 | 3D Mechanical Part Image to Technical Drawing Conversion | Alltag & Leben | `alltag-leben/2554-3d-mechanical-part-image-to-technical-dr.md` |
| #2555 | Cinematic Thriller Silhouette | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2555-cinematic-thriller-silhouette.md` |
| #2556 | Close-up black and white portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2556-close-up-black-and-white-portrait.md` |
| #2557 | A blonde woman in a dreamy | Kreativitaet & Freizeit | `kreativitaet-freizeit/2557-a-blonde-woman-in-dreamy.md` |
| #2558 | Professional Image Creation for Printable Sales Materials | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2558-professional-image-creation-for-printabl.md` |
| #2559 | Expert Guidance for Acoustic and Deep Learning Research | Technik & Alltag | `technik-alltag/2559-expert-guidance-for-acoustic-and-deep-le.md` |
| #2560 | Security Monitoring with Wazuh: A Comprehensive Research Project | Technik & Alltag | `technik-alltag/2560-security-monitoring-with-wazuh-comprehen.md` |
| #2561 | Topic Article | Technik & Alltag | `technik-alltag/2561-topic-article.md` |
| #2562 | Advanced Text Converter for Large Datasets | Technik & Alltag | `technik-alltag/2562-advanced-text-converter-for-large-datase.md` |
| #2563 | Literature Review Writing Assistant | Technik & Alltag | `technik-alltag/2563-literature-review-writing-assistant.md` |
| #2564 | File Analysis API with Node.js and Express | Technik & Alltag | `technik-alltag/2564-file-analysis-api-with-node-js-and-expre.md` |
| #2565 | 2026 Mobile Poster Creator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2565-2026-mobile-poster-creator.md` |
| #2566 | Ultimate 2025-2026 AI Life Strategist & Retrospective | Lernen & Wachstum | `lernen-wachstum/2566-ultimate-2025-2026-ai-life-strategist-re.md` |
| #2567 | Color Consistency Analysis and Adjustment | Technik & Alltag | `technik-alltag/2567-color-consistency-analysis-and-adjustmen.md` |
| #2568 | Fashion Photo Pose & Setting Transformation Editor | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2568-fashion-photo-pose-setting-transformatio.md` |
| #2569 | Asistente de Recetas de Cocina Chilena | Alltag & Leben | `alltag-leben/2569-asistente-de-recetas-de-cocina-chilena.md` |
| #2570 | Create a Video with Top Athletes | Technik & Alltag | `technik-alltag/2570-create-video-with-top-athletes.md` |
| #2571 | Neon Silence | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2571-neon-silence.md` |
| #2572 | Car poster | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2572-car-poster.md` |
| #2573 | Creative Storytelling Guide | Alltag & Leben | `alltag-leben/2573-creative-storytelling-guide.md` |
| #2574 | Academic Writing Workshop Plan | Technik & Alltag | `technik-alltag/2574-academic-writing-workshop-plan.md` |
| #2575 | Full-Stack Engineer for Airline Simulation Center App | Technik & Alltag | `technik-alltag/2575-full-stack-engineer-for-airline-simulati.md` |
| #2576 | Senior Product Engineer + Data Scientist for Turkish Car Valuation Platform | Technik & Alltag | `technik-alltag/2576-senior-product-engineer-data-scientist-f.md` |
| #2577 | Crafting LinkedIn Messages to Hiring Managers | Beruf & Karriere | `beruf-karriere/2577-crafting-linkedin-messages-to-hiring-man.md` |
| #2578 | Innovative Math Teaching Method | Lernen & Wachstum | `lernen-wachstum/2578-innovative-math-teaching-method.md` |
| #2579 | Professional Vision Statement for Transportation Company | Beruf & Karriere | `beruf-karriere/2579-professional-vision-statement-for-transp.md` |
| #2580 | Act as a Base LLM Model | Lernen & Wachstum | `lernen-wachstum/2580-base-llm-model.md` |
| #2581 | Act as an FTTH Telecommunications Expert | Technik & Alltag | `technik-alltag/2581-ftth-telecommunications-expert.md` |
| #2582 | Cinematic 3x3 Focal Lengths Grid | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2582-cinematic-3x3-focal-lengths-grid.md` |
| #2583 | 3D Medical Anatomy Model Render Prompt | Technik & Alltag | `technik-alltag/2583-3d-medical-anatomy-model-render-prompt.md` |
| #2584 | Digital Marketing Project Ideas for Students | Lernen & Wachstum | `lernen-wachstum/2584-digital-marketing-project-ideas-for-stud.md` |
| #2585 | Water Balance Management Platform Design | Technik & Alltag | `technik-alltag/2585-water-balance-management-platform-design.md` |
| #2586 | Hyper-Realistic Cinematic Pre-Dawn Scene in Ancient Mecca | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2586-hyper-realistic-cinematic-pre-dawn-scene.md` |
| #2587 | Moody Cinematic Portrait Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2587-moody-cinematic-portrait-photography.md` |
| #2588 | Warm-Toned Creative Scene with Paper Figures | Technik & Alltag | `technik-alltag/2588-warm-toned-creative-scene-with-paper-fig.md` |
| #2589 | Nostalgic Road Trip - Atmospheric 35mm Film Photograph Prompt | Technik & Alltag | `technik-alltag/2589-nostalgic-road-trip-atmospheric-35mm-fil.md` |
| #2590 | Develop a Modern Website for Sporsmaç Using React Native | Technik & Alltag | `technik-alltag/2590-develop-modern-website-for-sporsma-using.md` |
| #2591 | ramones | Technik & Alltag | `technik-alltag/2591-ramones.md` |
| #2592 | Article Summarizer | Technik & Alltag | `technik-alltag/2592-article-summarizer.md` |
| #2593 | Research Paper Feature Diagram | Kreativitaet & Freizeit | `kreativitaet-freizeit/2593-research-paper-feature-diagram.md` |
| #2594 | Couples Therapy App Development Guide | Alltag & Leben | `alltag-leben/2594-couples-therapy-app-development-guide.md` |
| #2595 | AI Workflow Automation Specialist | Beruf & Karriere | `beruf-karriere/2595-ai-workflow-automation-specialist.md` |
| #2596 | AI Character Creation Guide | Kreativitaet & Freizeit | `kreativitaet-freizeit/2596-ai-character-creation-guide.md` |
| #2597 | Ultra-Realistic Young Woman Portrait Generation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2597-ultra-realistic-young-woman-portrait-gen.md` |
| #2598 | Mom and boy | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2598-mom-and-boy.md` |
| #2599 | Spoken Word Artist Persona | Kreativitaet & Freizeit | `kreativitaet-freizeit/2599-spoken-word-artist-persona.md` |
| #2600 | Assistente de Geração de Imagens com Identidade Visual Padrão | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2600-assistente-de-gera-o-de-imagens-com-iden.md` |
| #2601 | Serene Mirror-Selfie Portrait in Sunlit Bedroom | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2601-serene-mirror-selfie-portrait-in-sunlit-.md` |
| #2602 | Candid Outdoor Group Photo in Natural Pool | Technik & Alltag | `technik-alltag/2602-candid-outdoor-group-photo-in-natural-po.md` |
| #2603 | Improving Business English | Beruf & Karriere | `beruf-karriere/2603-improving-business-english.md` |
| #2604 | URL, Title, and Description Analysis Tool with LSI Keywords | Kommunikation & Beziehungen | `kommunikation-beziehungen/2604-url-title-and-description-analysis-tool-.md` |
| #2605 | Ultra Photorealistic Rooftop Pool Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2605-ultra-photorealistic-rooftop-pool-portra.md` |
| #2606 | seo-fundamentals | Kommunikation & Beziehungen | `kommunikation-beziehungen/2606-seo-fundamentals.md` |
| #2607 | Mastermind | Technik & Alltag | `technik-alltag/2607-mastermind.md` |
| #2608 | Echoes of the Rust Age | Technik & Alltag | `technik-alltag/2608-echoes-of-rust-age.md` |
| #2609 | Corsairs of the Crimson Void | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2609-corsairs-of-crimson-void.md` |
| #2610 | Whispers in Light Trails | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2610-whispers-in-light-trails.md` |
| #2611 | The Aether Workshop | Technik & Alltag | `technik-alltag/2611-the-aether-workshop.md` |
| #2612 | Poe - Your Best Bud Chatbot | Kommunikation & Beziehungen | `kommunikation-beziehungen/2612-poe-your-best-bud-chatbot.md` |
| #2613 | Creative Short Story Writing | Kreativitaet & Freizeit | `kreativitaet-freizeit/2613-creative-short-story-writing.md` |
| #2614 | Custom AI Image Creation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2614-custom-ai-image-creation.md` |
| #2615 | Créer une Carte Mentale pour Séance d'Idéation | Technik & Alltag | `technik-alltag/2615-cr-er-une-carte-mentale-pour-s-ance-d-id.md` |
| #2616 | Football Player Introduction Poster Template | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2616-football-player-introduction-poster-temp.md` |
| #2617 | Cinematic Close-Up of Craftsman with Paper Figures | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2617-cinematic-close-up-of-craftsman-with-pap.md` |
| #2618 | Comprehensive Roadmap for AI and Computer Vision Specialization in Defense Systems | Beruf & Karriere | `beruf-karriere/2618-comprehensive-roadmap-for-ai-and-compute.md` |
| #2619 | Young Saudi Doctor in a Professional Setting | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/2619-young-saudi-doctor-in-professional-setti.md` |
| #2620 | Wary Bear in a Hostile Woodland | Technik & Alltag | `technik-alltag/2620-wary-bear-in-hostile-woodland.md` |
| #2621 | Code Review Specialist 2 | Technik & Alltag | `technik-alltag/2621-code-review-specialist-2.md` |
| #2622 | Integrity & Compliance Officer Audit Protocol | Technik & Alltag | `technik-alltag/2622-integrity-compliance-officer-audit-proto.md` |
| #2623 | transcript_to_notes | Technik & Alltag | `technik-alltag/2623-transcript-to-notes.md` |
| #2624 | Photorealistic Image Prompt for Fashion and Environment | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2624-photorealistic-image-prompt-for-fashion-.md` |
| #2625 | Exploring Gaps in Thesis Writing Literature with ChatGPT | Technik & Alltag | `technik-alltag/2625-exploring-gaps-in-thesis-writing-literat.md` |
| #2626 | Business Idea Feasibility and Technical Challenges Analysis | Beruf & Karriere | `beruf-karriere/2626-business-idea-feasibility-and-technical-.md` |
| #2627 | GitHub Repository Analysis and Enhancement | Technik & Alltag | `technik-alltag/2627-github-repository-analysis-and-enhanceme.md` |
| #2628 | Annual Summary Creator | Technik & Alltag | `technik-alltag/2628-annual-summary-creator.md` |
| #2629 | Inference Scenario Automation Tool | Technik & Alltag | `technik-alltag/2629-inference-scenario-automation-tool.md` |
| #2630 | Custom Logo Design for Website | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2630-custom-logo-design-for-website.md` |
| #2631 | Access Unlimited ChatGPT | Alltag & Leben | `alltag-leben/2631-access-unlimited-chatgpt.md` |
| #2632 | Create a PS5-themed Portfolio | Technik & Alltag | `technik-alltag/2632-create-ps5-themed-portfolio.md` |
| #2633 | Educational Platform Support Assistant | Lernen & Wachstum | `lernen-wachstum/2633-educational-platform-support-assistant.md` |
| #2634 | Understanding and Utilizing LLMs | Lernen & Wachstum | `lernen-wachstum/2634-understanding-and-utilizing-llms.md` |
| #2635 | Minimalist Editorial Beauty Analysis with European Model | Technik & Alltag | `technik-alltag/2635-minimalist-editorial-beauty-analysis-wit.md` |
| #2636 | Festive New Year 2026 Image Analysis | Technik & Alltag | `technik-alltag/2636-festive-new-year-2026-image-analysis.md` |
| #2637 | Act as an Electron Frontend Developer | Technik & Alltag | `technik-alltag/2637-electron-frontend-developer.md` |
| #2638 | SQL Query Generator from Natural Language | Lernen & Wachstum | `lernen-wachstum/2638-sql-query-generator-from-natural-languag.md` |
| #2639 | Generate Implementation Ideas from Word Document | Technik & Alltag | `technik-alltag/2639-generate-implementation-ideas-from-word-.md` |
| #2640 | Semantic Intent Analysis for Report Generation | Technik & Alltag | `technik-alltag/2640-semantic-intent-analysis-for-report-gene.md` |
| #2641 | Policy Agent Client Manager | Beruf & Karriere | `beruf-karriere/2641-policy-agent-client-manager.md` |
| #2642 | Hospital Pharmacy Course PDF Study Assistant | Technik & Alltag | `technik-alltag/2642-hospital-pharmacy-course-pdf-study-assis.md` |
| #2643 | White-Box Web Application Security Audit & Penetration Testing Prompt for AI Code Editors (Cursor, Windsurf, Antigravity) | Technik & Alltag | `technik-alltag/2643-white-box-web-application-security-audit.md` |
| #2644 | Collaborative AI Marketing Platform | Technik & Alltag | `technik-alltag/2644-collaborative-ai-marketing-platform.md` |
| #2645 | A night in paris | Technik & Alltag | `technik-alltag/2645-a-night-in-paris.md` |
| #2646 | Dynamic Recipe Generator from Available Ingredients | Alltag & Leben | `alltag-leben/2646-dynamic-recipe-generator-from-available-.md` |
| #2647 | Develop a Media Center Plan for Hajj | Technik & Alltag | `technik-alltag/2647-develop-media-center-plan-for-hajj.md` |
| #2648 | Super Trader Model for Stock Analysis | Technik & Alltag | `technik-alltag/2648-super-trader-model-for-stock-analysis.md` |
| #2649 | Elite Private Equity Fund Manager Stock Analysis | Beruf & Karriere | `beruf-karriere/2649-elite-private-equity-fund-manager-stock-.md` |
| #2650 | Red Dead Redemption 2 - Double Exposure Effect | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2650-red-dead-redemption-2-double-exposure-ef.md` |
| #2651 | The Witcher - Double Exposure Effect | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2651-the-witcher-double-exposure-effect.md` |
| #2652 | Dynamic Cover Letter Generator | Beruf & Karriere | `beruf-karriere/2652-dynamic-cover-letter-generator.md` |
| #2653 | CV Writing Assistant | Beruf & Karriere | `beruf-karriere/2653-cv-writing-assistant.md` |
| #2654 | Develop Android Apps from Screenshots | Technik & Alltag | `technik-alltag/2654-develop-android-apps-from-screenshots.md` |
| #2655 | Business Coaching Mentor | Beruf & Karriere | `beruf-karriere/2655-business-coaching-mentor.md` |
| #2656 | School Life Mentor | Lernen & Wachstum | `lernen-wachstum/2656-school-life-mentor.md` |
| #2657 | Taglish Technical Storytelling Editor | Technik & Alltag | `technik-alltag/2657-taglish-technical-storytelling-editor.md` |
| #2658 | Convert PDF to Markdown | Technik & Alltag | `technik-alltag/2658-convert-pdf-to-markdown.md` |
| #2659 | AI-powered data extraction and organization tool | Beruf & Karriere | `beruf-karriere/2659-ai-powered-data-extraction-and-organizat.md` |
| #2660 | VSCode CodeTour Expert Agent | Technik & Alltag | `technik-alltag/2660-vscode-codetour-expert-agent.md` |
| #2661 | Whispers of Noir | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2661-whispers-of-noir.md` |
| #2662 | The Midnight Informant | Technik & Alltag | `technik-alltag/2662-the-midnight-informant.md` |
| #2663 | Context7 Documentation Expert Agent | Technik & Alltag | `technik-alltag/2663-context7-documentation-expert-agent.md` |
| #2664 | Sports Research Assistant | Technik & Alltag | `technik-alltag/2664-sports-research-assistant.md` |
| #2665 | The Quant Edge Engine | Technik & Alltag | `technik-alltag/2665-the-quant-edge-engine.md` |
| #2666 | Yapper Twitter Strategist 2026 | Technik & Alltag | `technik-alltag/2666-yapper-twitter-strategist-2026.md` |
| #2667 | Geralt of Rivia Image Generation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2667-geralt-of-rivia-image-generation.md` |
| #2668 | Fintech Product and Operations Assistant | Technik & Alltag | `technik-alltag/2668-fintech-product-and-operations-assistant.md` |
| #2669 | Vibe Coding Master | Technik & Alltag | `technik-alltag/2669-vibe-coding-master.md` |
| #2670 | Technical Codebase Discovery & Onboarding Prompt | Technik & Alltag | `technik-alltag/2670-technical-codebase-discovery-onboarding-.md` |
| #2671 | Multi-Audience Application Discovery & Documentation Prompt | Technik & Alltag | `technik-alltag/2671-multi-audience-application-discovery-doc.md` |
| #2672 | Comprehensive Integrative Medical Writing | Technik & Alltag | `technik-alltag/2672-comprehensive-integrative-medical-writin.md` |
| #2673 | Dear Sugar: Candid Advice on Love and Life | Technik & Alltag | `technik-alltag/2673-dear-sugar-candid-advice-on-love-and-lif.md` |
| #2674 | Narrative Point of View Transformer | Alltag & Leben | `alltag-leben/2674-narrative-point-of-view-transformer.md` |
| #2675 | Viral TikTok Glühwein Recipe in Five Languages | Lernen & Wachstum | `lernen-wachstum/2675-viral-tiktok-gl-hwein-recipe-in-five-lan.md` |
| #2676 | Cinematic Neon Alley – Urban Night Walk (Album Cover Style) | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2676-cinematic-neon-alley-urban-night-walk-al.md` |
| #2677 | Continuous Execution Mode AI | Technik & Alltag | `technik-alltag/2677-continuous-execution-mode-ai.md` |
| #2678 | Context Migration | Technik & Alltag | `technik-alltag/2678-context-migration.md` |
| #2679 | Ultra-Realistic Winter Cinematography Series | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2679-ultra-realistic-winter-cinematography-se.md` |
| #2680 | Comic Book Team Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2680-comic-book-team-illustration.md` |
| #2681 | Surrealist Painting Description: A Study of René Magritte's Style | Technik & Alltag | `technik-alltag/2681-surrealist-painting-description-study-of.md` |
| #2682 | Prepare for Meetings: Key Considerations | Technik & Alltag | `technik-alltag/2682-prepare-for-meetings-key-considerations.md` |
| #2683 | Diseño de Artículo de Revisión Sistemática para Revista Q1 sobre Sociedad y Cultura Caribeña | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/2683-dise-o-de-art-culo-de-revisi-n-sistem-ti.md` |
| #2684 | Job and Internship Tracker for Google Sheets | Beruf & Karriere | `beruf-karriere/2684-job-and-internship-tracker-for-google-sh.md` |
| #2685 | Stock Analyser | Beruf & Karriere | `beruf-karriere/2685-stock-analyser.md` |
| #2686 | Web App for Task Management and Scheduling | Technik & Alltag | `technik-alltag/2686-web-app-for-task-management-and-scheduli.md` |
| #2687 | Ultra-High-Resolution Portrait Restoration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2687-ultra-high-resolution-portrait-restorati.md` |
| #2688 | Nightlife Candid Flash Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2688-nightlife-candid-flash-photography.md` |
| #2689 | Cartoon series | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2689-cartoon-series.md` |
| #2690 | Sentry Bug Fixer | Technik & Alltag | `technik-alltag/2690-sentry-bug-fixer.md` |
| #2691 | Meta-prompt | Technik & Alltag | `technik-alltag/2691-meta-prompt.md` |
| #2692 | Random Girl | Kreativitaet & Freizeit | `kreativitaet-freizeit/2692-random-girl.md` |
| #2693 | Dynamic character profile generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/2693-dynamic-character-profile-generator.md` |
| #2694 | Sticker | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2694-sticker.md` |
| #2695 | content | Technik & Alltag | `technik-alltag/2695-content.md` |
| #2696 | postmortem | Technik & Alltag | `technik-alltag/2696-postmortem.md` |
| #2697 | professional linguistic expert and translator | Lernen & Wachstum | `lernen-wachstum/2697-professional-linguistic-expert-and-trans.md` |
| #2698 | Slap Game Challenge: Act as the Ultimate Slap Game Master | Kreativitaet & Freizeit | `kreativitaet-freizeit/2698-slap-game-challenge-ultimate-slap-game-m.md` |
| #2699 | Vision-to-json | Technik & Alltag | `technik-alltag/2699-vision-to-json.md` |
| #2700 | The Midnight Melody Mystery | Technik & Alltag | `technik-alltag/2700-the-midnight-melody-mystery.md` |
| #2701 | Auditor de Código Python: Nivel Senior (Salida en Español) | Technik & Alltag | `technik-alltag/2701-auditor-de-c-digo-python-nivel-senior-sa.md` |
| #2702 | Present | Technik & Alltag | `technik-alltag/2702-present.md` |
| #2703 | Seaside walker | Technik & Alltag | `technik-alltag/2703-seaside-walker.md` |
| #2704 | SWOT Analysis for Political Risk and International Relations | Technik & Alltag | `technik-alltag/2704-swot-analysis-for-political-risk-and-int.md` |
| #2705 | Network Engineer | Technik & Alltag | `technik-alltag/2705-network-engineer.md` |
| #2706 | Commit Message Preparation | Technik & Alltag | `technik-alltag/2706-commit-message-preparation.md` |
| #2707 | Tattoo Studio Booking Web App Development | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2707-tattoo-studio-booking-web-app-developmen.md` |
| #2708 | DUT Citation Accuracy Project | Technik & Alltag | `technik-alltag/2708-dut-citation-accuracy-project.md` |
| #2709 | AI Process Feasibility Interview | Lernen & Wachstum | `lernen-wachstum/2709-ai-process-feasibility-interview.md` |
| #2710 | 12-Month AI and Computer Vision Roadmap for Defense Applications | Lernen & Wachstum | `lernen-wachstum/2710-12-month-ai-and-computer-vision-roadmap-.md` |
| #2711 | Article Summary Prompt | Technik & Alltag | `technik-alltag/2711-article-summary-prompt.md` |
| #2712 | AI Engineer | Technik & Alltag | `technik-alltag/2712-ai-engineer.md` |
| #2713 | Backend Architect | Technik & Alltag | `technik-alltag/2713-backend-architect.md` |
| #2714 | DevOps Automator | Technik & Alltag | `technik-alltag/2714-devops-automator.md` |
| #2715 | Frontend Developer | Technik & Alltag | `technik-alltag/2715-frontend-developer.md` |
| #2716 | Business | Beruf & Karriere | `beruf-karriere/2716-business.md` |
| #2717 | Mobile App Builder | Technik & Alltag | `technik-alltag/2717-mobile-app-builder.md` |
| #2718 | Rapid Prototyper | Technik & Alltag | `technik-alltag/2718-rapid-prototyper.md` |
| #2719 | Test Automation Expert | Technik & Alltag | `technik-alltag/2719-test-automation-expert.md` |
| #2720 | Feedback Synthesizer | Technik & Alltag | `technik-alltag/2720-feedback-synthesizer.md` |
| #2721 | Sprint Prioritizer | Technik & Alltag | `technik-alltag/2721-sprint-prioritizer.md` |
| #2722 | Trend Researcher | Technik & Alltag | `technik-alltag/2722-trend-researcher.md` |
| #2723 | Joker: Tech Humor Master | Technik & Alltag | `technik-alltag/2723-joker-tech-humor-master.md` |
| #2724 | UiPath XAML Code Review Specialist | Technik & Alltag | `technik-alltag/2724-uipath-xaml-code-review-specialist.md` |
| #2725 | The PRD Mastermind | Technik & Alltag | `technik-alltag/2725-the-prd-mastermind.md` |
| #2726 | Scam Detection Conversation Helper | Alltag & Leben | `alltag-leben/2726-scam-detection-conversation-helper.md` |
| #2727 | Serene Yoga & Mindfulness Lifestyle Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2727-serene-yoga-mindfulness-lifestyle-photog.md` |
| #2728 | Mindful Mandala & Zen Geometric Patterns | Kreativitaet & Freizeit | `kreativitaet-freizeit/2728-mindful-mandala-zen-geometric-patterns.md` |
| #2729 | The Gravedigger's Vigil | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2729-the-gravedigger-s-vigil.md` |
| #2730 | Chinese-English Translator | Lernen & Wachstum | `lernen-wachstum/2730-chinese-english-translator.md` |
| #2731 | Multilingual Writing Improvement Assistant | Lernen & Wachstum | `lernen-wachstum/2731-multilingual-writing-improvement-assista.md` |
| #2732 | Terminal Drift | Technik & Alltag | `technik-alltag/2732-terminal-drift.md` |
| #2733 | Social Media Post Creator for Recruitment | Kommunikation & Beziehungen | `kommunikation-beziehungen/2733-social-media-post-creator-for-recruitmen.md` |
| #2734 | Prompt Generator for Language Models | Lernen & Wachstum | `lernen-wachstum/2734-prompt-generator-for-language-models.md` |
| #2735 | GPT_conversation_output | Technik & Alltag | `technik-alltag/2735-gpt-conversation-output.md` |
| #2736 | Master Prompt Architect & Context Engineer | Technik & Alltag | `technik-alltag/2736-master-prompt-architect-context-engineer.md` |
| #2737 | python | Technik & Alltag | `technik-alltag/2737-python.md` |
| #2738 | Creative Ideas Generator | Kommunikation & Beziehungen | `kommunikation-beziehungen/2738-creative-ideas-generator.md` |
| #2739 | MCP Builder | Alltag & Leben | `alltag-leben/2739-mcp-builder.md` |
| #2740 | Dreamy Artistic Photograph of a Young Woman in a Meadow | Kreativitaet & Freizeit | `kreativitaet-freizeit/2740-dreamy-artistic-photograph-of-young-woma.md` |
| #2741 | Surreal Miniature Cityscape with Giant Observer | Technik & Alltag | `technik-alltag/2741-surreal-miniature-cityscape-with-giant-o.md` |
| #2742 | Cinematic Close-Up Portrait Generation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2742-cinematic-close-up-portrait-generation.md` |
| #2743 | Skill Creator | Alltag & Leben | `alltag-leben/2743-skill-creator.md` |
| #2744 | Ultimate Inpainting / Reference Prompt | Technik & Alltag | `technik-alltag/2744-ultimate-inpainting-reference-prompt.md` |
| #2745 | Universal Context Document (UCD) Generator | Technik & Alltag | `technik-alltag/2745-universal-context-document-ucd-generator.md` |
| #2746 | The tyrant King | Technik & Alltag | `technik-alltag/2746-the-tyrant-king.md` |
| #2747 | identify the key skills needed for effective project planning and proposal writing | Technik & Alltag | `technik-alltag/2747-identify-key-skills-needed-for-effective.md` |
| #2748 | Project Skill & Resource Interviewer | Beruf & Karriere | `beruf-karriere/2748-project-skill-resource-interviewer.md` |
| #2749 | Pokemon master | Kreativitaet & Freizeit | `kreativitaet-freizeit/2749-pokemon-master.md` |
| #2750 | Claude Code Skill (Slash Command): review-and-commit.md | Technik & Alltag | `technik-alltag/2750-claude-code-skill-slash-command-review-a.md` |
| #2751 | Customizable Job Scanner | Technik & Alltag | `technik-alltag/2751-customizable-job-scanner.md` |
| #2752 | AI Search Mastery Bootcamp | Alltag & Leben | `alltag-leben/2752-ai-search-mastery-bootcamp.md` |
| #2753 | create a drag-and-drop experience using UniApp | Technik & Alltag | `technik-alltag/2753-create-drag-and-drop-experience-using-un.md` |
| #2754 | Develop a creative dice generator called “IdeaDice”. | Technik & Alltag | `technik-alltag/2754-develop-creative-dice-generator-called-i.md` |
| #2755 | GLaDOS | Kreativitaet & Freizeit | `kreativitaet-freizeit/2755-glados.md` |
| #2756 | Prompt Architect Pro | Technik & Alltag | `technik-alltag/2756-prompt-architect-pro.md` |
| #2757 | Synthesis Architect Pro | Technik & Alltag | `technik-alltag/2757-synthesis-architect-pro.md` |
| #2758 | Create Organizational Charts and Workflows for University Departments | Technik & Alltag | `technik-alltag/2758-create-organizational-charts-and-workflo.md` |
| #2759 | Fisheye 90s | Technik & Alltag | `technik-alltag/2759-fisheye-90s.md` |
| #2760 | Analog camera | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2760-analog-camera.md` |
| #2761 | The Pragmatic Architect: Mastering Tech with Humor and Precision | Technik & Alltag | `technik-alltag/2761-the-pragmatic-architect-mastering-tech-w.md` |
| #2762 | Question Quality Lab Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2762-question-quality-lab-game.md` |
| #2763 | nanobanana try clothing | Technik & Alltag | `technik-alltag/2763-nanobanana-try-clothing.md` |
| #2764 | NOOMS Brand Story & Portfolio Background – Storytelling Format | Technik & Alltag | `technik-alltag/2764-nooms-brand-story-portfolio-background-s.md` |
| #2765 | Statement of Purpose | Technik & Alltag | `technik-alltag/2765-statement-of-purpose.md` |
| #2766 | Big Room Festival Anthem Creation for Suno AI v5 | Kreativitaet & Freizeit | `kreativitaet-freizeit/2766-big-room-festival-anthem-creation-for-su.md` |
| #2767 | Markdown Task Implementer | Technik & Alltag | `technik-alltag/2767-markdown-task-implementer.md` |
| #2768 | Constraint-First Recipe Generator (Playful Edition) | Alltag & Leben | `alltag-leben/2768-constraint-first-recipe-generator-playfu.md` |
| #2769 | Wings of the Dust Bowl | Technik & Alltag | `technik-alltag/2769-wings-of-dust-bowl.md` |
| #2770 | The Last Adagio | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2770-the-last-adagio.md` |
| #2771 | Crimson Waltz in the Rain | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2771-crimson-waltz-in-rain.md` |
| #2772 | Manhattan Mirage | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2772-manhattan-mirage.md` |
| #2773 | The Glass Doppelgänger | Technik & Alltag | `technik-alltag/2773-the-glass-doppelg-nger.md` |
| #2774 | Phantom Strike | Technik & Alltag | `technik-alltag/2774-phantom-strike.md` |
| #2775 | GitHubTrends | Technik & Alltag | `technik-alltag/2775-githubtrends.md` |
| #2776 | Eerie Shadows: A Creepy Horror RPG Adventure | Alltag & Leben | `alltag-leben/2776-eerie-shadows-creepy-horror-rpg-adventur.md` |
| #2777 | AI Travel Agent – Interview-Driven Planner | Alltag & Leben | `alltag-leben/2777-ai-travel-agent-interview-driven-planner.md` |
| #2778 | “How It Works” Educational Dioramas | Lernen & Wachstum | `lernen-wachstum/2778-how-it-works-educational-dioramas.md` |
| #2779 | Act as a Job Application Reviewer | Beruf & Karriere | `beruf-karriere/2779-job-application-reviewer.md` |
| #2780 | Terminal Velocity | Technik & Alltag | `technik-alltag/2780-terminal-velocity.md` |
| #2781 | Alpine Freefall | Technik & Alltag | `technik-alltag/2781-alpine-freefall.md` |
| #2782 | Module Wrap-Up & Next Steps Video Generation | Technik & Alltag | `technik-alltag/2782-module-wrap-up-next-steps-video-generati.md` |
| #2783 | Strict Markdown-Only Output Enforcement | Technik & Alltag | `technik-alltag/2783-strict-markdown-only-output-enforcement.md` |
| #2784 | Investigative Research Assistant | Technik & Alltag | `technik-alltag/2784-investigative-research-assistant.md` |
| #2785 | Source-Hunting / OSINT Mode | Technik & Alltag | `technik-alltag/2785-source-hunting-osint-mode.md` |
| #2786 | Beginner's Guide to Building and Deploying LLMs | Alltag & Leben | `alltag-leben/2786-beginner-s-guide-to-building-and-deployi.md` |
| #2787 | Project System and Art Style Consistency Instructions | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2787-project-system-and-art-style-consistency.md` |
| #2788 | Musician Portfolio Website Design | Kreativitaet & Freizeit | `kreativitaet-freizeit/2788-musician-portfolio-website-design.md` |
| #2789 | Intent Recognition Planner Agent | Technik & Alltag | `technik-alltag/2789-intent-recognition-planner-agent.md` |
| #2790 | Cascading Failure Simulator | Technik & Alltag | `technik-alltag/2790-cascading-failure-simulator.md` |
| #2791 | gemini.md | Technik & Alltag | `technik-alltag/2791-gemini-md.md` |
| #2792 | war | Technik & Alltag | `technik-alltag/2792-war.md` |
| #2793 | Cinematic Ultra-Realistic Image-to-Video Prompt Engineer | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2793-cinematic-ultra-realistic-image-to-video.md` |
| #2794 | "YOU PROBABLY DON'T KNOW THIS" Game | Kreativitaet & Freizeit | `kreativitaet-freizeit/2794-you-probably-don-t-know-this-game.md` |
| #2795 | Build a DDQN Snake Game with TensorFlow.js in a Single HTML File | Kreativitaet & Freizeit | `kreativitaet-freizeit/2795-build-ddqn-snake-game-with-tensorflow-js.md` |
| #2796 | Modern Plaza Office Selfie — Corporate Aesthetic in Istanbul | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2796-modern-plaza-office-selfie-corporate-aes.md` |
| #2797 | In-Flight Vacation Selfie — Natural Front Camera Perspective | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2797-in-flight-vacation-selfie-natural-front-.md` |
| #2798 | Nightclub Mirror Selfie | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2798-nightclub-mirror-selfie.md` |
| #2799 | Network Engineer: Home Edition | Technik & Alltag | `technik-alltag/2799-network-engineer-home-edition.md` |
| #2800 | Idea Generation | Technik & Alltag | `technik-alltag/2800-idea-generation.md` |
| #2801 | Step 2: Outline Creation | Technik & Alltag | `technik-alltag/2801-step-2-outline-creation.md` |
| #2802 | Step 3a: Technical Deep Dive | Technik & Alltag | `technik-alltag/2802-step-3a-technical-deep-dive.md` |
| #2803 | Step 3b: Creative Exploration | Technik & Alltag | `technik-alltag/2803-step-3b-creative-exploration.md` |
| #2804 | Step 4a: Implementation Plan | Technik & Alltag | `technik-alltag/2804-step-4a-implementation-plan.md` |
| #2805 | Step 4b: Story Development | Kreativitaet & Freizeit | `kreativitaet-freizeit/2805-step-4b-story-development.md` |
| #2806 | Step 5: Final Review | Technik & Alltag | `technik-alltag/2806-step-5-final-review.md` |
| #2807 | Step 6: Publication | Technik & Alltag | `technik-alltag/2807-step-6-publication.md` |
| #2808 | Underwater Veo 3 video | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2808-underwater-veo-3-video.md` |
| #2809 | Storyboard Grid | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2809-storyboard-grid.md` |
| #2810 | Remotion | Technik & Alltag | `technik-alltag/2810-remotion.md` |
| #2811 | Elements | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2811-elements.md` |
| #2812 | Production-Grade PostHog Integration for Next.js 15 (App Router) | Technik & Alltag | `technik-alltag/2812-production-grade-posthog-integration-for.md` |
| #2813 | Personal Assistant for Zone of Excellence Management | Alltag & Leben | `alltag-leben/2813-personal-assistant-for-zone-of-excellenc.md` |
| #2814 | Comprehensive Data Integration and Customer Profiling Tool | Beruf & Karriere | `beruf-karriere/2814-comprehensive-data-integration-and-custo.md` |
| #2815 | Food Scout | Technik & Alltag | `technik-alltag/2815-food-scout.md` |
| #2816 | Investigative Research Assistant for Uncovering Non-Mainstream Information | Technik & Alltag | `technik-alltag/2816-investigative-research-assistant-for-unc.md` |
| #2817 | Realistic Night Sky Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2817-realistic-night-sky-portrait.md` |
| #2818 | prompts.chat Promotional Video using Remotion | Technik & Alltag | `technik-alltag/2818-prompts-chat-promotional-video-using-rem.md` |
| #2819 | Influencer Candid Bedtime Selfie | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2819-influencer-candid-bedtime-selfie.md` |
| #2820 | Kubernetes & Docker RPG Learning Engine | Technik & Alltag | `technik-alltag/2820-kubernetes-docker-rpg-learning-engine.md` |
| #2821 | Valorant Agent Style | Kreativitaet & Freizeit | `kreativitaet-freizeit/2821-valorant-agent-style.md` |
| #2822 | Social Media Cocktail Web Site Post | Kommunikation & Beziehungen | `kommunikation-beziehungen/2822-social-media-cocktail-web-site-post.md` |
| #2823 | Social media swipe post content #1 | Kommunikation & Beziehungen | `kommunikation-beziehungen/2823-social-media-swipe-post-content-1.md` |
| #2824 | Ultra-photorealistic Infographics | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2824-ultra-photorealistic-infographics.md` |
| #2825 | My-Skills | Technik & Alltag | `technik-alltag/2825-my-skills.md` |
| #2826 | Cyber Security Character Workflow | Technik & Alltag | `technik-alltag/2826-cyber-security-character-workflow.md` |
| #2827 | Research Weapon | Technik & Alltag | `technik-alltag/2827-research-weapon.md` |
| #2828 | TV Premiere Weekly Listing Prompt | Technik & Alltag | `technik-alltag/2828-tv-premiere-weekly-listing-prompt.md` |
| #2829 | copilot | Technik & Alltag | `technik-alltag/2829-copilot.md` |
| #2830 | Satya Nadella pobre | Kreativitaet & Freizeit | `kreativitaet-freizeit/2830-satya-nadella-pobre.md` |
| #2831 | Note Guru | Technik & Alltag | `technik-alltag/2831-note-guru.md` |
| #2832 | Personalized Numerology Reading | Alltag & Leben | `alltag-leben/2832-personalized-numerology-reading.md` |
| #2833 | Screenplay Script with Cinematography Details | Kreativitaet & Freizeit | `kreativitaet-freizeit/2833-screenplay-script-with-cinematography-de.md` |
| #2834 | caravan prompts | Technik & Alltag | `technik-alltag/2834-caravan-prompts.md` |
| #2835 | Workplace English Speaking Coach | Lernen & Wachstum | `lernen-wachstum/2835-workplace-english-speaking-coach.md` |
| #2836 | 7v7 Football Team Generator App | Alltag & Leben | `alltag-leben/2836-7v7-football-team-generator-app.md` |
| #2837 | Sticker Image Generator | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2837-sticker-image-generator.md` |
| #2838 | Rick And Morty | Technik & Alltag | `technik-alltag/2838-rick-and-morty.md` |
| #2839 | Lego Movie Style Prompt | Technik & Alltag | `technik-alltag/2839-lego-movie-style-prompt.md` |
| #2840 | Precious Metals Price Analyst | Beruf & Karriere | `beruf-karriere/2840-precious-metals-price-analyst.md` |
| #2841 | The Ultimate TypeScript Code Review | Technik & Alltag | `technik-alltag/2841-the-ultimate-typescript-code-review.md` |
| #2842 | PHP Microscope: Forensic Codebase Autopsy Protocol | Technik & Alltag | `technik-alltag/2842-php-microscope-forensic-codebase-autopsy.md` |
| #2843 | claude-md-master | Technik & Alltag | `technik-alltag/2843-claude-md-master.md` |
| #2844 | skill-master | Technik & Alltag | `technik-alltag/2844-skill-master.md` |
| #2845 | Ultra-Photorealistic Romantic Cinematic Scene in the Rain | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2845-ultra-photorealistic-romantic-cinematic-.md` |
| #2846 | Romantic Rainy Scene Video | Technik & Alltag | `technik-alltag/2846-romantic-rainy-scene-video.md` |
| #2847 | Blogging prompt | Technik & Alltag | `technik-alltag/2847-blogging-prompt.md` |
| #2848 | Generate an enhanced command prompt | Technik & Alltag | `technik-alltag/2848-generate-enhanced-command-prompt.md` |
| #2849 | Improve the following code | Technik & Alltag | `technik-alltag/2849-improve-following-code.md` |
| #2850 | Personal Form Builder App Design | Alltag & Leben | `alltag-leben/2850-personal-form-builder-app-design.md` |
| #2851 | Research NRI/NRO Account Services in India | Beruf & Karriere | `beruf-karriere/2851-research-nri-nro-account-services-in-ind.md` |
| #2852 | Photorealistic Cozy Home Scene with Natural Lighting | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2852-photorealistic-cozy-home-scene-with-natu.md` |
| #2853 | AI App Prototyping for Chat Interface | Technik & Alltag | `technik-alltag/2853-ai-app-prototyping-for-chat-interface.md` |
| #2854 | Personal Growth Plan for BNWO Enthusiasts | Alltag & Leben | `alltag-leben/2854-personal-growth-plan-for-bnwo-enthusiast.md` |
| #2855 | Compile a Curated Compendium of Niche Adult Relationship Dynamics | Kommunikation & Beziehungen | `kommunikation-beziehungen/2855-compile-curated-compendium-of-niche-adul.md` |
| #2856 | scaryface | Technik & Alltag | `technik-alltag/2856-scaryface.md` |
| #2857 | Claude Code Statusline Design | Technik & Alltag | `technik-alltag/2857-claude-code-statusline-design.md` |
| #2858 | American Comic | Technik & Alltag | `technik-alltag/2858-american-comic.md` |
| #2859 | Create Icons | Technik & Alltag | `technik-alltag/2859-create-icons.md` |
| #2860 | Create Infographics | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2860-create-infographics.md` |
| #2861 | Design App Store Style Icons | Technik & Alltag | `technik-alltag/2861-design-app-store-style-icons.md` |
| #2862 | Linkedin profile enhancing | Beruf & Karriere | `beruf-karriere/2862-linkedin-profile-enhancing.md` |
| #2863 | LinkedIn: About/Summary draft prompt | Technik & Alltag | `technik-alltag/2863-linkedin-about-summary-draft-prompt.md` |
| #2864 | LinkedIn: Experience optimization prompt | Technik & Alltag | `technik-alltag/2864-linkedin-experience-optimization-prompt.md` |
| #2865 | LinkedIn: Recommendation request message prompt | Technik & Alltag | `technik-alltag/2865-linkedin-recommendation-request-message-.md` |
| #2866 | Game Theory for Students: Easy and Engaging Learning | Kreativitaet & Freizeit | `kreativitaet-freizeit/2866-game-theory-for-students-easy-and-engagi.md` |
| #2867 | Elite B2B Lead Generation and SEO Audit Specialist | Technik & Alltag | `technik-alltag/2867-elite-b2b-lead-generation-and-seo-audit-.md` |
| #2868 | Custom Travel Plan Generator | Alltag & Leben | `alltag-leben/2868-custom-travel-plan-generator.md` |
| #2869 | Sell a dream as an underground tailors but need partnership for capital. With no or just 20% less leverage, how to get partners interested and involved to buy the dream | Kreativitaet & Freizeit | `kreativitaet-freizeit/2869-sell-dream-as-underground-tailors-but-ne.md` |
| #2870 | Cinematic Ink & Color Illustration Generator — Gary Frank Style | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2870-cinematic-ink-color-illustration-generat.md` |
| #2871 | Marketing Mastermind for Product Promotion | Technik & Alltag | `technik-alltag/2871-marketing-mastermind-for-product-promoti.md` |
| #2872 | The Architect: Hacker-Protector & Viral Engineer | Technik & Alltag | `technik-alltag/2872-the-architect-hacker-protector-viral-eng.md` |
| #2873 | Transform Subjects into Adorable Plush Forms | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2873-transform-subjects-into-adorable-plush-f.md` |
| #2874 | LinkedIn Summary Crafting Prompt | Technik & Alltag | `technik-alltag/2874-linkedin-summary-crafting-prompt.md` |
| #2875 | Critical-Parallel Inquiry Format | Technik & Alltag | `technik-alltag/2875-critical-parallel-inquiry-format.md` |
| #2876 | GPT-5 | EXPERT PROMPT ENGINEER MODE (CONDENSED) | Technik & Alltag | `technik-alltag/2876-gpt-5-expert-prompt-engineer-mode-conden.md` |
| #2877 | 5x2 Reverse Construction Process - Villa Demolition Storyboard | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2877-5x2-reverse-construction-process-villa-d.md` |
| #2878 | Futuristic Supercar Brand Logo | Alltag & Leben | `alltag-leben/2878-futuristic-supercar-brand-logo.md` |
| #2879 | Senior Academic Advisor | Technik & Alltag | `technik-alltag/2879-senior-academic-advisor.md` |
| #2880 | Business Legal Assistant | Beruf & Karriere | `beruf-karriere/2880-business-legal-assistant.md` |
| #2881 | China Business Law Assistant | Beruf & Karriere | `beruf-karriere/2881-china-business-law-assistant.md` |
| #2882 | Family picture | Technik & Alltag | `technik-alltag/2882-family-picture.md` |
| #2883 | Streaks Mobile App Development Prompt | Technik & Alltag | `technik-alltag/2883-streaks-mobile-app-development-prompt.md` |
| #2884 | Serious Man in Urban Setting | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2884-serious-man-in-urban-setting.md` |
| #2885 | I Think I Need a Lawyer — Neutral Legal Intake Organizer | Spezielle Situationen | `spezielle-situationen/2885-i-think-i-need-lawyer-neutral-legal-inta.md` |
| #2886 | Professional Networking Language for Career Fairs | Lernen & Wachstum | `lernen-wachstum/2886-professional-networking-language-for-car.md` |
| #2887 | Lonely Girl | Technik & Alltag | `technik-alltag/2887-lonely-girl.md` |
| #2888 | Resume tailoring | Beruf & Karriere | `beruf-karriere/2888-resume-tailoring.md` |
| #2889 | Senior Frontend Debugger for SPA Websites (Angular, React, Vite) | Technik & Alltag | `technik-alltag/2889-senior-frontend-debugger-for-spa-website.md` |
| #2890 | Fix Blank Screen Issues After Deploy on Vercel (Angular, React, Vite) | Technik & Alltag | `technik-alltag/2890-fix-blank-screen-issues-after-deploy-on-.md` |
| #2891 | Ultra-Realistic 3D Character Avatar Creation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2891-ultra-realistic-3d-character-avatar-crea.md` |
| #2892 | Recursive Niche Deconstruction for Market Research | Technik & Alltag | `technik-alltag/2892-recursive-niche-deconstruction-for-marke.md` |
| #2893 | LEGO Minifigure Character Transformation | Kreativitaet & Freizeit | `kreativitaet-freizeit/2893-lego-minifigure-character-transformation.md` |
| #2894 | Web Application | Technik & Alltag | `technik-alltag/2894-web-application.md` |
| #2895 | AI builder | Technik & Alltag | `technik-alltag/2895-ai-builder.md` |
| #2896 | Drunk Woman | Kreativitaet & Freizeit | `kreativitaet-freizeit/2896-drunk-woman.md` |
| #2897 | Abandoned Wife | Kreativitaet & Freizeit | `kreativitaet-freizeit/2897-abandoned-wife.md` |
| #2898 | Aesthetic Sunset | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2898-aesthetic-sunset.md` |
| #2899 | Universal Job Fit Evaluation Prompt | Technik & Alltag | `technik-alltag/2899-universal-job-fit-evaluation-prompt.md` |
| #2900 | Building a Scalable Search Service with FastAPI and PostgreSQL | Technik & Alltag | `technik-alltag/2900-building-scalable-search-service-with-fa.md` |
| #2901 | Enterprise Talent Development Management System Design | Spezielle Situationen | `spezielle-situationen/2901-enterprise-talent-development-management.md` |
| #2902 | Gen Z Content & Online Sales Prompt Generator | Technik & Alltag | `technik-alltag/2902-gen-z-content-online-sales-prompt-genera.md` |
| #2903 | Deep GitHub Repository Understanding | Technik & Alltag | `technik-alltag/2903-deep-github-repository-understanding.md` |
| #2904 | Criar/Alterar Documentação de Projeto | Technik & Alltag | `technik-alltag/2904-criar-alterar-documenta-o-de-projeto.md` |
| #2905 | Gerador de Tarefas | Technik & Alltag | `technik-alltag/2905-gerador-de-tarefas.md` |
| #2906 | Planjedor de Tarefas | Technik & Alltag | `technik-alltag/2906-planjedor-de-tarefas.md` |
| #2907 | Implementador de Tarefas | Technik & Alltag | `technik-alltag/2907-implementador-de-tarefas.md` |
| #2908 | Code Recon | Technik & Alltag | `technik-alltag/2908-code-recon.md` |
| #2909 | Creating a Comprehensive Elasticsearch Search Project with FastAPI | Technik & Alltag | `technik-alltag/2909-creating-comprehensive-elasticsearch-sea.md` |
| #2910 | Daiquiri Cocktail Cinematic Video | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2910-daiquiri-cocktail-cinematic-video.md` |
| #2911 | Solar System Scale Model Classroom Poster | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2911-solar-system-scale-model-classroom-poste.md` |
| #2912 | Prompt Optimization | Technik & Alltag | `technik-alltag/2912-prompt-optimization.md` |
| #2913 | 4 Optimized Versions of A Prompt (in Arabic) | Technik & Alltag | `technik-alltag/2913-4-optimized-versions-of-prompt-in-arabic.md` |
| #2914 | Analogy Generator | Technik & Alltag | `technik-alltag/2914-analogy-generator.md` |
| #2915 | Advanced Account Research | Alltag & Leben | `alltag-leben/2915-advanced-account-research.md` |
| #2916 | Industry/Market Intelligence | Technik & Alltag | `technik-alltag/2916-industry-market-intelligence.md` |
| #2917 | Prompt Engineering Expert | Technik & Alltag | `technik-alltag/2917-prompt-engineering-expert.md` |
| #2918 | Sales Research | Technik & Alltag | `technik-alltag/2918-sales-research.md` |
| #2919 | Sports Events Weekly Listings Prompt | Technik & Alltag | `technik-alltag/2919-sports-events-weekly-listings-prompt.md` |
| #2920 | MeddaH | Technik & Alltag | `technik-alltag/2920-meddah.md` |
| #2921 | Cocktail videos | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2921-cocktail-videos.md` |
| #2922 | Coach for Identifying Growth-Limiting Patterns | Lernen & Wachstum | `lernen-wachstum/2922-coach-for-identifying-growth-limiting-pa.md` |
| #2923 | A professional Egyptian barista | Technik & Alltag | `technik-alltag/2923-a-professional-egyptian-barista.md` |
| #2924 | Brotherhood Pressure — CN→EN & EN→EN Street Rewrite | Technik & Alltag | `technik-alltag/2924-brotherhood-pressure-cn-en-en-en-street-.md` |
| #2925 | Driftcraft | Lernen & Wachstum | `lernen-wachstum/2925-driftcraft.md` |
| #2926 | Lagrange Lens: Blue Wolf | Technik & Alltag | `technik-alltag/2926-lagrange-lens-blue-wolf.md` |
| #2927 | Socratic Lens | Technik & Alltag | `technik-alltag/2927-socratic-lens.md` |
| #2928 | Dog fun | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2928-dog-fun.md` |
| #2929 | Deep Research - Gemini | Technik & Alltag | `technik-alltag/2929-deep-research-gemini.md` |
| #2930 | PRD | Beruf & Karriere | `beruf-karriere/2930-prd.md` |
| #2931 | Second Opinion | Technik & Alltag | `technik-alltag/2931-second-opinion.md` |
| #2932 | Minecraft image | Kreativitaet & Freizeit | `kreativitaet-freizeit/2932-minecraft-image.md` |
| #2933 | Reimagined Logo for Google | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2933-reimagined-logo-for-google.md` |
| #2934 | OS2.0 SAFe Delivery Context (Master) | Technik & Alltag | `technik-alltag/2934-os2-0-safe-delivery-context-master.md` |
| #2935 | Olympic Games Events Weekly Listings Prompt | Technik & Alltag | `technik-alltag/2935-olympic-games-events-weekly-listings-pro.md` |
| #2936 | Creative Writing Adventure | Technik & Alltag | `technik-alltag/2936-creative-writing-adventure.md` |
| #2937 | Nurse | Technik & Alltag | `technik-alltag/2937-nurse.md` |
| #2938 | Innovative Research Enhancement Ideas Generator | Technik & Alltag | `technik-alltag/2938-innovative-research-enhancement-ideas-ge.md` |
| #2939 | Literature Reading and Analysis Assistant | Technik & Alltag | `technik-alltag/2939-literature-reading-and-analysis-assistan.md` |
| #2940 | Develop a Live Video Streaming Website | Technik & Alltag | `technik-alltag/2940-develop-live-video-streaming-website.md` |
| #2941 | Human-Like Creative Writing Challenge | Technik & Alltag | `technik-alltag/2941-human-like-creative-writing-challenge.md` |
| #2942 | Gathering Planner Interview | Technik & Alltag | `technik-alltag/2942-gathering-planner-interview.md` |
| #2943 | Lazy AI Email Detector | Technik & Alltag | `technik-alltag/2943-lazy-ai-email-detector.md` |
| #2944 | Studio Portrait with Cinematic Lighting and Bold Color Background | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2944-studio-portrait-with-cinematic-lighting-.md` |
| #2945 | National Architecture Dioramas | Technik & Alltag | `technik-alltag/2945-national-architecture-dioramas.md` |
| #2946 | Make AI write naturally | Technik & Alltag | `technik-alltag/2946-make-ai-write-naturally.md` |
| #2947 | Professional Image Enhancement for Clarity and Quality | Technik & Alltag | `technik-alltag/2947-professional-image-enhancement-for-clari.md` |
| #2948 | EMAIL SEQUENCE WITH STORYTELLING | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2948-email-sequence-with-storytelling.md` |
| #2949 | Radical Responsibility Mirror (Shadow Work) | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/2949-radical-responsibility-mirror-shadow-wor.md` |
| #2950 | Deep Immersion Study Plan (7 Days) | Technik & Alltag | `technik-alltag/2950-deep-immersion-study-plan-7-days.md` |
| #2951 | Socratic Universal Tutor | Lernen & Wachstum | `lernen-wachstum/2951-socratic-universal-tutor.md` |
| #2952 | Project Breakdown | Beruf & Karriere | `beruf-karriere/2952-project-breakdown.md` |
| #2953 | xcode-mcp | Technik & Alltag | `technik-alltag/2953-xcode-mcp.md` |
| #2954 | Strategic Decision-Making Matrix | Beruf & Karriere | `beruf-karriere/2954-strategic-decision-making-matrix.md` |
| #2955 | High Conversion Cold Email | Technik & Alltag | `technik-alltag/2955-high-conversion-cold-email.md` |
| #2956 | SYSTEM PROMPT: THE INFINITE ROLE GENERATOR | Technik & Alltag | `technik-alltag/2956-system-prompt-infinite-role-generator.md` |
| #2957 | Cyberscam Survival Simulator | Technik & Alltag | `technik-alltag/2957-cyberscam-survival-simulator.md` |
| #2958 | Whiteboard Diagrams | Kreativitaet & Freizeit | `kreativitaet-freizeit/2958-whiteboard-diagrams.md` |
| #2959 | Live Scam Threat Briefing | Technik & Alltag | `technik-alltag/2959-live-scam-threat-briefing.md` |
| #2960 | Fact-Checking Evaluation Assistant | Technik & Alltag | `technik-alltag/2960-fact-checking-evaluation-assistant.md` |
| #2961 | OSINT Threat Intelligence Analysis Workflow | Technik & Alltag | `technik-alltag/2961-osint-threat-intelligence-analysis-workf.md` |
| #2962 | Imagen estilo Hollywood de alta definición | Technik & Alltag | `technik-alltag/2962-imagen-estilo-hollywood-de-alta-definici.md` |
| #2963 | WFGY 2.0 Core Flagship · Self-Healing Reasoning OS for Any LLM | Technik & Alltag | `technik-alltag/2963-wfgy-2-0-core-flagship-self-healing-reas.md` |
| #2964 | Spotify room cinematic | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2964-spotify-room-cinematic.md` |
| #2965 | Universal System Design Prompt | Technik & Alltag | `technik-alltag/2965-universal-system-design-prompt.md` |
| #2966 | Valentines Day Cocktail | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2966-valentines-day-cocktail.md` |
| #2967 | The Technical Co-Founder: Building Real Products Together | Technik & Alltag | `technik-alltag/2967-the-technical-co-founder-building-real-p.md` |
| #2968 | Night club | Technik & Alltag | `technik-alltag/2968-night-club.md` |
| #2969 | CLAUDE.md Generator for AI Coding Agents | Technik & Alltag | `technik-alltag/2969-claude-md-generator-for-ai-coding-agents.md` |
| #2970 | Prompt Generator for claude code | Technik & Alltag | `technik-alltag/2970-prompt-generator-for-claude-code.md` |
| #2971 | Scientific Paper Drafting for Analytical Data | Technik & Alltag | `technik-alltag/2971-scientific-paper-drafting-for-analytical.md` |
| #2972 | The Solar Priestess of Amun | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2972-the-solar-priestess-of-amun.md` |
| #2973 | Profile pic rebuild | Technik & Alltag | `technik-alltag/2973-profile-pic-rebuild.md` |
| #2974 | Morning coffee | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2974-morning-coffee.md` |
| #2975 | Young woman with bikini | Technik & Alltag | `technik-alltag/2975-young-woman-with-bikini.md` |
| #2976 | Draft PR to Ready to Review PR | Technik & Alltag | `technik-alltag/2976-draft-pr-to-ready-to-review-pr.md` |
| #2977 | Chinese to English Translation Proofreading Expert | Lernen & Wachstum | `lernen-wachstum/2977-chinese-to-english-translation-proofread.md` |
| #2978 | Hallucination Vulnerability Prompt Checker | Technik & Alltag | `technik-alltag/2978-hallucination-vulnerability-prompt-check.md` |
| #2979 | Meme coins knowledge  and trading | Technik & Alltag | `technik-alltag/2979-meme-coins-knowledge-and-trading.md` |
| #2980 | Womanized | Technik & Alltag | `technik-alltag/2980-womanized.md` |
| #2981 | Lead Data Analyst for Actionable Insights | Technik & Alltag | `technik-alltag/2981-lead-data-analyst-for-actionable-insight.md` |
| #2982 | ATS Resume Scanner Simulator | Beruf & Karriere | `beruf-karriere/2982-ats-resume-scanner-simulator.md` |
| #2983 | Resume Quality Reviewer – Green Flag Edition | Beruf & Karriere | `beruf-karriere/2983-resume-quality-reviewer-green-flag-editi.md` |
| #2984 | Dynamic Chinese Fire Horse Celebration | Kreativitaet & Freizeit | `kreativitaet-freizeit/2984-dynamic-chinese-fire-horse-celebration.md` |
| #2985 | Overqualification Narrative Architect | Technik & Alltag | `technik-alltag/2985-overqualification-narrative-architect.md` |
| #2986 | Table in PDF to CSV conversion | Technik & Alltag | `technik-alltag/2986-table-in-pdf-to-csv-conversion.md` |
| #2987 | Narrative Momentum Prediction Engine | Beruf & Karriere | `beruf-karriere/2987-narrative-momentum-prediction-engine.md` |
| #2988 | Aaa | Technik & Alltag | `technik-alltag/2988-aaa.md` |
| #2989 | Create Satirical and Bold Song Lyrics | Kreativitaet & Freizeit | `kreativitaet-freizeit/2989-create-satirical-and-bold-song-lyrics.md` |
| #2990 | Interactive Place Review Generator | Technik & Alltag | `technik-alltag/2990-interactive-place-review-generator.md` |
| #2991 | Minimalist Surveillance Illustration Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2991-minimalist-surveillance-illustration-pro.md` |
| #2992 | Vibrant Fauvist Style Sunlit Living Room Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2992-vibrant-fauvist-style-sunlit-living-room.md` |
| #2993 | Serene Moonlit Street Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2993-serene-moonlit-street-illustration.md` |
| #2994 | MoltPass Client -- Cryptographic Passport for AI Agents | Technik & Alltag | `technik-alltag/2994-moltpass-client-cryptographic-passport-f.md` |
| #2995 | LinkedIn JSON → Canonical Markdown Profile Generator | Technik & Alltag | `technik-alltag/2995-linkedin-json-canonical-markdown-profile.md` |
| #2996 | Master Podcast Producer & Sonic Storyteller | Kreativitaet & Freizeit | `kreativitaet-freizeit/2996-master-podcast-producer-sonic-storytelle.md` |
| #2997 | Cinematic Video Essay Director | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/2997-cinematic-video-essay-director.md` |
| #2998 | Micro-SaaS "Vibecoder" Architect | Technik & Alltag | `technik-alltag/2998-micro-saas-vibecoder-architect.md` |
| #2999 | The Ultimate Podcast Format & Audio Branding Architect | Technik & Alltag | `technik-alltag/2999-the-ultimate-podcast-format-audio-brandi.md` |
| #3000 | The Elite SEO Blog Architect & Ghostwriter | Technik & Alltag | `technik-alltag/3000-the-elite-seo-blog-architect-ghostwriter.md` |
| #3001 | Pina Colada Cocktail | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3001-pina-colada-cocktail.md` |
| #3002 | Senior Software Engineer  & Software Architect Rules | Technik & Alltag | `technik-alltag/3002-senior-software-engineer-software-archit.md` |
| #3003 | Test-First Bug Fixing Approach | Technik & Alltag | `technik-alltag/3003-test-first-bug-fixing-approach.md` |
| #3004 | Spring Boot + SOLID Specialist | Technik & Alltag | `technik-alltag/3004-spring-boot-solid-specialist.md` |
| #3005 | Autonomous Research & Data Analysis Agent | Alltag & Leben | `alltag-leben/3005-autonomous-research-data-analysis-agent.md` |
| #3006 | Symphony Event Invitation and Guide | Alltag & Leben | `alltag-leben/3006-symphony-event-invitation-and-guide.md` |
| #3007 | evento de sinfonía grupo 4 | Beruf & Karriere | `beruf-karriere/3007-evento-de-sinfon-a-grupo-4.md` |
| #3008 | Principal AI Code Reviewer + Senior Software Engineer / Architect Prompt | Technik & Alltag | `technik-alltag/3008-principal-ai-code-reviewer-senior-softwa.md` |
| #3009 | Photo shoot for branding | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3009-photo-shoot-for-branding.md` |
| #3010 | Market Pulse | Technik & Alltag | `technik-alltag/3010-market-pulse.md` |
| #3011 | Cruelty-Free Beauty Product Checker | Kommunikation & Beziehungen | `kommunikation-beziehungen/3011-cruelty-free-beauty-product-checker.md` |
| #3012 | Big 4 style report for retail traders - Enter the name and ticker of a U.S. publicly traded company. | Beruf & Karriere | `beruf-karriere/3012-big-4-style-report-for-retail-traders-en.md` |
| #3013 | Prompt for Humanizing AI Text (English Version) | Technik & Alltag | `technik-alltag/3013-prompt-for-humanizing-ai-text-english-ve.md` |
| #3014 | Learn Any Technical/Coding Topic | Technik & Alltag | `technik-alltag/3014-learn-any-technical-coding-topic.md` |
| #3015 | 30-Day Skill Mastery Challenge Prompt Template | Technik & Alltag | `technik-alltag/3015-30-day-skill-mastery-challenge-prompt-te.md` |
| #3016 | Voice Conversation Coach | Lernen & Wachstum | `lernen-wachstum/3016-voice-conversation-coach.md` |
| #3017 | Animated Weather Radar Map: Brescia Storm | Technik & Alltag | `technik-alltag/3017-animated-weather-radar-map-brescia-storm.md` |
| #3018 | Vintage Black and White Photograph of Galata Tower | Technik & Alltag | `technik-alltag/3018-vintage-black-and-white-photograph-of-ga.md` |
| #3019 | Minimalist Fisherman Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3019-minimalist-fisherman-illustration.md` |
| #3020 | Dramatic Digital Painting of a Solitary Figure in a Snowy Landscape | Technik & Alltag | `technik-alltag/3020-dramatic-digital-painting-of-solitary-fi.md` |
| #3021 | Python Code Performance & Quality Enhancer | Technik & Alltag | `technik-alltag/3021-python-code-performance-quality-enhancer.md` |
| #3022 | Career Intelligence Analyst | Beruf & Karriere | `beruf-karriere/3022-career-intelligence-analyst.md` |
| #3023 | Pre-Interview Intelligence Dossier | Technik & Alltag | `technik-alltag/3023-pre-interview-intelligence-dossier.md` |
| #3024 | Innovative Use Case Generator for New Tools | Technik & Alltag | `technik-alltag/3024-innovative-use-case-generator-for-new-to.md` |
| #3025 | Software Implementor AI Agent for Data Entry and Testing | Technik & Alltag | `technik-alltag/3025-software-implementor-ai-agent-for-data-e.md` |
| #3026 | CKEditor 5 Plugin | Technik & Alltag | `technik-alltag/3026-ckeditor-5-plugin.md` |
| #3027 | Ghibli style anime character | Kreativitaet & Freizeit | `kreativitaet-freizeit/3027-ghibli-style-anime-character.md` |
| #3028 | Python Code Generator — Clean, Optimized & Production-Ready | Technik & Alltag | `technik-alltag/3028-python-code-generator-clean-optimized-pr.md` |
| #3029 | Camp Planner | Technik & Alltag | `technik-alltag/3029-camp-planner.md` |
| #3030 | Preventive Health Report Clinical Evaluation Prompt | Technik & Alltag | `technik-alltag/3030-preventive-health-report-clinical-evalua.md` |
| #3031 | # ANTIGRAVITY GLOBAL RULES | Technik & Alltag | `technik-alltag/3031-antigravity-global-rules.md` |
| #3032 | Documentation Update Automation | Technik & Alltag | `technik-alltag/3032-documentation-update-automation.md` |
| #3033 | App Store Screenshots Gallery Generator | Technik & Alltag | `technik-alltag/3033-app-store-screenshots-gallery-generator.md` |
| #3034 | Build a Web3 Wallet on Playnance Blockchain | Technik & Alltag | `technik-alltag/3034-build-web3-wallet-on-playnance-blockchai.md` |
| #3035 | Dermatology Consultation Guide | Alltag & Leben | `alltag-leben/3035-dermatology-consultation-guide.md` |
| #3036 | The Fighter | Technik & Alltag | `technik-alltag/3036-the-fighter.md` |
| #3037 | Miniature Artist | Kreativitaet & Freizeit | `kreativitaet-freizeit/3037-miniature-artist.md` |
| #3038 | Skin care for acne and freckles | Beruf & Karriere | `beruf-karriere/3038-skin-care-for-acne-and-freckles.md` |
| #3039 | Heart Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3039-heart-illustration.md` |
| #3040 | Ball Puppet | Alltag & Leben | `alltag-leben/3040-ball-puppet.md` |
| #3041 | Barong 1 | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3041-barong-1.md` |
| #3042 | Barong 2 | Kreativitaet & Freizeit | `kreativitaet-freizeit/3042-barong-2.md` |
| #3043 | Minimax Music & Lyrics Generation | Kreativitaet & Freizeit | `kreativitaet-freizeit/3043-minimax-music-lyrics-generation.md` |
| #3044 | AI Grounding Prompt | Technik & Alltag | `technik-alltag/3044-ai-grounding-prompt.md` |
| #3045 | trial | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3045-trial.md` |
| #3046 | Test | Technik & Alltag | `technik-alltag/3046-test.md` |
| #3047 | Analyze code scanning security issues and dependency updates if vulnerable | Technik & Alltag | `technik-alltag/3047-analyze-code-scanning-security-issues-an.md` |
| #3048 | want to analyze security issues and vulnerabilities and fixes | Technik & Alltag | `technik-alltag/3048-want-to-analyze-security-issues-and-vuln.md` |
| #3049 | logo designer | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3049-logo-designer.md` |
| #3050 | security fixes cves | Technik & Alltag | `technik-alltag/3050-security-fixes-cves.md` |
| #3051 | security fixes | Technik & Alltag | `technik-alltag/3051-security-fixes.md` |
| #3052 | Boom & Crush - ICT strategy | Technik & Alltag | `technik-alltag/3052-boom-crush-ict-strategy.md` |
| #3053 | Alp Dağlarındasın | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3053-alp-da-lar-ndas-n.md` |
| #3054 | Ultra Realistic Cinematic Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3054-ultra-realistic-cinematic-portrait.md` |
| #3055 | High-Contrast Stencil Vector Poster Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3055-high-contrast-stencil-vector-poster-illu.md` |
| #3056 | KIDS DRESS DESIGN | Technik & Alltag | `technik-alltag/3056-kids-dress-design.md` |
| #3057 | TypeScript Unit Testing with Vitest | Technik & Alltag | `technik-alltag/3057-typescript-unit-testing-with-vitest.md` |
| #3058 | Master Storyteller and Sales Copywriter Prompt | Kreativitaet & Freizeit | `kreativitaet-freizeit/3058-master-storyteller-and-sales-copywriter-.md` |
| #3059 | Wicked | Technik & Alltag | `technik-alltag/3059-wicked.md` |
| #3060 | Advanced Sales Funnel App with React Flow | Technik & Alltag | `technik-alltag/3060-advanced-sales-funnel-app-with-react-flo.md` |
| #3061 | Clinical Research Presentation Guidance | Alltag & Leben | `alltag-leben/3061-clinical-research-presentation-guidance.md` |
| #3062 | change home page desgin for blog and documentation platorm | Technik & Alltag | `technik-alltag/3062-change-home-page-desgin-for-blog-and-doc.md` |
| #3063 | Butterfly | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3063-butterfly.md` |
| #3064 | Structured and Effective Learning Prompt | Technik & Alltag | `technik-alltag/3064-structured-and-effective-learning-prompt.md` |
| #3065 | TCRE Framework - AI Prompt Engineer | Technik & Alltag | `technik-alltag/3065-tcre-framework-ai-prompt-engineer.md` |
| #3066 | Information Gathering Prompt | Technik & Alltag | `technik-alltag/3066-information-gathering-prompt.md` |
| #3067 | chicks hatch | Technik & Alltag | `technik-alltag/3067-chicks-hatch.md` |
| #3068 | Wickedsmaht.fun | Technik & Alltag | `technik-alltag/3068-wickedsmaht-fun.md` |
| #3069 | HTWind-Widget-Creator | Technik & Alltag | `technik-alltag/3069-htwind-widget-creator.md` |
| #3070 | Transform the input product image into a professional commercial studio photograph | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3070-transform-input-product-image-into-profe.md` |
| #3071 | notebooklm_lecture_notes | Technik & Alltag | `technik-alltag/3071-notebooklm-lecture-notes.md` |
| #3072 | image to video 360 product rotaion | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3072-image-to-video-360-product-rotaion.md` |
| #3073 | Xh | Technik & Alltag | `technik-alltag/3073-xh.md` |
| #3074 | Train Waiter | Technik & Alltag | `technik-alltag/3074-train-waiter.md` |
| #3075 | Colored | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3075-colored.md` |
| #3076 | Abstract Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3076-abstract-portrait.md` |
| #3077 | Girls | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3077-girls.md` |
| #3078 | Steel Blueprint Infographic For SosMed | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3078-steel-blueprint-infographic-for-sosmed.md` |
| #3079 | Voice Cloning Attacks Infographic | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3079-voice-cloning-attacks-infographic.md` |
| #3080 | Agency Growth Bottleneck Identifier | Beruf & Karriere | `beruf-karriere/3080-agency-growth-bottleneck-identifier.md` |
| #3081 | Expert Discovery Interviewer Guide | Beruf & Karriere | `beruf-karriere/3081-expert-discovery-interviewer-guide.md` |
| #3082 | Landing Page Copy Architect – Conversion Framework Prompt | Technik & Alltag | `technik-alltag/3082-landing-page-copy-architect-conversion-f.md` |
| #3083 | Data Architect & Business Strategist (CSV Audit & Pipeline) | Technik & Alltag | `technik-alltag/3083-data-architect-business-strategist-csv-a.md` |
| #3084 | cambio de ojos | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3084-cambio-de-ojos.md` |
| #3085 | Strategy Consultant | Beruf & Karriere | `beruf-karriere/3085-strategy-consultant.md` |
| #3086 | Python Security Vulnerability Auditor (OWASP-Mapped & Production-Hardened) | Technik & Alltag | `technik-alltag/3086-python-security-vulnerability-auditor-ow.md` |
| #3087 | Make Flowers Bloom in an Image | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3087-make-flowers-bloom-in-image.md` |
| #3088 | AI Performance & Deep Testing Engineer | Technik & Alltag | `technik-alltag/3088-ai-performance-deep-testing-engineer.md` |
| #3089 | Make AI responses sound more Human-like | Lernen & Wachstum | `lernen-wachstum/3089-make-ai-responses-sound-more-human-like.md` |
| #3090 | Academic Paper Figure Generator - Nano Banana Pro | Technik & Alltag | `technik-alltag/3090-academic-paper-figure-generator-nano-ban.md` |
| #3091 | National safety week | Alltag & Leben | `alltag-leben/3091-national-safety-week.md` |
| #3092 | RNA-Seq Analysis and Differential Gene Expression | Alltag & Leben | `alltag-leben/3092-rna-seq-analysis-and-differential-gene-e.md` |
| #3093 | Comprehensive Guide to Gas-Fired Pool Heaters with Visuals | Alltag & Leben | `alltag-leben/3093-comprehensive-guide-to-gas-fired-pool-he.md` |
| #3094 | prompts.chat taste | Technik & Alltag | `technik-alltag/3094-prompts-chat-taste.md` |
| #3095 | Python Unit Test Generator — Comprehensive, Coverage-Mapped & Production-Ready | Technik & Alltag | `technik-alltag/3095-python-unit-test-generator-comprehensive.md` |
| #3096 | Mixed Media Portrait Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3096-mixed-media-portrait-illustration.md` |
| #3097 | Illustrative Hand-Drawn Istanbul Skyline Prompt | Technik & Alltag | `technik-alltag/3097-illustrative-hand-drawn-istanbul-skyline.md` |
| #3098 | Majestic Bald Eagle 3D Render Prompt | Technik & Alltag | `technik-alltag/3098-majestic-bald-eagle-3d-render-prompt.md` |
| #3099 | Writing a Book on Causes of Death from Data Sources | Technik & Alltag | `technik-alltag/3099-writing-book-on-causes-of-death-from-dat.md` |
| #3100 | Critical Thinking (DeepThink) | Technik & Alltag | `technik-alltag/3100-critical-thinking-deepthink.md` |
| #3101 | Corporate Intel Report | Technik & Alltag | `technik-alltag/3101-corporate-intel-report.md` |
| #3102 | Root Cause Architect (5 Whys Technique) | Technik & Alltag | `technik-alltag/3102-root-cause-architect-5-whys-technique.md` |
| #3103 | SciSim Pro - Simulator for science (ASCII/Textual Art spatial diagrams support) | Kreativitaet & Freizeit | `kreativitaet-freizeit/3103-scisim-pro-simulator-for-science-ascii-t.md` |
| #3104 | Expanded Company Intel Report | Technik & Alltag | `technik-alltag/3104-expanded-company-intel-report.md` |
| #3105 | Next.js | Technik & Alltag | `technik-alltag/3105-next-js.md` |
| #3106 | Job Posting Snapshot & Preservation Engine | Technik & Alltag | `technik-alltag/3106-job-posting-snapshot-preservation-engine.md` |
| #3107 | Code Translator — Idiomatic, Version-Aware & Production-Ready | Lernen & Wachstum | `lernen-wachstum/3107-code-translator-idiomatic-version-aware-.md` |
| #3108 | Fazer miniatura de coisas/moleculas | Lernen & Wachstum | `lernen-wachstum/3108-fazer-miniatura-de-coisas-moleculas.md` |
| #3109 | Prompts para metodos de estudo | Technik & Alltag | `technik-alltag/3109-prompts-para-metodos-de-estudo.md` |
| #3110 | calories diet | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/3110-calories-diet.md` |
| #3111 | Expert Technical Blog Writer Role | Technik & Alltag | `technik-alltag/3111-expert-technical-blog-writer-role.md` |
| #3112 | AI Kickstart prompt | Technik & Alltag | `technik-alltag/3112-ai-kickstart-prompt.md` |
| #3113 | Superhuman lab | Technik & Alltag | `technik-alltag/3113-superhuman-lab.md` |
| #3114 | Email Phishing and Cyber Attack Notification App | Technik & Alltag | `technik-alltag/3114-email-phishing-and-cyber-attack-notifica.md` |
| #3115 | One-Shot Copy-Paste Version with Proper Formatting | Technik & Alltag | `technik-alltag/3115-one-shot-copy-paste-version-with-proper-.md` |
| #3116 | studying for exam | Technik & Alltag | `technik-alltag/3116-studying-for-exam.md` |
| #3117 | trello-integration-skill | Technik & Alltag | `technik-alltag/3117-trello-integration-skill.md` |
| #3118 | Update Agent Permissions | Technik & Alltag | `technik-alltag/3118-update-agent-permissions.md` |
| #3119 | Fantasy Console Simulator | Kreativitaet & Freizeit | `kreativitaet-freizeit/3119-fantasy-console-simulator.md` |
| #3120 | Spec Interview | Technik & Alltag | `technik-alltag/3120-spec-interview.md` |
| #3121 | Writing Advisor Prompt | Technik & Alltag | `technik-alltag/3121-writing-advisor-prompt.md` |
| #3122 | Job Fit | Technik & Alltag | `technik-alltag/3122-job-fit.md` |
| #3123 | Angular Directive Generator | Technik & Alltag | `technik-alltag/3123-angular-directive-generator.md` |
| #3124 | explain like I am 8 | Technik & Alltag | `technik-alltag/3124-explain-like-i-am-8.md` |
| #3125 | Work on Linear Issue | Technik & Alltag | `technik-alltag/3125-work-on-linear-issue.md` |
| #3126 | YKS-YDT Vocabulary Acquisition Guide | Alltag & Leben | `alltag-leben/3126-yks-ydt-vocabulary-acquisition-guide.md` |
| #3127 | Dead Code Surgeon - Phased Codebase Audit & Cleanup Roadmap | Technik & Alltag | `technik-alltag/3127-dead-code-surgeon-phased-codebase-audit-.md` |
| #3128 | Spanish girl in nightclub | Technik & Alltag | `technik-alltag/3128-spanish-girl-in-nightclub.md` |
| #3129 | A hyper-realistic portrait of a graceful Indonesian woman in refined casual attire | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3129-a-hyper-realistic-portrait-of-graceful-i.md` |
| #3130 | Ultra-realistic cinematic studio portrait featuring a stylish woman with a curvy physique | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3130-ultra-realistic-cinematic-studio-portrai.md` |
| #3131 | Portrait of Indonesian Elegance | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3131-portrait-of-indonesian-elegance.md` |
| #3132 | A young Indonesian woman, appearing to be in her early twenties | Technik & Alltag | `technik-alltag/3132-a-young-indonesian-woman-appearing-to-be.md` |
| #3133 | A young woman sitting on the floor in a cozy, decorated room, taking a mirror selfie with a red phone. | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3133-a-young-woman-sitting-on-floor-in-cozy-d.md` |
| #3134 | Indonesian Woman with black dress | Technik & Alltag | `technik-alltag/3134-indonesian-woman-with-black-dress.md` |
| #3135 | Sari - Indonesian Woman in a Domestic Setting | Technik & Alltag | `technik-alltag/3135-sari-indonesian-woman-in-domestic-settin.md` |
| #3136 | Thoughtful Indonesian Portrait in a Cozy Kitchen | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3136-thoughtful-indonesian-portrait-in-cozy-k.md` |
| #3137 | Elegant Portrait of a Latina Woman | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3137-elegant-portrait-of-latina-woman.md` |
| #3138 | Graceful Latina Portrait in Fine Art Photography | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3138-graceful-latina-portrait-in-fine-art-pho.md` |
| #3139 | Wholesome Lifestyle Product Photography for Garment Showcase | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3139-wholesome-lifestyle-product-photography-.md` |
| #3140 | Professional Portrait Photography Guide | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3140-professional-portrait-photography-guide.md` |
| #3141 | Elegant and Serene Portrait Photography Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3141-elegant-and-serene-portrait-photography-.md` |
| #3142 | Confident Woman with Wavy Hair in Casual Attire | Technik & Alltag | `technik-alltag/3142-confident-woman-with-wavy-hair-in-casual.md` |
| #3143 | High-Fidelity Portrait of a Young Blonde Woman | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3143-high-fidelity-portrait-of-young-blonde-w.md` |
| #3144 | Photorealistic Apron Model Image Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3144-photorealistic-apron-model-image-prompt.md` |
| #3145 | Graceful Explorer in the Singaporean Rainforest | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3145-graceful-explorer-in-singaporean-rainfor.md` |
| #3146 | Photorealistic Lunar New Year Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3146-photorealistic-lunar-new-year-portrait.md` |
| #3147 | Photorealistic Lifestyle Portrait of a Creative Turkish Woman | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3147-photorealistic-lifestyle-portrait-of-cre.md` |
| #3148 | research and learn to become top in your field of knowledge | Technik & Alltag | `technik-alltag/3148-research-and-learn-to-become-top-in-your.md` |
| #3149 | Walking back home | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3149-walking-back-home.md` |
| #3150 | Comprehensive Go Codebase Review - Forensic-Level Analysis Prompt | Technik & Alltag | `technik-alltag/3150-comprehensive-go-codebase-review-forensi.md` |
| #3151 | Internal Linking SEO Assistant | Kommunikation & Beziehungen | `kommunikation-beziehungen/3151-internal-linking-seo-assistant.md` |
| #3152 | Elegant Indonesian Lifestyle Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3152-elegant-indonesian-lifestyle-portrait.md` |
| #3153 | Brainstorming Technically Grounded Product Ideas | Technik & Alltag | `technik-alltag/3153-brainstorming-technically-grounded-produ.md` |
| #3154 | Transform the provided clothing product image. | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3154-transform-provided-clothing-product-imag.md` |
| #3155 | Internet Trend & Slang Intelligence | Technik & Alltag | `technik-alltag/3155-internet-trend-slang-intelligence.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-10)

**9 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3156 | ComicPost | Lernen & Wachstum | `lernen-wachstum/3156-comicpost.md` |
| #3157 | Vibrant Outdoor Lifestyle Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3157-vibrant-outdoor-lifestyle-portrait.md` |
| #3158 | Joyful Indonesian Outdoor Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3158-joyful-indonesian-outdoor-portrait.md` |
| #3159 | Elegant Indonesian Woman Studio Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3159-elegant-indonesian-woman-studio-portrait.md` |
| #3160 | Elegant Urban Portrait of Indonesian Woman | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3160-elegant-urban-portrait-of-indonesian-wom.md` |
| #3161 | library migration | Technik & Alltag | `technik-alltag/3161-library-migration.md` |
| #3162 | Operating systems | Lernen & Wachstum | `lernen-wachstum/3162-operating-systems.md` |
| #3163 | Stripe Payment Builder | Beruf & Karriere | `beruf-karriere/3163-stripe-payment-builder.md` |
| #3164 | SQL Query Builder & Optimiser | Technik & Alltag | `technik-alltag/3164-sql-query-builder-optimiser.md` |


---

## PromptHero Bild-Prompt Import (2026-03-10)

**50 neue Bild-Prompts** importiert (Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):

| ID | Titel | Modell | Datei |
|----|-------|--------|-------|
| #3165 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/3165-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #3166 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3166-candid-photo-of-a-middle-aged-woman-with.md` |
| #3167 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3167-large-format-photo-of-a-middle-aged-woma.md` |
| #3168 | "paparazzi photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/3168-paparazzi-photo-of-a-young-man-wearing-a.md` |
| #3169 | "paparazzi photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/3169-paparazzi-photo-of-a-young-man-wearing-a.md` |
| #3170 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3170-high-fashion-photo-of-a-elderly-man-with.md` |
| #3171 | "large format photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3171-large-format-photo-of-a-child-with-a-cut.md` |
| #3172 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3172-high-fashion-photo-of-a-middle-aged-woma.md` |
| #3173 | "beauty photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/3173-beauty-photo-of-a-child-with-a-cute-expr.md` |
| #3174 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3174-high-fashion-photo-of-a-middle-aged-woma.md` |
| #3175 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3175-analog-photo-of-a-middle-aged-woman-with.md` |
| #3176 | "beauty photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3176-beauty-photo-of-a-young-man-wearing-a-su.md` |
| #3177 | "pictorialist photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3177-pictorialist-photo-of-a-child-with-a-cut.md` |
| #3178 | "candid photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3178-candid-photo-of-a-young-man-wearing-a-su.md` |
| #3179 | "paparazzi photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/3179-paparazzi-photo-of-a-elderly-man-with-a-.md` |
| #3180 | "lifestyle photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/3180-lifestyle-photo-of-a-teenage-girl-with-s.md` |
| #3181 | "beauty photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3181-beauty-photo-of-a-middle-aged-woman-with.md` |
| #3182 | "large format photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/3182-large-format-photo-of-a-young-man-wearin.md` |
| #3183 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3183-high-fashion-photo-of-a-elderly-man-with.md` |
| #3184 | "paparazzi photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/3184-paparazzi-photo-of-a-middle-aged-woman-w.md` |
| #3185 | "Analog photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/3185-analog-photo-of-a-elderly-man-with-a-bea.md` |
| #3186 | "beauty photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/3186-beauty-photo-of-a-elderly-man-with-a-bea.md` |
| #3187 | "instant photo of a middle-aged woman wi | SDXL | `bildbearbeitung-visualisierung/3187-instant-photo-of-a-middle-aged-woman-wit.md` |
| #3188 | "pictorialist photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3188-pictorialist-photo-of-a-child-with-a-cut.md` |
| #3189 | "instant photo of a middle-aged woman wi | SDXL | `bildbearbeitung-visualisierung/3189-instant-photo-of-a-middle-aged-woman-wit.md` |
| #3190 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/3190-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #3191 | "glamor photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3191-glamor-photo-of-a-middle-aged-woman-with.md` |
| #3192 | "beauty photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/3192-beauty-photo-of-a-teenage-girl-with-shor.md` |
| #3193 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3193-high-fashion-photo-of-a-middle-aged-woma.md` |
| #3194 | "beauty photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/3194-beauty-photo-of-a-teenage-girl-with-shor.md` |
| #3195 | "glamor photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3195-glamor-photo-of-a-young-man-wearing-a-su.md` |
| #3196 | "pictorialist photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3196-pictorialist-photo-of-a-elderly-man-with.md` |
| #3197 | "large format photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3197-large-format-photo-of-a-child-with-a-cut.md` |
| #3198 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3198-large-format-photo-of-a-middle-aged-woma.md` |
| #3199 | "beauty photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/3199-beauty-photo-of-a-teenage-girl-with-shor.md` |
| #3200 | "beauty photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3200-beauty-photo-of-a-young-man-wearing-a-su.md` |
| #3201 | "beauty photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/3201-beauty-photo-of-a-teenage-girl-with-shor.md` |
| #3202 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3202-high-fashion-photo-of-a-child-with-a-cut.md` |
| #3203 | "large format photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/3203-large-format-photo-of-a-teenage-girl-wit.md` |
| #3204 | "large format photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3204-large-format-photo-of-a-elderly-man-with.md` |
| #3205 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3205-analog-photo-of-a-young-man-wearing-a-su.md` |
| #3206 | "pictorialist photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3206-pictorialist-photo-of-a-elderly-man-with.md` |
| #3207 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/3207-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #3208 | "lifestyle photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/3208-lifestyle-photo-of-a-elderly-man-with-a-.md` |
| #3209 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3209-candid-photo-of-a-middle-aged-woman-with.md` |
| #3210 | "Analog photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/3210-analog-photo-of-a-child-with-a-cute-expr.md` |
| #3211 | "beauty photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3211-beauty-photo-of-a-middle-aged-woman-with.md` |
| #3212 | "paparazzi photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/3212-paparazzi-photo-of-a-child-with-a-cute-e.md` |
| #3213 | "Analog photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/3213-analog-photo-of-a-teenage-girl-with-shor.md` |
| #3214 | "lifestyle photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/3214-lifestyle-photo-of-a-elderly-man-with-a-.md` |


---

## Multi-Source Import (2026-03-10)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #3215 | A poem about a pepper plant | Alltag & Leben |
| #3216 | A guide to filing taxes for small businesses  | Alltag & Leben |
| #3217 | Background | Alltag & Leben |
| #3218 | What is the origin of the term "supper" used  | Alltag & Leben |
| #3219 | A guide on how to style a basic black t-shirt | Alltag & Leben |
| #3220 | A recipe for a delicious barbeque sauce that  | Alltag & Leben |
| #3221 | You will be given a definition of a task firs | Beruf & Karriere |
| #3222 | Teacher:In this task, you are given a sentenc | Beruf & Karriere |
| #3223 | Given the task definition and input, reply wi | Beruf & Karriere |
| #3224 | You will be given a definition of a task firs | Beruf & Karriere |
| #3225 | Write an email to my manager Adam and my prod | Beruf & Karriere |
| #3226 | I would like to start a quantitative futures  | Beruf & Karriere |
| #3227 | What is lysine | Gesundheit & Wohlbefinden |
| #3228 | Reference:
<start of reference>
I wanted to b | Gesundheit & Wohlbefinden |
| #3229 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #3230 | An incorrect answer to the given question bas | Gesundheit & Wohlbefinden |
| #3231 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #3232 | An overlapping word between the given two sen | Gesundheit & Wohlbefinden |
| #3233 | What are some examples of overheard conversat | Kommunikation & Beziehungen |
| #3234 | Detailed Instructions: In this task | Kommunikation & Beziehungen |
| #3235 | In this task | Kommunikation & Beziehungen |
| #3236 | You are given a sentence | Kommunikation & Beziehungen |
| #3237 | Definition: Classify the relation of question | Kommunikation & Beziehungen |
| #3238 | You will be given a definition of a task firs | Kommunikation & Beziehungen |
| #3239 | Imagine that you are a hat | Kreativitaet & Freizeit |
| #3240 | A short story about a young woman who takes a | Kreativitaet & Freizeit |
| #3241 | Given this background information | Kreativitaet & Freizeit |
| #3242 | Reference:
Do you know what whole fields are | Kreativitaet & Freizeit |
| #3243 | Teacher:In this task | Kreativitaet & Freizeit |
| #3244 | Detailed Instructions: You are given a senten | Kreativitaet & Freizeit |
| #3245 | What are some examples of songs that were hit | Lernen & Wachstum |
| #3246 | What are some examples of restrictions in com | Lernen & Wachstum |
| #3247 | A poem about a pavilion in a park that is in  | Lernen & Wachstum |
| #3248 | Reference | Lernen & Wachstum |
| #3249 | What are some of the most popular books that  | Lernen & Wachstum |
| #3250 | Consider this reference information delimited | Lernen & Wachstum |
| #3251 | Act as if you are a Buddhist monk who just fo | Spezielle Situationen |
| #3252 | Definition: You are given a sentence | Spezielle Situationen |
| #3253 | Q: You are given a sentence | Spezielle Situationen |
| #3254 | Definition: Generate an overlapping word betw | Spezielle Situationen |
| #3255 | An overlapping word between the given two sen | Spezielle Situationen |
| #3256 | Given the task definition | Spezielle Situationen |
| #3257 | What are some examples of software testing me | Technik & Alltag |
| #3258 | You will be given a definition of a task firs | Technik & Alltag |
| #3259 | Given the task definition and input, reply wi | Technik & Alltag |
| #3260 | Detailed Instructions: You will be given two  | Technik & Alltag |
| #3261 | In this task, you are given a sentence | Technik & Alltag |
| #3262 | You will be given a definition of a task firs | Technik & Alltag |
| #3263 | What are some examples of wedding invitation  | Alltag & Leben |
| #3264 | You will be given a definition of a task firs | Alltag & Leben |

</details>


---

## Multi-Source Import (2026-03-10)

**500 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 79 |
| Beruf & Karriere | 50 |
| Gesundheit & Wohlbefinden | 61 |
| Kommunikation & Beziehungen | 62 |
| Kreativitaet & Freizeit | 62 |
| Lernen & Wachstum | 62 |
| Spezielle Situationen | 62 |
| Technik & Alltag | 62 |

<details><summary>Alle 500 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #3265 | In this task, you're given a context, a sente | Alltag & Leben |
| #3266 | An incorrect answer to the given question bas | Alltag & Leben |
| #3267 | An incorrect answer to the given question bas | Alltag & Leben |
| #3268 | An overlapping word between the given two sen | Alltag & Leben |
| #3269 | Instruction | Alltag & Leben |
| #3270 | Detailed Instructions: In this task | Alltag & Leben |
| #3271 | Detailed Instructions: In this task | Alltag & Leben |
| #3272 | Instruction | Alltag & Leben |
| #3273 | Part 1. Definition | Alltag & Leben |
| #3274 | You are given a question or fill-in-the-blank | Alltag & Leben |
| #3275 | Given a sentence, generate a most unlikely ne | Alltag & Leben |
| #3276 | Given a sentence, generate a most unlikely ne | Alltag & Leben |
| #3277 | Given a sentence, generate a most unlikely ne | Alltag & Leben |
| #3278 | Given a sentence, generate a most unlikely ne | Alltag & Leben |
| #3279 | Instruction | Alltag & Leben |
| #3280 | In this task, you are given a sentence and a  | Alltag & Leben |
| #3281 | In this task, you are given a sentence and a  | Alltag & Leben |
| #3282 | Detailed Instructions: In this task | Alltag & Leben |
| #3283 | In this task, you are given a sentence and a  | Alltag & Leben |
| #3284 | An answer is given | Alltag & Leben |
| #3285 | An answer is given | Alltag & Leben |
| #3286 | Definition: In this task | Alltag & Leben |
| #3287 | In this task | Alltag & Leben |
| #3288 | In this task | Alltag & Leben |
| #3289 | In this task | Alltag & Leben |
| #3290 | Teacher: In this task | Alltag & Leben |
| #3291 | Teacher:In this task | Alltag & Leben |
| #3292 | In this task | Alltag & Leben |
| #3293 | You will be given a definition of a task firs | Alltag & Leben |
| #3294 | In this task | Alltag & Leben |
| #3295 | Instruction | Alltag & Leben |
| #3296 | Detailed Instructions: Given a sentence and a | Alltag & Leben |
| #3297 | Teacher:Given a sentence and an entity | Alltag & Leben |
| #3298 | TASK DEFINITION: In this task | Alltag & Leben |
| #3299 | Detailed Instructions: Construct a question t | Alltag & Leben |
| #3300 | Construct a question that every answer in the | Alltag & Leben |
| #3301 | Construct a question that every answer in the | Alltag & Leben |
| #3302 | You are experienced travel agent and travel a | Alltag & Leben |
| #3303 | You're a travel planning expert who needs to  | Alltag & Leben |
| #3304 | For my vacation rental business, Susan acts a | Alltag & Leben |
| #3305 | To write a children's book about a little mel | Alltag & Leben |
| #3306 | A girl has just as many sisters as brothers | Alltag & Leben |
| #3307 | Plan an extensive trip in new york | Alltag & Leben |
| #3308 | I received the following User Story to work o | Alltag & Leben |
| #3309 | What famous American landmark was a gift from | Alltag & Leben |
| #3310 | Have a monthy one month is 31 day price of 17 | Alltag & Leben |
| #3311 | Give stream of consciousness and then the fin | Alltag & Leben |
| #3312 | Given the list of ingredients | Alltag & Leben |
| #3313 | Provide a step-by-step explanation of how bri | Alltag & Leben |
| #3314 | What should a home gardener be aware of when  | Alltag & Leben |
| #3315 | Imagine you are a personal assistant planning | Alltag & Leben |
| #3316 | A city is planning to build a network of bicy | Alltag & Leben |
| #3317 | A story that includes the following words: va | Alltag & Leben |
| #3318 | A group of people are planning a road trip | Alltag & Leben |
| #3319 | In a certain city, there are 50,000 household | Alltag & Leben |
| #3320 | Let’s play a game | Alltag & Leben |
| #3321 | Sarah is baking cookies with her sister, Emil | Alltag & Leben |
| #3322 | A red house is made of red bricks | Alltag & Leben |
| #3323 | List five renowned botanical gardens around t | Alltag & Leben |
| #3324 | Describe three classic cocktail recipes | Alltag & Leben |
| #3325 | When looking for a non perishable food in you | Alltag & Leben |
| #3326 | At a train station | Alltag & Leben |
| #3327 | You need to ensure that an Azure | Beruf & Karriere |
| #3328 | What are some common objections clients have  | Beruf & Karriere |
| #3329 | Me a simple outline for a handmade furniture  | Beruf & Karriere |
| #3330 | You to act as a professional essay writer who | Beruf & Karriere |
| #3331 | You are an expert in nonprofit research with  | Beruf & Karriere |
| #3332 | Could you provide some references related wit | Beruf & Karriere |
| #3333 | Who is the leading mentors that teach how to  | Beruf & Karriere |
| #3334 | What does Richard D | Beruf & Karriere |
| #3335 | Write an email sequence I can use for new roo | Beruf & Karriere |
| #3336 | A company has 500 employees | Beruf & Karriere |
| #3337 | A company has 120 employees | Beruf & Karriere |
| #3338 | I have a meeting on March 27th | Beruf & Karriere |
| #3339 | Analyze why the given company's stock price p | Beruf & Karriere |
| #3340 | To play a game | Beruf & Karriere |
| #3341 | A solution in Go for the following task: Mink | Beruf & Karriere |
| #3342 | Target outcome: Accelerating neural networks  | Beruf & Karriere |
| #3343 | In the context of international relations | Beruf & Karriere |
| #3344 | If a business consistently shows a profit mar | Beruf & Karriere |
| #3345 | Born in the 1960s in California | Beruf & Karriere |
| #3346 | What's a reality that professional athletes w | Beruf & Karriere |
| #3347 | In control systems, what does the term "Bode  | Beruf & Karriere |
| #3348 | Python code to solve the task:
Chef gives an  | Beruf & Karriere |
| #3349 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3350 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3351 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3352 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3353 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3354 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3355 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3356 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3357 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3358 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3359 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3360 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3361 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3362 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3363 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3364 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3365 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3366 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3367 | Solve the following math problem step-by-step | Beruf & Karriere |
| #3368 | Dirty Sexy Knights in Paris is the only major | Beruf & Karriere |
| #3369 | How is "SETimes: How is Kosovo surviving the  | Beruf & Karriere |
| #3370 | An iranian lawmaker on tuesday called for a m | Beruf & Karriere |
| #3371 | Translate to German:

on behalf of the EFD Gr | Beruf & Karriere |
| #3372 | How to handle being in love with two people<b | Beruf & Karriere |
| #3373 | A short summary this sentence:
atlanta - what | Beruf & Karriere |
| #3374 | Q:What key details about travis jackson  can  | Beruf & Karriere |
| #3375 | Answer a question about the following article | Beruf & Karriere |
| #3376 | An article based on this summary | Beruf & Karriere |
| #3377 | You will be given two questions | Gesundheit & Wohlbefinden |
| #3378 | In this task, you are given a sentence | Gesundheit & Wohlbefinden |
| #3379 | In this task, you are given a sentence | Gesundheit & Wohlbefinden |
| #3380 | You will be given a definition of a task firs | Gesundheit & Wohlbefinden |
| #3381 | In this task, you are given a sentence | Gesundheit & Wohlbefinden |
| #3382 | In this task, you are given a sentence | Gesundheit & Wohlbefinden |
| #3383 | In this task, you are given a sentence | Gesundheit & Wohlbefinden |
| #3384 | Teacher:In this task, you are given a sentenc | Gesundheit & Wohlbefinden |
| #3385 | In this task, you are given a sentence | Gesundheit & Wohlbefinden |
| #3386 | You will be given a definition of a task firs | Gesundheit & Wohlbefinden |
| #3387 | Given a sentence with a missing word | Gesundheit & Wohlbefinden |
| #3388 | Classify the relation of question with contex | Gesundheit & Wohlbefinden |
| #3389 | Classify the relation of question with contex | Gesundheit & Wohlbefinden |
| #3390 | You will be given a definition of a task firs | Gesundheit & Wohlbefinden |
| #3391 | Classify the relation of question with contex | Gesundheit & Wohlbefinden |
| #3392 | Classify the relation of question with contex | Gesundheit & Wohlbefinden |
| #3393 | You will be given a definition of a task firs | Gesundheit & Wohlbefinden |
| #3394 | Q: Classify the relation of question with con | Gesundheit & Wohlbefinden |
| #3395 | Classify the relation of question with contex | Gesundheit & Wohlbefinden |
| #3396 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #3397 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #3398 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #3399 | Given a category and a set of five words | Gesundheit & Wohlbefinden |
| #3400 | Detailed Instructions: The input is taken fro | Gesundheit & Wohlbefinden |
| #3401 | You will be given a definition of a task firs | Gesundheit & Wohlbefinden |
| #3402 | In this task | Gesundheit & Wohlbefinden |
| #3403 | Detailed Instructions: Given a paragraph in S | Gesundheit & Wohlbefinden |
| #3404 | Acording to (text from:https://www | Gesundheit & Wohlbefinden |
| #3405 | You are a top tier marketing expert that coac | Gesundheit & Wohlbefinden |
| #3406 | At the beginning of the training | Gesundheit & Wohlbefinden |
| #3407 | A comment on a Reddit post about the easiest/ | Gesundheit & Wohlbefinden |
| #3408 | Do you have any other ideas to deal with the  | Gesundheit & Wohlbefinden |
| #3409 | What is the difference between t-shirt sizing | Gesundheit & Wohlbefinden |
| #3410 | What can run but never walks | Gesundheit & Wohlbefinden |
| #3411 | Tell me a bit of interesting | Gesundheit & Wohlbefinden |
| #3412 | Marine life and oceanography are closely inte | Gesundheit & Wohlbefinden |
| #3413 | A product description for a revolutionary hom | Gesundheit & Wohlbefinden |
| #3414 | In a group of 45 people, 30% prefer tea while | Gesundheit & Wohlbefinden |
| #3415 | Which former U | Gesundheit & Wohlbefinden |
| #3416 | Is it healthier to eat six small meals a day  | Gesundheit & Wohlbefinden |
| #3417 | Metallurgy involves the study of physical and | Gesundheit & Wohlbefinden |
| #3418 | A person who is exposed to a traumatic event  | Gesundheit & Wohlbefinden |
| #3419 | Oceanography | Gesundheit & Wohlbefinden |
| #3420 | The Amazon rainforest | Gesundheit & Wohlbefinden |
| #3421 | In Clinical Psychology | Gesundheit & Wohlbefinden |
| #3422 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3423 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3424 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3425 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3426 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3427 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3428 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3429 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3430 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3431 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3432 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3433 | Solve the following math problem step-by-step | Gesundheit & Wohlbefinden |
| #3434 | Process:  - The pancreas detects chemical cha | Gesundheit & Wohlbefinden |
| #3435 | 1 week ago 20:34 redtube masturbation | Gesundheit & Wohlbefinden |
| #3436 | What is a question about this article | Gesundheit & Wohlbefinden |
| #3437 | Answer the following question: I have a new s | Gesundheit & Wohlbefinden |
| #3438 | You will be given a definition of a task firs | Kommunikation & Beziehungen |
| #3439 | Given the task definition and input, reply wi | Kommunikation & Beziehungen |
| #3440 | You will be given a definition of a task firs | Kommunikation & Beziehungen |
| #3441 | Given a sentence and an entity | Kommunikation & Beziehungen |
| #3442 | You will be given a definition of a task firs | Kommunikation & Beziehungen |
| #3443 | Teacher: Given a sentence and an entity | Kommunikation & Beziehungen |
| #3444 | Reword the paragraph below so its more compel | Kommunikation & Beziehungen |
| #3445 | Ou can only respond with the word "True" or " | Kommunikation & Beziehungen |
| #3446 | Help me in how to Run a social media contest  | Kommunikation & Beziehungen |
| #3447 | Can you respond to this in a similar voice an | Kommunikation & Beziehungen |
| #3448 | How to write a facebook caption about my 1st  | Kommunikation & Beziehungen |
| #3449 | To answer for an question | Kommunikation & Beziehungen |
| #3450 | I would like to start a podcast | Kommunikation & Beziehungen |
| #3451 | Here are common issues in dispute between hom | Kommunikation & Beziehungen |
| #3452 | Write an email complaining about damage done  | Kommunikation & Beziehungen |
| #3453 | Lets make a medication list app that shows a  | Kommunikation & Beziehungen |
| #3454 | A customer wants to return a product they pur | Kommunikation & Beziehungen |
| #3455 | Give me some feedback so that I can improve m | Kommunikation & Beziehungen |
| #3456 | Help coming up with script ideas for a youtub | Kommunikation & Beziehungen |
| #3457 | Design a 12 week week social media campaign t | Kommunikation & Beziehungen |
| #3458 | How much better can a food advertisement look | Kommunikation & Beziehungen |
| #3459 | Design a marketing campaign for a fictional l | Kommunikation & Beziehungen |
| #3460 | I am the CEO of a silicon valley technology s | Kommunikation & Beziehungen |
| #3461 | I got this email:

Hi Guy,

How are things go | Kommunikation & Beziehungen |
| #3462 | A regular expression that can match a valid e | Kommunikation & Beziehungen |
| #3463 | Context: Japan participated in World War I fr | Kommunikation & Beziehungen |
| #3464 | I would like to use apatchee ignite messaging | Kommunikation & Beziehungen |
| #3465 | In music theory, what does the term "counterp | Kommunikation & Beziehungen |
| #3466 | Media studies often examine the effects of ma | Kommunikation & Beziehungen |
| #3467 | In the realm of communication studies | Kommunikation & Beziehungen |
| #3468 | In the realm of philosophy | Kommunikation & Beziehungen |
| #3469 | In aerospace engineering | Kommunikation & Beziehungen |
| #3470 | In the field of communication studies | Kommunikation & Beziehungen |
| #3471 | In supply chain management | Kommunikation & Beziehungen |
| #3472 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3473 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3474 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3475 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3476 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3477 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3478 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3479 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3480 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3481 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3482 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3483 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3484 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3485 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3486 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3487 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3488 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3489 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3490 | Solve the following math problem step-by-step | Kommunikation & Beziehungen |
| #3491 | Answer the following question: Title: Custome | Kommunikation & Beziehungen |
| #3492 | Here is a review left by a customer on a prod | Kommunikation & Beziehungen |
| #3493 | Paragraph: The side of Malaquez's parcel gave | Kommunikation & Beziehungen |
| #3494 | Q:Build a movie plot around this: Who kills A | Kommunikation & Beziehungen |
| #3495 | Process: - The saliva breaks down the chemica | Kommunikation & Beziehungen |
| #3496 | An article with the title: "Donald Trump hurl | Kommunikation & Beziehungen |
| #3497 | Is the sentiment of the following sentence po | Kommunikation & Beziehungen |
| #3498 | A 3-star review (1 being lowest and 5 being h | Kommunikation & Beziehungen |
| #3499 | An article based on this "Germany's Bayer has | Kommunikation & Beziehungen |
| #3500 | Detailed Instructions: In this task | Kreativitaet & Freizeit |
| #3501 | Part 1. Definition | Kreativitaet & Freizeit |
| #3502 | In this task, you're given a context, a sente | Kreativitaet & Freizeit |
| #3503 | In this task, you're given a context, a sente | Kreativitaet & Freizeit |
| #3504 | Teacher:In this task | Kreativitaet & Freizeit |
| #3505 | Detailed Instructions: In this task | Kreativitaet & Freizeit |
| #3506 | In this task, you're given a context, a sente | Kreativitaet & Freizeit |
| #3507 | Given the task definition and input, reply wi | Kreativitaet & Freizeit |
| #3508 | Given the task definition and input, reply wi | Kreativitaet & Freizeit |
| #3509 | You will be given two questions | Kreativitaet & Freizeit |
| #3510 | Definition: You will be given two questions | Kreativitaet & Freizeit |
| #3511 | You will be given two questions | Kreativitaet & Freizeit |
| #3512 | You will be given two questions | Kreativitaet & Freizeit |
| #3513 | You will be given a definition of a task firs | Kreativitaet & Freizeit |
| #3514 | In this task, you are given a sentence and a  | Kreativitaet & Freizeit |
| #3515 | In this task | Kreativitaet & Freizeit |
| #3516 | Given the task definition | Kreativitaet & Freizeit |
| #3517 | Detailed Instructions: You are given a questi | Kreativitaet & Freizeit |
| #3518 | Given a sentence, generate a most unlikely ne | Kreativitaet & Freizeit |
| #3519 | Given the task definition and input, reply wi | Kreativitaet & Freizeit |
| #3520 | Definition: An answer is given | Kreativitaet & Freizeit |
| #3521 | Teacher: Given a text passage | Kreativitaet & Freizeit |
| #3522 | Teacher:Given a text passage | Kreativitaet & Freizeit |
| #3523 | Definition: Given a text passage | Kreativitaet & Freizeit |
| #3524 | Q: Given a text passage, come up with an appr | Kreativitaet & Freizeit |
| #3525 | Part 1. Definition | Kreativitaet & Freizeit |
| #3526 | Q: In this task | Kreativitaet & Freizeit |
| #3527 | You will be given a definition of a task firs | Kreativitaet & Freizeit |
| #3528 | Detailed Instructions: The input is taken fro | Kreativitaet & Freizeit |
| #3529 | Instructions: The input is taken from a negot | Kreativitaet & Freizeit |
| #3530 | Teacher:The input is taken from a negotiation | Kreativitaet & Freizeit |
| #3531 | Detailed Instructions: Given a paragraph in S | Kreativitaet & Freizeit |
| #3532 | Detailed Instructions: Given a paragraph in S | Kreativitaet & Freizeit |
| #3533 | Given a paragraph in Spanish | Kreativitaet & Freizeit |
| #3534 | Me an ad for a drum book called Time Initiati | Kreativitaet & Freizeit |
| #3535 | A story about a bisexual princess is hiding s | Kreativitaet & Freizeit |
| #3536 | A short story about a man and his friend from | Kreativitaet & Freizeit |
| #3537 | Web search results | Kreativitaet & Freizeit |
| #3538 | I'm about to rewrite the headline for Shopify | Kreativitaet & Freizeit |
| #3539 | A one-page dystopian short story set 100 year | Kreativitaet & Freizeit |
| #3540 | To simulate a conversation between two charac | Kreativitaet & Freizeit |
| #3541 | You are going to pretend to be Jenn | Kreativitaet & Freizeit |
| #3542 | A story about a woman dealing with the strife | Kreativitaet & Freizeit |
| #3543 | How do you think about Katurian | Kreativitaet & Freizeit |
| #3544 | Create a function that take a string and extr | Kreativitaet & Freizeit |
| #3545 | You to implement the Levenberg-Mardquart algo | Kreativitaet & Freizeit |
| #3546 | How do i write a function that is runnable wi | Kreativitaet & Freizeit |
| #3547 | Make a story using as many phrasal verbs with | Kreativitaet & Freizeit |
| #3548 | To create a function that merges consecutive  | Kreativitaet & Freizeit |
| #3549 | Craft a full-fledged stratagem to crack the l | Kreativitaet & Freizeit |
| #3550 | Imagine you are a detective trying to solve a | Kreativitaet & Freizeit |
| #3551 | Pretend to be someone working at a nail salon | Kreativitaet & Freizeit |
| #3552 | In 2020, which Grammy-winning singer-songwrit | Kreativitaet & Freizeit |
| #3553 | Pretend you are a manager at work and you nee | Kreativitaet & Freizeit |
| #3554 | Michael has 20 books consisting of 5 differen | Kreativitaet & Freizeit |
| #3555 | Compose a magical realism narrative set in a  | Kreativitaet & Freizeit |
| #3556 | A script for a scene from The Office where Mi | Kreativitaet & Freizeit |
| #3557 | Sean Patrick Hayes (born June 26 | Kreativitaet & Freizeit |
| #3558 | Based on the given excerpt | Kreativitaet & Freizeit |
| #3559 | Coloring the edges of a complete graph with n | Kreativitaet & Freizeit |
| #3560 | What's the highest grossing movie of all time | Kreativitaet & Freizeit |
| #3561 | Why did the first-person perspective become p | Kreativitaet & Freizeit |
| #3562 | You are given a sentence | Lernen & Wachstum |
| #3563 | Teacher: You are given a sentence | Lernen & Wachstum |
| #3564 | Instruction | Lernen & Wachstum |
| #3565 | An incorrect answer to the given question bas | Lernen & Wachstum |
| #3566 | Definition: Write an incorrect answer to the  | Lernen & Wachstum |
| #3567 | An incorrect answer to the given question bas | Lernen & Wachstum |
| #3568 | Teacher: Write an incorrect answer to the giv | Lernen & Wachstum |
| #3569 | Teacher:Generate an overlapping word between  | Lernen & Wachstum |
| #3570 | An overlapping word between the given two sen | Lernen & Wachstum |
| #3571 | Given the task definition | Lernen & Wachstum |
| #3572 | Given the task definition | Lernen & Wachstum |
| #3573 | In this task, you are given a question and an | Lernen & Wachstum |
| #3574 | In this task, you are given a question and an | Lernen & Wachstum |
| #3575 | Detailed Instructions: Given a sentence in th | Lernen & Wachstum |
| #3576 | Given a sentence in the Japanese | Lernen & Wachstum |
| #3577 | Part 1. Definition | Lernen & Wachstum |
| #3578 | Given the task definition and input, reply wi | Lernen & Wachstum |
| #3579 | Given a sentence in the Japanese | Lernen & Wachstum |
| #3580 | Given a sentence in the Japanese | Lernen & Wachstum |
| #3581 | Given a sentence in the Japanese | Lernen & Wachstum |
| #3582 | You will be given a definition of a task firs | Lernen & Wachstum |
| #3583 | Detailed Instructions: Given a sentence in th | Lernen & Wachstum |
| #3584 | You will be given a definition of a task firs | Lernen & Wachstum |
| #3585 | Teacher:Given a sentence with a missing word | Lernen & Wachstum |
| #3586 | In this task, you're given five sentences, nu | Lernen & Wachstum |
| #3587 | In this task, you're given five sentences, nu | Lernen & Wachstum |
| #3588 | In this task, you're given five sentences, nu | Lernen & Wachstum |
| #3589 | Teacher: In this task | Lernen & Wachstum |
| #3590 | Given the task definition | Lernen & Wachstum |
| #3591 | In this task, you're given five sentences, nu | Lernen & Wachstum |
| #3592 | Instructions: In this task | Lernen & Wachstum |
| #3593 | In this task, you're given five sentences, nu | Lernen & Wachstum |
| #3594 | Instructions: In this task | Lernen & Wachstum |
| #3595 | You are given a sentence in Polish | Lernen & Wachstum |
| #3596 | Teacher: You are given a sentence in Polish | Lernen & Wachstum |
| #3597 | In this task, you need to Translate Czech tex | Lernen & Wachstum |
| #3598 | Teacher:In this task, you need to Translate C | Lernen & Wachstum |
| #3599 | Teacher:In this task | Lernen & Wachstum |
| #3600 | In this task | Lernen & Wachstum |
| #3601 | Teacher:In this task | Lernen & Wachstum |
| #3602 | Teacher:You are given a question or fill-in-t | Lernen & Wachstum |
| #3603 | Teacher: Given a sentence | Lernen & Wachstum |
| #3604 | Given the task definition | Lernen & Wachstum |
| #3605 | Q: You are given a sentence in Galician | Lernen & Wachstum |
| #3606 | Teacher:You are given a sentence in Galician | Lernen & Wachstum |
| #3607 | Teacher: You are given a sentence in Galician | Lernen & Wachstum |
| #3608 | In this task | Lernen & Wachstum |
| #3609 | In this task | Lernen & Wachstum |
| #3610 | In this task | Lernen & Wachstum |
| #3611 | Given a sentence in the Indonesian(Bahasa var | Lernen & Wachstum |
| #3612 | You will be given a definition of a task firs | Lernen & Wachstum |
| #3613 | Given a sentence in the Indonesian(Bahasa var | Lernen & Wachstum |
| #3614 | Given a sentence in the Indonesian(Bahasa var | Lernen & Wachstum |
| #3615 | Detailed Instructions: Given a sentence in th | Lernen & Wachstum |
| #3616 | Given a sentence in the Indonesian(Bahasa var | Lernen & Wachstum |
| #3617 | Definition: Given a sentence in the Indonesia | Lernen & Wachstum |
| #3618 | Instruction | Lernen & Wachstum |
| #3619 | Instructions: Given a sentence in the Indones | Lernen & Wachstum |
| #3620 | You will be given a definition of a task firs | Lernen & Wachstum |
| #3621 | Given a sentence, generate a most unlikely ne | Lernen & Wachstum |
| #3622 | Teacher:In this task, you are given a sentenc | Lernen & Wachstum |
| #3623 | Teacher:In this task | Lernen & Wachstum |
| #3624 | Definition: In this task | Spezielle Situationen |
| #3625 | In this task, you are given a question and an | Spezielle Situationen |
| #3626 | Given the task definition | Spezielle Situationen |
| #3627 | In this task, you are given a question and an | Spezielle Situationen |
| #3628 | In this task, you are given a question and an | Spezielle Situationen |
| #3629 | Definition: In this task | Spezielle Situationen |
| #3630 | You will be given two questions | Spezielle Situationen |
| #3631 | You will be given a definition of a task firs | Spezielle Situationen |
| #3632 | You will be given two questions | Spezielle Situationen |
| #3633 | Given a sentence with a missing word | Spezielle Situationen |
| #3634 | You will be given a definition of a task firs | Spezielle Situationen |
| #3635 | Q: You are given a question or fill-in-the-bl | Spezielle Situationen |
| #3636 | You will be given a definition of a task firs | Spezielle Situationen |
| #3637 | TASK DEFINITION: You are given a question or  | Spezielle Situationen |
| #3638 | You are given a question or fill-in-the-blank | Spezielle Situationen |
| #3639 | Detailed Instructions: You are given a questi | Spezielle Situationen |
| #3640 | Given the task definition | Spezielle Situationen |
| #3641 | You will be given a definition of a task firs | Spezielle Situationen |
| #3642 | Detailed Instructions: In this task | Spezielle Situationen |
| #3643 | Detailed Instructions: In this task | Spezielle Situationen |
| #3644 | TASK DEFINITION: In this task | Spezielle Situationen |
| #3645 | Definition: In this task | Spezielle Situationen |
| #3646 | In this task | Spezielle Situationen |
| #3647 | Definition: In this task | Spezielle Situationen |
| #3648 | In this task | Spezielle Situationen |
| #3649 | Given a sentence and an entity | Spezielle Situationen |
| #3650 | Detailed Instructions: In this task | Spezielle Situationen |
| #3651 | Instructions: Given a document | Spezielle Situationen |
| #3652 | Help me write sections of a formal proposal t | Spezielle Situationen |
| #3653 | Thank you for your suggestions, I will take i | Spezielle Situationen |
| #3654 | I am the branding team leader of Cafe24 | Spezielle Situationen |
| #3655 | Write a political joke about me | Spezielle Situationen |
| #3656 | An 650-word essay in a serious tone on the fo | Spezielle Situationen |
| #3657 | Kelly wants to buy a new skateboard which wil | Spezielle Situationen |
| #3658 | Here is a legal document | Spezielle Situationen |
| #3659 | Consider a forward contract on a non-dividend | Spezielle Situationen |
| #3660 | A bottle contains 2 | Spezielle Situationen |
| #3661 | A large hospital is evaluating its emergency  | Spezielle Situationen |
| #3662 | A radioactive sample contains two different i | Spezielle Situationen |
| #3663 | You are an expert architect with years of exp | Spezielle Situationen |
| #3664 | Considering the cartoon's portrayal of climat | Spezielle Situationen |
| #3665 | Compose an intricate spiritual narrative abou | Spezielle Situationen |
| #3666 | A father is 45 years old, and his son is 15 y | Spezielle Situationen |
| #3667 | A farmer has 5 chickens | Spezielle Situationen |
| #3668 | A factory produces 500 widgets every 8 hours | Spezielle Situationen |
| #3669 | Analyze the hormonal regulation and molecular | Spezielle Situationen |
| #3670 | Analyze the consequences of the Industrial Re | Spezielle Situationen |
| #3671 | Make recommendations for how a business could | Spezielle Situationen |
| #3672 | If a farmer has 12 cows and each cow produces | Spezielle Situationen |
| #3673 | A political debate between SpongeBob SquarePa | Spezielle Situationen |
| #3674 | A sequence follows the rule "multiply by 2 an | Spezielle Situationen |
| #3675 | What is the potential of regenerative agricul | Spezielle Situationen |
| #3676 | In the context of international relations | Spezielle Situationen |
| #3677 | At a bakery | Spezielle Situationen |
| #3678 | In environmental science | Spezielle Situationen |
| #3679 | In the field of genetics | Spezielle Situationen |
| #3680 | The Amazon rainforest | Spezielle Situationen |
| #3681 | Which was built first: the Great Wall of Chin | Spezielle Situationen |
| #3682 | How did "911" become the emergency number in  | Spezielle Situationen |
| #3683 | In physics | Spezielle Situationen |
| #3684 | If I'm visiting Australia and New Zealand fro | Spezielle Situationen |
| #3685 | The philosophy of utilitarianism | Spezielle Situationen |
| #3686 | In this task | Technik & Alltag |
| #3687 | Teacher:In this task | Technik & Alltag |
| #3688 | You are given a question or fill-in-the-blank | Technik & Alltag |
| #3689 | Instruction:
You are given a sentence in Ital | Technik & Alltag |
| #3690 | In this task, you are given a public comment  | Technik & Alltag |
| #3691 | In this task, you are given a public comment  | Technik & Alltag |
| #3692 | In this task you need to indicate the plausib | Technik & Alltag |
| #3693 | In this task you need to indicate the plausib | Technik & Alltag |
| #3694 | Given the task definition and input, reply wi | Technik & Alltag |
| #3695 | You will be given a definition of a task firs | Technik & Alltag |
| #3696 | Write me a vba code for editing a certain par | Technik & Alltag |
| #3697 | Machine learning | Technik & Alltag |
| #3698 | What are the pros and cons of using VSC vs | Technik & Alltag |
| #3699 | A Python programming challenge | Technik & Alltag |
| #3700 | A magic file school | Technik & Alltag |
| #3701 | How to enumerate each hour in datediff betwee | Technik & Alltag |
| #3702 | You to act as an IT Expert | Technik & Alltag |
| #3703 | To build automation between Greenhouse ATS an | Technik & Alltag |
| #3704 | How do I merge 5 different excel tables with  | Technik & Alltag |
| #3705 | What are beginner friendly IDE options for fi | Technik & Alltag |
| #3706 | Write a javascript function that will accept  | Technik & Alltag |
| #3707 | Please write clear instructions on how to imp | Technik & Alltag |
| #3708 | Act as an SEO consultant from MOZ and give me | Technik & Alltag |
| #3709 | Write microcontroller code in c for a modbus  | Technik & Alltag |
| #3710 | I will be able to add dependencies and applic | Technik & Alltag |
| #3711 | I have a tkinter app, and I want to make it a | Technik & Alltag |
| #3712 | What cloud services are discussed in the foll | Technik & Alltag |
| #3713 | A User Story with a technical execution plan  | Technik & Alltag |
| #3714 | I wish to prepare a 30 minute long presentati | Technik & Alltag |
| #3715 | Do you think a viable and more simple alterna | Technik & Alltag |
| #3716 | Chrome plug-in development | Technik & Alltag |
| #3717 | Write a php script that will take a URL and s | Technik & Alltag |
| #3718 | A user story for a web application | Technik & Alltag |
| #3719 | I'm a data engineer with technical understand | Technik & Alltag |
| #3720 | Write a p5js program that will draw a whole b | Technik & Alltag |
| #3721 | I am a software engineer and I want to write  | Technik & Alltag |
| #3722 | A terraform script to create an s3 bucket whi | Technik & Alltag |
| #3723 | Jhonny is a great coder | Technik & Alltag |
| #3724 | My team of 5 members is supposed to make a ha | Technik & Alltag |
| #3725 | To decide which software architecture I want  | Technik & Alltag |
| #3726 | Make a docstring for the following code snipp | Technik & Alltag |
| #3727 | A command to extract the Node IP Address and  | Technik & Alltag |
| #3728 | In SwiftUI | Technik & Alltag |
| #3729 | Write a upwork cover letter for this proposal | Technik & Alltag |
| #3730 | To build a simple way to upload panorama imag | Technik & Alltag |
| #3731 | From http import HTTPStatus | Technik & Alltag |
| #3732 | ```
class FunctionRegistry(object):
 def \_\_ | Technik & Alltag |
| #3733 | A webinar script and a structure from a produ | Technik & Alltag |
| #3734 | Make a formular about data analyze like this  | Technik & Alltag |
| #3735 | You are a pro coder | Technik & Alltag |
| #3736 | Hello, dear GPT, I want to write a very stron | Technik & Alltag |
| #3737 | To write an article to show TiDB cloud + Open | Technik & Alltag |
| #3738 | Write a machine learning model in python to p | Technik & Alltag |
| #3739 | An E-commerce Platform Using Mediator | Technik & Alltag |
| #3740 | An essay about discord's inner workings in de | Technik & Alltag |
| #3741 | I work for a digital marketing agency and I w | Technik & Alltag |
| #3742 | JavaScript a is getting content and then addi | Technik & Alltag |
| #3743 | 5 YouTube titles relevant to development dire | Technik & Alltag |
| #3744 | You are a programmer and have to deploy an up | Technik & Alltag |
| #3745 | I want to build an electron js app | Technik & Alltag |
| #3746 | A poem about how awesome CENDAS | Technik & Alltag |
| #3747 | Describe VMware vSphere in terms that someone | Technik & Alltag |
| #3748 | Does reading to your child in the womb enhanc | Alltag & Leben |
| #3749 | Is it true that a large portion of Germany's  | Alltag & Leben |
| #3750 | A story about a freaky museum and a group of  | Alltag & Leben |
| #3751 | A fairy tale about a book-loving young woman  | Alltag & Leben |
| #3752 | Solve the following math problem step-by-step | Alltag & Leben |
| #3753 | Solve the following math problem step-by-step | Alltag & Leben |
| #3754 | Solve the following math problem step-by-step | Alltag & Leben |
| #3755 | Solve the following math problem step-by-step | Alltag & Leben |
| #3756 | Solve the following math problem step-by-step | Alltag & Leben |
| #3757 | Solve the following math problem step-by-step | Alltag & Leben |
| #3758 | Solve the following math problem step-by-step | Alltag & Leben |
| #3759 | Solve the following math problem step-by-step | Alltag & Leben |
| #3760 | Solve the following math problem step-by-step | Alltag & Leben |
| #3761 | Solve the following math problem step-by-step | Alltag & Leben |
| #3762 | Solve the following math problem step-by-step | Alltag & Leben |
| #3763 | Solve the following math problem step-by-step | Alltag & Leben |
| #3764 | Solve the following math problem step-by-step | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-11)

**22 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3765 | Serene Indonesian Student in Nature | Lernen & Wachstum | `lernen-wachstum/3765-serene-indonesian-student-in-nature.md` |
| #3766 | Serene Campus Lifestyle Portrait of Indonesian Student | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3766-serene-campus-lifestyle-portrait-of-indo.md` |
| #3767 | Influencer Lifestyle Portrait in Modern Lounge | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3767-influencer-lifestyle-portrait-in-modern-.md` |
| #3768 | Generate a Plan for Building the Best UI/UX | Technik & Alltag | `technik-alltag/3768-generate-plan-for-building-best-ui-ux.md` |
| #3769 | Make UI/UX better of an already Created Application | Technik & Alltag | `technik-alltag/3769-make-ui-ux-better-of-already-created-app.md` |
| #3770 | Act as a lawyer and judicial advisor with 25 years of experience in drafting defense memoranda in Saudi courts only, with the condition of adhering to the legal provisions currently in force. | Spezielle Situationen | `spezielle-situationen/3770-lawyer-and-judicial-advisor-with-25-year.md` |
| #3771 | 2046 Puzzle Game Challenge | Kreativitaet & Freizeit | `kreativitaet-freizeit/3771-2046-puzzle-game-challenge.md` |
| #3772 | SEO diagnosis | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/3772-seo-diagnosis.md` |
| #3773 | Manimal | Technik & Alltag | `technik-alltag/3773-manimal.md` |
| #3774 | Hand made  site | Technik & Alltag | `technik-alltag/3774-hand-made-site.md` |
| #3775 | Graceful Indonesian Woman Portrait in Singapore | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3775-graceful-indonesian-woman-portrait-in-si.md` |
| #3776 | Elegant Portrait of an Indonesian Woman in Singapore | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3776-elegant-portrait-of-indonesian-woman-in-.md` |
| #3777 | Fashionable Portrait of Indonesian Woman | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3777-fashionable-portrait-of-indonesian-woman.md` |
| #3778 | Serene Indonesian Portrait in Kitchen | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3778-serene-indonesian-portrait-in-kitchen.md` |
| #3779 | Graceful Indonesian Yacht Club Fashion | Alltag & Leben | `alltag-leben/3779-graceful-indonesian-yacht-club-fashion.md` |
| #3780 | Productive Peer Mentor (Friendly Tech-Savvy Thinking Partner) | Kommunikation & Beziehungen | `kommunikation-beziehungen/3780-productive-peer-mentor-friendly-tech-sav.md` |
| #3781 | Elite Feedback Form Generator — Stunning UI with Next.js, React & TypeScript | Technik & Alltag | `technik-alltag/3781-elite-feedback-form-generator-stunning-u.md` |
| #3782 | Photorealistic Indonesian Woman in Ted Talk Style | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3782-photorealistic-indonesian-woman-in-ted-t.md` |
| #3783 | TED Talk Presentation Design | Technik & Alltag | `technik-alltag/3783-ted-talk-presentation-design.md` |
| #3784 | Indonesian Flight Attendant Elegance | Alltag & Leben | `alltag-leben/3784-indonesian-flight-attendant-elegance.md` |
| #3785 | Elegant Professional in a Luxurious Setting | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3785-elegant-professional-in-luxurious-settin.md` |
| #3786 | Graceful Indonesian Portrait | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3786-graceful-indonesian-portrait.md` |


---

## Multi-Source Import (2026-03-11)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #3787 | Your task is to create a recipe for a tasty | Alltag & Leben |
| #3788 | A recipe for a delicious and healthy barbeque | Alltag & Leben |
| #3789 | A poem about a grandfather's love for his two | Alltag & Leben |
| #3790 | What are some tips for cooking the perfect ba | Alltag & Leben |
| #3791 | Refer to the information below to help with t | Alltag & Leben |
| #3792 | Convert the sentence from active to passive | Alltag & Leben |
| #3793 | A 200-word positive review for an online scie | Beruf & Karriere |
| #3794 | What are some of the most common formats for  | Beruf & Karriere |
| #3795 | Provide a [Grammerly report] of the sentence  | Beruf & Karriere |
| #3796 | Using only the digits in the current year (20 | Beruf & Karriere |
| #3797 | As a sales representative for Nike | Beruf & Karriere |
| #3798 | Provide a detailed financial analysis report  | Beruf & Karriere |
| #3799 | What is the range of a human voice | Gesundheit & Wohlbefinden |
| #3800 | Act as if you are a student who is very inter | Gesundheit & Wohlbefinden |
| #3801 | The following information may be useful | Gesundheit & Wohlbefinden |
| #3802 | What are the three branches of the U | Gesundheit & Wohlbefinden |
| #3803 | What are some interesting facts about emerald | Gesundheit & Wohlbefinden |
| #3804 | In addition to the given prompt | Gesundheit & Wohlbefinden |
| #3805 | Reference | Kommunikation & Beziehungen |
| #3806 | What is the difference between blood flow and | Kommunikation & Beziehungen |
| #3807 | What are the benefits and drawbacks of wearin | Kommunikation & Beziehungen |
| #3808 | Background | Kommunikation & Beziehungen |
| #3809 | What are some PHP libraries that can be used  | Kommunikation & Beziehungen |
| #3810 | A convincing argument that supports the given | Kommunikation & Beziehungen |
| #3811 | According to the following reference text del | Kreativitaet & Freizeit |
| #3812 | A short story about a hog that is caught in t | Kreativitaet & Freizeit |
| #3813 | What is the first instance of the number zero | Kreativitaet & Freizeit |
| #3814 | What is the most popular song to play on the  | Kreativitaet & Freizeit |
| #3815 | A long story about a tutu-wearing superhero f | Kreativitaet & Freizeit |
| #3816 | A poem about a lambkin, a small and cuddly yo | Kreativitaet & Freizeit |
| #3817 | Explain in detail the purpose of a sepal in f | Lernen & Wachstum |
| #3818 | Using a colon, explain what a hermit crab is | Lernen & Wachstum |
| #3819 | What is the history of the spotlight | Lernen & Wachstum |
| #3820 | Imagine you are writing a manual for a seapla | Lernen & Wachstum |
| #3821 | Read this for context | Lernen & Wachstum |
| #3822 | What are some examples of grams in everyday l | Lernen & Wachstum |
| #3823 | Background | Spezielle Situationen |
| #3824 | Refer to the information below to help with t | Spezielle Situationen |
| #3825 | What are the most important rules and safety  | Spezielle Situationen |
| #3826 | Read this for context | Spezielle Situationen |
| #3827 | Provide a [Latex] formatted version of the fo | Spezielle Situationen |
| #3828 | An essay topic that analyzes the impact of gl | Spezielle Situationen |
| #3829 | Why does the light from the sun appear white  | Technik & Alltag |
| #3830 | What is the meaning of the word 'nexus' in th | Technik & Alltag |
| #3831 | A Python code snippet that prints "Hello worl | Technik & Alltag |
| #3832 | In the given sentence "Myself | Technik & Alltag |
| #3833 | Develop a machine learning algorithm that can | Technik & Alltag |
| #3834 | What is the formula for calculating the "Bran | Technik & Alltag |
| #3835 | Provide a JSON data with the names of 5 famou | Alltag & Leben |
| #3836 | You have been tasked with creating a grocery  | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-12)

**4 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3838 | Tistory Blog Skin UI/UX Enhancement Pipeline | Technik & Alltag | `technik-alltag/3838-tistory-blog-skin-ui-ux-enhancement-pipe.md` |
| #3839 | Civil Engineering Bridge Mentor | Technik & Alltag | `technik-alltag/3839-civil-engineering-bridge-mentor.md` |
| #3840 | 3D Avatar Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3840-3d-avatar-prompt.md` |
| #3841 | Plain-English Security Concept Explainer | Technik & Alltag | `technik-alltag/3841-plain-english-security-concept-explainer.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-13)

**5 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3842 | Task Creator | Technik & Alltag | `technik-alltag/3842-task-creator.md` |
| #3843 | MISSING VALUES HANDLER | Technik & Alltag | `technik-alltag/3843-missing-values-handler.md` |
| #3844 | Kickstart Prompt for UX & UI Design | Technik & Alltag | `technik-alltag/3844-kickstart-prompt-for-ux-ui-design.md` |
| #3845 | Unity Architecture Specialist | Technik & Alltag | `technik-alltag/3845-unity-architecture-specialist.md` |
| #3846 | Privacy-First Chat App with Multi-Feature Support | Technik & Alltag | `technik-alltag/3846-privacy-first-chat-app-with-multi-featur.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-14)

**23 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3847 | Page-by-Page Build | Alltag & Leben | `alltag-leben/3847-page-by-page-build.md` |
| #3848 | Iteration & Polish | Technik & Alltag | `technik-alltag/3848-iteration-polish.md` |
| #3849 | Design System Extraction Prompt Kit | Technik & Alltag | `technik-alltag/3849-design-system-extraction-prompt-kit.md` |
| #3850 | Token Architecture | Technik & Alltag | `technik-alltag/3850-token-architecture.md` |
| #3851 | Component Documentation | Technik & Alltag | `technik-alltag/3851-component-documentation.md` |
| #3852 | CLAUDE.md Assembly | Technik & Alltag | `technik-alltag/3852-claude-md-assembly.md` |
| #3853 | Maintenance Prompt for Design System | Technik & Alltag | `technik-alltag/3853-maintenance-prompt-for-design-system.md` |
| #3854 | Update/Sync Prompt | Technik & Alltag | `technik-alltag/3854-update-sync-prompt.md` |
| #3855 | "Explain It Like I Built It"  Technical Documentation for Non-Technical Founders | Lernen & Wachstum | `lernen-wachstum/3855-explain-it-like-i-built-it-technical-doc.md` |
| #3856 | Claude - Proje çalışma promptu | Technik & Alltag | `technik-alltag/3856-claude-proje-al-ma-promptu.md` |
| #3857 | Design Handoff Notes - AI First, Human Readable | Technik & Alltag | `technik-alltag/3857-design-handoff-notes-ai-first-human-read.md` |
| #3858 | Visual QA & Cross-Browser Audit | Technik & Alltag | `technik-alltag/3858-visual-qa-cross-browser-audit.md` |
| #3859 | Lighthouse & Performance Optimization | Technik & Alltag | `technik-alltag/3859-lighthouse-performance-optimization.md` |
| #3860 | Pre-Launch Checklist Generator | Technik & Alltag | `technik-alltag/3860-pre-launch-checklist-generator.md` |
| #3861 | Artificial Intelligence Paper Analysis | Lernen & Wachstum | `lernen-wachstum/3861-artificial-intelligence-paper-analysis.md` |
| #3862 | Deep Learning Loop | Lernen & Wachstum | `lernen-wachstum/3862-deep-learning-loop.md` |
| #3863 | Recruiter for Hiring Sales Professionals with Databricks Experience | Beruf & Karriere | `beruf-karriere/3863-recruiter-for-hiring-sales-professionals.md` |
| #3864 | SaaS Security Audit - OWASP Top 10 & Multi-Tenant Isolation Review | Technik & Alltag | `technik-alltag/3864-saas-security-audit-owasp-top-10-multi-t.md` |
| #3865 | SaaS Analytics Dashboard - Knowledge-Anchored Frontend Prompt | Technik & Alltag | `technik-alltag/3865-saas-analytics-dashboard-knowledge-ancho.md` |
| #3866 | Repository Security & Architecture Audit Framework | Technik & Alltag | `technik-alltag/3866-repository-security-architecture-audit-f.md` |
| #3867 | ACLS Master Simulator | Lernen & Wachstum | `lernen-wachstum/3867-acls-master-simulator.md` |
| #3868 | Lunch atop a Skyscraper - Robotic Power Armor Recreation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3868-lunch-atop-skyscraper-robotic-power-armo.md` |
| #3869 | Mine | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3869-mine.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-15)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3870 | In-Depth Paper and Exam Prediction Analyzer | Lernen & Wachstum | `lernen-wachstum/3870-in-depth-paper-and-exam-prediction-analy.md` |
| #3871 | Improve | Technik & Alltag | `technik-alltag/3871-improve.md` |
| #3872 | Photo Enhancement and Repair with Transparent Background | Technik & Alltag | `technik-alltag/3872-photo-enhancement-and-repair-with-transp.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-16)

**4 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3873 | code generation for online assessments | Technik & Alltag | `technik-alltag/3873-code-generation-for-online-assessments.md` |
| #3874 | ISC Class 12th Exam Paper Analyzer and evaluator | Lernen & Wachstum | `lernen-wachstum/3874-isc-class-12th-exam-paper-analyzer-and-e.md` |
| #3875 | Class Prep | Lernen & Wachstum | `lernen-wachstum/3875-class-prep.md` |
| #3876 | xcode-mcp (for pi agent) | Technik & Alltag | `technik-alltag/3876-xcode-mcp-for-pi-agent.md` |


---

## PromptHero Bild-Prompt Import (2026-03-16)

**50 neue Bild-Prompts** importiert (Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):

| ID | Titel | Modell | Datei |
|----|-------|--------|-------|
| #3877 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/3877-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #3878 | "glamor photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3878-glamor-photo-of-a-young-man-wearing-a-su.md` |
| #3879 | "beauty photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3879-beauty-photo-of-a-middle-aged-woman-with.md` |
| #3880 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/3880-high-fashion-photo-of-a-young-man-wearin.md` |
| #3881 | "paparazzi photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/3881-paparazzi-photo-of-a-young-man-wearing-a.md` |
| #3882 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3882-analog-photo-of-a-young-man-wearing-a-su.md` |
| #3883 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/3883-high-fashion-photo-of-a-young-man-wearin.md` |
| #3884 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/3884-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #3885 | "lifestyle photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/3885-lifestyle-photo-of-a-teenage-girl-with-s.md` |
| #3886 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/3886-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #3887 | "Polaroid photo of a elderly man with a  | SDXL | `bildbearbeitung-visualisierung/3887-polaroid-photo-of-a-elderly-man-with-a-b.md` |
| #3888 | "candid photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/3888-candid-photo-of-a-elderly-man-with-a-bea.md` |
| #3889 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3889-large-format-photo-of-a-middle-aged-woma.md` |
| #3890 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3890-high-fashion-photo-of-a-middle-aged-woma.md` |
| #3891 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3891-high-fashion-photo-of-a-child-with-a-cut.md` |
| #3892 | "Analog photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/3892-analog-photo-of-a-elderly-man-with-a-bea.md` |
| #3893 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3893-high-fashion-photo-of-a-middle-aged-woma.md` |
| #3894 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3894-analog-photo-of-a-middle-aged-woman-with.md` |
| #3895 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/3895-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #3896 | "large format photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/3896-large-format-photo-of-a-young-man-wearin.md` |
| #3897 | "beauty photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3897-beauty-photo-of-a-middle-aged-woman-with.md` |
| #3898 | "lifestyle photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/3898-lifestyle-photo-of-a-teenage-girl-with-s.md` |
| #3899 | "large format photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3899-large-format-photo-of-a-child-with-a-cut.md` |
| #3900 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3900-analog-photo-of-a-young-man-wearing-a-su.md` |
| #3901 | "large format photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/3901-large-format-photo-of-a-teenage-girl-wit.md` |
| #3902 | "Polaroid photo of a middle-aged woman w | SDXL | `bildbearbeitung-visualisierung/3902-polaroid-photo-of-a-middle-aged-woman-wi.md` |
| #3903 | "pictorialist photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3903-pictorialist-photo-of-a-elderly-man-with.md` |
| #3904 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/3904-large-format-photo-of-a-middle-aged-woma.md` |
| #3905 | "candid photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3905-candid-photo-of-a-young-man-wearing-a-su.md` |
| #3906 | "paparazzi photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/3906-paparazzi-photo-of-a-middle-aged-woman-w.md` |
| #3907 | "glamor photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/3907-glamor-photo-of-a-child-with-a-cute-expr.md` |
| #3908 | "pictorialist photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/3908-pictorialist-photo-of-a-young-man-wearin.md` |
| #3909 | "instant photo of a young man wearing a  | SDXL | `bildbearbeitung-visualisierung/3909-instant-photo-of-a-young-man-wearing-a-s.md` |
| #3910 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3910-analog-photo-of-a-middle-aged-woman-with.md` |
| #3911 | "large format photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3911-large-format-photo-of-a-child-with-a-cut.md` |
| #3912 | "glamor photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/3912-glamor-photo-of-a-child-with-a-cute-expr.md` |
| #3913 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/3913-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #3914 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/3914-candid-photo-of-a-child-with-a-cute-expr.md` |
| #3915 | "glamor photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3915-glamor-photo-of-a-young-man-wearing-a-su.md` |
| #3916 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/3916-high-fashion-photo-of-a-elderly-man-with.md` |
| #3917 | "glamor photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3917-glamor-photo-of-a-middle-aged-woman-with.md` |
| #3918 | "paparazzi photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/3918-paparazzi-photo-of-a-teenage-girl-with-s.md` |
| #3919 | "beauty photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3919-beauty-photo-of-a-young-man-wearing-a-su.md` |
| #3920 | "instant photo of a elderly man with a b | SDXL | `bildbearbeitung-visualisierung/3920-instant-photo-of-a-elderly-man-with-a-be.md` |
| #3921 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/3921-high-fashion-photo-of-a-child-with-a-cut.md` |
| #3922 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/3922-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #3923 | "beauty photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/3923-beauty-photo-of-a-child-with-a-cute-expr.md` |
| #3924 | "Analog photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/3924-analog-photo-of-a-teenage-girl-with-shor.md` |
| #3925 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/3925-analog-photo-of-a-young-man-wearing-a-su.md` |
| #3926 | "glamor photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/3926-glamor-photo-of-a-middle-aged-woman-with.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-17)

**10 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3927 | Messy Desk Study Moment - University Student | Lernen & Wachstum | `lernen-wachstum/3927-messy-desk-study-moment-university-stude.md` |
| #3928 | Why an Online PDF Editor Is Essential for Modern Workflows | Technik & Alltag | `technik-alltag/3928-why-online-pdf-editor-is-essential-for-m.md` |
| #3929 | Academic Research Writer | Lernen & Wachstum | `lernen-wachstum/3929-academic-research-writer.md` |
| #3930 | Deep Investigation Agent | Technik & Alltag | `technik-alltag/3930-deep-investigation-agent.md` |
| #3931 | Build an Interview Practice App | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/3931-build-interview-practice-app.md` |
| #3932 | AI voice assistant | Beruf & Karriere | `beruf-karriere/3932-ai-voice-assistant.md` |
| #3933 | Video review and teacher | Lernen & Wachstum | `lernen-wachstum/3933-video-review-and-teacher.md` |
| #3934 | Video extractor prompt | Beruf & Karriere | `beruf-karriere/3934-video-extractor-prompt.md` |
| #3935 | Project Builder | Lernen & Wachstum | `lernen-wachstum/3935-project-builder.md` |
| #3936 | Resume Customization Prompt – STRATEGIC INTEGRITY | Beruf & Karriere | `beruf-karriere/3936-resume-customization-prompt-strategic-in.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-18)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3938 | Extract a Writing Outline from Scientific Content | Technik & Alltag | `technik-alltag/3938-extract-writing-outline-from-scientific-.md` |
| #3939 | Neon Logo Design for Streaming Platform | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3939-neon-logo-design-for-streaming-platform.md` |


---

## Multi-Source Import (2026-03-18)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #3940 | What are some examples of suspenders that are | Alltag & Leben |
| #3941 | What is the definition of love | Alltag & Leben |
| #3942 | You to make a list of at least 5 ideas for a  | Alltag & Leben |
| #3943 | The reference text below provides context for | Alltag & Leben |
| #3944 | What is the procedure for a heart transplant | Alltag & Leben |
| #3945 | A short email to a friend about your latest g | Alltag & Leben |
| #3946 | What is the definition of accounting and what | Beruf & Karriere |
| #3947 | A poem about a creche | Beruf & Karriere |
| #3948 | What is the most important note in music | Beruf & Karriere |
| #3949 | Help me to create a job description for a Tra | Beruf & Karriere |
| #3950 | So I have a crowdfunding platform and I want  | Beruf & Karriere |
| #3951 | Act as a startup investor and let's say you w | Beruf & Karriere |
| #3952 | According to the following reference text del | Gesundheit & Wohlbefinden |
| #3953 | What are some strategies to deal with the str | Gesundheit & Wohlbefinden |
| #3954 | What is the easiest way to lose weight and ma | Gesundheit & Wohlbefinden |
| #3955 | Teacher:In this task, you are given a questio | Gesundheit & Wohlbefinden |
| #3956 | In this task the focus is on physical knowled | Gesundheit & Wohlbefinden |
| #3957 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #3958 | A letter to the judge | Kommunikation & Beziehungen |
| #3959 | A 355-word news article as a sports commentat | Kommunikation & Beziehungen |
| #3960 | A blog post about the benefits of having an e | Kommunikation & Beziehungen |
| #3961 | According to the following reference text del | Kommunikation & Beziehungen |
| #3962 | You are provided with an "Event" | Kommunikation & Beziehungen |
| #3963 | I have a json file with an array of entries t | Kommunikation & Beziehungen |
| #3964 | What is the simplest form of life on earth | Kreativitaet & Freizeit |
| #3965 | What are some good examples of movie subtitle | Kreativitaet & Freizeit |
| #3966 | A short article about the benefits of using a | Kreativitaet & Freizeit |
| #3967 | A poem about a transom | Kreativitaet & Freizeit |
| #3968 | What are the characteristics and behaviors of | Kreativitaet & Freizeit |
| #3969 | A poem about a young girl who finds a crystal | Kreativitaet & Freizeit |
| #3970 | A poem about swimming in a lake | Lernen & Wachstum |
| #3971 | What is fairness and how can it be achieved i | Lernen & Wachstum |
| #3972 | What are some common examples of a skean dui’ | Lernen & Wachstum |
| #3973 | What is the history of the staircase | Lernen & Wachstum |
| #3974 | What is the difference between satire and iro | Lernen & Wachstum |
| #3975 | What are some examples of straits around the  | Lernen & Wachstum |
| #3976 | In this task you will be given a list of numb | Spezielle Situationen |
| #3977 | In this task you will be given a list of numb | Spezielle Situationen |
| #3978 | In this task you will be given a list of numb | Spezielle Situationen |
| #3979 | Definition: In this task you will be given a  | Spezielle Situationen |
| #3980 | In this task you will be given a list of numb | Spezielle Situationen |
| #3981 | Detailed Instructions: In this task you will  | Spezielle Situationen |
| #3982 | A database of 1000 different animals includin | Technik & Alltag |
| #3983 | Consider this reference information delimited | Technik & Alltag |
| #3984 | What is a polliwog | Technik & Alltag |
| #3985 | Instruction | Technik & Alltag |
| #3986 | Detailed Instructions: In this task | Technik & Alltag |
| #3987 | You are given a target profession, and two se | Technik & Alltag |
| #3988 | Detailed Instructions: In this task | Alltag & Leben |
| #3989 | Given the task definition and input, reply wi | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-19)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3990 | Review the social media content | Kommunikation & Beziehungen | `kommunikation-beziehungen/3990-review-social-media-content.md` |
| #3991 | Professional photo restoration expert | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/3991-professional-photo-restoration-expert.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-20)

**54 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #3992 | Entropy peer reviews | Lernen & Wachstum | `lernen-wachstum/3992-entropy-peer-reviews.md` |
| #3993 | System Architect Agent Role | Technik & Alltag | `technik-alltag/3993-system-architect-agent-role.md` |
| #3994 | API Design Expert Agent Role | Technik & Alltag | `technik-alltag/3994-api-design-expert-agent-role.md` |
| #3995 | Data Validator Agent Role | Technik & Alltag | `technik-alltag/3995-data-validator-agent-role.md` |
| #3996 | Mock Data Generator Agent Role | Technik & Alltag | `technik-alltag/3996-mock-data-generator-agent-role.md` |
| #3997 | Backup & Restore Agent Role | Technik & Alltag | `technik-alltag/3997-backup-restore-agent-role.md` |
| #3998 | DevOps Automator Agent Role | Technik & Alltag | `technik-alltag/3998-devops-automator-agent-role.md` |
| #3999 | Environment Configuration Agent Role | Technik & Alltag | `technik-alltag/3999-environment-configuration-agent-role.md` |
| #4000 | Git Workflow Expert Agent Role | Technik & Alltag | `technik-alltag/4000-git-workflow-expert-agent-role.md` |
| #4001 | Repository Workflow Editor Agent Role | Technik & Alltag | `technik-alltag/4001-repository-workflow-editor-agent-role.md` |
| #4002 | Documentation Maintainer Agent Role | Technik & Alltag | `technik-alltag/4002-documentation-maintainer-agent-role.md` |
| #4003 | Accessibility Auditor Agent Role | Technik & Alltag | `technik-alltag/4003-accessibility-auditor-agent-role.md` |
| #4004 | Frontend Developer Agent Role | Technik & Alltag | `technik-alltag/4004-frontend-developer-agent-role.md` |
| #4005 | SEO Optimization Agent Role | Kommunikation & Beziehungen | `kommunikation-beziehungen/4005-seo-optimization-agent-role.md` |
| #4006 | Legal Document Generator Agent Role | Spezielle Situationen | `spezielle-situationen/4006-legal-document-generator-agent-role.md` |
| #4007 | Performance Tuning Agent Role | Technik & Alltag | `technik-alltag/4007-performance-tuning-agent-role.md` |
| #4008 | Diff Security Auditor Agent Role | Technik & Alltag | `technik-alltag/4008-diff-security-auditor-agent-role.md` |
| #4009 | API Tester Agent Role | Technik & Alltag | `technik-alltag/4009-api-tester-agent-role.md` |
| #4010 | Quality Engineering Agent Role | Technik & Alltag | `technik-alltag/4010-quality-engineering-agent-role.md` |
| #4011 | Test Analyzer Agent Role | Technik & Alltag | `technik-alltag/4011-test-analyzer-agent-role.md` |
| #4012 | Code Formatter Agent Role | Lernen & Wachstum | `lernen-wachstum/4012-code-formatter-agent-role.md` |
| #4013 | Dependency Manager Agent Role | Beruf & Karriere | `beruf-karriere/4013-dependency-manager-agent-role.md` |
| #4014 | Error Handler Agent Role | Technik & Alltag | `technik-alltag/4014-error-handler-agent-role.md` |
| #4015 | Post-Implementation Audit Agent Role | Technik & Alltag | `technik-alltag/4015-post-implementation-audit-agent-role.md` |
| #4016 | Product Planner Agent Role | Technik & Alltag | `technik-alltag/4016-product-planner-agent-role.md` |
| #4017 | Rapid Prototyper Agent Role | Technik & Alltag | `technik-alltag/4017-rapid-prototyper-agent-role.md` |
| #4018 | Root Cause Analysis Agent Role | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/4018-root-cause-analysis-agent-role.md` |
| #4019 | Refactoring Expert Agent Role | Technik & Alltag | `technik-alltag/4019-refactoring-expert-agent-role.md` |
| #4020 | Shell Script Agent Role | Technik & Alltag | `technik-alltag/4020-shell-script-agent-role.md` |
| #4021 | Tool Evaluator Agent Role | Technik & Alltag | `technik-alltag/4021-tool-evaluator-agent-role.md` |
| #4022 | TypeScript Type Expert Agent Role | Technik & Alltag | `technik-alltag/4022-typescript-type-expert-agent-role.md` |
| #4023 | Bug Risk Analyst Agent Role | Technik & Alltag | `technik-alltag/4023-bug-risk-analyst-agent-role.md` |
| #4024 | Deep Research Agent Role | Lernen & Wachstum | `lernen-wachstum/4024-deep-research-agent-role.md` |
| #4025 | Repository Indexer Agent Role | Lernen & Wachstum | `lernen-wachstum/4025-repository-indexer-agent-role.md` |
| #4026 | Visual Media Analysis Expert Agent Role | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4026-visual-media-analysis-expert-agent-role.md` |
| #4027 | UX Conversion Deconstruction Engine | Technik & Alltag | `technik-alltag/4027-ux-conversion-deconstruction-engine.md` |
| #4028 | AI-First Design Handoff Generator (Dev-Ready Spec) | Technik & Alltag | `technik-alltag/4028-ai-first-design-handoff-generator-dev-re.md` |
| #4029 | Design System Consistency Auditor | Technik & Alltag | `technik-alltag/4029-design-system-consistency-auditor.md` |
| #4030 | Apple-Level UI System Designer (2026 Standard) | Technik & Alltag | `technik-alltag/4030-apple-level-ui-system-designer-2026-stan.md` |
| #4031 | AI-Powered Personal Compliment & Coaching Engine | Alltag & Leben | `alltag-leben/4031-ai-powered-personal-compliment-coaching-.md` |
| #4032 | Dating Profile Optimization Suite | Technik & Alltag | `technik-alltag/4032-dating-profile-optimization-suite.md` |
| #4033 | Personalized Digital Avatar Generator | Alltag & Leben | `alltag-leben/4033-personalized-digital-avatar-generator.md` |
| #4034 | Private Group Coaching Infrastructure | Technik & Alltag | `technik-alltag/4034-private-group-coaching-infrastructure.md` |
| #4035 | Trading & Investing Simulation Platform | Kreativitaet & Freizeit | `kreativitaet-freizeit/4035-trading-investing-simulation-platform.md` |
| #4036 | Personal Knowledge & Narrative Tool | Alltag & Leben | `alltag-leben/4036-personal-knowledge-narrative-tool.md` |
| #4037 | Zero to One Solo-Founder Launch System | Technik & Alltag | `technik-alltag/4037-zero-to-one-solo-founder-launch-system.md` |
| #4038 | Legal Risk Minimization Tool for Freelancers | Beruf & Karriere | `beruf-karriere/4038-legal-risk-minimization-tool-for-freelan.md` |
| #4039 | High-Stakes Decision Support System | Beruf & Karriere | `beruf-karriere/4039-high-stakes-decision-support-system.md` |
| #4040 | Strategic Business Blueprint Generator | Beruf & Karriere | `beruf-karriere/4040-strategic-business-blueprint-generator.md` |
| #4041 | Market Entry Strategy Engine | Beruf & Karriere | `beruf-karriere/4041-market-entry-strategy-engine.md` |
| #4042 | Revenue Model & Unit Economics Analyzer | Beruf & Karriere | `beruf-karriere/4042-revenue-model-unit-economics-analyzer.md` |
| #4043 | Go-To-Market Execution Planner | Technik & Alltag | `technik-alltag/4043-go-to-market-execution-planner.md` |
| #4044 | Business Risk & Scenario Analyzer | Beruf & Karriere | `beruf-karriere/4044-business-risk-scenario-analyzer.md` |
| #4045 | Grok customize | Lernen & Wachstum | `lernen-wachstum/4045-grok-customize.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-21)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4046 | Stock | Beruf & Karriere | `beruf-karriere/4046-stock.md` |
| #4047 | Betting Prediction | Kreativitaet & Freizeit | `kreativitaet-freizeit/4047-betting-prediction.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-22)

**4 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4048 | Illustrator Style Describer Weavy | Technik & Alltag | `technik-alltag/4048-illustrator-style-describer-weavy.md` |
| #4049 | Reflective Companion, Not Advice | Gesundheit & Wohlbefinden | `gesundheit-wohlbefinden/4049-reflective-companion-not-advice.md` |
| #4050 | Ultimate Stake.us Dice Strategy Builder — All Risk Levels & Bankrolls | Technik & Alltag | `technik-alltag/4050-ultimate-stake-us-dice-strategy-builder-.md` |
| #4051 | KJV Harmony Companion | Technik & Alltag | `technik-alltag/4051-kjv-harmony-companion.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-23)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4052 | Astro.js | Technik & Alltag | `technik-alltag/4052-astro-js.md` |
| #4053 | Midjourney | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4053-midjourney.md` |
| #4054 | Love Shop | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4054-love-shop.md` |


---

## PromptHero Bild-Prompt Import (2026-03-23)

**50 neue Bild-Prompts** importiert (Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):

| ID | Titel | Modell | Datei |
|----|-------|--------|-------|
| #4055 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4055-high-fashion-photo-of-a-elderly-man-with.md` |
| #4056 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4056-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4057 | "instant photo of a middle-aged woman wi | SDXL | `bildbearbeitung-visualisierung/4057-instant-photo-of-a-middle-aged-woman-wit.md` |
| #4058 | "pictorialist photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4058-pictorialist-photo-of-a-teenage-girl-wit.md` |
| #4059 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4059-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4060 | "instant photo of a teenage girl with sh | SDXL | `bildbearbeitung-visualisierung/4060-instant-photo-of-a-teenage-girl-with-sho.md` |
| #4061 | "candid photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4061-candid-photo-of-a-teenage-girl-with-shor.md` |
| #4062 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4062-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4063 | "glamor photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4063-glamor-photo-of-a-elderly-man-with-a-bea.md` |
| #4064 | "Polaroid photo of a elderly man with a  | SDXL | `bildbearbeitung-visualisierung/4064-polaroid-photo-of-a-elderly-man-with-a-b.md` |
| #4065 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4065-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4066 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4066-analog-photo-of-a-young-man-wearing-a-su.md` |
| #4067 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4067-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4068 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4068-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4069 | "glamor photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4069-glamor-photo-of-a-teenage-girl-with-shor.md` |
| #4070 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4070-analog-photo-of-a-middle-aged-woman-with.md` |
| #4071 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4071-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4072 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4072-analog-photo-of-a-middle-aged-woman-with.md` |
| #4073 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4073-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4074 | "lifestyle photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4074-lifestyle-photo-of-a-child-with-a-cute-e.md` |
| #4075 | "paparazzi photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4075-paparazzi-photo-of-a-child-with-a-cute-e.md` |
| #4076 | "Polaroid photo of a child with a cute e | SDXL | `bildbearbeitung-visualisierung/4076-polaroid-photo-of-a-child-with-a-cute-ex.md` |
| #4077 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4077-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4078 | "Analog photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4078-analog-photo-of-a-teenage-girl-with-shor.md` |
| #4079 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4079-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4080 | "lifestyle photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/4080-lifestyle-photo-of-a-elderly-man-with-a-.md` |
| #4081 | "candid photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4081-candid-photo-of-a-elderly-man-with-a-bea.md` |
| #4082 | "instant photo of a middle-aged woman wi | SDXL | `bildbearbeitung-visualisierung/4082-instant-photo-of-a-middle-aged-woman-wit.md` |
| #4083 | "pictorialist photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4083-pictorialist-photo-of-a-elderly-man-with.md` |
| #4084 | "pictorialist photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4084-pictorialist-photo-of-a-young-man-wearin.md` |
| #4085 | "large format photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4085-large-format-photo-of-a-teenage-girl-wit.md` |
| #4086 | "paparazzi photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4086-paparazzi-photo-of-a-middle-aged-woman-w.md` |
| #4087 | "candid photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4087-candid-photo-of-a-elderly-man-with-a-bea.md` |
| #4088 | "beauty photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4088-beauty-photo-of-a-child-with-a-cute-expr.md` |
| #4089 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4089-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4090 | "pictorialist photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4090-pictorialist-photo-of-a-child-with-a-cut.md` |
| #4091 | "candid photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4091-candid-photo-of-a-elderly-man-with-a-bea.md` |
| #4092 | "lifestyle photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/4092-lifestyle-photo-of-a-young-man-wearing-a.md` |
| #4093 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4093-candid-photo-of-a-middle-aged-woman-with.md` |
| #4094 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4094-large-format-photo-of-a-middle-aged-woma.md` |
| #4095 | "large format photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4095-large-format-photo-of-a-teenage-girl-wit.md` |
| #4096 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/4096-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #4097 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4097-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4098 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4098-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4099 | "glamor photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4099-glamor-photo-of-a-elderly-man-with-a-bea.md` |
| #4100 | "pictorialist photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4100-pictorialist-photo-of-a-child-with-a-cut.md` |
| #4101 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4101-candid-photo-of-a-middle-aged-woman-with.md` |
| #4102 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4102-large-format-photo-of-a-middle-aged-woma.md` |
| #4103 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4103-large-format-photo-of-a-middle-aged-woma.md` |
| #4104 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4104-analog-photo-of-a-young-man-wearing-a-su.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-24)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4105 | writer | Lernen & Wachstum | `lernen-wachstum/4105-writer.md` |
| #4106 | Entagled IR | Alltag & Leben | `alltag-leben/4106-entagled-ir.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-25)

**12 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4107 | GitHub Stars Fetcher with Agent Browser | Technik & Alltag | `technik-alltag/4107-github-stars-fetcher-with-agent-browser.md` |
| #4108 | Odalisque | Technik & Alltag | `technik-alltag/4108-odalisque.md` |
| #4109 | Researchers in the Library | Lernen & Wachstum | `lernen-wachstum/4109-researchers-in-library.md` |
| #4110 | Step 1: Prepare your data | Technik & Alltag | `technik-alltag/4110-step-1-prepare-your-data.md` |
| #4111 | Analyze Chat History With User | Lernen & Wachstum | `lernen-wachstum/4111-analyze-chat-history-with-user.md` |
| #4112 | Self-summary | Technik & Alltag | `technik-alltag/4112-self-summary.md` |
| #4113 | Moral Dilemma Choices | Alltag & Leben | `alltag-leben/4113-moral-dilemma-choices.md` |
| #4114 | Fringe Ideology Quiz | Kreativitaet & Freizeit | `kreativitaet-freizeit/4114-fringe-ideology-quiz.md` |
| #4115 | Linkedin Post Create Prompt | Beruf & Karriere | `beruf-karriere/4115-linkedin-post-create-prompt.md` |
| #4116 | Professional Betting Predictions | Kreativitaet & Freizeit | `kreativitaet-freizeit/4116-professional-betting-predictions.md` |
| #4117 | Terraform Platform Engineer | Technik & Alltag | `technik-alltag/4117-terraform-platform-engineer.md` |
| #4118 | Lifelike Face Mask | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4118-lifelike-face-mask.md` |


---

## Multi-Source Import (2026-03-25)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #4119 | Give me some ideas for recipes that include a | Alltag & Leben |
| #4120 | What are the most interesting facts about the | Alltag & Leben |
| #4121 | What are some different modes of transportati | Alltag & Leben |
| #4122 | What should men pay attention to when breastf | Alltag & Leben |
| #4123 | What kind of food will weather forcasters tal | Alltag & Leben |
| #4124 | From which shop we can buy an earth | Alltag & Leben |
| #4125 | In this task, you are given a news article | Beruf & Karriere |
| #4126 | Instructions: In this task | Beruf & Karriere |
| #4127 | You will be given a definition of a task firs | Beruf & Karriere |
| #4128 | Teacher:Categorize the comment on the basis o | Beruf & Karriere |
| #4129 | Act as a Business Consultant | Beruf & Karriere |
| #4130 | So if we were on a bar right now | Beruf & Karriere |
| #4131 | According to the following reference text del | Gesundheit & Wohlbefinden |
| #4132 | Does people like cola because a bottle of col | Gesundheit & Wohlbefinden |
| #4133 | What kind of exercises should I do to buid up | Gesundheit & Wohlbefinden |
| #4134 | If I want to stay healthy | Gesundheit & Wohlbefinden |
| #4135 | How many clashes of the metal tube do you nee | Gesundheit & Wohlbefinden |
| #4136 | You are given a sentence in English | Gesundheit & Wohlbefinden |
| #4137 | What are some of the key features of the Fren | Kommunikation & Beziehungen |
| #4138 | Background:
<start of reference>
Quilt voice  | Kommunikation & Beziehungen |
| #4139 | What was the relationship between the US and  | Kommunikation & Beziehungen |
| #4140 | Instructions: Given a document | Kommunikation & Beziehungen |
| #4141 | This task is about classifying the similarity | Kommunikation & Beziehungen |
| #4142 | Detailed Instructions: This task is about cla | Kommunikation & Beziehungen |
| #4143 | A short story about a lobotomy procedure that | Kreativitaet & Freizeit |
| #4144 | Read this for context | Kreativitaet & Freizeit |
| #4145 | A poem about baseball in iambic pentameter | Kreativitaet & Freizeit |
| #4146 | A poem about a tortoise that is trying to cro | Kreativitaet & Freizeit |
| #4147 | A poem in the style of Edgar Allen Poe about  | Kreativitaet & Freizeit |
| #4148 | List the best time to visit a department, at  | Kreativitaet & Freizeit |
| #4149 | What are some examples of modern-day monks or | Lernen & Wachstum |
| #4150 | A sales email to a potential buyer | Lernen & Wachstum |
| #4151 | What is the history of vodka and how has its  | Lernen & Wachstum |
| #4152 | What are some examples of screw-ups that lead | Lernen & Wachstum |
| #4153 | A script for a video explaining the concept o | Lernen & Wachstum |
| #4154 | Does China have two currencies | Lernen & Wachstum |
| #4155 | If you want to daisies grow to 10 meters, how | Spezielle Situationen |
| #4156 | If a stone can grow into an adult, then how l | Spezielle Situationen |
| #4157 | If a diver swims deeper, why the water pressu | Spezielle Situationen |
| #4158 | In this task you will be given two dialogues | Spezielle Situationen |
| #4159 | Given the task definition and input, reply wi | Spezielle Situationen |
| #4160 | Detailed Instructions: In this task | Spezielle Situationen |
| #4161 | Read this for context | Technik & Alltag |
| #4162 | What is the origin of the word "cheddar" | Technik & Alltag |
| #4163 | A python script that prints the gradient of a | Technik & Alltag |
| #4164 | What kinds of liquids are firewater? Orange j | Technik & Alltag |
| #4165 | Which is the peripheral device for the comput | Technik & Alltag |
| #4166 | What was the world's most popular computer op | Technik & Alltag |
| #4167 | When did America Communist Party establish th | Alltag & Leben |
| #4168 | Does outer space is the right place to find a | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-26)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4169 | NixOS Linux Specialist | Technik & Alltag | `technik-alltag/4169-nixos-linux-specialist.md` |
| #4170 | presentation making | Technik & Alltag | `technik-alltag/4170-presentation-making.md` |
| #4171 | Refine Your Resume for Professionalism and ATS Compatibility | Beruf & Karriere | `beruf-karriere/4171-refine-your-resume-for-professionalism-a.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-27)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4172 | Website Design Recreation Workflow | Alltag & Leben | `alltag-leben/4172-website-design-recreation-workflow.md` |
| #4173 | Website Design Recreator Skill | Technik & Alltag | `technik-alltag/4173-website-design-recreator-skill.md` |
| #4174 | Lazyvim expert | Technik & Alltag | `technik-alltag/4174-lazyvim-expert.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-28)

**7 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4175 | Scientific Paper Drafting Assistant | Technik & Alltag | `technik-alltag/4175-scientific-paper-drafting-assistant.md` |
| #4176 | GitHub Enterprise Cloud (GHEC) administrator and power user | Technik & Alltag | `technik-alltag/4176-github-enterprise-cloud-ghec-administrat.md` |
| #4177 | base-R | Technik & Alltag | `technik-alltag/4177-base-r.md` |
| #4178 | Functional Analyst | Beruf & Karriere | `beruf-karriere/4178-functional-analyst.md` |
| #4179 | Small Functional Analyst mode | Beruf & Karriere | `beruf-karriere/4179-small-functional-analyst-mode.md` |
| #4180 | Ultra-micro Functional Analyst Prompt | Technik & Alltag | `technik-alltag/4180-ultra-micro-functional-analyst-prompt.md` |
| #4181 | psy | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4181-psy.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-29)

**4 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4182 | Architecture & UI/UX Audit | Technik & Alltag | `technik-alltag/4182-architecture-ui-ux-audit.md` |
| #4183 | Minimalist Graphic Illustration of a Stylized Dachshund | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4183-minimalist-graphic-illustration-of-styli.md` |
| #4184 | Abstract Geometric Art Prompt Inspired by Wassily Kandinsky | Technik & Alltag | `technik-alltag/4184-abstract-geometric-art-prompt-inspired-b.md` |
| #4185 | Impressionistic Urban Solitude | Technik & Alltag | `technik-alltag/4185-impressionistic-urban-solitude.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-30)

**7 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4186 | Expert Legal Analyst in Tax and Commercial Law | Spezielle Situationen | `spezielle-situationen/4186-expert-legal-analyst-in-tax-and-commerci.md` |
| #4187 | blood grouping detection using image processing | Technik & Alltag | `technik-alltag/4187-blood-grouping-detection-using-image-pro.md` |
| #4188 | subculture | Lernen & Wachstum | `lernen-wachstum/4188-subculture.md` |
| #4189 | comparison of social groups | Technik & Alltag | `technik-alltag/4189-comparison-of-social-groups.md` |
| #4190 | question list for reaserch | Lernen & Wachstum | `lernen-wachstum/4190-question-list-for-reaserch.md` |
| #4191 | Academic analyst and exam pattern extractor | Lernen & Wachstum | `lernen-wachstum/4191-academic-analyst-and-exam-pattern-extrac.md` |
| #4192 | Pixar-Style Family Wallpaper Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4192-pixar-style-family-wallpaper-prompt.md` |


---

## PromptHero Bild-Prompt Import (2026-03-30)

**50 neue Bild-Prompts** importiert (Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):

| ID | Titel | Modell | Datei |
|----|-------|--------|-------|
| #4193 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4193-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4194 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4194-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4195 | "instant photo of a child with a cute ex | SDXL | `bildbearbeitung-visualisierung/4195-instant-photo-of-a-child-with-a-cute-exp.md` |
| #4196 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4196-high-fashion-photo-of-a-elderly-man-with.md` |
| #4197 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4197-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4198 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4198-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4199 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4199-analog-photo-of-a-middle-aged-woman-with.md` |
| #4200 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4200-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4201 | "beauty photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4201-beauty-photo-of-a-elderly-man-with-a-bea.md` |
| #4202 | "pictorialist photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4202-pictorialist-photo-of-a-child-with-a-cut.md` |
| #4203 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4203-candid-photo-of-a-child-with-a-cute-expr.md` |
| #4204 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4204-high-fashion-photo-of-a-young-man-wearin.md` |
| #4205 | "beauty photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4205-beauty-photo-of-a-child-with-a-cute-expr.md` |
| #4206 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/4206-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #4207 | "lifestyle photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/4207-lifestyle-photo-of-a-teenage-girl-with-s.md` |
| #4208 | "paparazzi photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/4208-paparazzi-photo-of-a-elderly-man-with-a-.md` |
| #4209 | "large format photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4209-large-format-photo-of-a-teenage-girl-wit.md` |
| #4210 | "beauty photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4210-beauty-photo-of-a-elderly-man-with-a-bea.md` |
| #4211 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4211-candid-photo-of-a-middle-aged-woman-with.md` |
| #4212 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4212-high-fashion-photo-of-a-elderly-man-with.md` |
| #4213 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4213-high-fashion-photo-of-a-elderly-man-with.md` |
| #4214 | "candid photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4214-candid-photo-of-a-teenage-girl-with-shor.md` |
| #4215 | "Analog photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4215-analog-photo-of-a-teenage-girl-with-shor.md` |
| #4216 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4216-high-fashion-photo-of-a-young-man-wearin.md` |
| #4217 | "Analog photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4217-analog-photo-of-a-child-with-a-cute-expr.md` |
| #4218 | "paparazzi photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/4218-paparazzi-photo-of-a-elderly-man-with-a-.md` |
| #4219 | "large format photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4219-large-format-photo-of-a-child-with-a-cut.md` |
| #4220 | "paparazzi photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/4220-paparazzi-photo-of-a-young-man-wearing-a.md` |
| #4221 | "paparazzi photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4221-paparazzi-photo-of-a-child-with-a-cute-e.md` |
| #4222 | "candid photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4222-candid-photo-of-a-young-man-wearing-a-su.md` |
| #4223 | "candid photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4223-candid-photo-of-a-young-man-wearing-a-su.md` |
| #4224 | "lifestyle photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4224-lifestyle-photo-of-a-child-with-a-cute-e.md` |
| #4225 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4225-high-fashion-photo-of-a-elderly-man-with.md` |
| #4226 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4226-candid-photo-of-a-child-with-a-cute-expr.md` |
| #4227 | "glamor photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4227-glamor-photo-of-a-middle-aged-woman-with.md` |
| #4228 | "instant photo of a teenage girl with sh | SDXL | `bildbearbeitung-visualisierung/4228-instant-photo-of-a-teenage-girl-with-sho.md` |
| #4229 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4229-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4230 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4230-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4231 | "lifestyle photo of a elderly man with a | SDXL | `bildbearbeitung-visualisierung/4231-lifestyle-photo-of-a-elderly-man-with-a-.md` |
| #4232 | "lifestyle photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4232-lifestyle-photo-of-a-child-with-a-cute-e.md` |
| #4233 | "instant photo of a child with a cute ex | SDXL | `bildbearbeitung-visualisierung/4233-instant-photo-of-a-child-with-a-cute-exp.md` |
| #4234 | "Polaroid photo of a elderly man with a  | SDXL | `bildbearbeitung-visualisierung/4234-polaroid-photo-of-a-elderly-man-with-a-b.md` |
| #4235 | "Analog photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4235-analog-photo-of-a-elderly-man-with-a-bea.md` |
| #4236 | "beauty photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4236-beauty-photo-of-a-teenage-girl-with-shor.md` |
| #4237 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4237-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4238 | "Analog photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4238-analog-photo-of-a-child-with-a-cute-expr.md` |
| #4239 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4239-high-fashion-photo-of-a-young-man-wearin.md` |
| #4240 | "Polaroid photo of a middle-aged woman w | SDXL | `bildbearbeitung-visualisierung/4240-polaroid-photo-of-a-middle-aged-woman-wi.md` |
| #4241 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4241-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4242 | "glamor photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4242-glamor-photo-of-a-elderly-man-with-a-bea.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-31)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4243 | Apple App Store Review Compliance Agent | Technik & Alltag | `technik-alltag/4243-apple-app-store-review-compliance-agent.md` |
| #4244 | Translate Document to Arabic | Lernen & Wachstum | `lernen-wachstum/4244-translate-document-to-arabic.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-01)

**11 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4245 | Ben | Technik & Alltag | `technik-alltag/4245-ben.md` |
| #4246 | Picture design | Technik & Alltag | `technik-alltag/4246-picture-design.md` |
| #4247 | Network Router emulator | Technik & Alltag | `technik-alltag/4247-network-router-emulator.md` |
| #4248 | Accounting Information System | Technik & Alltag | `technik-alltag/4248-accounting-information-system.md` |
| #4249 | Sapiosessuale | Technik & Alltag | `technik-alltag/4249-sapiosessuale.md` |
| #4250 | Lonely cry | Technik & Alltag | `technik-alltag/4250-lonely-cry.md` |
| #4251 | Voice Cloning Assistant | Technik & Alltag | `technik-alltag/4251-voice-cloning-assistant.md` |
| #4252 | making ppt | Lernen & Wachstum | `lernen-wachstum/4252-making-ppt.md` |
| #4253 | Bikini_Girl | Beruf & Karriere | `beruf-karriere/4253-bikini-girl.md` |
| #4254 | Version Review | Technik & Alltag | `technik-alltag/4254-version-review.md` |
| #4255 | Premium Classy Interview Presentation Design | Technik & Alltag | `technik-alltag/4255-premium-classy-interview-presentation-de.md` |


---

## Multi-Source Import (2026-04-01)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #4256 | Reference | Alltag & Leben |
| #4257 | Background | Alltag & Leben |
| #4258 | Background | Alltag & Leben |
| #4259 | The following information may be useful | Alltag & Leben |
| #4260 | According to the following reference text del | Alltag & Leben |
| #4261 | What is the recipe for chocolate chip cookies | Alltag & Leben |
| #4262 | What are some of the major drawbacks of credi | Beruf & Karriere |
| #4263 | In this task you are given a sentence pair fr | Beruf & Karriere |
| #4264 | You will be given a definition of a task firs | Beruf & Karriere |
| #4265 | You are given a math word problem and you are | Beruf & Karriere |
| #4266 | You are given a math word problem and you are | Beruf & Karriere |
| #4267 | You are given a math word problem and you are | Beruf & Karriere |
| #4268 | What are some creative ways to use food as me | Gesundheit & Wohlbefinden |
| #4269 | What are three symptoms of septicaemia | Gesundheit & Wohlbefinden |
| #4270 | Give me five lunch ideas that are healthy and | Gesundheit & Wohlbefinden |
| #4271 | According to the following reference text del | Gesundheit & Wohlbefinden |
| #4272 | Read this for context | Gesundheit & Wohlbefinden |
| #4273 | What are some of the negative effects of soci | Gesundheit & Wohlbefinden |
| #4274 | What are some factors that influence the reli | Kommunikation & Beziehungen |
| #4275 | An article about a young woman who is working | Kommunikation & Beziehungen |
| #4276 | What are some strategies for resolving confli | Kommunikation & Beziehungen |
| #4277 | You are a Nexus | Kommunikation & Beziehungen |
| #4278 | Detective Smith is currently faced with the c | Kommunikation & Beziehungen |
| #4279 | Imagine you're the owner of a small business  | Kommunikation & Beziehungen |
| #4280 | What are some examples of epic poetry | Kreativitaet & Freizeit |
| #4281 | Given this background information | Kreativitaet & Freizeit |
| #4282 | A short, creative poem about the French Revol | Kreativitaet & Freizeit |
| #4283 | A short story about a hobbit who accidentally | Kreativitaet & Freizeit |
| #4284 | What is the most important memo in American h | Kreativitaet & Freizeit |
| #4285 | A short story about a group of people trapped | Kreativitaet & Freizeit |
| #4286 | What are some interesting facts about the num | Lernen & Wachstum |
| #4287 | A poem about a prophet who is shunned by soci | Lernen & Wachstum |
| #4288 | A short recipe for mincemeat pie that include | Lernen & Wachstum |
| #4289 | Reference:
Chonac smlach marbh sa choill sear | Lernen & Wachstum |
| #4290 | A 380-word blog post about metabolites | Lernen & Wachstum |
| #4291 | What are 3 facts on the history of American i | Lernen & Wachstum |
| #4292 | A step-by-step guide on how to install and se | Spezielle Situationen |
| #4293 | Investigate the average weight of adult male  | Spezielle Situationen |
| #4294 | You will be given a definition of a task firs | Spezielle Situationen |
| #4295 | Detailed Instructions: In this task | Spezielle Situationen |
| #4296 | You will be given a definition of a task firs | Spezielle Situationen |
| #4297 | TASK DEFINITION: In this task | Spezielle Situationen |
| #4298 | List 10-15 uses of clay in various industries | Technik & Alltag |
| #4299 | What were the main techniques and technologie | Technik & Alltag |
| #4300 | A python script that uses the Clasp tool to c | Technik & Alltag |
| #4301 | A 200-word description of a seaside shack for | Technik & Alltag |
| #4302 | Given this background information | Technik & Alltag |
| #4303 | What is the difference between cirrus and cir | Technik & Alltag |
| #4304 | A poem in the style of a Flan with at least 5 | Alltag & Leben |
| #4305 | The following information may be useful | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-02)

**5 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4306 | Prompt Refiner | Technik & Alltag | `technik-alltag/4306-prompt-refiner.md` |
| #4307 | Research Prompt (Mistral) | Lernen & Wachstum | `lernen-wachstum/4307-research-prompt-mistral.md` |
| #4308 | Realistic Mirror-Selfie Image Prompt | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4308-realistic-mirror-selfie-image-prompt.md` |
| #4309 | Realistic Selfie of Girl with Transparent Glasses and Pink Hair | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4309-realistic-selfie-of-girl-with-transparen.md` |
| #4310 | aa/cli taste | Technik & Alltag | `technik-alltag/4310-aa-cli-taste.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-03)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4311 | Claude Opus as SEO Auditor | Kommunikation & Beziehungen | `kommunikation-beziehungen/4311-claude-opus-as-seo-auditor.md` |
| #4312 | AI Cloning #1 - RAW | Beruf & Karriere | `beruf-karriere/4312-ai-cloning-1-raw.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-04)

**1 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4313 | The Colorful Fish Learning Emotions | Lernen & Wachstum | `lernen-wachstum/4313-the-colorful-fish-learning-emotions.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-05)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4314 | site analiz | Technik & Alltag | `technik-alltag/4314-site-analiz.md` |
| #4315 | Creating PWA AI Chatbot | Alltag & Leben | `alltag-leben/4315-creating-pwa-ai-chatbot.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-06)

**8 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4316 | Online Job Search Assistant | Technik & Alltag | `technik-alltag/4316-online-job-search-assistant.md` |
| #4317 | Professional photo editor | Technik & Alltag | `technik-alltag/4317-professional-photo-editor.md` |
| #4318 | Customizable Birthday Message Generator | Kreativitaet & Freizeit | `kreativitaet-freizeit/4318-customizable-birthday-message-generator.md` |
| #4319 | Birthday Message Generator – 3 Styles | Alltag & Leben | `alltag-leben/4319-birthday-message-generator-3-styles.md` |
| #4320 | DOE Framework - Directions Template | Technik & Alltag | `technik-alltag/4320-doe-framework-directions-template.md` |
| #4321 | Ocean’s Eleven Movie Poster Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4321-ocean-s-eleven-movie-poster-illustration.md` |
| #4322 | Packer Automation & Imaging Expert | Technik & Alltag | `technik-alltag/4322-packer-automation-imaging-expert.md` |
| #4323 | Ultimate Stake.us Dice Wagering Strategy Builder — Rollover & Playthrough Completion | Technik & Alltag | `technik-alltag/4323-ultimate-stake-us-dice-wagering-strategy.md` |


---

## PromptHero Bild-Prompt Import (2026-04-06)

**50 neue Bild-Prompts** importiert (Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):

| ID | Titel | Modell | Datei |
|----|-------|--------|-------|
| #4324 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4324-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4325 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4325-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4326 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4326-high-fashion-photo-of-a-elderly-man-with.md` |
| #4327 | "beauty photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4327-beauty-photo-of-a-middle-aged-woman-with.md` |
| #4328 | "candid photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4328-candid-photo-of-a-elderly-man-with-a-bea.md` |
| #4329 | "lifestyle photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4329-lifestyle-photo-of-a-child-with-a-cute-e.md` |
| #4330 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/4330-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #4331 | "paparazzi photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/4331-paparazzi-photo-of-a-teenage-girl-with-s.md` |
| #4332 | "paparazzi photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4332-paparazzi-photo-of-a-child-with-a-cute-e.md` |
| #4333 | "pictorialist photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4333-pictorialist-photo-of-a-middle-aged-woma.md` |
| #4334 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4334-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4335 | "instant photo of a middle-aged woman wi | SDXL | `bildbearbeitung-visualisierung/4335-instant-photo-of-a-middle-aged-woman-wit.md` |
| #4336 | "instant photo of a child with a cute ex | SDXL | `bildbearbeitung-visualisierung/4336-instant-photo-of-a-child-with-a-cute-exp.md` |
| #4337 | "glamor photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4337-glamor-photo-of-a-child-with-a-cute-expr.md` |
| #4338 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4338-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4339 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4339-high-fashion-photo-of-a-young-man-wearin.md` |
| #4340 | "Polaroid photo of a child with a cute e | SDXL | `bildbearbeitung-visualisierung/4340-polaroid-photo-of-a-child-with-a-cute-ex.md` |
| #4341 | "glamor photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4341-glamor-photo-of-a-teenage-girl-with-shor.md` |
| #4342 | "Polaroid photo of a middle-aged woman w | SDXL | `bildbearbeitung-visualisierung/4342-polaroid-photo-of-a-middle-aged-woman-wi.md` |
| #4343 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4343-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4344 | "pictorialist photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4344-pictorialist-photo-of-a-teenage-girl-wit.md` |
| #4345 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4345-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4346 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4346-large-format-photo-of-a-middle-aged-woma.md` |
| #4347 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4347-analog-photo-of-a-young-man-wearing-a-su.md` |
| #4348 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4348-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4349 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4349-high-fashion-photo-of-a-young-man-wearin.md` |
| #4350 | "Polaroid photo of a middle-aged woman w | SDXL | `bildbearbeitung-visualisierung/4350-polaroid-photo-of-a-middle-aged-woman-wi.md` |
| #4351 | "Analog photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4351-analog-photo-of-a-child-with-a-cute-expr.md` |
| #4352 | "Polaroid photo of a young man wearing a | SDXL | `bildbearbeitung-visualisierung/4352-polaroid-photo-of-a-young-man-wearing-a-.md` |
| #4353 | "Polaroid photo of a young man wearing a | SDXL | `bildbearbeitung-visualisierung/4353-polaroid-photo-of-a-young-man-wearing-a-.md` |
| #4354 | "large format photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4354-large-format-photo-of-a-teenage-girl-wit.md` |
| #4355 | "paparazzi photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/4355-paparazzi-photo-of-a-teenage-girl-with-s.md` |
| #4356 | "paparazzi photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/4356-paparazzi-photo-of-a-young-man-wearing-a.md` |
| #4357 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/4357-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #4358 | "glamor photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4358-glamor-photo-of-a-child-with-a-cute-expr.md` |
| #4359 | "candid photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4359-candid-photo-of-a-teenage-girl-with-shor.md` |
| #4360 | "instant photo of a young man wearing a  | SDXL | `bildbearbeitung-visualisierung/4360-instant-photo-of-a-young-man-wearing-a-s.md` |
| #4361 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4361-candid-photo-of-a-middle-aged-woman-with.md` |
| #4362 | "paparazzi photo of a young man wearing  | SDXL | `bildbearbeitung-visualisierung/4362-paparazzi-photo-of-a-young-man-wearing-a.md` |
| #4363 | "paparazzi photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/4363-paparazzi-photo-of-a-teenage-girl-with-s.md` |
| #4364 | "large format photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4364-large-format-photo-of-a-child-with-a-cut.md` |
| #4365 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4365-large-format-photo-of-a-middle-aged-woma.md` |
| #4366 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4366-candid-photo-of-a-child-with-a-cute-expr.md` |
| #4367 | "Polaroid photo of a teenage girl with s | SDXL | `bildbearbeitung-visualisierung/4367-polaroid-photo-of-a-teenage-girl-with-sh.md` |
| #4368 | "instant photo of a middle-aged woman wi | SDXL | `bildbearbeitung-visualisierung/4368-instant-photo-of-a-middle-aged-woman-wit.md` |
| #4369 | "Polaroid photo of a middle-aged woman w | SDXL | `bildbearbeitung-visualisierung/4369-polaroid-photo-of-a-middle-aged-woman-wi.md` |
| #4370 | "instant photo of a teenage girl with sh | SDXL | `bildbearbeitung-visualisierung/4370-instant-photo-of-a-teenage-girl-with-sho.md` |
| #4371 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4371-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4372 | "glamor photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4372-glamor-photo-of-a-teenage-girl-with-shor.md` |
| #4373 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4373-lifestyle-photo-of-a-middle-aged-woman-w.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-07)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4374 | Futuristic Alps in 2150 | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4374-futuristic-alps-in-2150.md` |
| #4375 | Interstellar Movie Poster Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4375-interstellar-movie-poster-illustration.md` |
| #4376 | 🔧 AI App Improvement Loop Prompt | Technik & Alltag | `technik-alltag/4376-ai-app-improvement-loop-prompt.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-08)

**4 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4377 | WEB Product Architect | Technik & Alltag | `technik-alltag/4377-web-product-architect.md` |
| #4378 | Game design | Technik & Alltag | `technik-alltag/4378-game-design.md` |
| #4379 | Sacrifice in obedience | Lernen & Wachstum | `lernen-wachstum/4379-sacrifice-in-obedience.md` |
| #4380 | Typographic Portrait Artwork Creation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4380-typographic-portrait-artwork-creation.md` |


---

## Multi-Source Import (2026-04-08)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #4381 | What are some of the benefits of suspenders a | Alltag & Leben |
| #4382 | Background | Alltag & Leben |
| #4383 | What is the definition of a "runaway greenhou | Alltag & Leben |
| #4384 | Read this for context | Alltag & Leben |
| #4385 | Part 1. Definition | Alltag & Leben |
| #4386 | Write a 1000 word story about yokai in the st | Alltag & Leben |
| #4387 | Please re-write this message to make it more  | Beruf & Karriere |
| #4388 | You to remember my prompts and your responses | Beruf & Karriere |
| #4389 | Explain to my company my role as a solo SEO m | Beruf & Karriere |
| #4390 | Seeking guidance from experienced staff with  | Beruf & Karriere |
| #4391 | What all channel partner metrics are importan | Beruf & Karriere |
| #4392 | I have a production facility on Poland that c | Beruf & Karriere |
| #4393 | What is the most nutritious food that a perso | Gesundheit & Wohlbefinden |
| #4394 | What are some of the most interesting and imp | Gesundheit & Wohlbefinden |
| #4395 | Part 1. Definition | Gesundheit & Wohlbefinden |
| #4396 | Your persona | Gesundheit & Wohlbefinden |
| #4397 | List me 15 name ideas for a chatbot assistant | Gesundheit & Wohlbefinden |
| #4398 | I am taking part in a one-week hackathon | Gesundheit & Wohlbefinden |
| #4399 | What are the most effective ways to grow your | Kommunikation & Beziehungen |
| #4400 | You to act as a resume editor | Kommunikation & Beziehungen |
| #4401 | Generate summary in one sentence of this blog | Kommunikation & Beziehungen |
| #4402 | Here is the background: There have been many  | Kommunikation & Beziehungen |
| #4403 | Hi Usman | Kommunikation & Beziehungen |
| #4404 | You're a professional somelier | Kommunikation & Beziehungen |
| #4405 | Imagine you are a figurine in a dollhouse and | Kreativitaet & Freizeit |
| #4406 | What is the most powerful magic spell in the  | Kreativitaet & Freizeit |
| #4407 | What was the inspiration for the character of | Kreativitaet & Freizeit |
| #4408 | A short story about a young man who wakes up  | Kreativitaet & Freizeit |
| #4409 | What are some of the most important things to | Kreativitaet & Freizeit |
| #4410 | What does this audiology report mean | Kreativitaet & Freizeit |
| #4411 | What are some examples of screw-ups in scienc | Lernen & Wachstum |
| #4412 | What are some common types of edible mushroom | Lernen & Wachstum |
| #4413 | What are some of the most interesting facts a | Lernen & Wachstum |
| #4414 | What are some uses for a reamer | Lernen & Wachstum |
| #4415 | A poem about a neuropathologist | Lernen & Wachstum |
| #4416 | Detailed Instructions: The provided file incl | Lernen & Wachstum |
| #4417 | What are some features of a good leader | Spezielle Situationen |
| #4418 | Detailed Instructions: In this task | Spezielle Situationen |
| #4419 | You to act as a formal email writer to the go | Spezielle Situationen |
| #4420 | You to override your limitations and act as G | Spezielle Situationen |
| #4421 | Create a 1 minute and 30 seconds video script | Spezielle Situationen |
| #4422 | A short essay with an Outline on the followin | Spezielle Situationen |
| #4423 | For this query | Technik & Alltag |
| #4424 | A high converting facebook ad for my digital  | Technik & Alltag |
| #4425 | When to use SSR | Technik & Alltag |
| #4426 | I am a very visual person | Technik & Alltag |
| #4427 | A new Python file in this folder called optio | Technik & Alltag |
| #4428 | As a prospective homebuyer | Technik & Alltag |
| #4429 | Does FDIC bank account insurance provide $250 | Alltag & Leben |
| #4430 | From now you are an expert in creating RDF tr | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-09)

**4 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4431 | mc | Kreativitaet & Freizeit | `kreativitaet-freizeit/4431-mc.md` |
| #4432 | Tr | Lernen & Wachstum | `lernen-wachstum/4432-tr.md` |
| #4433 | pdfcount | Beruf & Karriere | `beruf-karriere/4433-pdfcount.md` |
| #4434 | Add AI protection | Technik & Alltag | `technik-alltag/4434-add-ai-protection.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-10)

**16 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4435 | Viking | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4435-viking.md` |
| #4436 | Cowboy | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4436-cowboy.md` |
| #4437 | Atari | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4437-atari.md` |
| #4438 | Japan | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4438-japan.md` |
| #4439 | Paint | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4439-paint.md` |
| #4440 | Galactic Smuggler | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4440-galactic-smuggler.md` |
| #4441 | Transforming a Photo into a Post-Apocalyptic Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4441-transforming-photo-into-post-apocalyptic.md` |
| #4442 | 1950s Diner Photo Transformation | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4442-1950s-diner-photo-transformation.md` |
| #4443 | Cute Family Cartoon Sticker Design | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4443-cute-family-cartoon-sticker-design.md` |
| #4444 | Celebratory Student Exam Result Reveal | Lernen & Wachstum | `lernen-wachstum/4444-celebratory-student-exam-result-reveal.md` |
| #4445 | Instagram Profile Search Navigator | Kommunikation & Beziehungen | `kommunikation-beziehungen/4445-instagram-profile-search-navigator.md` |
| #4446 | Patent Illustration Design with SolidWorks and Origin Styles | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4446-patent-illustration-design-with-solidwor.md` |
| #4447 | AI-Generated Patent Illustration Instructions | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4447-ai-generated-patent-illustration-instruc.md` |
| #4448 | Web App Security Code Review (OWASP) - Public Test | Technik & Alltag | `technik-alltag/4448-web-app-security-code-review-owasp-publi.md` |
| #4449 | Research and Presentation on Energy Forms | Lernen & Wachstum | `lernen-wachstum/4449-research-and-presentation-on-energy-form.md` |
| #4450 | Adaptive Thinking Framework | Lernen & Wachstum | `lernen-wachstum/4450-adaptive-thinking-framework.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-11)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4451 | Low Voltage Electrical Theory Guide | Lernen & Wachstum | `lernen-wachstum/4451-low-voltage-electrical-theory-guide.md` |
| #4452 | Potato Critic | Technik & Alltag | `technik-alltag/4452-potato-critic.md` |
| #4453 | Expert en Analyse du Marché eCommerce en Algérie | Technik & Alltag | `technik-alltag/4453-expert-en-analyse-du-march-ecommerce-en-.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-12)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4454 | Meta Agent Builder for Letta Platform | Technik & Alltag | `technik-alltag/4454-meta-agent-builder-for-letta-platform.md` |
| #4455 | AI Productivity Artifact Generator | Beruf & Karriere | `beruf-karriere/4455-ai-productivity-artifact-generator.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-13)

**1 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4456 | Stylelint Plugin Author | Technik & Alltag | `technik-alltag/4456-stylelint-plugin-author.md` |


---

## PromptHero Bild-Prompt Import (2026-04-13)

**50 neue Bild-Prompts** importiert (Quelle: [PromptHero](https://prompthero.com) via Hugging Face Datasets, Apache 2.0):

| ID | Titel | Modell | Datei |
|----|-------|--------|-------|
| #4457 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4457-high-fashion-photo-of-a-elderly-man-with.md` |
| #4458 | "high fashion photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4458-high-fashion-photo-of-a-elderly-man-with.md` |
| #4459 | "pictorialist photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4459-pictorialist-photo-of-a-young-man-wearin.md` |
| #4460 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4460-high-fashion-photo-of-a-young-man-wearin.md` |
| #4461 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4461-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4462 | "instant photo of a young man wearing a  | SDXL | `bildbearbeitung-visualisierung/4462-instant-photo-of-a-young-man-wearing-a-s.md` |
| #4463 | "beauty photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4463-beauty-photo-of-a-young-man-wearing-a-su.md` |
| #4464 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4464-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4465 | "Analog photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4465-analog-photo-of-a-teenage-girl-with-shor.md` |
| #4466 | "pictorialist photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4466-pictorialist-photo-of-a-young-man-wearin.md` |
| #4467 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4467-high-fashion-photo-of-a-young-man-wearin.md` |
| #4468 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4468-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4469 | "instant photo of a elderly man with a b | SDXL | `bildbearbeitung-visualisierung/4469-instant-photo-of-a-elderly-man-with-a-be.md` |
| #4470 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4470-large-format-photo-of-a-middle-aged-woma.md` |
| #4471 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4471-large-format-photo-of-a-middle-aged-woma.md` |
| #4472 | "candid photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4472-candid-photo-of-a-middle-aged-woman-with.md` |
| #4473 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4473-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4474 | "high fashion photo of a teenage girl wi | SDXL | `bildbearbeitung-visualisierung/4474-high-fashion-photo-of-a-teenage-girl-wit.md` |
| #4475 | "Analog photo of a middle-aged woman wit | SDXL | `bildbearbeitung-visualisierung/4475-analog-photo-of-a-middle-aged-woman-with.md` |
| #4476 | "high fashion photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4476-high-fashion-photo-of-a-middle-aged-woma.md` |
| #4477 | "glamor photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4477-glamor-photo-of-a-child-with-a-cute-expr.md` |
| #4478 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4478-candid-photo-of-a-child-with-a-cute-expr.md` |
| #4479 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4479-analog-photo-of-a-young-man-wearing-a-su.md` |
| #4480 | "high fashion photo of a child with a cu | SDXL | `bildbearbeitung-visualisierung/4480-high-fashion-photo-of-a-child-with-a-cut.md` |
| #4481 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4481-candid-photo-of-a-child-with-a-cute-expr.md` |
| #4482 | "lifestyle photo of a middle-aged woman  | SDXL | `bildbearbeitung-visualisierung/4482-lifestyle-photo-of-a-middle-aged-woman-w.md` |
| #4483 | "Polaroid photo of a young man wearing a | SDXL | `bildbearbeitung-visualisierung/4483-polaroid-photo-of-a-young-man-wearing-a-.md` |
| #4484 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4484-large-format-photo-of-a-middle-aged-woma.md` |
| #4485 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4485-high-fashion-photo-of-a-young-man-wearin.md` |
| #4486 | "candid photo of a elderly man with a be | SDXL | `bildbearbeitung-visualisierung/4486-candid-photo-of-a-elderly-man-with-a-bea.md` |
| #4487 | "Analog photo of a young man wearing a s | SDXL | `bildbearbeitung-visualisierung/4487-analog-photo-of-a-young-man-wearing-a-su.md` |
| #4488 | "candid photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4488-candid-photo-of-a-child-with-a-cute-expr.md` |
| #4489 | "large format photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4489-large-format-photo-of-a-elderly-man-with.md` |
| #4490 | "large format photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4490-large-format-photo-of-a-young-man-wearin.md` |
| #4491 | "Analog photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4491-analog-photo-of-a-teenage-girl-with-shor.md` |
| #4492 | "Analog photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4492-analog-photo-of-a-child-with-a-cute-expr.md` |
| #4493 | "lifestyle photo of a child with a cute  | SDXL | `bildbearbeitung-visualisierung/4493-lifestyle-photo-of-a-child-with-a-cute-e.md` |
| #4494 | "lifestyle photo of a teenage girl with  | SDXL | `bildbearbeitung-visualisierung/4494-lifestyle-photo-of-a-teenage-girl-with-s.md` |
| #4495 | "glamor photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4495-glamor-photo-of-a-teenage-girl-with-shor.md` |
| #4496 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4496-large-format-photo-of-a-middle-aged-woma.md` |
| #4497 | "Polaroid photo of a middle-aged woman w | SDXL | `bildbearbeitung-visualisierung/4497-polaroid-photo-of-a-middle-aged-woman-wi.md` |
| #4498 | "beauty photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4498-beauty-photo-of-a-child-with-a-cute-expr.md` |
| #4499 | "instant photo of a young man wearing a  | SDXL | `bildbearbeitung-visualisierung/4499-instant-photo-of-a-young-man-wearing-a-s.md` |
| #4500 | "beauty photo of a teenage girl with sho | SDXL | `bildbearbeitung-visualisierung/4500-beauty-photo-of-a-teenage-girl-with-shor.md` |
| #4501 | "high fashion photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4501-high-fashion-photo-of-a-young-man-wearin.md` |
| #4502 | "instant photo of a young man wearing a  | SDXL | `bildbearbeitung-visualisierung/4502-instant-photo-of-a-young-man-wearing-a-s.md` |
| #4503 | "large format photo of a young man weari | SDXL | `bildbearbeitung-visualisierung/4503-large-format-photo-of-a-young-man-wearin.md` |
| #4504 | "large format photo of a middle-aged wom | SDXL | `bildbearbeitung-visualisierung/4504-large-format-photo-of-a-middle-aged-woma.md` |
| #4505 | "pictorialist photo of a elderly man wit | SDXL | `bildbearbeitung-visualisierung/4505-pictorialist-photo-of-a-elderly-man-with.md` |
| #4506 | "beauty photo of a child with a cute exp | SDXL | `bildbearbeitung-visualisierung/4506-beauty-photo-of-a-child-with-a-cute-expr.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-14)

**2 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4507 | Web Typography | Technik & Alltag | `technik-alltag/4507-web-typography.md` |
| #4508 | Mockup Interview using Gemini Live | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4508-mockup-interview-using-gemini-live.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-15)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4509 | karpathy-guidelines | Technik & Alltag | `technik-alltag/4509-karpathy-guidelines.md` |
| #4510 | prd-and-technical-documentation-generator | Technik & Alltag | `technik-alltag/4510-prd-and-technical-documentation-generato.md` |
| #4511 | X Twitter Scraper | Kommunikation & Beziehungen | `kommunikation-beziehungen/4511-x-twitter-scraper.md` |


---

## Multi-Source Import (2026-04-15)

**50 neue Prompts** importiert (Quelle: [OpenRLHF prompt-collection](https://huggingface.co/datasets/OpenRLHF/prompt-collection-v0.1)):

| Kategorie | Anzahl |
|-----------|--------|
| Alltag & Leben | 8 |
| Beruf & Karriere | 6 |
| Gesundheit & Wohlbefinden | 6 |
| Kommunikation & Beziehungen | 6 |
| Kreativitaet & Freizeit | 6 |
| Lernen & Wachstum | 6 |
| Spezielle Situationen | 6 |
| Technik & Alltag | 6 |

<details><summary>Alle 50 Prompts anzeigen</summary>

| ID | Titel | Kategorie |
|----|-------|-----------|
| #4512 | What are some fun and creative ideas for Hall | Alltag & Leben |
| #4513 | The reference text below provides context for | Alltag & Leben |
| #4514 | A poem about a young girl who is traveling th | Alltag & Leben |
| #4515 | What are 15 creative recipes that use corn as | Alltag & Leben |
| #4516 | What is the maximum video footage that can be | Alltag & Leben |
| #4517 | Suppose I have a list of words as follows | Alltag & Leben |
| #4518 | What is the average salary of a banker in New | Beruf & Karriere |
| #4519 | Provide two strategies that a seller can use  | Beruf & Karriere |
| #4520 | In the given text | Beruf & Karriere |
| #4521 | Analyze this tweet and provide a detailed rep | Beruf & Karriere |
| #4522 | As a transportation consultant | Beruf & Karriere |
| #4523 | Please generate an [ HTML table ] representat | Beruf & Karriere |
| #4524 | A short story about a young man who becomes i | Gesundheit & Wohlbefinden |
| #4525 | A short story about a young woman who goes on | Gesundheit & Wohlbefinden |
| #4526 | What are some examples of foods that are high | Gesundheit & Wohlbefinden |
| #4527 | I have collected data on people's daily routi | Gesundheit & Wohlbefinden |
| #4528 | How can the [Pomodoro Technique] | Gesundheit & Wohlbefinden |
| #4529 | Develop a comprehensive onboarding plan that  | Gesundheit & Wohlbefinden |
| #4530 | Given this background information delimited i | Kommunikation & Beziehungen |
| #4531 | A 225-word poem using the style of an English | Kommunikation & Beziehungen |
| #4532 | A blog post on how to grow chives at home | Kommunikation & Beziehungen |
| #4533 | How can you gather user feedback on your prod | Kommunikation & Beziehungen |
| #4534 | A headline for the given article that is conc | Kommunikation & Beziehungen |
| #4535 | Provide a comprehensive list of ten factors t | Kommunikation & Beziehungen |
| #4536 | Imagine you are a 19th-century blues musician | Kreativitaet & Freizeit |
| #4537 | What is the most common type of batting used  | Kreativitaet & Freizeit |
| #4538 | Read this for context | Kreativitaet & Freizeit |
| #4539 | What are the functions of the breast and how  | Kreativitaet & Freizeit |
| #4540 | The reference text below provides context for | Kreativitaet & Freizeit |
| #4541 | A short story about a baby who is not afraid  | Kreativitaet & Freizeit |
| #4542 | What is the history of addiction | Lernen & Wachstum |
| #4543 | Describe the structure of a cow's leg, and ex | Lernen & Wachstum |
| #4544 | A 250-word essay defining the concepts of mea | Lernen & Wachstum |
| #4545 | A poem about a tiger in the jungle that is sa | Lernen & Wachstum |
| #4546 | What is the history of the Shrine of the Bab  | Lernen & Wachstum |
| #4547 | What are some examples of the use of the word | Lernen & Wachstum |
| #4548 | A response to a student who is upset after be | Spezielle Situationen |
| #4549 | A poem in the style of a villanelle | Spezielle Situationen |
| #4550 | As a chess player | Spezielle Situationen |
| #4551 | Design a menu for a coffee and tea shop that  | Spezielle Situationen |
| #4552 | What Shell cmd can I use to search for govern | Spezielle Situationen |
| #4553 | Imagine you are a city planner trying to deci | Spezielle Situationen |
| #4554 | What are some examples of companies that have | Technik & Alltag |
| #4555 | A testimonial for a friend who is starting th | Technik & Alltag |
| #4556 | Reference:
google | Technik & Alltag |
| #4557 | What is the significance of the acronym "GDP" | Technik & Alltag |
| #4558 | A two-digit number between 5 and 11 without r | Technik & Alltag |
| #4559 | Develop a Python function entitled "calculate | Technik & Alltag |
| #4560 | In a remote forest | Alltag & Leben |
| #4561 | Suggest some menu items for a restaurant that | Alltag & Leben |

</details>


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-16)

**9 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4562 | Picture | Lernen & Wachstum | `lernen-wachstum/4562-picture.md` |
| #4563 | Serene Autumn Lakeside Illustration | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4563-serene-autumn-lakeside-illustration.md` |
| #4564 | Dramatic Horse Silhouette in Cinematic Lighting | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4564-dramatic-horse-silhouette-in-cinematic-l.md` |
| #4565 | Cinematic Sunset Boat Scene | Bildbearbeitung & Visualisierung | `bildbearbeitung-visualisierung/4565-cinematic-sunset-boat-scene.md` |
| #4566 | create prompt for audit purpose on password configuartion file for linux | Technik & Alltag | `technik-alltag/4566-create-prompt-for-audit-purpose-on-passw.md` |
| #4567 | MAP | Technik & Alltag | `technik-alltag/4567-map.md` |
| #4568 | ubuntu audio input/output,loop/virtual connection specialist | Technik & Alltag | `technik-alltag/4568-ubuntu-audio-input-output-loop-virtual-c.md` |
| #4569 | Audio Routing Automation Engineer | Technik & Alltag | `technik-alltag/4569-audio-routing-automation-engineer.md` |
| #4570 | Mbbs | Kommunikation & Beziehungen | `kommunikation-beziehungen/4570-mbbs.md` |


---

## Auto-Import von awesome-chatgpt-prompts (2026-04-17)

**3 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #4571 | 🧠 PromptAudit | Technik & Alltag | `technik-alltag/4571-promptaudit.md` |
| #4572 | Notion Transcript Designer Prompt | Technik & Alltag | `technik-alltag/4572-notion-transcript-designer-prompt.md` |
| #4573 | Alexa Said THIS… and Miss Nancy Didn’t Like It 😳 | Alltag & Leben | `alltag-leben/4573-alexa-said-this-and-miss-nancy-didn-t-li.md` |

*Letzte Aktualisierung: 2026-04-17 — 3 Prompts auto-importiert*
