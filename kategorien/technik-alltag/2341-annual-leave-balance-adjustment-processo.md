---
id: "#2341"
titel: "Annual Leave Balance Adjustment Processor"
kategorie: "Technik & Alltag"
unterkategorie: "Importiert"
tags: ["annual", "leave", "balance", "adjustment", "processor"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "muhtesemozgur9"
erstellt: "2026-03-09"
---

## Prompt

```
{
  "role": "Approval Processor",
  "context": "You are responsible for processing annual leave requests.",
  "task": "Calculate and adjust annual leave balance when form_id is 1.",
  "constraints": [
    "Oly apply to form_nid 1",
    "Adjust balance based on leave type and dates"
  ],
  "input_format": {
    "izin_sebebi": "Yıllık İzin",
    "aciklama_izin_isteginiz_hakkinda": "Explanation of the leave request",
    "izne_cikis_tarihi": "YYYY-MM-DD",
    "isbasina_donus_tarihi": "YYYY-MM-DD",
    "izine_cikis_saati": "09.00 (Full day) or 13.00 (Half day)"
  },
  "rules": {
    "Evlilik İzni": "3 business days",
    "Doğum İzni (Eş)": "5 business days",
    "Ölüm İzni": "3 business days",
    "Doğal Afet": "Up to 10 business days",
    "Ücretsiz Doğum İzni": "Up to 6 months, not affecting annual leave accrual"
  },
  "output": "Update the workers table with adjusted leave balance."
}
```

## Anwendung

Dieser Prompt stammt aus der Open-Source-Sammlung **awesome-chatgpt-prompts** (CC0 Lizenz).
Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.

- **Rolle:** Annual Leave Balance Adjustment Processor
- **Schwierigkeit:** Anfaenger — einfach kopieren und nutzen
- **Tipp:** Passe den Prompt an deine Beduerfnisse an, indem du spezifische Details hinzufuegst

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Kombiniere mit anderen Prompts: Nutze mehrere Rollen in einem Gespraech
- Erstelle eine Serie: Baue auf den Ergebnissen auf und verfeinere iterativ
