# Narodna Inicijativa - Analiza Zakona o Igrama na Sreću

Sveobuhvatna analiza predloga Narodne inicijative za izmenu Zakona o igrama na sreću u Republici Srbiji.

## O projektu

Ovaj repozitorijum sadrži detaljnu pravnu, ekonomsku i socijalnu analizu predloga za reformu sistema licenciranja igara na sreću u Srbiji. Analiza uključuje više nezavisnih izveštaja generisanih različitim AI modelima, meta-analizu, fact-checking, kao i specijalizovane studije.

### Ključni nalazi

- **Srbija je na 2. mestu u Evropi** po gustini kladionica (44.3/100k stanovnika)
- **51,000-93,000 problematičnih kockara** procenjeno u Srbiji (procena iz 2018, zastarelo)
- **320 miliona EUR godišnje** prihoda od igara na sreću (0.36-0.39% BDP-a, 2024)
- **Visoke pravne i ustavne barijere** za uspeh inicijative

## Struktura dokumentacije

```
docs/
├── izvestaji/           # Glavni analitički izveštaji
│   ├── claude-raw1.md           # Claude analiza
│   ├── Analiza predloga...md    # Gemini analiza
│   ├── gpt51rawv1.md            # GPT analiza
│   ├── codex_high.md            # Codex analiza
│   ├── Meta-Analiza-*.md        # Meta-analiza i sinteza
│   └── *-V2.md                  # Unapređene verzije
│
├── pravna-analiza/      # Pravna i ustavna analiza
│   ├── Pravni-Memo-Clan48-Verifikacija.md
│   ├── Precedenti-Clan48-Analiza.md
│   ├── Ustavnosudska-Analiza.md
│   └── ICSID-Arbitraza-Rizici.md
│
├── fiskalna-analiza/    # Ekonomska i fiskalna analiza
│   ├── Fiskalni-Model-Aukcije.md
│   ├── Trenutni-Fiskalni-Prihodi-*.md
│   └── FISKALNI-MODEL-*.md
│
├── istrazivanja/        # Istraživačke studije
│   ├── Prevalenca-Zavisnosti-*.md
│   └── Komparativna-Studija-Kvote.md
│
├── ria/                 # Regulatory Impact Assessment
│   ├── RIA-Terms-of-Reference.md
│   └── RIA-Potencijalni-Izvrsitelji.md
│
├── prezentacije/        # Prezentacioni materijali
│   ├── Policy-Brief-Executive.md
│   ├── Prezentacija-Struktura.md
│   └── Infografika-Struktura.md
│
└── proces/              # Procesna dokumentacija
    └── *.md
```

## Ključna dokumenta

| Dokument | Opis |
|----------|------|
| [Policy Brief](docs/prezentacije/Policy-Brief-Executive.md) | Executive summary za donosioce odluka (5-7 min čitanja) |
| [Meta-Analiza](docs/izvestaji/Meta-Analiza-Izvestaja.md) | Uporedna verifikacija svih izveštaja |
| [Pravni Memo - Član 48](docs/pravna-analiza/Pravni-Memo-Clan48-Verifikacija.md) | Analiza proceduralne barijere |
| [Fiskalni Model](docs/fiskalna-analiza/Fiskalni-Model-Aukcije.md) | Matematički model fiskalnih efekata |
| [Komparativna Studija](docs/istrazivanja/Komparativna-Studija-Kvote.md) | Analiza sistema u Belgiji, Italiji i Holandiji |

## Glavni pravni rizici

1. **Član 48 Zakona o referendumu** - Zabrana za "poreske i druge finansijske zakone" (50-70% verovatnoća blokade)
2. **Član 97 Ustava** - Nadležnost Republike za poreski sistem (60-70% rizik od poništavanja)
3. **ICSID arbitraža** - Rizik od međunarodnih investicionih tužbi

## Tehnički detalji

Projekat koristi Claude Code subagente za specijalizovane analize:
- Pravna verifikacija člana 48
- Istraživanje precedenata Narodne skupštine
- Fiskalno modeliranje
- Komparativne studije
- Ustavnosudska analiza
- Priprema RIA dokumentacije

## Ključni nalazi analize

Analiza identifikuje značajne pravne i fiskalne rizike inicijative u trenutnom obliku. Pravne barijere uključuju član 48 Zakona o referendumu i član 97 Ustava. Postoje alternativni pristupi koji nose manje rizike.

### Alternativne strategije za razmatranje

1. **Centralizovana regulatorna reforma** - Izmena zakona kroz redovnu proceduru
2. **Gradualni pristup** - Postepeno smanjenje broja dozvola
3. **Strožije regulatorne mere** - Zabrana reklama, ograničenje radnog vremena

---

**Datum analize:** Novembar 2025
**Status:** Analiza završena
