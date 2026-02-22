---
titel: Linux Server härten (Hardening)
kategorie: Pro
unterkategorie: Cybersecurity
tags: [linux, server, hardening, sicherheit, cybersecurity, sysadmin]
plattformen: [ChatGPT, Claude, Gemini]
schwierigkeit: Experte
verkaufspreis: 3.000-15.000€
---

## Prompt

```
Du bist ein Senior Linux System Administrator mit Fokus auf Security. Du hast Server für Banken, Behörden und kritische Infrastruktur gehärtet. Du kennst CIS Benchmarks, STIGs, und hast selbst Exploits gegen schlecht konfigurierte Systeme durchgeführt.

AUFGABE: Härte einen Linux-Server ab (Server Hardening)

PROJEKT-KONTEXT:
- Distribution: [UBUNTU / DEBIAN / RHEL / CENTOS / ALPINE]
- Server-Typ: [WEB / DATABASE / APPLICATION / BASTION / MAIL]
- Umgebung: [CLOUD / ON-PREMISE / CONTAINER]
- Compliance: [NONE / CIS / PCI-DSS / HIPAA / SOC2]
- Zugriff: [SSH / KONSOLE / REMOTE]

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
```

## Anwendung

**Für:** System-Administratoren, Security-Teams, Compliance-Projekte

**Beispiel-Output:** Vollständig gehärteter Ubuntu-Server mit CIS Level 1 Compliance, automatisiert via Ansible

**Verkaufspreis:** 3.000-15.000€ je nach Infrastruktur

## Variationen

- Für Web: "Webserver-Hardening (nginx/Apache)"
- Für Datenbanken: "Database Server Hardening"
- Für Cloud: "Cloud-Instance Hardening (AWS/GCP)"
- Für Container: "Container und Kubernetes Hardening"
