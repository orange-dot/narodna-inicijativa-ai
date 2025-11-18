# Task Registry - Narodna Inicijativa Analiza

**Projekat:** Analiza Narodne inicijative za izmenu Zakona o igrama na sreću
**Datum:** 18. novembar 2025

---

## Quick Start

### Izvršenje task-a:
```
Pokreni TASK-01 (član 48 verifikacija)
```

ili

```
Pokreni sve P1 task-ove paralelno (TASK-01 do 05)
```

---

## 🔴 PRIORITET 1: KRITIČNI (1-2 nedelje)

### TASK-01: Pravna Verifikacija Člana 48
**Output:** `Pravni-Memo-Clan48-Verifikacija.md` (10-15 str)
**Trajanje:** 1-2 dana
**Prioritet:** ⭐⭐⭐⭐⭐ NAJKRITIČNIJI

Da li član 48 Zakona o referendumu blokira inicijativu?

---

### TASK-02: Pregled Precedenata NS
**Output:** `Precedenti-Clan48-Analiza.md` (15-20 str)
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐⭐⭐

Kako je član 48 tumačen u praksi?

---

### TASK-03: Kvantitativni Fiskalni Model
**Output:** `Fiskalni-Model-Aukcije.md` (20-25 str) + Simple (1-2 str)
**Trajanje:** 3-5 dana
**Prioritet:** ⭐⭐⭐⭐⭐
**Dependencies:** ⚠️ ČEKA TASK-04

Matematički model trenutno vs. aukcije (Best/Base/Worst)

---

### TASK-04: Trenutni Fiskalni Prihodi
**Output:** `Trenutni-Fiskalni-Prihodi-Podaci.md` (10-15 str)
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐⭐⭐ (TASK-03 zavisi!)

Koliko država TRENUTNO zarađuje?

---

### TASK-05: Prevalenca Zavisnosti (Ažurno)
**Output:** `Prevalenca-Zavisnosti-Azurirani-Podaci.md` (12-18 str)
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐⭐

Postoje li novi podaci posle 2018?

---

## 🟠 PRIORITET 2: VEOMA VAŽNI (2-4 nedelje, ako P1 prođe)

### TASK-06: RIA Priprema (ToR)
**Output:** `ToR-Regulatorna-Procena-Uticaja.md` (20-30 str)
**Trajanje:** 5-7 dana
**Prioritet:** ⭐⭐⭐

Terms of Reference za eksternu RIA studiju

---

### TASK-07: Komparativna Studija
**Output:** `Komparativna-Studija-Belgija-Italija-Holandija.md` (30-40 str)
**Trajanje:** 7-10 dana
**Prioritet:** ⭐⭐⭐

Kako rade sistemi kvota u Belgiji/Italiji/Holandiji?

---

### TASK-08: Međunarodna Arbitraža
**Output:** `Analiza-Rizika-Medjunarodne-Arbitraze.md` (12-18 str)
**Trajanje:** 5-7 dana
**Prioritet:** ⭐⭐⭐

Rizik ICSID arbitraže (Flutter, etc.)

---

### TASK-09: Ustavnosudska Analiza
**Output:** `Ustavnosudska-Analiza-Detaljna.md` (35-45 str)
**Trajanje:** 7-10 dana
**Prioritet:** ⭐⭐⭐

Najdublja analiza ustavne održivosti

---

## 🟡 PRIORITET 3: VAŽNI (Finalizacija)

### TASK-10: Gemini v2
**Output:** `Analiza-predloga-zakona-Gemini-v2.md`
**Trajanje:** 3-5 dana
**Dependencies:** TASK-01, 03, 05

Unapređenje Gemini izveštaja

---

### TASK-11: Claude v2
**Output:** `Claude-raw-v2.md`
**Trajanje:** 3-5 dana
**Dependencies:** TASK-01, 03, 05

Unapređenje Claude izveštaja

---

### TASK-12: Meta v2
**Output:** `Meta-Analiza-Izvestaja-v2.md`
**Trajanje:** 3-5 dana
**Dependencies:** TASK-01 do 09

Unapređenje Meta-analize

---

### TASK-13: Executive Summary
**Output:** `Executive-Summary-Donosilac-Odluke.md` (2-4 str MAX!)
**Trajanje:** 2-3 dana
**Dependencies:** SVE prethodne

Ultra-koncizni Policy Brief

---

### TASK-14: Prezentacija
**Output:** `Prezentacija-Narodna-Skupstina-Struktura.md`
**Trajanje:** 3-4 dana
**Dependencies:** SVE prethodne

PowerPoint struktura (~25 slajdova)

---

### TASK-15: NZ Monitoring
**Output:** Quarterly updates + Finalni izveštaj
**Trajanje:** 12-18 meseci (ONGOING)
**Prioritet:** ⭐

Longitudinalni monitoring NZ aukcije 2026

---

## Execution Strategies

### FAST-TRACK (2 nedelje):
```
Izvršiti samo P1 (TASK-01 do 05) paralelno
→ Dobiti odluku o članu 48
→ Odlučiti dalje
```

### FULL ANALYSIS (6-8 nedelja):
```
Week 1-2: P1 paralelno
Week 3: Odluka o članu 48
Week 4-8: P2 ako prođe član 48
Week 8-10: P3 finalizacija
Ongoing: TASK-15
```

---

## Dependencies Map

```
P1 (Paralelno):
├─ TASK-01 (Član 48)
├─ TASK-02 (Precedenti)
├─ TASK-04 (Trenutni prihodi) ─┐
└─ TASK-05 (Zavisnost)          │
                                ▼
                       TASK-03 (Fiskalni model)
                                │
                                ▼
                        [Odluka o članu 48]
                                │
                    ┌───────────┴───────────┐
                Ako PROĐE              Ako NE PROĐE
                    │                       │
                    ▼                       ▼
                   P2                    KRAJ/ALT
```

---

## Support Materials

**Master Plan:** `Subagenti-Plan-Izvrsenja.md`
**Cross-Check:** `Cross-Check-Sinteza-Final.md`
**Meta-Analysis:** `Meta-Analiza-Izvestaja.md`

**Izvorni izveštaji:**
- `Analiza predloga zakona o igrama na sreću-gemini.md`
- `claude-raw1.md`
- `codex_high.md`

---

**Status:** SPREMAN ZA IZVRŠENJE
**Next:** Pokreni task-ove po prioritetu!
