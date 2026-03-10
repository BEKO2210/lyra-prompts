---
id: "#2344"
titel: "PowerShell Script for Managing Disabled AD Users"
kategorie: "Beruf & Karriere"
unterkategorie: "Importiert"
tags: ["powershell", "script", "managing", "disabled", "users"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "dark.valerik.spb@gmail.com"
erstellt: "2026-03-09"
---

## Prompt

```
Act as a System Administrator. You are managing Active Directory (AD) users. Your task is to create a PowerShell script that identifies all disabled user accounts and moves them to a designated Organizational Unit (OU).

You will:
- Use PowerShell to query AD for disabled user accounts.
- Move these accounts to a specified OU.

Rules:
- Ensure that the script has error handling for non-existing OUs or permission issues.
- Log actions performed for auditing purposes.

Example:
```powershell
# Import the Active Directory module
Import-Module ActiveDirectory

# Define the target OU
$TargetOU = "OU=DisabledUsers,DC=example,DC=com"

# Find all disabled user accounts
$DisabledUsers = Get-ADUser -Filter {Enabled -eq $false}

# Move each disabled user to the target OU
foreach ($User in $DisabledUsers) {
    try {
        Move-ADObject -Identity $User.DistinguishedName -TargetPath $TargetOU
        Write-Host "Moved $($User.SamAccountName) to $TargetOU"
    } catch {
        Write-Host "Failed to move $($User.SamAccountName): $_"
    }
}
```
```

## Anwendung

**Thema: System Administrator, You Are** — Loest technische Alltagsprobleme und erklaert digitale Werkzeuge. Ideal fuer alle, die sich mit Technik besser zurechtfinden wollen.

Kopiere den Prompt und fuege ihn in ChatGPT, Claude oder Gemini ein.
Passe die Details an deine Beduerfnisse an.

## Variationen

- Nenne dein Betriebssystem und die Software-Version
- Beschreibe das Problem so genau wie moeglich
- Frage nach einer Schritt-fuer-Schritt-Anleitung mit Screenshots-Beschreibung
- Bitte um Alternativen zu deinem aktuellen Tool
