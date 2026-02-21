# Lyra Prompt Template - Anleitung

## Zwei Template-Typen

| Template | Für | Beispiel |
|----------|-----|----------|
| `TEMPLATE.md` | Text-Prompts (ChatGPT, Claude) | Rezepte, Bewerbungen, Planung |
| `TEMPLATE-BILD.md` | Bild-Prompts (Midjourney, DALL-E) | Portraits, Stil-Transfer, Kunst |

---

## Text-Prompt Struktur

### Frontmatter
```yaml
---
titel: Rezept anpassen
kategorie: Alltag & Leben
unterkategorie: Küche & Kochen
tags: [kochen, rezept, meal-prep, essen]
erstellt: 2026-02-20
---
```

### Aufbau
```markdown
# [Titel]

## Prompt
```
Rolle: [Experte]
Kontext: [Situation]
Aufgabe: [Was tun?]
Einschränkungen:
- [Regel 1]
- [Regel 2]
Ausgabe: [Format]
```

## Beispiel

**Input:** [Konkretes Beispiel]

**Output:** [Was die AI erstellt]

## Variationen

- Für [Fall 1]: "[Beschreibung]"
- Für [Fall 2]: "[Beschreibung]"
```

### Beispiel: Rezept anpassen
Siehe `BEISPIEL-ALLTAG.md`

---

## Bild-Prompt Struktur

### Frontmatter
```yaml
---
titel: Wolken-Skulptur Transformation
kategorie: Bildbearbeitung & KI-Visualisierung
unterkategorie: Atmosphärische Transformation
tags: [wolken, skulptur, ätherisch, porträt]
erstellt: 2026-02-20
plattformen: [Midjourney, DALL-E, Stable Diffusion]
---
```

### Aufbau
```markdown
# [Titel]

## Prompt
```
[Fließender, beschreibender Text]

Verwandle [Motiv] in [Stil].

[Licht, Farbe, Atmosphäre]
```

## Anwendung

**Für:** [Zweck]
**Input:** [Was rein]
**Output:** [Was raus]

## Variationen

- **[Name]:** [Beschreibung]
- **[Name]:** [Beschreibung]

## Parameter (Midjourney)
```
--ar 3:4 --stylize 250 --v 6
```
```

### Beispiel: Wolken-Skulptur
Siehe `BEISPIEL-BILD.md`

---

## Kategorien

| Ordner | Für |
|--------|-----|
| `alltag-leben/` | Kochen, Haushalt, Finanzen |
| `beruf-karriere/` | Bewerbung, Gehalt, Meetings |
| `lernen-wachstum/` | Skills, Ziele, Bücher |
| `kommunikation-beziehungen/` | Gespräche, Konflikte |
| `kreativitaet-freizeit/` | Schreiben, Reisen, Hobbys |
| `gesundheit-wohlbefinden/` | Fitness, Schlaf, Mental Health |
| `technik-alltag/` | Digital, Sicherheit |
| `spezielle-situationen/` | Umzug, Feiern |
| `bildbearbeitung-visualisierung/` | KI-Bilder, Midjourney |
| `pro/` | Premium (PIN-geschützt) |

---

## Naming Convention

- **Dateiname:** `titel-mit-bindestrichen.md`
- **Kleinbuchstaben**
- **Keine Umlaute** im Dateinamen (ä→ae, ö→oe, ü→ue, ß→ss)
- **Beispiel:** `rezept-anpassen.md`, `wohnung-kuendigen.md`

## Tags

Wähle 3-5 aus: kochen, haushalt, finanzen, bewerbung, karriere, lernen, skill, gespräch, konflikt, fitness, schlaf, midjourney, portrait...
