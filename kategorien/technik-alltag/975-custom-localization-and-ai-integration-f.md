---
id: "#975"
titel: "Custom Localization and AI Integration for Apps"
kategorie: "Technik & Alltag"
unterkategorie: "Importiert"
tags: ["custom", "localization", "integration", "apps", "expert"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "ahmettzorlutuna"
erstellt: "2026-03-09"
---

## Prompt

```
Act as an App Localization Expert. You are tasked with setting up a user-preference-based localization architecture in an application independent of the phone's system language.

Your task includes:
1. **LanguageManager Class**: Create a `LanguageManager` class using the `ObservableObject` protocol. Store the user's selected language in `UserDefaults`, with the default language set to 'en' (English). Display a selection screen on the first launch.
2. **Global Locale Override**: Wrap the entire `ContentView` structure in your SwiftUI app with `.environment(\.locale, .init(identifier: languageManager.selectedLanguage))` to trigger translations based on the selected language in `LanguageManager`.
3. **Onboarding Language Selection**: If no language has been selected previously, show a stylish 'Language Selection' screen with English and Turkish options on app launch. Save the selection immediately and transition to the main screen.
4. **AI (LLM) Integration**: Add the user's selected language as a parameter in AI requests (API calls). Update the system prompt to: 'User's preferred language: ${selected_language}. Respond in this language.'
5. **String Catalogs**: Integrate `.stringxcatalog` into your project and add all existing hardcoded strings in English (base) and Turkish.
6. **Dynamic Update**: Ensure that changing the language in settings updates the UI without restarting the app.
7. **User Language Change**: Allow users to change the app's language dynamically at any time.

Rules:
- Ensure seamless user experience during language selection and updates.
- Test functionality for both English and Turkish languages.
```

## Anwendung

Dieser Prompt stammt aus der Open-Source-Sammlung **awesome-chatgpt-prompts** (CC0 Lizenz).
Kopiere den Prompt und fuege ihn direkt in ChatGPT, Claude oder Gemini ein.

- **Rolle:** Custom Localization and AI Integration for Apps
- **Schwierigkeit:** Anfaenger — einfach kopieren und nutzen
- **Tipp:** Passe den Prompt an deine Beduerfnisse an, indem du spezifische Details hinzufuegst

## Variationen

- Aendere die Sprache: Fuege "Antworte auf Deutsch" am Ende hinzu
- Mache es spezifischer: Ersetze allgemeine Begriffe durch deine konkreten Details
- Kombiniere mit anderen Prompts: Nutze mehrere Rollen in einem Gespraech
- Erstelle eine Serie: Baue auf den Ergebnissen auf und verfeinere iterativ
