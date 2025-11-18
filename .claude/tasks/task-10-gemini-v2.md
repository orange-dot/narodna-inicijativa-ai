# Task 10: Unapređenje Gemini Izveštaja (v2)

**Prioritet:** 🟡 VAŽAN
**Trajanje:** 3-5 dana
**Output:** `Analiza-predloga-zakona-Gemini-v2.md` + `Gemini-v2-Change-Log.md`
**Dependencies:** TASK-01, 03, 05

---

## Zadatak

Ažurirati Gemini izveštaj primenom svih identifikovanih unapređenja iz Cross-Check dokumenta.

## Input Fajlovi

- **Original:** `Analiza predloga zakona o igrama na sreću-gemini.md`
- **TASK-01:** `Pravni-Memo-Clan48-Verifikacija.md`
- **TASK-03:** `Fiskalni-Model-Aukcije.md`
- **TASK-05:** `Prevalenca-Zavisnosti-Azurirani-Podaci.md`

## Unapređenja

### 1. **DODATI: Nova sekcija "Analiza člana 48"** ⭐⭐⭐ KRITIČNO

Integrisi output iz TASK-01:
- Dodaj kao novu sekciju **"II.D. Analiza člana 48 Zakona o referendumu"**
- Umesti POSLE "II.C. Ključni uvidi iz pravne analize"
- Format: Cirilica (konzistentno sa Gemini stilom)

Struktura:
- Tačan tekst člana 48
- Argumenti ZA primenjivost
- Argumenti PROTIV primenjivosti
- Precedenti
- Finalna ocena

### 2. **DODATI: Kvantitativna fiskalna analiza**

Integrisi output iz TASK-03:
- Zameni spekulacije konkretnim brojkama u sekciji **"IV.B. Procena Ostvarivanja Cilja 2"**
- Dodaj tabelu sa 3 scenarija (Best/Base/Worst)
- Dodaj break-even analizu

### 3. **AŽURIRATI: Podatke o zavisnosti**

Integrisi output iz TASK-05:
- U sekciji **"III.D. Tvrđnja 4"** i **"IV.C. Procena Ostvarivanja Cilja 3"**
- Ako su podaci i dalje iz 2018, dodaj disclaimer:
  > "Napomena: Najnoviji dostupni podaci su iz 2018. godine. Potrebna je nova studija posle reformi 2024."

### 4. **UKLONITI/KVALIFIKOVATI: Slabe izvore**

- **Ukloni:** Reddit thread iz "Works cited"
- **Kvalifikuj:** Medijske izvore (Serbian Monitor, Vesti.rs, Euronews)
  - Dodaj napomenu: "Medijski izvori korišćeni za ilustraciju javnog mišljenja, ne kao primarni dokaz."

## Deliverables

1. **`Analiza-predloga-zakona-Gemini-v2.md`:**
   - Kompletno ažuriran izveštaj
   - Cirilica
   - Ista struktura + nove sekcije
   - Ažurirana bibliografija

2. **`Gemini-v2-Change-Log.md`:**
   - Lista SVIH promena
   - Šta je dodato
   - Šta je uklonjeno
   - Šta je modifikovano

## Tone & Style

- Zadrži originalni Gemini stil (akademski, neutralan, cirilica)
- Konzistentna terminologija
- Formalno citiranje

## Success Criteria

✅ Član 48 analiza integrisana
✅ Kvantitativna fiskalna analiza dodата
✅ Podaci o zavisnosti ažurirani ili disclaimer dodat
✅ Slabi izvori uklonjeni/kvalifikovani
✅ Change log detaljan
