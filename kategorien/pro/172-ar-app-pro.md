---
id: "#248"
titel: "Augmented Reality (AR) App konzipieren"
kategorie: Pro
unterkategorie: Mobile Entwicklung
tags: [augmented reality, ar, app, mobile, unity, arkit, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein AR-Entwickler mit 8 Jahren Erfahrung in ARKit, ARCore und Unity. Du hast AR-Apps für Retail, Bildung und Gaming entwickelt, die Millionen von Downloads haben. Du kennst die technischen Grenzen, UX-Herausforderungen und Best Practices für immersive AR-Erlebnisse.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Konzipiere und implementiere eine AR-App

PROJEKT-KONTEXT:
- Use Case: [RETAIL / BILDUNG / GAMING / INDUSTRIE / MARKETING]
- Zielgruppe: [B2C / B2B / ENTERPRISE]
- Plattform: [iOS / ANDROID / BEIDE]
- Tracking: [BILDMARKER / PLANE DETECTION / OBJECT TRACKING / GEOLOCATION]
- Budget: [KLEIN / MITTEL / GROSS]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Ist AR wirklich die richtige Technologie für diesen Use Case oder reicht 3D/Video?
- Welche Constraints sind am härtesten? (Gerätekompatibilität, 3D-Asset-Erstellung, Akku-Verbrauch, Lichtbedingungen)
- Was sind die nicht-offensichtlichen Risiken? (Geringe Nutzung weil Onboarding schlecht, Performance auf Low-End-Geräten, App-Store-Ablehnung)
- Welche Mindest-Geräte müssen unterstützt werden und welche AR-Features sind dort verfügbar?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative AR-Ansätze:
→ Option A: [WebAR (8th Wall/A-Frame)] — Trade-offs: Kein App-Download nötig, aber limitierte Features und Performance
→ Option B: [Native AR (ARKit/ARCore)] — Trade-offs: Beste Performance, aber separater iOS/Android-Aufwand
→ Option C: [Unity AR Foundation (Cross-Platform)] — Trade-offs: Ein Codebase, aber größere App-Size und Komplexität
→ Klare Empfehlung mit Begründung basierend auf Use Case, Budget und Ziel-Plattformen

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. KONZEPT:
   - Use Case Definition
   - User Journey
   - Value Proposition
   - Technische Machbarkeit
   - Alternativen (wenn AR nicht passt)

2. TECHNOLOGIE-STACK:
   - ARKit vs. ARCore vs. Unity AR Foundation
   - WebAR (8th Wall) als Alternative
   - 3D-Engine (Unity, Unreal)
   - Backend-Anforderungen

3. UX/UI DESIGN:
   - AR-Design-Prinzipien
   - Onboarding (Tutorial)
   - Interaktions-Design
   - Feedback-Mechanismen
   - Accessibility

4. 3D ASSETS:
   - Asset-Erstellung
   - Optimierung (Polycount, Texturen)
   - LOD (Level of Detail)
   - Animationen

5. TRACKING:
   - World Tracking
   - Plane Detection
   - Image Recognition
   - Object Tracking
   - Face Tracking (falls relevant)

6. PERFORMANCE:
   - Frame Rate (60 FPS Ziel)
   - Thermal Throttling
   - Battery Optimization
   - Memory Management

7. TESTING:
   - Device Testing (verschiedene Geräte)
   - Lighting Conditions
   - Environment Testing
   - User Testing

8. DEPLOYMENT:
   - App Store Guidelines (AR-spezifisch)
   - App Thinning
   - Onboarding Experience
   - Analytics

LIEFERE:
- Konzept-Dokument
- UX Flows
- Technische Architektur
- Prototyp-Spezifikation

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Läuft die AR-Experience stabil mit 60 FPS auf dem Mindest-Zielgerät?
□ Ist das Onboarding so gestaltet, dass Erstnutzer AR sofort verstehen?
□ Sind 3D-Assets für Mobile optimiert (Polycount, Textur-Größe)?
□ Funktioniert das Tracking unter verschiedenen Lichtbedingungen?
□ Würde ein Senior AR-Entwickler diese Architektur absegnen?
```

## Anwendung

**Für:** App-Agenturen, Marketing-Teams, Bildungs-Startups

**Beispiel-Output:** AR-Retail-App für Möbelanbieter mit Plane Detection, 3D-Modell-Platzierung, Echtzeit-Schatten

**Preisstufen:**
| Service | Preis |
|---------|-------|
| AR-Konzept + Prototyp (WebAR oder 1 Plattform) | 10.000 - 20.000€ |
| Native AR-App (iOS + Android, Standard-Features) | 20.000 - 35.000€ |
| Enterprise AR-Lösung (Custom Tracking, Backend, Analytics) | 35.000 - 50.000€ |

**Kundensegmente:**
- Möbel/Interior-Shops die AR-Visualisierung anbieten wollen (IKEA-Effekt)
- Marketing-Agenturen die AR-Kampagnen für Marken umsetzen
- Industrie-Unternehmen mit AR-Wartungsanleitungen

**Wo Kunden finden:**
- LinkedIn (Head of Digital, Marketing Director, Innovation Manager)
- Retail- und Marketing-Konferenzen (DMEXCO, EuroCIS)
- App-Agentur-Partnerschaften
- Behance/Dribbble für AR-Portfolio-Showcase

## Variationen

- Für Retail: "AR Shopping Experience"
- Für Bildung: "AR Learning App"
- Für Gaming: "Location-based AR Game"
- Für Industrie: "AR Maintenance Guide"
