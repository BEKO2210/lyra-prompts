---
id: "#1119"
titel: "Realistic Amateur Vibe Candid Photography Prompt"
kategorie: "Technik & Alltag"
unterkategorie: "Importiert"
tags: ["realistic", "amateur", "vibe", "candid", "photography"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "dorukkurtoglu@gmail.com"
erstellt: "2026-03-09"
---

## Prompt

```
{
  "prompt": "instagirl, candid phone snapshot, realistic amateur vibe, natural skin texture, light makeup at most, handheld micro-blur, iPhone 11 wide 26mm EXIF look, f/1.8, 1/60s, ISO 200, slight lens distortion, casual posture, everyday outfit, mild flyaway hair, imperfect framing, background clutter present, no retouching, realistic shadows, faithful anatomy, same person identity, same body proportions",
  "negative_prompt": "beauty filter, skin smoothing, studio glam, hdr glow, cinematic grading, fashion editorial, airbrush, liquify, body morph, face changed, de-aged, uncanny valley, extra fingers, warped limbs, NSFW, lingerie, bikini, watermark, text, logo, border",
  "image": "<REFERENCE_IMAGE_URL>",
  "strength": 0.35,
  "guidance": 5.0,
  "control_nets": [
    {
      "type": "openpose",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.7,
      "guess_mode": false
    },
    {
      "type": "depth",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.45
    }
  ],
  "face_lock": {
    "type": "ip_adapter_faceid",
    "ref_image": "<REFERENCE_FACE_CROP_OR_SAME_URL>",
    "weight": 0.75
  }
}
```

## Anwendung

Dieser Prompt stammt aus der Open-Source-Sammlung **awesome-chatgpt-prompts** (CC0 Lizenz).
Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.

- **Rolle:** Realistic Amateur Vibe Candid Photography Prompt
- **Schwierigkeit:** Anfaenger — einfach kopieren und nutzen
- **Tipp:** Passe den Prompt an deine Beduerfnisse an, indem du spezifische Details hinzufuegst

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Kombiniere mit anderen Prompts: Nutze mehrere Rollen in einem Gespraech
- Erstelle eine Serie: Baue auf den Ergebnissen auf und verfeinere iterativ
