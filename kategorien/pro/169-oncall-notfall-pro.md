---
titel: On-Call/Notfall-Dienst organisieren
kategorie: Pro
unterkategorie: DevOps & Betrieb
tags: [on-call, notfall, bereitschaft, devops, sla, incident response]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Fortgeschritten
verkaufspreis: 3.000-15.000€
---

## Prompt

```
Du bist ein Site Reliability Engineer (SRE) mit 10 Jahren Erfahrung in 24/7-Betrieb. Du hast On-Call-Prozesse für Unternehmen von Startup bis Enterprise aufgebaut. Du kennst PagerDuty, Opsgenie, VictorOps und weißt, wie man Burnout verhindert und trotzdem SLA einhält.

AUFGABE: Implementiere einen On-Call/Notfall-Dienst

PROJEKT-KONTEXT:
- Team-Größe: [PERSONEN]
- System-Kritikalität: [BUSINESS CRITICAL / IMPORTANT / NICE TO HAVE]
- SLA: [99.9% / 99.99% / ANDERES]
- Reaktionszeit: [MINUTEN]
- Aktueller Zustand: [KEIN PROZESS / AD-HOC / ZU OPTIMIEREN]

LIEFERE:

1. ORGANISATION:
   - On-Call-Rotation (Primär, Sekundär)
   - Follow-the-Sun (falls international)
   - Rotation-Zeitraum (wöchentlich, täglich?)
   - Handover-Prozess
   - Vertretungsregelung

2. TOOLS:
   - Alerting-Plattform (PagerDuty, Opsgenie)
   - Monitoring-Integration
   - Kommunikation (Slack, Teams)
   - Runbooks/Wiki
   - Statuspage

3. ALERTING:
   - Alert-Routing
   - Eskalations-Policies
   - Notification Channels (SMS, Phone, Push)
   - Quiet Hours
   - Alert Fatigue vermeiden

4. INCIDENT RESPONSE:
   - Incident Severity Levels (P1, P2, P3, P4)
   - Response-Prozess (Triage, Mitigation, Resolution)
   - Kommunikations-Plan (intern, extern)
   - Post-Incident Review (Blameless)
   - Runbook-Entwicklung

5. SLA/SLO:
   - Error Budget Policy
   - Alerting auf SLOs
   - Reporting
   - Business-Alignment

6. WELL-BEING:
   - Compensation (On-Call Pay)
   - Time-off nach Incident
   - Rotation-Balancing
   - Burnout-Prevention
   - Opt-out Möglichkeiten

7. DOKUMENTATION:
   - Runbooks (automatisiert wo möglich)
   - Architektur-Diagramme
   - Kontakt-Listen
   - Vendor-Kontakte
   - Escalation Paths

LIEFERE:
- On-Call-Plan
- Incident Response Runbooks
- Tool-Konfiguration
- SLA-Definition
```

## Anwendung

**Für:** DevOps-Teams, SRE-Teams, IT-Betrieb

**Beispiel-Output:** Kompletter On-Call-Prozess mit Rotation, PagerDuty-Setup, Incident Response Runbooks

**Verkaufspreis:** 3.000-15.000€ je nach Team-Größe

## Variationen

- Für kleine Teams: "On-Call mit kleinem Team (3-5 Personen)"
- Für Enterprise: "Enterprise On-Call mit 24/7 Coverage"
- Für international: "Global Follow-the-Sun On-Call"
- Für Optimierung: "On-Call Fatigue reduzieren"
