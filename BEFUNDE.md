# Maintainer-Befunde

## 2026-08-01 — Live-Zahlen des öffentlichen Ökosystem-Indexes weichen ab

Status: offen; keine kuratierte Indexzahl eigenmächtig geändert.

Der lokale Index in `README.md`, `profile/README.md`, `profile/README_de.md` und
`llms.txt` behauptet weiterhin 89 aktive öffentliche Produkt- oder
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

Die vier Indexoberflächen sind dadurch nicht mehr als aktueller gemeinsamer
Stand belegbar. Eine Korrektur erfordert eine abgestimmte Prüfung der
organisationsübergreifenden Repository-Liste und der repräsentativen Links;
dieser Maintainer-Lauf nimmt diese kuratierte Inhaltsentscheidung nicht vor.
