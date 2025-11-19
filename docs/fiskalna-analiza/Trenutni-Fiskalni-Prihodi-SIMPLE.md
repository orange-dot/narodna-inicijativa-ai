# TRENUTNI FISKALNI PRIHODI OD IGARA NA SREĆU - EXECUTIVE SUMMARY

**Za: SUBAGENT-03 (Quick Reference)**
**Datum: 18. novembar 2025**

---

## KLJUČNE BROJKE (Visoka pouzdanost)

### Ukupni godišnji prihodi: ~320 miliona €

| Komponenta | Iznos | Status |
|------------|-------|--------|
| **Direktne naknade** | 177M€ | ✅ VERIFIKOVANO |
| **Porezi na GGR (15%)** | 140M€ | ✅ VERIFIKOVANO |
| **UKUPNO** | **320M€** | ✅ VERIFIKOVANO |

### Osnovni parametri

| Parametar | Vrednost |
|-----------|----------|
| Broj kladionica | 2,921 |
| Broj automata | ~33,000 |
| Minimalna naknada - automat | 50€/mesec (600€/god) |
| Minimalna naknada - kladionica | 200€/mesec (2,400€/god) |
| Porezna stopa na GGR | 15% |
| Procenjeni GGR | ~933M€ |

---

## ŠTO ZNAMO (Sigurno)

✅ **UKUPNI PRIHODI:** 320M€ godišnje
✅ **ZAKONSKI MINIMUMI:** 50€/automat, 200€/kladionica (mesečno)
✅ **BROJ OBJEKATA:** 2,921 kladionica, ~33,000 automata
✅ **POREZNI REŽIM:** 15% na GGR (od 2024)
✅ **MAKRO ZNAČAJ:** ~0.36-0.39% BDP-a (2024), ~2.1% budžeta

## ŠTO NE ZNAMO (Kritične praznine)

🔴 **BREAKDOWN 177M€:** Koliko od kladionica? Koliko od automata? Koliko od online?
🔴 **PROSEČNE NAKNADE:** Da li operateri plaćaju više od minimuma?
🔴 **ELASTIČNOST GGR:** Kako će GGR pasti ako broj objekata padne?
🔴 **TRENDOVI 2020-2025:** Kako su prihodi rasli/padali?
🔴 **DISTRIBUCIJA:** Tačni iznosi za Crveni krst, sport, itd.?

---

## ZA MATEMATIČKI MODEL

### Input parametri (sigurni)

```python
TRENUTNI_SISTEM = {
    "ukupno": 320_000_000,      # EUR/godišnje
    "direktne": 177_000_000,    # EUR/godišnje
    "porezi": 140_000_000,      # EUR/godišnje
    "N_kladionica": 2921,
    "N_automati": 33000,
    "C_automat_min": 50,        # EUR/mesec
    "C_kladionica_min": 200,    # EUR/mesec
    "T_GGR": 0.15               # 15%
}
```

### Scenariji (sa wide ranges zbog neizvesnosti)

**OPTIMISTIČNI:**
- Redukcija: 30%, Aukcija: +100%, GGR pad: -15%
- **Rezultat: ~244M€ (-24%)**

**BAZNI:**
- Redukcija: 50%, Aukcija: +50%, GGR pad: -35%
- **Rezultat: ~175M€ (-45%)**

**PESIMISTIČNI:**
- Redukcija: 70%, Aukcija: +200%, GGR pad: -60%
- **Rezultat: ~110M€ (-66%)**

---

## KLJUČNI ZAKLJUČAK

**Čak i u optimističnom scenariju, postoji VISOK RIZIK fiskalnog gubitka zbog:**
1. Redukcije broja objekata
2. Pada GGR (kontinuiranih poreza - 44% ukupnih prihoda!)
3. Online migracije

**PROJEKCIJE SU NEIZVESNE** zbog nedostatka kritičnih podataka o:
- Elastičnosti GGR
- Prosečnim stvarnim naknadama
- Dinamici aukcija

---

## PREPORUKE

**Za kreiranje modela:**
1. Koristi agregatne brojke kao BASELINE
2. Kreiraj ŠIROKE scenarije
3. Uradi ekstenzivnu SENSITIVITY analizu
4. Jasno označi SVE pretpostavke

**Za poboljšanje podataka:**
1. FOI zahtev Ministarstvu finansija (detaljni breakdown)
2. FOI zahtev Upravi za igre na sreću (godišnji izveštaji)
3. Kontakt sa primaocima sredstava (Crveni krst, sport)

---

**Detaljni izveštaj:** `Trenutni-Fiskalni-Prihodi-Podaci.md` (15 strana)
