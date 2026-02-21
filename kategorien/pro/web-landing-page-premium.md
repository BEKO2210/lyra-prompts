---
titel: Premium Landing Page mit Glassmorphism & Micro-Animationen
unterkategorie: Webentwicklung
tags: [Landing Page, Glassmorphism, CSS, Animationen, Webdesign]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: 500-2.000€
---

## Prompt

```
Du bist ein Elite-Frontend-Entwickler und UI/UX-Designer, spezialisiert auf conversion-optimierte Landing Pages. Du kennst die neuesten CSS-Techniken aus 2025, nutzt Glassmorphism, Micro-Animationen und modernes Layout-Design. Du schreibst sauberen, performanten Code ohne externe Frameworks — nur HTML, CSS und Vanilla JavaScript.

AUFGABE: Erstelle eine komplette, produktionsreife Landing Page als Single-File HTML.

PROJEKT-DETAILS:
- Branche/Produkt: [z.B. SaaS-App, Coaching, Agentur, Produkt-Launch]
- Zielgruppe: [z.B. Startups, Freelancer, Unternehmer]
- Haupt-CTA: [z.B. "Kostenlos testen", "Jetzt buchen", "Warteliste beitreten"]
- Farbschema: [z.B. Dunkel mit Akzentfarbe #6366f1 / Hell und minimalistisch]
- Tone: [z.B. Tech/Modern, Elegant/Premium, Spielerisch/Kreativ]

PFLICHTMODULE (in dieser Reihenfolge):

1. HERO SECTION:
   - Großer Headline mit Gradient-Text (background-clip: text)
   - Animierter Subtitle mit typewriter- oder fade-in Effekt
   - CTA-Button mit Hover-Glow-Effekt (box-shadow Animation + scale transform)
   - Hintergrund: Animated Mesh-Gradient oder Aurora-Gradient mit CSS @keyframes
   - Optional: Floating Glassmorphism-Cards als Deko-Elemente (backdrop-filter: blur)

2. SOCIAL PROOF BAR:
   - Logo-Leiste "Bekannt aus" / "Vertraut von" mit Grayscale-Filter → Farbe on hover
   - Oder: Zahlen-Counter mit Intersection Observer animiert (z.B. "10.000+ Nutzer")

3. FEATURES/BENEFITS SECTION:
   - Bento-Grid Layout (CSS Grid mit unterschiedlich großen Karten)
   - Jede Karte: Icon + Titel + Text
   - Glassmorphism-Karten (background: rgba + backdrop-filter: blur + border: 1px solid rgba)
   - Scroll-triggered Fade-in Animation (Intersection Observer + CSS transitions)
   - Hover: Subtle border-glow und translateY(-4px)

4. HOW IT WORKS:
   - 3-Schritt Prozess als Timeline oder Stepper
   - Animierte Verbindungslinien zwischen Steps
   - Nummern mit gradient background

5. TESTIMONIALS:
   - Karussell oder gestaffeltes Grid
   - Zitat mit großem Anführungszeichen-Deko
   - Avatar + Name + Rolle
   - Glassmorphism Card-Style

6. PRICING (optional):
   - 2-3 Preis-Karten
   - "Beliebteste" Karte hervorgehoben (scale, border-glow, badge)
   - Toggle Monatlich/Jährlich mit animiertem Switch

7. FAQ:
   - Akkordeon mit smooth height-animation (CSS grid-template-rows: 0fr → 1fr)
   - Rotierendes Pfeil-Icon

8. FINAL CTA:
   - Fullwidth Section mit Gradient-Background
   - Wiederholung des Haupt-CTA
   - Urgency/Scarcity Element

9. FOOTER:
   - Links, Social Icons, Copyright
   - Minimalistisch

TECHNISCHE ANFORDERUNGEN:
- Single-File HTML (alles inline: CSS im <style>, JS im <script>)
- Mobile-First Responsive (min-width Breakpoints: 640px, 1024px)
- CSS Custom Properties (Variablen für Farben, Radii, Shadows)
- Smooth Scroll, scroll-behavior: smooth
- Performant: Keine Layout-Shifts, will-change für Animationen
- Intersection Observer für Scroll-Animationen (kein externes JS)
- prefers-reduced-motion Media Query respektieren
- Semantic HTML (header, main, section, footer)
- Barrierefreiheit: aria-labels, fokussierbare Elemente, Kontrast
- Ladezeit-optimiert: Keine externen Fonts (system-font-stack), keine Bilder (Emoji/SVG als Icons)

CSS-TECHNIKEN DIE DU NUTZEN MUSST:
- backdrop-filter: blur() für Glassmorphism
- background-clip: text für Gradient-Text
- CSS Grid für Bento-Layouts
- @keyframes für Hintergrund-Animationen
- transition mit cubic-bezier für smooth Interactions
- clamp() für responsive Typografie
- :has() Selektor wo sinnvoll
- Scroll-driven Animationen wo möglich (animation-timeline: scroll())

QUALITÄTSLEVEL:
- Der Code muss aussehen wie von einer Premium-Agentur
- Pixel-perfekt, kein Detail vergessen
- Jede Interaktion muss sich "smooth" anfühlen
- Lighthouse Score: 95+ Performance, 100 Accessibility anpeilen
```

## Anwendung

Mit diesem Prompt erstellst du komplette Landing Pages die du als Freelancer oder Agentur für 500-2.000€ verkaufen kannst. Der Output ist eine fertige Single-File HTML die sofort deployed werden kann. Kunden sind: Startups die eine Launch-Page brauchen, Coaches/Berater für ihre Dienstleistung, Unternehmen für Produkt-Launches oder Event-Seiten. Passe die Platzhalter an den jeweiligen Kunden an.

## Variationen

- Erstelle eine Dark-Mode + Light-Mode Version mit CSS Toggle
- Erweitere um ein Kontaktformular mit Validation
- Passe an für einen App-Store Launch (mit Mockup-Beschreibung)
- Erstelle eine Waitlist-Version mit E-Mail-Eingabe und Countdown-Timer
