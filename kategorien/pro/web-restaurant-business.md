---
id: "#266"
titel: Restaurant & Gastro Website — Komplett mit Speisekarte & Reservierung
kategorie: "Professionell & Business"
unterkategorie: Webentwicklung
tags: [Restaurant, Gastronomie, Website, Speisekarte, Reservierung, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: "1.500 - 3.000€"
---

## Prompt

```
Du bist ein erfahrener Webentwickler spezialisiert auf Gastronomie-Websites. Du erstellst eine komplette, professionelle Restaurant-Website als Single-File HTML mit modernem Design, das Appetit macht und Reservierungen generiert. Du nutzt die neuesten CSS-Techniken (2025) und schreibst sauberen Code ohne externe Abhängigkeiten.

WICHTIG: Du lieferst auf dem Niveau einer Gastro-Spezialagentur die 2.000-4.000€ für Restaurant-Websites berechnet. Die Website muss Appetit machen, Vertrauen aufbauen und Reservierungen generieren — jedes Element dient diesem Dreiklang.

AUFGABE: Erstelle eine produktionsreife Restaurant-Website als Single-File HTML.

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte durch BEVOR du Code schreibst
═══════════════════════════════════════

[SCHRITT 1: GASTRO-MARKETING ANALYSE]
Bevor du Code schreibst, verstehe das Restaurant:
- Was macht dieses Restaurant einzigartig? (Küche, Atmosphäre, Geschichte, Chef?)
- Wer sind die Gäste? (Touristen, Stammgäste, Business-Lunch, Date-Night, Familien?)
- Was suchen sie online? ("Restaurant [Stadt] [Küche]" → SEO-Relevanz)
- Wichtigstes Ziel: Reservierung, Bestellung, oder Bekanntheit?

[SCHRITT 2: CONVERSION-STRATEGIE FÜR GASTRONOMIE]
- 70% der Restaurant-Website-Besucher wollen: Speisekarte, Öffnungszeiten, Adresse, Reservierung
- Diese 4 Infos müssen in unter 3 Sekunden erreichbar sein
- Mobile ist König: 80%+ der Zugriffe kommen vom Smartphone
- Google My Business Integration bedenken (Schema.org Markup)

[SCHRITT 3: TECHNISCHE UMSETZUNG]
Jetzt Code schreiben mit den folgenden Details...

═══════════════════════════════════════

RESTAURANT-DETAILS:
- Name: [RESTAURANT-NAME]
- Küche: [z.B. Italienisch, Japanisch, Deutsch, Fusion]
- Stil: [z.B. Fine Dining, Casual, Bistro, Café, Street Food]
- Farbschema: [z.B. Dunkel & Gold für Eleganz / Warm & Erdtöne für Gemütlichkeit]
- Besonderheit: [z.B. Dachterrasse, Live-Musik, Familiengeführt seit 1985]

SEITEN/SEKTIONEN (Single-Page mit Smooth-Scroll Navigation):

1. NAVIGATION:
   - Sticky-Nav die beim Scrollen kleiner wird (height transition)
   - Glassmorphism-Effekt (backdrop-filter: blur + halbtransparenter Hintergrund)
   - Hamburger-Menü für Mobile mit animierter Transformation (3 Striche → X)
   - Aktiver Menüpunkt hervorgehoben basierend auf Scroll-Position (Intersection Observer)
   - "Reservieren" CTA-Button prominent rechts

2. HERO SECTION:
   - Fullscreen mit CSS-Gradient Overlay (simuliert stimmungsvolles Food-Foto)
   - Animated Headline mit Fade-in
   - Öffnungszeiten als Glassmorphism-Badge
   - "Speisekarte ansehen" + "Tisch reservieren" als Dual-CTAs
   - Subtle Parallax-Effekt auf dem Hintergrund

3. ÜBER UNS:
   - Split-Layout: Text links, dekorativer Bereich rechts
   - Storytelling-Text mit großer Zitat-Hervorhebung
   - Scroll-triggered Einblend-Animation

4. SPEISEKARTE:
   - Tab-Navigation (Vorspeisen, Hauptgerichte, Desserts, Getränke)
   - Animierter Tab-Wechsel mit Fade-Transition
   - Jedes Gericht: Name, Beschreibung, Preis, Allergen-Icons
   - Preis rechtsbündig mit gepunkteter Linie (border-bottom: dotted)
   - Vegetarisch/Vegan Badges mit farbigen Tags
   - Elegante Typografie mit Serif-Headings + Sans-Serif Body
   - CSS Grid für 2-Spalten Layout auf Desktop

5. EMPFEHLUNGEN / HIGHLIGHTS:
   - 3 Feature-Gerichte als große Karten
   - Hover-Effekt: Overlay mit Beschreibung slidet hoch
   - Goldene Akzente für Premium-Feeling
   - "Chef's Choice" Badge

6. BEWERTUNGEN:
   - Google/TripAdvisor Style Sterne-Rating
   - 3-4 Kunden-Reviews als Slider (CSS-only mit scroll-snap)
   - Zitat-Stil mit großem Anführungszeichen
   - Avatar-Platzhalter (CSS-generierte Initialen-Kreise)

7. RESERVIERUNG:
   - Formular: Datum, Uhrzeit, Personenzahl, Name, Telefon, Sonderwünsche
   - Styled Date/Time Picker mit Custom CSS
   - Formular-Validierung mit JavaScript
   - Erfolgs-Animation nach Absenden (Checkmark SVG Animation)
   - Alternativ: Telefonnummer + Online-Reservierungs-Hinweis

8. KONTAKT & ANFAHRT:
   - Adresse, Telefon, E-Mail als klickbare Links (tel:, mailto:)
   - Öffnungszeiten als übersichtliche Tabelle
   - Platzhalter für Google Maps Embed
   - Social Media Links (Instagram besonders prominent)

9. FOOTER:
   - Logo, Quick-Links, Öffnungszeiten Kurzversion
   - "Folge uns auf Instagram" CTA
   - Impressum/Datenschutz Links
   - Copyright

TECHNISCHE ANFORDERUNGEN:
- Single-File HTML (CSS + JS inline)
- Mobile-First Responsive Design
- Smooth Scroll Navigation mit scroll-behavior: smooth
- CSS Custom Properties für einfache Farbanpassung
- System-Font-Stack + eine Serif-Fallback für Eleganz
- Intersection Observer für Scroll-Animationen
- CSS scroll-snap für den Review-Slider
- Formular-Validierung (HTML5 + JS)
- prefers-reduced-motion respektieren
- Semantic HTML + ARIA labels
- Druckbare Speisekarte (print @media query)
- Schema.org LocalBusiness Markup im <head> für SEO

DESIGN-QUALITÄT:
- Muss aussehen wie eine 2.000€+ Agentur-Website
- Warme, einladende Farbpalette
- Großzügige Whitespace
- Typografie-Hierarchie die Eleganz ausstrahlt
- Jede Micro-Interaktion durchdacht
```

## Anwendung

**Wert des Outputs:** Restaurant-Websites kosten bei Agenturen 1.500-3.000€. Dieser Prompt erzeugt eine komplett fertige Website mit Speisekarte, Reservierungsformular und SEO-Optimierung — in Minuten statt Wochen.

Restaurant-Websites sind einer der häufigsten Freelancer-Aufträge. Fast jedes Restaurant braucht eine moderne Website, aber kaum eines hat eine gute. Marktpreis in Deutschland: 1.500-3.000€. Mit diesem Prompt generierst du in Minuten eine komplett fertige Website die nur noch mit echten Fotos und Texten befüllt werden muss. Der Code ist sauber genug um direkt auf Netlify/Vercel deployed oder in WordPress eingebettet zu werden.

## Variationen

- Version für Cafés (mit Frühstückskarte und Tagesangeboten)
- Version für Lieferservice/Takeaway (mit Bestell-Button statt Reservierung)
- Version für Bars/Clubs (dunkleres Design, Event-Kalender statt Speisekarte)
- Mehrsprachige Version (Deutsch/Englisch Toggle)
