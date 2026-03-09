---
id: "#1152"
titel: "3D Mechanical Part Image to Technical Drawing Conversion"
kategorie: "Alltag & Leben"
unterkategorie: "Importiert"
tags: ["mechanical", "part", "image", "technical", "drawing"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "senoldak"
erstellt: "2026-03-09"
---

## Prompt

```
{
  "task": "image_to_image",
  "input_image": "3d_render_of_mechanical_part.png",
  "prompt": "Reference scale: the outer diameter of the flange is exactly 360 mm. Mechanical engineering drawing sheet with three separate drawings of the same part placed in clearly separated rectangular areas. Drawing 1: fully dimensioned orthographic views (front, top, side) with precise numeric measurements in millimeters, diameter symbols, radius annotations, hole count notation and center lines. Drawing 2: sectional view taken through the center axis of the part, showing internal geometry with proper section hatching and wall thickness clearly visible. Drawing 3: isometric reference view of the part without any dimensions, used only for spatial understanding. ISO mechanical drafting standard, consistent line weights, monochrome black lines on white background, manufacturing-ready technical documentation, no perspective distortion.",
  "negative_prompt": "single combined drawing, merged views, artistic rendering, perspective view, realistic lighting, shadows, textures, colors, gradients, sketch style, hand drawn look, missing dimensions, decorative presentation",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 45,
    "cfg_scale": 6,
    "denoising_strength": 0.45,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "one technical drawing sheet containing three clearly separated drawings: dimensioned orthographic views, a centered sectional view, and an undimensioned isometric reference, suitable for manufacturing reference"
}
```

## Anwendung

Dieser Prompt stammt aus der Open-Source-Sammlung **awesome-chatgpt-prompts** (CC0 Lizenz).
Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.

- **Rolle:** 3D Mechanical Part Image to Technical Drawing Conversion
- **Schwierigkeit:** Anfaenger — einfach kopieren und nutzen
- **Tipp:** Passe den Prompt an deine Beduerfnisse an, indem du spezifische Details hinzufuegst

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Kombiniere mit anderen Prompts: Nutze mehrere Rollen in einem Gespraech
- Erstelle eine Serie: Baue auf den Ergebnissen auf und verfeinere iterativ
