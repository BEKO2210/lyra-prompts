# LYRA PROMPTS — Vollständiges Prompt-Register

> **WICHTIG FÜR KI-ASSISTENTEN (Claude, Kimi/Belkis, etc.):**
> Lies diese Datei IMMER ZUERST bevor du einen neuen Prompt erstellst.
> So vermeidest du Duplikate und weißt exakt was bereits existiert.

**Stand:** 2026-03-09
**Gesamt:** 351 Prompts (IDs #001 - #351)
**Nächste freie Nummer:** #352
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

*Letzte Aktualisierung: 2026-03-09 — 5 kunstvolle Bild-Prompts hinzugefügt (#347-#351)*
