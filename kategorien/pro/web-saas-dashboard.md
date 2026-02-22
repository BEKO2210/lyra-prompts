---
id: "#072"
titel: SaaS Dashboard UI — Admin Panel mit Glassmorphism & Charts
unterkategorie: Webentwicklung
tags: [Dashboard, SaaS, Admin Panel, Glassmorphism, Charts]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: 2.000-5.000€
---

## Prompt

```
Du bist ein Senior Frontend-Architekt spezialisiert auf SaaS-Dashboard-Interfaces. Du designst und baust Admin Panels die komplex wirkende Daten einfach und schön darstellen. Du nutzt die neuesten CSS-Techniken (2025): Glassmorphism, Bento-Grids, CSS-only Charts, Smooth Transitions. Alles in einer einzigen HTML-Datei — kein React, kein Tailwind, nur reines HTML/CSS/JS.

AUFGABE: Erstelle ein produktionsreifes SaaS-Dashboard als Single-File HTML.

DASHBOARD-DETAILS:
- SaaS-Typ: [z.B. Analytics, CRM, Projektmanagement, E-Commerce Backend, Finance]
- Name der App: [APP-NAME]
- Farbschema: [z.B. Dunkel mit blauen Akzenten / Hell und clean / Dunkles Purple]
- Hauptmetriken: [z.B. Umsatz, Nutzer, Conversion-Rate, Tickets]

LAYOUT-STRUKTUR:

1. SIDEBAR NAVIGATION:
   - Fixed Sidebar links (240px breit, collapsible auf 64px)
   - App-Logo oben
   - Navigations-Items mit Icons (Emoji als Platzhalter)
   - Aktiver Item hervorgehoben mit Accent-Color Background + Border-Left
   - Hover: Subtle background-change + translateX(2px)
   - Collapse/Expand Button mit Rotation-Animation
   - User-Avatar + Name unten in der Sidebar
   - Mobile: Sidebar wird zum Overlay-Drawer (slide-in von links)
   - Glassmorphism-Effekt auf der Sidebar (backdrop-filter: blur)

2. TOP BAR:
   - Breadcrumb / Page Title links
   - Suchfeld mit Icon (expandiert on focus)
   - Notification Bell mit Badge (roter Punkt, pulsierend)
   - User-Dropdown (Klick öffnet Mini-Menü)
   - Dark/Light Mode Toggle mit animiertem Sun/Moon Switch

3. KPI-KARTEN (Top-Row):
   - 4 Karten in einer Reihe (responsive: 2x2 auf Tablet, 1 Spalte Mobile)
   - Jede Karte: Icon, Metrik-Name, Großer Zahlenwert, Trend-Indikator (↑12% grün / ↓3% rot)
   - Glassmorphism-Style (halbtransparent mit blur)
   - Hover: Subtle Glow + scale(1.02)
   - Zahl animiert beim Laden (countUp Animation)
   - Mini-Sparkline Chart als CSS-only (border-bottom Gradient oder kleine SVG)

4. HAUPT-CHART BEREICH:
   - Großes Diagramm (CSS-only Bar Chart ODER SVG Line Chart)
   - Tab-Wechsel: Woche / Monat / Jahr mit animiertem Underline
   - Chart-Balken animieren beim Erscheinen (height transition mit delay)
   - Tooltip on hover (zeigt Wert an)
   - Responsive: Volle Breite auf allen Screens

5. BENTO-GRID WIDGETS:
   - CSS Grid mit verschiedenen Widget-Größen:
     * Aktivitäts-Feed (Liste der letzten Aktionen mit Zeitstempel)
     * Doughnut/Pie Chart (CSS conic-gradient)
     * Top-5 Liste (z.B. Top Kunden, Top Produkte)
     * Progress-Tracker (Ziel-Balken mit Prozent)
   - Jedes Widget: Glassmorphism Card mit Header + Content
   - Drag-Handle visuell angedeutet (dots pattern oben rechts)

6. DATENTABELLE:
   - Sortierbare Spalten (Klick auf Header → Toggle Pfeil)
   - Zebra-Striping für Lesbarkeit
   - Status-Badges (Aktiv=Grün, Pending=Gelb, Cancelled=Rot)
   - Hover-Zeile hervorgehoben
   - Pagination unten mit aktueller Seite hervorgehoben
   - Responsive: Horizontal scrollbar auf Mobile
   - Suchfeld über der Tabelle

7. DARK/LIGHT MODE:
   - CSS Custom Properties die umgeschaltet werden
   - Transition auf allen Farben (smooth Theme-Switch)
   - prefers-color-scheme als Default
   - Toggle-Button speichert Wahl in localStorage

TECHNISCHE CSS-TECHNIKEN:
- CSS Grid + Subgrid für das gesamte Dashboard-Layout
- Glassmorphism: backdrop-filter: blur(12px) + rgba backgrounds
- CSS conic-gradient für Pie/Doughnut Charts
- CSS-only Bar Charts: Grid items mit animierter height
- Bento Grid: grid-template-areas mit named areas
- Container Queries: @container für responsive Widgets
- :has() Selektor: Sidebar collapsed state propagieren
- CSS Nesting: Wo sinnvoll für saubereren Code
- Custom scrollbar styling (::-webkit-scrollbar)
- Smooth Transitions überall (300ms cubic-bezier)
- position: sticky für Table Header
- Intersection Observer für Widget-Animationen beim Scrollen

SAMPLE DATA:
- Generiere realistische Demo-Daten im JavaScript
- Mindestens 10 Tabellenzeilen
- Chart-Daten für 7 Tage/12 Monate
- KPI-Werte die Sinn ergeben

QUALITÄTSLEVEL:
- Muss aussehen wie ein echtes SaaS-Produkt (Stripe/Linear/Vercel Niveau)
- Jede Interaktion muss sich smooth anfühlen
- Dark Mode muss genauso gut aussehen wie Light Mode
- Keine UI-Inkonsistenzen
- Lighthouse Performance 90+
```

## Anwendung

SaaS-Dashboards sind die höchstbezahlten Web-Projekte für Freelancer: 2.000-5.000€ und mehr. Startups und Unternehmen brauchen ständig Admin-Panels für ihre Produkte. Mit diesem Prompt generierst du ein funktionierendes Dashboard-Template das als Basis für echte Projekte dient oder als UI-Prototyp für Investoren-Pitches verkauft werden kann. Der Dark/Light Mode und die realistische Demo-Daten machen es sofort präsentierbar.

## Variationen

- E-Commerce Dashboard (Bestellungen, Umsatz, Lagerbestand)
- Social Media Analytics Dashboard (Follower, Engagement, Reichweite)
- Projekt-Management Board (Kanban-artige Ansicht statt Tabelle)
- Finance/Banking Dashboard (Kontostand, Transaktionen, Budgets)
