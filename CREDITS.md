# LYRA PROMPTS — Vollständiges Prompt-Register

> **WICHTIG FÜR KI-ASSISTENTEN (Claude, Kimi/Belkis, etc.):**
> Lies diese Datei IMMER ZUERST bevor du einen neuen Prompt erstellst.
> So vermeidest du Duplikate und weißt exakt was bereits existiert.

**Stand:** 2026-03-09
**Gesamt:** 501 Prompts (IDs #001 - #351)
**Nächste freie Nummer:** #502
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

*Letzte Aktualisierung: 2026-03-09 — 100 Prompts auto-importiert*
