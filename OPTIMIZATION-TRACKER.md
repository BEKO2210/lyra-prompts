# Lyra 4-D Optimierung — Batch-Tracker

> **Stand:** 2026-03-11 | **Fortschritt:** 6/50 Batches | 192/2.243 Prompts optimiert

---

## Lyra 4-D Prinzip (Referenz)

Jeder Prompt wird nach diesem Schema optimiert:

| Schritt | Element | Beschreibung |
|---------|---------|-------------|
| 1 | **ROLLE** | Klare Expertenpersona ("Du bist ein...") |
| 2 | **KONTEXT** | Situation + Platzhalter [IN KLAMMERN] |
| 3 | **AUFGABE** | Präzise Handlungsanweisung |
| 4 | **AUSGABE** | Gewünschtes Format (Liste, Tabelle, Plan) |

---

## Batch-Übersicht

### Alltag & Leben (107 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 01 | ✅ | Alltag — Eigene | 22 | 22 eigene Prompts: Frontmatter vereinheitlicht (plattformen, schwierigkeit, Quotes), Rolle als "Du bist..."-Persona, Kontext mit Platzhaltern, Ausgabe als nummerierte Liste, "Beispiel" → "Anwendung" umbenannt | 2026-03-10 |
| 02 | ✅ | Alltag — Import 1 | 36 | 36 importierte Prompts (#1762-#2277): Englisch→Deutsch, Lyra 4-D (Rolle/Kontext/Aufgabe/Ausgabe), deutsche Tags, passende Unterkategorien, Anwendung+Variationen thematisch angepasst | 2026-03-10 |
| 03 | ✅ | Alltag — Import 2 | 42 | 42 importierte Prompts (#2303-#3040): Englisch→Deutsch, Lyra 4-D, NSFW bereinigt (#2854), Mega-Prompt kondensiert (#2461), Bild/Video-Prompts mit Kontext-Platzhaltern | 2026-03-10 |

### Beruf & Karriere (146 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 04 | ✅ | Beruf — Eigene | 18 | 18 eigene Prompts: Lyra 4-D (Rolle/Kontext/Aufgabe/Ausgabe im Code-Block), Frontmatter vereinheitlicht (Quotes, plattformen, schwierigkeit), "Beispiel"→"Anwendung", Variationen mit ### Überschriften, #051 Homeoffice komplett umstrukturiert (Duplikat-Sektionen bereinigt) | 2026-03-11 |
| 05 | ✅ | Beruf — Import 1 | 37 | 37 importierte Prompts (#1757-#2196): Englisch→Deutsch, Lyra 4-D, deutsche Tags, passende Unterkategorien (Bewerbung, IT, Finanzen, Gründung, Marketing), Anwendung+Variationen thematisch angepasst. Hinweise: #2043 ist Bild-Prompt (falsche Kategorie), #2068/#2080 Near-Duplikate (beide verallgemeinert), #2014/#2026/#2027 sind Coding-Prompts | 2026-03-11 |
| 06 | ✅ | Beruf — Import 2 | 37 | 37 importierte Prompts (#2204-#2632): Englisch/Türkisch/Chinesisch/Französisch→Deutsch, Lyra 4-D, Unterkategorien zugewiesen. Hinweise: #2519 Bild-Prompt (falsche Kategorie), #2344/#2345 Near-Duplikate (differenziert: AD-Verwaltung vs. allg. PowerShell-Automatisierung), #2375/#2385 Near-Duplikate (differenziert: Redesign vs. Nachbau), #2380 Französisch→Deutsch | 2026-03-11 |
| 07 | ⬜ | Beruf — Import 3 | ~35 | Restliche importierte Karriere-Prompts optimieren | — |

### Bildbearbeitung & Visualisierung (353 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 08 | ⬜ | Bild — Natur | ~45 | Eigene Styles: Atmosphärisch & Natur (Wolken, Blüten, Rauch) | — |
| 09 | ⬜ | Bild — Material | ~45 | Eigene Styles: Material & Struktur (Kristall, Metall, Marmor) | — |
| 10 | ⬜ | Bild — Digital | ~45 | Eigene Styles: Digital & Futuristisch (Glitch, Neon, Retro) | — |
| 11 | ⬜ | Bild — Import 1 | ~45 | Importierte Bild-Prompts Teil 1 nach Lyra 4-D | — |
| 12 | ⬜ | Bild — Import 2 | ~45 | Importierte Bild-Prompts Teil 2 nach Lyra 4-D | — |
| 13 | ⬜ | Bild — Import 3 | ~45 | Importierte Bild-Prompts Teil 3 nach Lyra 4-D | — |
| 14 | ⬜ | Bild — Import 4 | ~45 | Importierte Bild-Prompts Teil 4 nach Lyra 4-D | — |
| 15 | ⬜ | Bild — Import 5 | ~38 | Restliche importierte Bild-Prompts optimieren | — |

### Gesundheit & Wohlbefinden (56 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 16 | ⬜ | Gesundheit — Eigene | ~28 | Eigene Gesundheits-Prompts + Duplikat-Ersatz optimieren | — |
| 17 | ⬜ | Gesundheit — Import | ~28 | Importierte Gesundheits-Prompts nach Lyra 4-D | — |

### Kommunikation & Beziehungen (81 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 18 | ⬜ | Komm. — Eigene | ~41 | Eigene Kommunikations-Prompts + Duplikat-Ersatz optimieren | — |
| 19 | ⬜ | Komm. — Import | ~40 | Importierte Kommunikations-Prompts nach Lyra 4-D | — |

### Kreativität & Freizeit (123 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 20 | ⬜ | Kreativ — Eigene | ~41 | Eigene Kreativitäts-Prompts optimieren | — |
| 21 | ⬜ | Kreativ — Import 1 | ~41 | Importierte Kreativ-Prompts Teil 1 nach Lyra 4-D | — |
| 22 | ⬜ | Kreativ — Import 2 | ~41 | Restliche importierte Kreativ-Prompts optimieren | — |

### Lernen & Wachstum (207 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 23 | ⬜ | Lernen — Eigene | ~42 | Eigene Lern-Prompts optimieren | — |
| 24 | ⬜ | Lernen — Import 1 | ~42 | Importierte Lern-Prompts Teil 1 nach Lyra 4-D | — |
| 25 | ⬜ | Lernen — Import 2 | ~42 | Importierte Lern-Prompts Teil 2 nach Lyra 4-D | — |
| 26 | ⬜ | Lernen — Import 3 | ~42 | Importierte Lern-Prompts Teil 3 nach Lyra 4-D | — |
| 27 | ⬜ | Lernen — Import 4 | ~39 | Restliche importierte Lern-Prompts optimieren | — |

### Pro & Business (22 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 28 | ⬜ | Pro — Feinschliff | 22 | Bereits hochwertig — Feinschliff & Konsistenz-Check | — |

### Spezielle Situationen (28 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 29 | ⬜ | Spezial — Alle | 28 | Alle Spezial-Prompts nach Lyra 4-D optimieren | — |

### Technik & Alltag (511 Prompts)

| # | Status | Batch | Prompts | Beschreibung | Erledigt am |
|---|--------|-------|---------|-------------|-------------|
| 30 | ⬜ | Technik — Eigene | ~43 | Eigene Technik-Prompts optimieren | — |
| 31 | ⬜ | Technik — Import 1 | ~43 | Importierte Technik-Prompts Teil 1 | — |
| 32 | ⬜ | Technik — Import 2 | ~43 | Importierte Technik-Prompts Teil 2 | — |
| 33 | ⬜ | Technik — Import 3 | ~43 | Importierte Technik-Prompts Teil 3 | — |
| 34 | ⬜ | Technik — Import 4 | ~43 | Importierte Technik-Prompts Teil 4 | — |
| 35 | ⬜ | Technik — Import 5 | ~43 | Importierte Technik-Prompts Teil 5 | — |
| 36 | ⬜ | Technik — Import 6 | ~43 | Importierte Technik-Prompts Teil 6 | — |
| 37 | ⬜ | Technik — Import 7 | ~43 | Importierte Technik-Prompts Teil 7 | — |
| 38 | ⬜ | Technik — Import 8 | ~43 | Importierte Technik-Prompts Teil 8 | — |
| 39 | ⬜ | Technik — Import 9 | ~43 | Importierte Technik-Prompts Teil 9 | — |
| 40 | ⬜ | Technik — Import 10 | ~43 | Importierte Technik-Prompts Teil 10 | — |
| 41 | ⬜ | Technik — Import 11 | ~45 | Restliche importierte Technik-Prompts | — |

### Qualitätssicherung & Finalisierung

| # | Status | Batch | Beschreibung | Erledigt am |
|---|--------|-------|-------------|-------------|
| 42 | ⬜ | QA — CREDITS 1 | CREDITS.md komplett aktualisieren (Kategorien 1–5) | — |
| 43 | ⬜ | QA — CREDITS 2 | CREDITS.md komplett aktualisieren (Kategorien 6–10) | — |
| 44 | ⬜ | QA — Website | index.html Kategorie-Anzeige prüfen & aktualisieren | — |
| 45 | ⬜ | QA — Frontmatter | Konsistenz-Check: IDs, Tags, Plattformen, Schwierigkeit | — |
| 46 | ⬜ | QA — Duplikate | Ähnliche Prompts identifizieren & zusammenführen | — |
| 47 | ⬜ | QA — Links | Broken Links & fehlende Dateien prüfen | — |
| 48 | ⬜ | QA — README | README.md Statistiken & Beschreibungen aktualisieren | — |
| 49 | ⬜ | QA — Stichprobe | Gesamttest: 20 Prompts pro Kategorie auf Lyra 4-D prüfen | — |
| 50 | ⬜ | QA — Final | Finaler Commit, Version taggen, Zusammenfassung | — |

---

## Run-Log

| Run | Datum | Batches | Prompts bearbeitet | Notizen |
|-----|-------|---------|-------------------|---------|
| 1 | 2026-03-10 | Batch 01 | 22 | Alltag & Leben eigene Prompts: Lyra 4-D, Frontmatter-Konsistenz |
| 2 | 2026-03-10 | Batch 02 | 36 | Alltag & Leben Import 1: Englisch→Deutsch, Lyra 4-D, Tags/Unterkategorien/Anwendung angepasst |
| 3 | 2026-03-10 | Batch 03 | 42 | Alltag & Leben Import 2: #2303-#3040, inkl. Bild-Prompts, NSFW-Bereinigung, Mega-Prompt-Kondensierung |
| 4 | 2026-03-11 | Batch 04 | 18 | Beruf & Karriere eigene Prompts: Lyra 4-D, Frontmatter-Konsistenz, Umstrukturierung langer Prompts (#049, #051, #052, #053) |
| 5 | 2026-03-11 | Batch 05 | 37 | Beruf & Karriere Import 1: #1757-#2196, Englisch→Deutsch, Lyra 4-D, Unterkategorien zugewiesen, #2043 Bild-Prompt identifiziert, #2068/#2080 Duplikate verallgemeinert |
| 6 | 2026-03-11 | Batch 06 | 37 | Beruf & Karriere Import 2: #2204-#2632, Englisch/Türkisch/Chinesisch/Französisch→Deutsch, Lyra 4-D, Near-Duplikate differenziert (#2344/#2345, #2375/#2385), #2519 Bild-Prompt identifiziert |

---

## Statistik

```
Gesamt-Prompts:     2.243
Optimiert:            192  (9%)
Noch offen:         2.051
Batches fertig:       6/50
Geschätzte Runs:    ~38
```
