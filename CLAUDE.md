# LYRA PROMPTS — Anweisungen für KI-Assistenten

> Diese Datei gilt für ALLE KI-Assistenten die an diesem Projekt arbeiten:
> Claude, Kimi Claw (Belkis), ChatGPT, oder andere.

## Projekt-Übersicht

**Lyra Prompts** ist eine Prompt-Bibliothek mit einer Website (index.html).
- **Kostenlose Prompts:** Alltags-Helfer für jeden (Kochen, Finanzen, Karriere, etc.)
- **Pro-Prompts:** Premium-Prompts deren OUTPUT als Dienstleistung verkauft werden kann (Webentwicklung, Marketing, Beratung)
- **Bild-Prompts:** KI-Bildgenerierungs-Styles (für ChatGPT/DALL-E, Midjourney, etc.)

## WICHTIGSTE REGEL

**Bevor du IRGENDETWAS erstellst oder änderst:**

```
1. Lies CREDITS.md — Das ist das vollständige Prompt-Register
2. Prüfe ob ein ähnlicher Prompt bereits existiert
3. Wenn ja → verbessere den bestehenden, erstelle KEINEN neuen
4. Wenn nein → erstelle den Prompt und trage ihn in CREDITS.md ein
```

## Prompt-Register: CREDITS.md

Die Datei `CREDITS.md` ist die Single Source of Truth für alle Prompts:
- Jeder Prompt hat eine **eindeutige Nummer** (#001 - #XXX)
- Nummern werden **NIE wiederverwendet**
- Die **"Nächste freie Nummer"** steht ganz oben in der Datei
- Nach jedem neuen Prompt: CREDITS.md aktualisieren!

## Workflow: Neuen Prompt erstellen

### Schritt 1: CREDITS.md lesen
```
Lies CREDITS.md komplett durch.
Prüfe: Gibt es schon einen ähnlichen Prompt?
```

### Schritt 2: Kategorie wählen
```
kategorien/
├── alltag-leben/           # Haushalt, Organisation, Finanzen
├── beruf-karriere/         # Job, Bewerbung, Arbeit
├── bildbearbeitung-visualisierung/  # KI-Bild-Styles
├── gesundheit-wohlbefinden/  # Fitness, Schlaf, Mental Health
├── kommunikation-beziehungen/  # Gespräche, Konflikte
├── kreativitaet-freizeit/  # Hobbys, Reisen, Content
├── lernen-wachstum/        # Bildung, Kurse, Ziele
├── spezielle-situationen/  # Events, Feiern
├── technik-alltag/         # Digital, Software
└── pro/                    # PREMIUM — als Service verkaufbar
```

### Schritt 3: Prompt-Datei erstellen

**Dateiname:** Kleinbuchstaben, Bindestriche, deutsch, max. 40 Zeichen.
Beispiel: `kategorien/pro/web-coaching-plattform.md`

**Frontmatter (YAML):**
```yaml
---
titel: [Klarer, beschreibender Titel]
unterkategorie: [z.B. Digitale Dienstleistung, Webentwicklung]
tags: [Tag1, Tag2, Tag3, Tag4]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: [Anfänger / Fortgeschritten]
verkaufspreis: [NUR bei Pro-Prompts — z.B. "500 - 2.000€"]
---
```

**Struktur:**
```markdown
## Prompt

\```
[Der eigentliche Prompt hier]
\```

## Anwendung

[Erklärung: Was das Output wert ist, wer die Kunden sind, wo man sie findet]

## Variationen

- [Variation 1]
- [Variation 2]
- [Variation 3]
- [Variation 4]
```

### Schritt 4: CREDITS.md aktualisieren

1. Trage den neuen Prompt in die richtige Kategorie-Tabelle ein
2. Vergib die nächste freie Nummer
3. Erhöhe "Nächste freie Nummer" um 1
4. Aktualisiere die Statistik-Tabelle (Anzahl + IDs)

### Schritt 5: index.html aktualisieren (falls nötig)

Die Website `index.html` muss den neuen Prompt anzeigen.
Prüfe ob er in der richtigen Kategorie auf der Website erscheint.

## Qualitäts-Standards

### Kostenlose Prompts (Anfänger)
- Einfach und sofort nutzbar
- Klare Platzhalter in [ECKIGEN KLAMMERN]
- Ergebnis in unter 1 Minute
- Keine Fachbegriffe ohne Erklärung

### Pro-Prompts (Fortgeschritten)
- **Output muss als Dienstleistung verkaufbar sein**
- Agentur-/Berater-Niveau Qualität
- Realistische Verkaufspreise (basierend auf deutschem Markt)
- Anwendung erklärt: WER sind die Kunden, WO findet man sie, WAS ist das Output wert
- Keine "verkaufe den Prompt für 4,99€" — stattdessen: "verkaufe das ERGEBNIS als Service"

### Bild-Prompts
- Für ChatGPT/DALL-E optimiert
- Beschreibender Titel
- Klare visuelle Anweisungen
- Variationen für verschiedene Stile

## Pro-Prompt Preise (Referenz)

Diese Preise basieren auf deutschen Freelancer-/Agentur-Marktpreisen:

| Service-Typ | Preisrange | Beispiel |
|-------------|-----------|----------|
| Webentwicklung | 500 - 5.000€ | Landing Page, Shop, Dashboard |
| Social-Media Management | 300 - 1.500€/Monat | Content-Plan, Strategie |
| Bewerbungs-Service | 150 - 500€ | Anschreiben, CV, Interview-Prep |
| Finanz-Coaching | 200 - 800€ | Finanzplan, Budget, Schulden-Strategie |
| E-Commerce Setup | 200 - 600€ | Etsy/Shop-Einrichtung, Listings |
| E-Mail-Marketing | 500 - 2.000€ | Funnel, Automationen, Newsletter |
| Business-Beratung | 300 - 1.500€ | Businessplan, Gründungs-Coaching |

## Git-Workflow

- Branch für Entwicklung: Wird pro Session festgelegt
- Commit-Messages: Deutsch, beschreibend, was + warum
- Immer CREDITS.md mit-committen wenn Prompts geändert wurden

## Projekt-Dateien

| Datei | Beschreibung |
|-------|-------------|
| `index.html` | Die Website — zeigt alle Prompts an |
| `CREDITS.md` | Prompt-Register (IMMER ZUERST LESEN) |
| `CLAUDE.md` | Diese Datei — Anweisungen für KI-Assistenten |
| `README.md` | Projekt-Beschreibung |
| `kategorien/` | Alle Prompt-Dateien nach Kategorie |
