# FISKALNI MODEL - DOKUMENTACIJA

**CHECKPOINT 2: Fiskalna analiza aukcijskog sistema za igre na sreću**

**Datum:** 18. novembar 2025

---

## Dokumenti (čitati ovim redom)

### 1. Za donosioca odluke (POČNI OVDE)

**`CHECKPOINT-02-PREPORUKA.md`** (4 strane)
- Analiza fiskalnih efekata
- Ključni nalazi i rizici
- Opcije za razmatranje

**`Fiskalni-Model-Aukcije-SIMPLE.md`** (2 strane)
- Executive summary sa tabelama
- Svi scenariji i projekcije
- Quick reference

### 2. Za detaljnu analizu

**`Fiskalni-Model-Aukcije.md`** (25 strana, ~25,000 reči)
- Kompletan matematički model
- Svi proračuni i formule
- Sensitivity analiza
- Break-even analiza
- Rizici i uporedni primeri
- Python kod (ilustrativan)

### 3. Pozadinski podaci

**`Trenutni-Fiskalni-Prihodi-Podaci.md`** (15 strana)
- Istraživački izveštaj SUBAGENT-04
- Baseline podaci (320M EUR)
- Zakonski okvir (član 75, 90 ZoIS)
- Metodologija i ograničenja

**`Trenutni-Fiskalni-Prihodi-SIMPLE.md`** (2 strane)
- Quick reference trenutnog sistema
- Input parametri za model

---

## Ključni nalazi (TL;DR)

**PITANJE:**
Može li aukcijski sistem generisati iste ili veće fiskalne prihode?

**ODGOVOR:**
**NE.** Očekivani gubitak: **-45%** (-143M EUR godišnje)

**RAZLOG:**
Kontinuirani porezi (44% prihoda) strukturalno padaju zbog smanjenja broja objekata. Aukcije ne mogu nadoknaditi ovaj gubitak.

**VEROVATNOĆA FISKALNOG PROFITA:**
<10% (scenarijska procena bez empirijske validacije)

**NALAZ:**
Model identifikuje značajan fiskalni rizik

---

## Projekcije - Brzi pregled

| Scenario | Težina (subjektivna) | Prihod | Delta |
|----------|----------------------|--------|-------|
| **Trenutno** | - | 320M EUR | - |
| **Optimistični** | Niži rizik | 244M EUR | -76M EUR (-24%) |
| **Bazni** | Interna procena | 175M EUR | -145M EUR (-45%) |
| **Pesimistični** | Visok rizik | 110M EUR | -210M EUR (-66%) |

**Weighted average:** 177M EUR (-143M EUR, -45%) — ilustrativna tezina zasnovana na internim pretpostavkama.

---

## Alternativni koraci

**AKO SE IPAK ODLUČI NASTAVITI:**

1. **Regulatory Impact Assessment (RIA)** - nezavisna studija (3-6 meseci)
2. **Pilot program** - 2-3 opštine, 12-24 meseca
3. **Robusna online regulativa** - enforcement prvo
4. **Aukcijski dizajn** - angažovati eksperta

**ALTERNATIVNE POLITIKE (bez fiskalnog rizika):**

1. Enhanced enforcement (200m od škola)
2. Revenue sharing sa opštinama
3. Opt-out mechanism
4. Investicija u tretman (5-10M EUR godišnje)

---

## Kontakt za pitanja

**Model pripremio:** Financial Modeling Economist (SUBAGENT-03)
**Pozadinski podaci:** Data Research Agent (SUBAGENT-04)

**Verifikacija:** Sve agregatne brojke (320M EUR) verifikovane iz više nezavisnih izvora.

**Ograničenja:** Projekcije imaju velike neizvesnosne opsege zbog nedostatka empirijskih podataka o elastičnosti GGR i aukcijskoj dinamici.

---

## Struktura modela

```
UKUPNI FISKALNI PRIHOD = DIREKTNE NAKNADE + KONTINUIRANI POREZI

DIREKTNE NAKNADE = broj_objekata × naknada_po_objektu × 12
  - Trenutno: 177M EUR
  - Sa aukcijama: Zavisi od aukcijskih cena i redukcije broja

KONTINUIRANI POREZI = GGR × 15%
  - Trenutno: 140M EUR (iz GGR od 933M EUR)
  - Sa aukcijama: PADA (manje objekata = manji GGR)

KLJUČNI PROBLEM:
  Pad kontinuiranih poreza NADMAŠUJE rast direktnih naknada
```

---

## Metodologija

**Verifikovani input podaci:**
- Ukupni prihodi: 320M EUR (Nova Ekonomija, 12. maj 2025 + izjava Ministarstva finansija; EGBA 2023 nije javno dostupan)
- Broj kladionica: 2,921 (zvanični registar)
- Broj automata: ~33,000 (procena)
- Zakonski minimumi: 50€/200€ mesečno (član 75, 90 ZoIS)
- Porezna stopa: 15% na GGR (Zakon 142/2024)

**Procene sa neizvesnošću:**
- Elastičnost GGR: 0.3 - 1.5 (nemamo empirijskih podataka)
- Aukcijske cene: 1.2× - 3.0× trenutne (nijedna aukcija održana)
- Offshore migracija: 5% - 30% (zavisi od enforcement)

**Model:** Scenario-based (3 scenarija) + sensitivity analiza + Monte Carlo (konceptualno)

---

## Kvalitet podataka

| Komponenta | Pouzdanost | Komentar |
|------------|------------|----------|
| Ukupni prihodi (320M) | VISOKA | Verifikovano iz više izvora |
| Zakonski minimumi | VISOKA | Član 75, 90 ZoIS |
| Broj objekata | VISOKA | 2,921 kladionica tačno |
| Breakdown direktnih naknada | SREDNJA | Procenjeno (nedostaje službeni breakdown) |
| Elastičnost GGR | NISKA | Nema empirijskih studija za Srbiju |
| Aukcijska dinamika | NISKA | Nijedna aukcija održana |

**Transparentnost:** Sve neizvesnosti jasno označene. Model je verifikabilan.

---

**Za brzo čitanje:** Počni sa `CHECKPOINT-02-PREPORUKA.md`

**Za detalje:** Pročitaj `Fiskalni-Model-Aukcije.md`

**Za background:** Vidi `Trenutni-Fiskalni-Prihodi-Podaci.md`

---

**ZAKLJUČAK ANALIZE**

Model identifikuje značajan fiskalni rizik. Opcije za razmatranje: pilot program ili alternativne politike.

---
