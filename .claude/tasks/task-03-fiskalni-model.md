# Task 03: Kvantitativni Fiskalni Model

**Prioritet:** 🔴 KRITIČAN
**Trajanje:** 3-5 dana
**Output:** `Fiskalni-Model-Aukcije.md` + `Fiskalni-Model-Aukcije-SIMPLE.md`
**Dependencies:** ⚠️ ČEKA podatke iz TASK-04

---

## Zadatak

Kreiraj **matematički model** koji kvantifikuje fiskalne efekte:
- **Trenutni sistem:** Fiksne naknade
- **Predloženi sistem:** Aukcije za licence

## Potrebni Podaci (iz TASK-04)

```
TRENUTNO:
- Kladionice: 2,921 × X€/mesec × 12 = Y€/god
- Automati: 33,000 × Z€/mesec × 12 = W€/god
- Porezi (15% GGR): V€/god
UKUPNO: T€
```

## Kreiraj 3 Scenarija

**SCENARIO A: OPTIMISTIČNI**
- Redukcija broja: 30%
- Aukcijska cena: +100% vs. trenutne
- GGR: bez promene
- **Rezultat:** X€ (Delta: +Y%)

**SCENARIO B: BAZNI**
- Redukcija: 50%
- Aukcijska cena: +50%
- GGR: -15%
- **Rezultat:** Z€ (Delta: +/-W%)

**SCENARIO C: PESIMISTIČNI**
- Redukcija: 70%
- Aukcijska cena: +200%
- GGR: -35%
- **Rezultat:** V€ (Delta: -T%)

## Break-Even Analiza

**Pitanje:** Koliko mora biti aukcijska cena da se nadoknadi gubitak od smanjenja broja?

Formula:
```
Break_Even = (Trenutna_Naknada × Trenutni_Broj) / Novi_Broj
```

Tabela:
| Redukcija | Potrebna cena | Realno? |
|-----------|---------------|---------|
| 30% | +43% | DA |
| 50% | +100% | MOŽDA |
| 70% | +233% | MALO VEROVATNO |

## Deliverables

1. **`Fiskalni-Model-Aukcije.md`** (20-25 str):
   - Metodologija
   - Trenutni sistem (detaljno)
   - 3 scenarija sa formulama
   - Break-even analiza
   - Sensitivity analiza
   - Rizici
   - Finalna procena (weighted average)

2. **`Fiskalni-Model-Aukcije-SIMPLE.md`** (1-2 str):
   - Samo tabela i zaključak za donosioca odluke

## Kritično

**SVE formule moraju biti transparentne i proverljive.** Eksterni ekonomista mora moći da replicira rezultate.
