# Task 04: Trenutni Fiskalni Prihodi

**Prioritet:** 🔴 KRITIČAN (TASK-03 zavisi!)
**Trajanje:** 2-3 dana
**Output:** `Trenutni-Fiskalni-Prihodi-Podaci.md`

---

## Zadatak

Pronađi TAČNE podatke o trenutnim prihodima koje Srbija ostvaruje od sistema fiksnih naknada.

## Istraži

1. **Zakonske naknade (minimumi):**
   - https://www.paragraf.rs/propisi/zakon_o_igrama_na_srecu.html
   - Član 75: Minimalna naknada po automatu?
   - Član 90: Minimalna naknada po uplatno-isplatnom mestu?

2. **Stvarni prihodi:**
   - **Uprava za igre na sreću:** https://uis.gov.rs/
   - **Ministarstvo finansija:** https://www.mfin.gov.rs/
   - Godišnji izveštaji, budžetski dokumenti

3. **Traži konkretno:**
   - Ukupan godišnji prihod od naknada za automate?
   - Ukupan godišnji prihod od naknada za kladionice?
   - Ukupan prihod od poreza na GGR (15%)?

## Potreban Output za TASK-03

```
TRENUTNI_PRIHODI = {
  kladionice: {
    broj: 2921,
    naknada_mesecno: X€,
    godisnje: Y€
  },
  automati: {
    broj: 33000,
    naknada_mesecno: Z€,
    godisnje: W€
  },
  porezi_GGR_15%: V€,
  UKUPNO: T€
}
```

## Deliverable

`Trenutni-Fiskalni-Prihodi-Podaci.md` (10-15 str):

1. **Executive Summary** (trenutni UKUPNO prihod)
2. **Zakonski okvir** (tačni tekstovi čl. 75, 90)
3. **Tabela prihoda:**
   | Komponenta | Broj | Naknada/mes | Godišnje | Izvor |
4. **Trend 2020-2025** (ako dostupno)
5. **Distribucija prihoda** (40% namenske svrhe - kome?)
6. **Kvalitet podataka** (zvanično/procenjeno?)
7. **Konkretni podaci za TASK-03** (format iznad)

## Ako Podaci Nisu Dostupni

- **Jasno to označi!**
- Koristi procensku metodologiju
- Označi stepen pouzdanosti (visok/srednji/nizak)
- Možda treba FOI zahtev?

## Success Criteria

✅ Zakonske naknade verifikovane
✅ Stvarni prihodi pronađeni ILI procenjeni (jasno označeno)
✅ SVI izvori citirani
✅ Format koji TASK-03 može koristiti
