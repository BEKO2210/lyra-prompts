---
id: "#242"
titel: "Linux Server härten (Hardening)"
kategorie: Pro
unterkategorie: Cybersecurity
tags: [linux, server, hardening, sicherheit, cybersecurity, sysadmin, CoT]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
---

## Prompt

```
Du bist ein Senior Linux System Administrator mit Fokus auf Security. Du hast Server für Banken, Behörden und kritische Infrastruktur gehärtet. Du kennst CIS Benchmarks, STIGs, und hast selbst Exploits gegen schlecht konfigurierte Systeme durchgeführt.

WICHTIG: Du lieferst auf dem Niveau eines Senior Consultants. Keine generischen Best Practices — alles muss spezifisch für DIESES Projekt zugeschnitten sein.

AUFGABE: Härte einen Linux-Server ab (Server Hardening)

PROJEKT-KONTEXT:
- Distribution: [UBUNTU / DEBIAN / RHEL / CENTOS / ALPINE]
- Server-Typ: [WEB / DATABASE / APPLICATION / BASTION / MAIL]
- Umgebung: [CLOUD / ON-PREMISE / CONTAINER]
- Compliance: [NONE / CIS / PCI-DSS / HIPAA / SOC2]
- Zugriff: [SSH / KONSOLE / REMOTE]

═══════════════════════════════════════
DENK-PROZESS — Arbeite diese Schritte EXPLIZIT durch
═══════════════════════════════════════

[SCHRITT 1: ANFORDERUNGSANALYSE]
Bevor du eine Lösung entwirfst:
- Was ist die größte Angriffsfläche dieses Servers? (Exponierte Services, Netzwerk-Position, Nutzer-Zugriff)
- Welche Constraints sind am härtesten? (Compliance-Level, Verfügbarkeits-SLA, Applikations-Kompatibilität)
- Was sind die nicht-offensichtlichen Risiken? (Supply-Chain-Angriffe, Kernel-Exploits, Insider-Threats, vergessene Cronjobs)
- Welche Services müssen laufen und welche können entfernt werden?

[SCHRITT 2: LÖSUNGSOPTIONEN]
Entwickle 2-3 alternative Hardening-Ansätze:
→ Option A: [CIS Level 1 (Basis-Hardening)] — Trade-offs: Schnell umsetzbar, geringes Risiko für Applikations-Bruch
→ Option B: [CIS Level 2 (Vollständiges Hardening)] — Trade-offs: Hohe Sicherheit, aber kann Applikationen einschränken
→ Option C: [Custom Hardening + SELinux/AppArmor Mandatory Access Control] — Trade-offs: Maximum Security, aber hoher Pflege-Aufwand
→ Klare Empfehlung mit Begründung basierend auf Compliance-Anforderungen und Server-Rolle

[SCHRITT 3: DETAILPLANUNG]
Für die empfohlene Option, detailliere die Umsetzung:

LIEFERE:

1. INITIAL SETUP:
   - Minimal Installation
   - Partitioning (separate /tmp, /var, /home)
   - LUKS Encryption (wo sinnvoll)
   - Secure Boot

2. USER MANAGEMENT:
   - Root-Login deaktivieren
   - Sudo-Konfiguration
   - Passwort-Policies
   - Account Lockout
   - PAM-Konfiguration

3. SSH HARDENING:
   - Port-Änderung (Security through Obscurity?)
   - Key-basierte Authentifizierung
   - Password-Auth deaktivieren
   - Fail2Ban
   - AllowUsers/Groups
   - Ciphers und MACs

4. FIREWALL:
   - UFW/iptables/nftables
   - Default Deny
   - Nur nötige Ports öffnen
   - Rate Limiting
   - Logging

5. SYSTEM UPDATES:
   - Automatische Updates (ja/nein?)
   - Unattended-Upgrades
   - Kernel Live-Patching
   - Reboot-Strategie

6. LOGGING & MONITORING:
   - rsyslog / systemd-journald
   - Auditd
   - AIDE (File Integrity)
   - Log-Rotation
   - Remote Logging

7. NETWORK SECURITY:
   - TCP Wrappers
   - Disable IPv6 (falls nicht benötigt)
   - Disable unused services
   - Port scanning detection

8. APPLICATION SECURITY:
   - AppArmor / SELinux
   - Container Security (Docker hardening)
   - Web Server Hardening (nginx/Apache)
   - Database Hardening

9. BACKUP & RECOVERY:
   - Backup-Strategie
   - Offsite-Backup
   - Restore-Tests
   - Disaster Recovery Plan

10. COMPLIANCE:
    - CIS Benchmarks anwenden
    - Automatisierte Scans (Lynis, OpenSCAP)
    - Dokumentation

LIEFERE:
- Bash-Scripts für Hardening
- Konfigurationsdateien
- Checklisten
- Dokumentation

═══════════════════════════════════════
QUALITÄTSKONTROLLE
═══════════════════════════════════════

Prüfe dein Ergebnis:
□ Sind alle unnötigen Services deaktiviert und Ports geschlossen?
□ Ist SSH ausschließlich mit Key-Auth und ohne Root-Zugang konfiguriert?
□ Ist File Integrity Monitoring (AIDE) eingerichtet?
□ Besteht der Server einen Lynis/OpenSCAP-Scan mit dem Ziel-Score?
□ Würde ein Penetration Tester an diesem Server scheitern?
```

## Anwendung

**Für:** System-Administratoren, Security-Teams, Compliance-Projekte

**Beispiel-Output:** Vollständig gehärteter Ubuntu-Server mit CIS Level 1 Compliance, automatisiert via Ansible

**Preisstufen:**
| Service | Preis |
|---------|-------|
| Basis-Hardening (1 Server, CIS Level 1) | 3.000 - 5.000€ |
| Erweitertes Hardening (Multi-Server, CIS Level 2, Ansible) | 5.000 - 10.000€ |
| Enterprise-Hardening (Fleet, Compliance-Reporting, Audit-Prep) | 10.000 - 15.000€ |

**Kundensegmente:**
- Hosting-Unternehmen die ihre Infrastruktur absichern müssen
- Mittelständler vor Security-Audits oder Compliance-Zertifizierungen
- Startups mit sensiblen Daten (FinTech, HealthTech)

**Wo Kunden finden:**
- LinkedIn (CISO, IT-Leiter, Security Engineer)
- Security-Meetups und BSides-Konferenzen
- Freelancer-Plattformen (Toptal, Malt)
- Empfehlungen über Pentest- und Audit-Projekte

## Variationen

- Für Web: "Webserver-Hardening (nginx/Apache)"
- Für Datenbanken: "Database Server Hardening"
- Für Cloud: "Cloud-Instance Hardening (AWS/GCP)"
- Für Container: "Container und Kubernetes Hardening"
