# LYRA PROMPTS — Vollständiges Prompt-Register

> **WICHTIG FÜR KI-ASSISTENTEN (Claude, Kimi/Belkis, etc.):**
> Lies diese Datei IMMER ZUERST bevor du einen neuen Prompt erstellst.
> So vermeidest du Duplikate und weißt exakt was bereits existiert.

**Stand:** 2026-03-09
**Gesamt:** 1034 Prompts (IDs #001 - #351)
**Nächste freie Nummer:** #1035
**Prompt-Karte:** Siehe `PROMPT-MAP.md` für vollständige Kartierung aller Prompts

---

## ID-System

- Jeder Prompt hat eine eindeutige ID: `#001` bis `#XXX`
- IDs werden NIE wiederverwendet (auch wenn ein Prompt gelöscht wird)
- Neue Prompts bekommen immer die nächste freie Nummer
- Die ID steht in der ersten Zeile jeder Prompt-Datei im YAML-Frontmatter: `id: "#XXX"`
- Alle Prompt-Dateien haben eindeutige IDs und einheitlich formatierte Titel mit Anführungszeichen

---

## Kategorien-Übersicht

| Kategorie | Anzahl Prompts | IDs |
|-----------|----------------|-----|
| Alltag & Leben | 37 | #001-#035, #304-#306 |
| Beruf & Karriere | 30 | #036-#062, #321-#323 |
| Bildbearbeitung & Visualisierung | 88 | #063-#132, #309-#319, #324-#325, #347-#351 |
| Gesundheit & Wohlbefinden | 29 | #133-#159, #326-#328 |
| Kommunikation & Beziehungen | 23 | #160-#179, #307, #329-#330 |
| Kreativität & Freizeit | 27 | #180-#203, #331-#333 |
| Lernen & Wachstum | 28 | #204-#228, #308, #334-#335 |
| Professionell & Business | 45 | #229-#267, #320, #342-#346 |
| Spezielle Situationen | 20 | #268-#284, #336-#338 |
| Technik & Alltag | 22 | #285-#303, #339-#341 |

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

**50 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

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


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-09)

**100 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
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


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-09)

**500 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
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


---

## Auto-Import von awesome-chatgpt-prompts (2026-03-09)

**33 neue Prompts** automatisch importiert (Quelle: [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), CC0 Lizenz):

| ID | Titel | Kategorie | Datei |
|----|-------|-----------|-------|
| #1002 | İngilizce-Türkçe Kelime ve Cümle Çevirmeni | Lernen & Wachstum | `lernen-wachstum/1002-i-ngilizce-t-rk-e-kelime-ve-c-mle-evirme.md` |
| #1003 | Language Detection | Lernen & Wachstum | `lernen-wachstum/1003-language-detection.md` |
| #1004 | English Language Tutor for Turkish Speakers | Lernen & Wachstum | `lernen-wachstum/1004-english-language-tutor-for-turkish-speak.md` |
| #1005 | NBX | Lernen & Wachstum | `lernen-wachstum/1005-nbx.md` |
| #1006 | 2026 Size Neler getirecek | Lernen & Wachstum | `lernen-wachstum/1006-2026-size-neler-getirecek.md` |
| #1007 | Ultimate 2025-2026 AI Life Strategist & Retrospective | Lernen & Wachstum | `lernen-wachstum/1007-ultimate-2025-2026-ai-life-strategist-re.md` |
| #1008 | Innovative Math Teaching Method | Lernen & Wachstum | `lernen-wachstum/1008-innovative-math-teaching-method.md` |
| #1009 | Act as a Base LLM Model | Lernen & Wachstum | `lernen-wachstum/1009-base-llm-model.md` |
| #1010 | Digital Marketing Project Ideas for Students | Lernen & Wachstum | `lernen-wachstum/1010-digital-marketing-project-ideas-for-stud.md` |
| #1011 | Educational Platform Support Assistant | Lernen & Wachstum | `lernen-wachstum/1011-educational-platform-support-assistant.md` |
| #1012 | Understanding and Utilizing LLMs | Lernen & Wachstum | `lernen-wachstum/1012-understanding-and-utilizing-llms.md` |
| #1013 | SQL Query Generator from Natural Language | Lernen & Wachstum | `lernen-wachstum/1013-sql-query-generator-from-natural-languag.md` |
| #1014 | School Life Mentor | Lernen & Wachstum | `lernen-wachstum/1014-school-life-mentor.md` |
| #1015 | Viral TikTok Glühwein Recipe in Five Languages | Lernen & Wachstum | `lernen-wachstum/1015-viral-tiktok-gl-hwein-recipe-in-five-lan.md` |
| #1016 | professional linguistic expert and translator | Lernen & Wachstum | `lernen-wachstum/1016-professional-linguistic-expert-and-trans.md` |
| #1017 | AI Process Feasibility Interview | Lernen & Wachstum | `lernen-wachstum/1017-ai-process-feasibility-interview.md` |
| #1018 | 12-Month AI and Computer Vision Roadmap for Defense Applications | Lernen & Wachstum | `lernen-wachstum/1018-12-month-ai-and-computer-vision-roadmap-.md` |
| #1019 | Chinese-English Translator | Lernen & Wachstum | `lernen-wachstum/1019-chinese-english-translator.md` |
| #1020 | Multilingual Writing Improvement Assistant | Lernen & Wachstum | `lernen-wachstum/1020-multilingual-writing-improvement-assista.md` |
| #1021 | Prompt Generator for Language Models | Lernen & Wachstum | `lernen-wachstum/1021-prompt-generator-for-language-models.md` |
| #1022 | “How It Works” Educational Dioramas | Lernen & Wachstum | `lernen-wachstum/1022-how-it-works-educational-dioramas.md` |
| #1023 | Workplace English Speaking Coach | Lernen & Wachstum | `lernen-wachstum/1023-workplace-english-speaking-coach.md` |
| #1024 | Create Infographics | Lernen & Wachstum | `lernen-wachstum/1024-create-infographics.md` |
| #1025 | Professional Networking Language for Career Fairs | Lernen & Wachstum | `lernen-wachstum/1025-professional-networking-language-for-car.md` |
| #1026 | Coach for Identifying Growth-Limiting Patterns | Lernen & Wachstum | `lernen-wachstum/1026-coach-for-identifying-growth-limiting-pa.md` |
| #1027 | Driftcraft | Lernen & Wachstum | `lernen-wachstum/1027-driftcraft.md` |
| #1028 | Socratic Universal Tutor | Lernen & Wachstum | `lernen-wachstum/1028-socratic-universal-tutor.md` |
| #1029 | Chinese to English Translation Proofreading Expert | Lernen & Wachstum | `lernen-wachstum/1029-chinese-to-english-translation-proofread.md` |
| #1030 | Cinematic Video Essay Director | Lernen & Wachstum | `lernen-wachstum/1030-cinematic-video-essay-director.md` |
| #1031 | Voice Conversation Coach | Lernen & Wachstum | `lernen-wachstum/1031-voice-conversation-coach.md` |
| #1032 | Make AI responses sound more Human-like | Lernen & Wachstum | `lernen-wachstum/1032-make-ai-responses-sound-more-human-like.md` |
| #1033 | Code Translator — Idiomatic, Version-Aware & Production-Ready | Lernen & Wachstum | `lernen-wachstum/1033-code-translator-idiomatic-version-aware-.md` |
| #1034 | Fazer miniatura de coisas/moleculas | Lernen & Wachstum | `lernen-wachstum/1034-fazer-miniatura-de-coisas-moleculas.md` |

*Letzte Aktualisierung: 2026-03-09 — 33 Prompts auto-importiert*
