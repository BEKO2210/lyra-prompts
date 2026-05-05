---
id: "#4704"
titel: "Cyber-Pulse: 3D Neon Particle Swarm"
kategorie: "Technik & Alltag"
unterkategorie: "Programmiersprachen"
tags: ["cyber", "pulse", "neon", "particle", "swarm"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "loshu2000"
erstellt: "2026-04-24"
---

## Prompt

```
Game Concept: A fast-paced arcade "dodge-em-up" set in a digital void. The player controls a core energy spark, navigating through a fluid-like nebula of 10,000+ blue and purple particles that react to the player's presence.
Technical Prompt:
Create a Three.js scene featuring a Points system with 15,000 particles. Use a custom ShaderMaterial for a glow effect. Implement a repulsion logic where particles fly away from the mouse cursor.

JavaScript
// Core repulsion math
let dist = particlePos.distanceTo(mousePos);
if (dist < 5) {
  direction.subVectors(particlePos, mousePos).normalize();
  particlePos.addScaledVector(direction, 0.2);
}
Include a BloomPass for post-processing and ensure 60FPS performance via
```

## Anwendung

Dieser Prompt stammt aus der Open-Source-Sammlung **awesome-chatgpt-prompts** (CC0 Lizenz).
Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.

- **Rolle:** Cyber-Pulse: 3D Neon Particle Swarm
- **Schwierigkeit:** Anfaenger — einfach kopieren und nutzen
- **Tipp:** Passe den Prompt an deine Beduerfnisse an, indem du spezifische Details hinzufuegst

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Kombiniere mit anderen Prompts: Nutze mehrere Rollen in einem Gespraech
- Erstelle eine Serie: Baue auf den Ergebnissen auf und verfeinere iterativ
