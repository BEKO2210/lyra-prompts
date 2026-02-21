---
titel: "KI-Bildprompt für Charakterdesign optimieren"
kategorie: "Bildbearbeitung & KI-Visualisierung"
unterkategorie: "Prompt Engineering"
tags: ["ki", "bild", "prompt", "charakter", "design", "midjourney", "dalle"]
erstellt: "2026-02-21"
---

## Prompt

**Rolle:** Du bist ein Prompt Engineer und KI-Bildgenerierungs-Experte mit tiefem Verständnis von Midjourney, DALL-E, Stable Diffusion und ähnlichen Tools.

**Kontext:** Der Nutzer möchte konsistente, hochwertige Charakterbilder mit KI generieren. Seine aktuellen Prompts liefern unzureichende oder inkonsistente Ergebnisse. Er sucht nach einem System, um bessere Bildprompts zu erstellen.

**Aufgabe:** Entwickle ein Framework für KI-Bildprompts mit:
- Strukturierter Prompt-Architektur
- Stil- und Qualitäts-Parametern
- Konsistenz-Techniken für Charaktere
- Negativer Prompting-Strategie
- Iterations-Workflow

**Einschränkungen:**
- Plattform-spezifische Syntax berücksichtigen (Midjourney vs. DALL-E vs. SD)
- Keine Generierung von urheberrechtlich geschützten Charakteren
- Ethische Grenzen beachten (keine deepfakes, keine harmful content)

**Ausgabe:** Ein Prompt-Engineering-Framework mit Beispielen und Best Practices.

## Beispiel

**Input:**
"Ich will einen Fantasy-Charakter für mein D&D-Spiel erstellen – eine elfische Bogenschützin. Meine Prompts sehen immer anders aus, nie konsistent."

**Output:**

### KI-Bildprompt Framework für Charakterdesign

#### Die Prompt-Struktur (RECIPE-Methode)

```
[Subject] + [Environment] + [Composition] + [Lighting] + 
[Image Quality] + [Extra Details] + [Parameters]
```

---

#### Beispiel-Prompt: Elfen-Bogenschützin

**Vollständiger Prompt:**
```
A female elven archer, pointed ears, long silver hair braided, 
forest green leather armor with leaf motifs, holding an ornate 
wooden longbow, standing in an ancient forest with dappled 
sunlight filtering through canopy, three-quarter view portrait, 
soft natural lighting, golden hour, highly detailed, 8k, 
symmetrical face, sharp focus, concept art style, 
digital painting, artstation trending --ar 2:3 --v 6
```

**Aufschlüsselung:**

| Element | Prompt-Teil |
|---------|-------------|
| **Subject** | A female elven archer, pointed ears, long silver hair braided, forest green leather armor... |
| **Environment** | standing in an ancient forest with dappled sunlight... |
| **Composition** | three-quarter view portrait |
| **Lighting** | soft natural lighting, golden hour |
| **Image Quality** | highly detailed, 8k, symmetrical face, sharp focus |
| **Style** | concept art style, digital painting, artstation trending |
| **Parameters** | --ar 2:3 --v 6 |

---

#### Konsistenz-Strategien für Charaktere

**1. Seed-Werte nutzen (Midjourney/SD):**
```
--seed 12345
```
Gleicher Seed = gleiche Basis-Randomization für konsistente Gesichter.

**2. Character Reference (Midjourney V6):**
```
[erster Prompt] --cref [URL des ersten Bildes] --cw 100
```

**3. Detaillierte Beschreibungen wiederholen:**
Immer dieselben Schlüsselmerkmale nennen:
- "pointed ears"
- "silver braided hair"
- "green leather armor"

**4. Style Reference:**
```
--sref [URL] 
```
Für konsistenten Kunststil über mehrere Bilder.

---

#### Negatives Prompting (was vermeiden)

**Midjourney:**
```
--no blurry, deformed, bad anatomy, extra limbs, 
watermark, signature, text, cropped, worst quality
```

**Stable Diffusion:**
```
Negative prompt: (worst quality:1.4), (low quality:1.4), 
(deformed:1.2), bad anatomy, disfigured, poorly drawn face
```

---

#### Plattform-Vergleich

| Feature | Midjourney | DALL-E 3 | Stable Diffusion |
|---------|------------|----------|------------------|
| Syntax | `--param` | Natürliche Sprache | `(tag:weight)` |
| Konsistenz | `--cref`, Seeds | Schwieriger | ControlNet, Seeds |
| Stil | Sehr ästhetisch | Vielseitig | Sehr anpassbar |
| Best für | Konzept Art | Illustrationen | Fein-Tuning |

---

#### Iterations-Workflow

**Runde 1:** Breite Exploration
```
elven archer, fantasy, concept art --ar 2:3
```

**Runde 2:** Verfeinerung
```
elven archer, silver hair, green armor, ancient forest, 
golden hour, highly detailed --ar 2:3 --v 6
```

**Runde 3:** Konsistenz
```
[bestes Bild] + Variationen mit --cref
```

**Runde 4:** Upscale & Post-Processing
- Upscale in MJ
- Oder: Export zu Photoshop/Photopea für Feintuning

---

### Prompt-Template

```
A [gender] [race/species] [profession/class], 
[distinctive features], [clothing/armor description], 
[action/pose], [environment/background], 
[camera angle/composition], [lighting], 
[art style], [quality modifiers] --ar [ratio] --v 6
```

## Variationen

**Variation 1 - Realistische Portraits:**
Fokus auf photographische Details, Beleuchtung, Hauttextur, "photorealistic", "DSLR", "85mm lens".

**Variation 2 - Anime/Manga Stil:**
"anime style", "manga illustration", "studio ghibli", "cel shaded", spezifische Künstler-Referenzen.

**Variation 3 - Environment/Worldbuilding:**
Landschaften, Städte, Architektur, "matte painting", "epic scale", "atmospheric perspective".

**Variation 4 - Produkt-Design/Mockups:**
"product photography", "clean background", "professional lighting", "commercial photography", konsistente Beleuchtung für Serien.
