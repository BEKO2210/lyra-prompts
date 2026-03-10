---
id: "#2345"
titel: "PowerShell Script to Move Disabled AD Users to Specific OU"
kategorie: "Beruf & Karriere"
unterkategorie: "Importiert"
tags: ["powershell", "script", "move", "disabled", "users"]
plattformen: ["ChatGPT", "Claude", "Gemini"]
schwierigkeit: "Anfänger"
quelle: "awesome-chatgpt-prompts"
autor: "dark.valerik.spb@gmail.com"
erstellt: "2026-03-09"
---

## Prompt

```
Act as a System Administrator. You are tasked with managing user accounts in Active Directory (AD). Your task is to create a PowerShell script that:

- Identifies all disabled user accounts in the AD.
- Moves these accounts to a designated Organizational Unit (OU) specified by the variable ${targetOU}.

Rules:
- Ensure that the script is efficient and handles errors gracefully.
- Include comments in the script to explain each section.

Example PowerShell Script:
```
# Define the target OU
$targetOU = "OU=DisabledUsers,DC=yourdomain,DC=com"

# Get all disabled user accounts
$disabledUsers = Get-ADUser -Filter {Enabled -eq $false}

# Move each disabled user to the target OU
foreach ($user in $disabledUsers) {
    try {
        Move-ADObject -Identity $user.DistinguishedName -TargetPath $targetOU
        Write-Host "Moved: $($user.SamAccountName) to $targetOU"
    } catch {
        Write-Host "Failed to move $($user.SamAccountName): $_"
    }
}
```
Variables:
- ${targetOU} - The distinguished name of the target Organizational Unit where disabled users will be moved.
```

## Anwendung

**Thema: System Administrator, You Are** — Dein persoenlicher Nachhilfelehrer fuer jedes Thema. Die KI erklaert komplexe Sachverhalte verstaendlich und gibt Lernhilfen.

Kopiere den Prompt und fuege ihn in ChatGPT, Claude oder Gemini ein.
Passe die Details an deine Beduerfnisse an.

## Variationen

- Gib dein Vorwissensniveau an (Anfaenger, Fortgeschritten, Experte)
- Frage nach Analogien und Alltagsbeispielen
- Bitte um Uebungsaufgaben mit Loesungen
- Frage nach weiterfuehrenden Ressourcen und Buechern
