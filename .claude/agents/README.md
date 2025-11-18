# Agent Registry - Narodna Inicijativa Analiza

**Datum:** 18. novembar 2025
**Projekat:** Analiza Narodne inicijative za izmenu Zakona o igrama na sreću

---

## Kako koristiti agente

### Opcija 1: Direktan poziv (ako podržano)
```
/agent subagent-01-clan48-verifikacija
```

### Opcija 2: Kroz Task tool
U razgovoru sa Claude-om, koristi Task tool da pozoveš agenta autonomno.

---

## 🔴 PRIORITET 1: KRITIČNI AGENTI (1-2 nedelje)

### SUBAGENT-01: Pravna Verifikacija Člana 48
**Fajl:** `subagent-01-clan48-verifikacija.md`
**Opis:** Pravna verifikacija primenjivosti člana 48 Zakona o referendumu
**Output:** `Pravni-Memo-Clan48-Verifikacija.md` (10-15 str)
**Trajanje:** 1-2 dana
**Prioritet:** ⭐⭐⭐⭐⭐ NAJKRITIČNIJI

**Ključna pitanja:**
- Da li član 48 blokira inicijativu?
- "Finansijski zakoni" - usko ili široko tumačenje?
- Precedenti u praksi NS?

---

### SUBAGENT-02: Pregled Precedenata Narodne Skupštine
**Fajl:** `subagent-02-precedenti-skupstina.md`
**Opis:** Istorijska analiza primene člana 48
**Output:** `Precedenti-Clan48-Analiza.md` (15-20 str)
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐⭐⭐ KRITIČAN

**Ključna pitanja:**
- Koliko puta je član 48 bio primenjen?
- Kako su tumačeni "fiskalni zakoni"?
- Relevantni slučajevi?

---

### SUBAGENT-03: Kvantitativna Fiskalna Analiza
**Fajl:** `subagent-03-fiskalni-model.md`
**Opis:** Matematički model trenutnih vs. aukcijskih prihoda
**Output:**
- `Fiskalni-Model-Aukcije.md` (20-25 str)
- `Fiskalni-Model-Aukcije-SIMPLE.md` (1-2 str)
**Trajanje:** 3-5 dana
**Prioritet:** ⭐⭐⭐⭐⭐ KRITIČAN
**Dependencies:** ČEKA podatke iz SUBAGENT-04

**Ključne deliverables:**
- Best/Base/Worst scenariji
- Break-even analiza
- Sensitivity analiza

---

### SUBAGENT-04: Trenutni Fiskalni Prihodi
**Fajl:** `subagent-04-trenutni-prihodi.md`
**Opis:** Istraživanje TAČNIH trenutnih prihoda od naknada
**Output:** `Trenutni-Fiskalni-Prihodi-Podaci.md` (10-15 str)
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐⭐⭐ KRITIČAN (SUBAGENT-03 zavisi od ovoga!)

**Ključna pitanja:**
- Koliko država TRENUTNO zarađuje?
- Minimalne vs. prosečne naknade?
- Breakdown po tipu (kladionice/automati/porezi)?

---

### SUBAGENT-05: Prevalenca Zavisnosti (Ažurni Podaci)
**Fajl:** `subagent-05-prevalenca-zavisnosti.md`
**Opis:** Najnoviji podaci o problematičnim kockarima
**Output:** `Prevalenca-Zavisnosti-Azurirani-Podaci.md` (12-18 str)
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐⭐

**Ključna pitanja:**
- Postoji li studija POSLE 2018?
- ESPAD 2023/2024 podaci?
- Efekti reformi 2024?

---

## 🟠 PRIORITET 2: VEOMA VAŽNI AGENTI (2-4 nedelje, samo ako P1 prođe)

### SUBAGENT-06: RIA Priprema (Terms of Reference)
**Fajl:** `subagent-06-ria-priprema.md`
**Opis:** Priprema ToR dokumenta za eksternu RIA studiju
**Output:**
- `ToR-Regulatorna-Procena-Uticaja.md` (20-30 str)
- `RIA-Potencijalni-Izvrsitelji.md`
**Trajanje:** 5-7 dana
**Prioritet:** ⭐⭐⭐

---

### SUBAGENT-07: Komparativna Studija
**Fajl:** `subagent-07-komparativna-studija.md`
**Opis:** Belgija, Italija, Holandija - kako rade sistemi kvota?
**Output:** `Komparativna-Studija-Belgija-Italija-Holandija.md` (30-40 str)
**Trajanje:** 7-10 dana
**Prioritet:** ⭐⭐⭐

**Za svaku zemlju:**
- Pravni okvir
- Proces implementacije
- Efekti (fiskalni, socijalni)
- Lekcije za Srbiju

---

### SUBAGENT-08: Međunarodna Arbitraža (Rizik ICSID)
**Fajl:** `subagent-08-medjunarodna-arbitraza.md`
**Opis:** Rizik od investicionih arbitraža (Flutter, etc.)
**Output:** `Analiza-Rizika-Medjunarodne-Arbitraze.md` (12-18 str)
**Trajanje:** 5-7 dana
**Prioritet:** ⭐⭐⭐

**Ključna pitanja:**
- BIT ugovori?
- Precedenti (gaming sector)?
- Potencijalni iznos odštete?

---

### SUBAGENT-09: Ustavnosudska Analiza (Detaljno)
**Fajl:** `subagent-09-ustavnosudska-analiza.md`
**Opis:** Najdublja analiza ustavne održivosti
**Output:**
- `Ustavnosudska-Analiza-Detaljna.md` (35-45 str)
- `Executive-Summary-Ustavni-Sud.md` (2 str)
**Trajanje:** 7-10 dana
**Prioritet:** ⭐⭐⭐

**Analiza:** Član 97, 177, 178, 195, 203 + precedenti US

---

## 🟡 PRIORITET 3: VAŽNI AGENTI (Finalizacija i dokumentacija)

### SUBAGENT-10: Unapređenje Gemini Izveštaja
**Fajl:** `subagent-10-gemini-v2.md`
**Output:**
- `Analiza-predloga-zakona-Gemini-v2.md`
- `Gemini-v2-Change-Log.md`
**Trajanje:** 3-5 dana
**Prioritet:** ⭐⭐

**Unapređenja:**
- Dodati analizu člana 48
- Kvantitativna fiskalna analiza
- Ažurirani podaci
- Ukloniti Reddit iz izvora

---

### SUBAGENT-11: Unapređenje Claude Izveštaja
**Fajl:** `subagent-11-claude-v2.md`
**Output:**
- `Claude-raw-v2.md`
- `Claude-v2-Change-Log.md`
**Trajanje:** 3-5 dana
**Prioritet:** ⭐⭐

**Unapređenja:**
- Formalna bibliografija
- Scenario analiza umesto "<10%"
- Kvantitativna fiskalna analiza
- Ublažiti asertivan ton

---

### SUBAGENT-12: Unapređenje Meta-Analize
**Fajl:** `subagent-12-meta-v2.md`
**Output:**
- `Meta-Analiza-Izvestaja-v2.md`
- `Meta-v2-Change-Log.md`
**Trajanje:** 3-5 dana
**Prioritet:** ⭐⭐

**Unapređenja:**
- Integriraj sve nove nalaze (SUBAGENT-01 do 09)
- Kvantitativna fiskalna sekcija
- Ocena pouzdanosti izvora

---

### SUBAGENT-13: Executive Summary
**Fajl:** `subagent-13-executive-summary.md`
**Opis:** Ultra-koncizni Policy Brief za donosioca odluke
**Output:**
- `Executive-Summary-Donosilac-Odluke.md` (2-4 str MAX)
- `Infografika-Struktura.md`
**Trajanje:** 2-3 dana
**Prioritet:** ⭐⭐⭐

**Format:** 4 strane MAX, bullet points, actionable

---

### SUBAGENT-14: Prezentacija za Skupštinu
**Fajl:** `subagent-14-prezentacija.md`
**Opis:** Struktura PowerPoint prezentacije (~25 slajdova)
**Output:** `Prezentacija-Narodna-Skupstina-Struktura.md`
**Trajanje:** 3-4 dana
**Prioritet:** ⭐⭐

**Deliverable:** Detaljna struktura svaki slajd + speaker notes

---

### SUBAGENT-15: NZ Monitoring (Ongoing)
**Fajl:** `subagent-15-nz-monitoring.md`
**Opis:** Longitudinalni monitoring NZ aukcije 2026
**Output:** Quarterly updates + finalni izveštaj
**Trajanje:** 12-18 meseci (ongoing)
**Prioritet:** ⭐

**Timeline:**
- Q1 2025: Status update
- Q2-Q3 2025: Auction monitoring
- Q4 2025/Q1 2026: Rezultati
- Q2-Q4 2026: Evaluacija

---

## Execution Strategy

### FAST-TRACK (2 nedelje):
Izvršiti samo P1 agente (01-05) paralelno
→ Dobiti odluku o članu 48
→ Odlučiti o daљim koracima

### FULL ANALYSIS (6-8 nedelja):
1. **Nedelje 1-2:** P1 agenti (01-05) paralelno
2. **Nedelja 3:** Odluka o članu 48
3. **Nedelje 4-8:** P2 agenti (06-09) ako prođe član 48
4. **Nedelje 8-10:** P3 agenti (10-14) finalizacija
5. **Ongoing:** SUBAGENT-15 (NZ monitoring)

---

## Dependencies Map

```
PRIORITET 1 (Paralelno):
├─ SUBAGENT-01 (Član 48) ────┐
├─ SUBAGENT-02 (Precedenti) ──┤
├─ SUBAGENT-04 (Trenutni prihodi) ─┐
└─ SUBAGENT-05 (Zavisnost) ────────┘
                                    │
                                    ▼
                    SUBAGENT-03 (Fiskalni model)
                                    │
                                    ▼
                            [Odluka o članu 48]
                                    │
                        ┌───────────┴───────────┐
                    Ako PROĐE              Ako NE PROĐE
                        │                       │
                        ▼                       ▼
                 PRIORITET 2              KRAJ (ili alternative)
```

---

## Quality Control Checklist

Svaki agent mora ispoštovati:
- [ ] Svi izvori citirani sa URL-ovima
- [ ] Jasno razlikovanje ČINJENICA vs. PROCENA
- [ ] Transparentna metodologija
- [ ] Eksplicitna ograničenja analize
- [ ] Konkretni, action-oriented deliverables
- [ ] Markdown format sa jasnim naslovima

---

## Support Materials

**Bazni dokumenti (već postojeći):**
- `Subagenti-Plan-Izvrsenja.md` - Detaljan master plan
- `Cross-Check-Sinteza-Final.md` - Cross-check sve 4 analize
- `Meta-Analiza-Izvestaja.md` - Originalna meta-analiza

**Ulazni dokumenti:**
- `Analiza predloga zakona o igrama na sreću-gemini.md` (Gemini)
- `claude-raw1.md` (Claude)
- `codex_high.md` (Codex High)

---

**Kreirao:** AI Agent System
**Datum:** 18. novembar 2025
**Status:** SPREMAN ZA IZVRŠENJE

**Next Step:** Pokreni agente po prioritetu ili sve odjednom!
