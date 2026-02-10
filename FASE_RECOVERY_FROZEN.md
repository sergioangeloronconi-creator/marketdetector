# FASE RECOVERY — Documentazione Ufficiale Congelata

**Modulo:** Market Detector — RECOVERY  
**Versione:** 1.0 FINAL - Congelata (Concetto)  
**Stato:** FROZEN / CONGELATO - LIVELLO CONCETTUALE  
**Data Freeze:** 2026-02-09  
**Autore:** Q-Mentor Framework  
**Status:** PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE

**🔒 COSTITUZIONE DEL MARKET DETECTOR - FASE CONGELATA**

---

## 📋 STATUS

**Fase:** RECOVERY  
**Livello:** 1 (fase strutturale, pari a Bull / Bear / Lateral)  
**Stato:** CONGELATA A LIVELLO CONCETTUALE  
**Modificabile:** ❌ (solo tuning implementativo consentito)

---

## 📖 DEFINIZIONE UFFICIALE

**Recovery è la fase in cui il regime ribassista ha perso efficacia strutturale,**
**ma il mercato non ha ancora dimostrato di essere tornato in regime rialzista.**

---

## 🔒 PROPRIETÀ VINCOLANTI

### Recovery È:

- ✅ **Price-driven** - Determinata dal comportamento del prezzo
- ✅ **Strutturale** - Fase di LIVELLO 1, non processo
- ✅ **Temporanea** - Non persistente come Bull/Bear
- ✅ **Fallibile** - Può fallire e tornare a Bear

### Recovery NON È:

- ❌ **Rimbalzo** - Non è solo un rimbalzo tecnico
- ❌ **Bull precoce** - Non anticipa Bull senza conferme
- ❌ **Lateralità generica** - Ha memoria di stress, nasce dopo Bear
- ❌ **Processo** - Accumulation ≠ Recovery (Accumulation è LIVELLO 3)

---

## 🔄 TRANSIZIONI AMMESSE (CONGELATE)

### Transizioni Valide

✅ **BEAR → RECOVERY → BEAR** (fallimento)  
✅ **BEAR → RECOVERY → LATERAL**  
✅ **BEAR → RECOVERY → BULL** (raro)  
✅ **CRASH → BEAR → RECOVERY**  
✅ **CRASH → RECOVERY → BEAR**

### ❌ Transizioni Vietate

❌ **BEAR → BULL diretto** (non ammesso - deve passare per Recovery o Lateral)

**Regola:** Recovery è una fase di transizione obbligatoria dopo Bear, prima di poter tornare a Bull.

---

## 🎯 GERARCHIA

### Recovery NON può essere sovrascritta da:

- ❌ Accumulation / Distribution (LIVELLO 3 - processi)
- ❌ Rotazione settoriale (LIVELLO 4)
- ❌ Eventi locali di stress (LIVELLO 2)

### Recovery può coesistere con:

- ✅ Processi latenti (ACCUMULATION, DISTRIBUTION, NONE)
- ✅ Rotazioni settoriali
- ✅ Eventi locali (LoCE, Capitulation locale)

**Regola:** Recovery è LIVELLO 1, quindi ha priorità su LIVELLO 2, 3, 4, 5.

---

## 🔍 DISTINZIONI CONCETTUALI

### Recovery vs Bear

- **BEAR:** Nuovi minimi continuano, accelerazione ribassista possibile
- **RECOVERY:** Fallimento ripetuto nel fare nuovi minimi, Bear perde efficacia operativa

**Transizione:** Bear → Recovery quando Bear perde efficacia strutturale.

### Recovery vs Lateral

- **LATERAL:** Equilibrio neutro, assenza di memoria direzionale, può avvenire ovunque
- **RECOVERY:** Nasce solo dopo Bear, ha memoria di stress, contesto fragile, può tornare a Bear

**Asimmetria fondamentale:** Una LATERAL non può tornare BEAR, una RECOVERY sì.

### Recovery vs Bull

- **BULL:** Struttura positiva, trend efficiente, nuovi massimi relativi
- **RECOVERY:** Non richiede struttura rialzista, prezzo ancora sotto medie chiave, leadership assente/instabile

**Transizione:** Recovery → Bull richiede conferme aggiuntive (non automatica).

### Recovery vs Crash

- **CRASH:** Evento di LIVELLO 0, interrompe tutto, non è un regime
- **RECOVERY:** Fase strutturale di LIVELLO 1

**Dopo CRASH:** Sistema rientra in BEAR (default), Recovery emerge solo se Bear perde efficacia.

---

## 📊 COLLISION TEST

**Status:** ✅ SUPERATO

Vedi `COLLISION_TEST_RECOVERY.md` per dettagli completi.

**Risultato:** Nessuna collisione fatale individuata. Recovery è semanticamente distinta, non ridondante, non pericolosa.

---

## 🎯 REGOLA D'ORO (CHIUSURA)

**Recovery non dice che il mercato salirà.**  
**Dice solo che il Bear, per ora, non riesce più a funzionare.**

Questa è la proprietà fondamentale che distingue Recovery da altre fasi.

---

## 💻 IMPLEMENTAZIONE

### Status Implementativo

- ⚠️ **Logica implementativa:** In sviluppo (tuning consentito)
- ✅ **Concetto:** Congelato (non modificabile)

**Nota:** Il concetto è congelato, ma la logica implementativa può essere ottimizzata per rilevare correttamente Recovery.

### File Codice

- `phases/phase_4_recovery.pine` - Implementazione (in sviluppo)

---

## 🔗 Riferimenti

- `MANIFESTO_GERARCHIA.md` - Gerarchia costituzionale completa
- `COLLISION_TEST_RECOVERY.md` - Test di collisione (superato)
- `FASE_BULL_BEAR.md` - Documentazione fase Bull/Bear (congelata)
- `FASE_LATERAL_v2.1_FROZEN.md` - Documentazione fase LATERAL (congelata)
- `market_detector.pine` - Implementazione codice

---

## 📝 Changelog

### Versione 1.0 FINAL (2026-02-09) - Congelata

- ✅ Definizione ufficiale formalizzata
- ✅ Proprietà vincolanti documentate
- ✅ Transizioni ammesse/vietate definite
- ✅ Gerarchia chiarita
- ✅ Distinzioni concettuali documentate
- ✅ Collision Test superato
- ✅ Regola d'oro formalizzata
- ✅ CONGELAMENTO A LIVELLO CONCETTUALE

---

## ⚠️ NOTA FINALE

**Questo documento è ora parte della Costituzione del Market Detector.**

Il concetto di Recovery è **congelato** e **non modificabile** senza decisione architetturale esplicita.

Solo il tuning implementativo è consentito per migliorare la rilevazione della fase.

---

**Q-Mentor Framework | Market Detector | Fase RECOVERY v1.0 FINAL - CONGELATA (Concetto)**
