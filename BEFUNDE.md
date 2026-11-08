# Maintainer-Befunde

## 2026-08-01 — Live-Zahlen des öffentlichen Ökosystem-Indexes weichen ab

Status: erledigt am 2026-08-03; die kuratierte Indexzahl wurde nach Live-GitHub-Abgleich aktualisiert.

Der lokale Index in `README.md`, `profile/README.md`, `profile/README_de.md` und
`llms.txt` behauptete 89 aktive öffentliche Produkt- oder
Forschungs-Repositories plus 10 aktive öffentliche `.github`-Profil-Repositories
(insgesamt 99).

Live-Prüfung am 2026-08-01 um 18:07 Europe/Berlin mit:

```powershell
gh repo list <organisation> --limit 100 --json name,isArchived,isFork,isPrivate
```

Gezählt wurden `isArchived=false`, `isFork=false`, `isPrivate=false`;
das aktive Repository `.github` wurde als Profil-Repository separat gezählt:

| Organisation | aktive Repositories | aktive `.github`-Profile | aktive Produkt-/Forschungs-Repositories |
|---|---:|---:|---:|
| file-bricks | 15 | 1 | 14 |
| doc-bricks | 10 | 1 | 9 |
| dev-bricks | 10 | 1 | 9 |
| ellmos-ai | 47 | 1 | 46 |
| research-line | 6 | 1 | 5 |
| biotec-line | 3 | 1 | 2 |
| assistassets-ai | 2 | 1 | 1 |
| entertain-and-more | 4 | 1 | 3 |
| um-bruch | 6 | 1 | 5 |
| open-bricks | 1 | 1 | 0 |
| **Summe** | **104** | **10** | **94** |

Abweichungen gegenüber der veröffentlichten Tabelle:

- `dev-bricks`: 9 live statt 15 dokumentiert
- `ellmos-ai`: 46 live statt 36 dokumentiert
- `entertain-and-more`: 3 live statt 2 dokumentiert

Die vier Indexoberflächen waren dadurch nicht mehr als aktueller gemeinsamer
Stand belegbar. Der Folgelauf am 2026-08-03 hat `README.md`, `profile/README.md`,
`profile/README_de.md` und `llms.txt` auf 94 aktive Produkt-/Forschungs-Repos
plus 10 aktive `.github`-Profilrepos aktualisiert und die veralteten
`dev-bricks`-Beispiellinks ersetzt.

## 2026-11-08 — Turnusmäßiger Health-Audit & Paritäts-Abgleich

Status: erledigt am 2026-11-08; sämtliche Indexoberflächen auf 150 aktive öffentliche Repositories synchronisiert.

Vollständiger Live-Inventar-Abgleich über alle 10 Organisationen mit `gh repo list <org> --limit 200 --json name,isArchived,isFork,isPrivate`:

| Organisation | aktive Repositories | aktive `.github`-Profile | aktive Produkt-/Forschungs-Repositories |
|---|---:|---:|---:|---:|
| file-bricks | 17 | 1 | 16 |
| doc-bricks | 12 | 1 | 11 |
| dev-bricks | 14 | 1 | 13 (+1 arch.) |
| ellmos-ai | 83 | 1 | 82 (+2 arch.) |
| research-line | 8 | 1 | 7 (+1 arch.) |
| biotec-line | 3 | 1 | 2 |
| assistassets-ai | 2 | 1 | 1 |
| entertain-and-more | 4 | 1 | 3 |
| um-bruch | 6 | 1 | 5 |
| open-bricks | 1 | 1 | 0 |
| **Summe** | **150** | **10** | **140** |

Abweichungen und Korrekturen gegenüber Stand 2026-11-01:
- `ellmos-ai`: 82 aktive Produkt-Repositories (+15 gegenüber der aggregierten Zählung vom 01.11.; u. a. `ellmos-plugins` als neuer Marktplatzkatalog, `ellmos-codecommander-mcp`, `skills`, `lock-master`, `decision-clicker`, `ticket-master`).
- `research-line`: 7 aktive Produkt-Repositories (+1; `eth-dependency-atlas` zur formale Dependenz- und Smart-Contract-Analyse aufgenommen).
- Gesamtzahl aktiver öffentlicher Repositories von 134 auf 150 aktualisiert.
- Paritätstestsuite `tests/test_profile_parity.py` aktualisiert (8/8 Tests 100% grün).

## 2026-11-01 — Turnusmäßiger Health-Audit & Paritäts-Abgleich

Status: erledigt am 2026-11-01; sämtliche Indexoberflächen auf 134 aktive öffentliche Repositories synchronisiert.

Vollständiger Live-Inventar-Abgleich über alle 10 Organisationen mit `gh repo list <org> --limit 100 --json name,isArchived,isFork,isPrivate`:

| Organisation | aktive Repositories | aktive `.github`-Profile | aktive Produkt-/Forschungs-Repositories |
|---|---:|---:|---:|
| file-bricks | 17 | 1 | 16 |
| doc-bricks | 12 | 1 | 11 |
| dev-bricks | 14 | 1 | 13 (+1 arch.) |
| ellmos-ai | 68 | 1 | 67 |
| research-line | 7 | 1 | 6 (+1 arch.) |
| biotec-line | 3 | 1 | 2 |
| assistassets-ai | 2 | 1 | 1 |
| entertain-and-more | 4 | 1 | 3 |
| um-bruch | 6 | 1 | 5 |
| open-bricks | 1 | 1 | 0 |
| **Summe** | **134** | **10** | **124** |

Abweichungen und Korrekturen gegenüber Stand 2026-10-10:
- `file-bricks`: 16 aktive Produkt-Repos (+1; `KnowledgeDigest`, `absorber` und `RSS-BOOK` in Index und Spotlight aufgenommen).
- `dev-bricks`: 13 aktive Produkt-Repos (+2; `companion-for-agy` gemäß D-20261030-011 kanonisch indiziert, `githubbot-core` aufgenommen).
- `ellmos-ai`: 67 aktive Produkt-Repos (Konsolidierung / Bereinigung; veralteter doppelter Eintrag von `companion-for-agy` bereinigt).
- `um-bruch`: 5 aktive Produkt-Repos (`verordnungsampel`, `regressangst`, `system-medicine`, `multiaxial-diagnostic-system`, `locuterra` vollständig indiziert).
- Gesamtzahl von 139 auf 134 aktive öffentliche Repositories korrigiert.
- Paritätstestsuite `tests/test_profile_parity.py` erweitert (8/8 Tests 100% grün).
