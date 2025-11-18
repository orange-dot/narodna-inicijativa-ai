# Task 11: Unapređenje Claude Izveštaja (v2)

**Prioritet:** 🟡 VAŽAN
**Trajanje:** 3-5 dana
**Output:** `Claude-raw-v2.md` + `Claude-v2-Change-Log.md`
**Dependencies:** TASK-01, 03, 05

---

## Zadatak

Ažurirati Claude izveštaj primenom svih identifikovanih unapređenja.

## Input Fajlovi

- **Original:** `claude-raw1.md`
- **TASK-01, 03, 05** outputi

## Unapređenja

### 1. **DODATI: Formalna bibliografija** ⭐⭐ VAŽNO

Kreirati "Works Cited" sekciju na kraju:
- Svi izvori sa URL-ovima
- Akademski format
- Grupisano po tipu (zakoni, studije, mediji)

Format:
```
## Works Cited

### Legal Sources
1. Zakon o referendumu i narodnoj inicijativi. https://www.paragraf.rs/...
2. Ustav Republike Srbije. https://www.paragraf.rs/...

### Academic & Research
3. EGBA (2024). Gambling Statistics...

### Official Reports
4. Uprava za igre na sreću (2024). Godišnji izveštaj...

### Media (for context)
5. Serbian Monitor (2024). "Serbia to limit betting operations"...
```

### 2. **ZAMENITI: Procenu "<10%"**

U sekciji **"Ustavna analiza: Višestruke fundamentalne prepreke"**:

UKLONI:
> "Verovatnoća uspeha: Manje od 10%"

ZAMENI SA:
> **Scenario analiza verovatnoće uspeha:**
>
> - **Scenario A** (član 48 se primenjuje): 0-5%
> - **Scenario B** (član 48 se NE primenjuje): 10-20%
> - **Scenario C** (pravna neizvesnost): Prolongiranje 6-12 meseci
>
> *Napomena: Ovo je analitička procena zasnovana na pravnoj analizi, ne pravno mišljenje stručne službe.*

### 3. **DODATI: Kvantitativna fiskalna analiza**

Integrisi TASK-03:
- U sekciji **"Ekonomski i socijalni efekti"**
- Zameni spekulacije "350-500M€" konkretnim modelom

### 4. **AŽURIRATI: Zastarele podatke**

Integrisi TASK-05:
- 51k-93k (2018) + disclaimer

### 5. **UBLAŽITI: Preterano asertivan ton**

Pretraži i zameni:
- "potpuno netačno" → "faktografski netačno"
- "krajnje neprobabnim" → "malo verovatnim"
- Zadrži asertivnost gde je zasnovana na dokazima

## Deliverables

1. **`Claude-raw-v2.md`:**
   - Ažuriran izveštaj
   - Latinica (original stil)
   - Formalna bibliografija
   - Scenario analiza

2. **`Claude-v2-Change-Log.md`:**
   - Detaljne promene

## Success Criteria

✅ Bibliografija dodата
✅ Scenario analiza umesto "<10%"
✅ Kvantitativna analiza integrisana
✅ Ton ublažen gde potrebno
