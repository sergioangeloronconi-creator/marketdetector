# FASE LATERAL v2.1 — Documentazione Ufficiale Congelata

**Modulo:** Market Detector — LATERAL  
**Versione:** v2.1 FINAL  
**Stato:** FROZEN / CONGELATO  
**Data Freeze:** 2026-02-09  
**Autore:** Q-Mentor Framework  
**Status:** PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE

**IMPORTANTE:** La fase LATERAL ha **precedenza su Bear e Bull** (Priorità 2 > Priorità 1)

---

## 🔒 DECISIONE STRATEGICA

La fase LATERAL v2.1 è dichiarata:

**DEFINITIVA, CONGELATA, NON MODIFICABILE**

A partire da questo momento:
- ❌ Il codice non va più modificato
- ❌ Le soglie non vanno ottimizzate
- ❌ La logica non va estesa
- ✅ Il modulo viene trattato come verità operativa

---

## 📋 SCOPO DELLA FASE LATERAL

La LATERAL è una fase primaria del Market Detector e ha il solo compito di:

1. **Identificare periodi** in cui il prezzo non esprime direzionalità efficiente
2. **Fungere da gate di contesto**
3. **Impedire decisioni direzionali** non giustificate

### Cosa NON fa la LATERAL

- ❌ NON distingue accumulazione o distribuzione
- ❌ NON utilizza breadth
- ❌ NON anticipa fasi future
- ❌ NON è ottimizzata per performance di trading

---

## 🏗️ PRINCIPI ARCHITETTURALI (VINCOLANTI)

### 1. Fase Primaria

- La LATERAL è allo stesso livello di Bull / Bear
- **Sovrascrive Bull/Bear quando attiva**
- Priorità: 2 (superiore a Baseline, inferiore a fasi avanzate)

### 2. Stato Persistente

- La LATERAL è uno **stato**, non una condizione istantanea
- **Detection ≠ Stato**
- Richiede conferma prima di attivarsi

### 3. Ingresso Conservativo, Uscita Intelligente

- **Ingresso:** Lento e robusto
- **Uscita:** Rapida su:
  - Violazione core conditions
  - Movimento significativo del prezzo

### 4. Nessuna Dipendenza dal Futuro

- ❌ Nessuna logica basata su outcome
- ❌ Nessun look-ahead concettuale
- ✅ Solo dati storici e presenti

---

## ⚙️ IMPLEMENTAZIONE TECNICA v2.1

### Core Conditions

Condizioni fondamentali per identificare lateralità:

1. **Assenza di direzionalità**
2. **Inefficienza del movimento**

### Additional Conditions

Condizioni aggiuntive come conferma:

- Validano le core conditions
- Aumentano la robustezza della detection

### State Machine

La fase LATERAL implementa uno state machine con:

1. **CANDIDATO** (Candidate)
   - Rilevamento iniziale delle condizioni
   - Non ancora confermato

2. **CONFERMA** (Confirm)
   - Validazione delle condizioni
   - Stato LATERAL attivo

3. **USCITA** (Exit)
   - Uscita con isteresi
   - Prevenzione chattering

### Exit Dinamico

- **Exit su movimento cumulativo:** Rileva movimenti significativi del prezzo
- **Exit accelerato:** Su violazione delle core conditions

### Output Standardizzato

La fase LATERAL produce:

- `md_phase`: Fase corrente (LATERAL o altro)
- `md_phase_duration`: Durata della fase in barre
- `md_phase_confidence`: Livello di confidenza (0-1)
- `exit_reason`: Motivo dell'uscita (audit/debug)

---

## 🎨 Visualizzazione

### Colore

- **Grigio** - Sovrascrive Bull/Bear visivamente
- Priorità visiva: 2

### Comportamento

- Quando attiva, sovrascrive il colore verde (BULL) o rosso (BEAR)
- Il background diventa grigio durante la fase LATERAL

---

## 🚫 COSA È ESPLICITAMENTE FUORI SCOPE

Le seguenti evoluzioni **NON DEVONO** modificare questo modulo:

- ❌ Introduzione di LATERAL_ACCUM
- ❌ Introduzione di LATERAL_DIST
- ❌ Uso della breadth
- ❌ Integrazione con Decision Layer
- ❌ Ottimizzazione dei parametri
- ❌ Miglioramento estetico dei grafici

**Tutte queste evoluzioni devono avvenire SOPRA la LATERAL, mai DENTRO.**

---

## ✅ PROBLEMI RISOLTI IN v2.1

La versione v2.1 ha risolto:

1. ✅ **Instabilità di stato** - State machine robusto
2. ✅ **Chattering** - Exit con isteresi
3. ✅ **Eccessiva persistenza** - Exit dinamico migliorato
4. ✅ **Exit tardive** - Exit accelerato su violazione core
5. ✅ **Ambiguità semantiche** - Logica chiara e documentata

---

## 📊 VERSIONING UFFICIALE

**Modulo:** Market Detector — LATERAL  
**Versione:** v2.1 FINAL  
**Stato:** FROZEN  
**Data Freeze:** 2026-02-09  
**Autore:** Q-Mentor Framework

---

## 🔒 REGOLE DI CONGELAMENTO

### Cosa è Congelato

✅ **Logica di detection:**
- Core conditions
- Additional conditions
- State machine (candidato → conferma → uscita)

✅ **Sistema di exit:**
- Exit dinamico su movimento cumulativo
- Exit accelerato su violazione core
- Isteresi per prevenire chattering

✅ **Output standardizzato:**
- md_phase
- md_phase_duration
- md_phase_confidence
- exit_reason

### Modifiche Consentite

⚠️ **Solo con approvazione formale:**
- Modifiche alla logica di detection
- Cambiamenti alle soglie
- Modifiche allo state machine
- Aggiornamenti al sistema di exit

### Processo di Modifica

1. **Richiesta formale** di modifica
2. **Nuova versione** (es. v2.2)
3. **Nuovo documento** di versione
4. **Validazione completa** con dati storici
5. **Test di regressione** completi
6. **Approvazione** prima del commit

---

## 📝 NOTA CONCLUSIVA

**Congelare un modulo è una decisione di maturità progettuale.**

La fase LATERAL ha raggiunto il suo massimo livello utile.

Ogni ulteriore miglioramento:
- Appartiene alle **sottofasi**
- Non a questa **fase primaria**

**FREEZE APPROVATO.**

---

## ⚠️ ISTRUZIONE FINALE

Questo documento:
- ✅ NON è una bozza
- ✅ NON è un report esplorativo
- ✅ NON è materiale didattico
- ✅ **È un documento operativo definitivo**

Il codice riportato rappresenta:
- ✅ L'unica implementazione valida della fase LATERAL
- ✅ Qualsiasi modifica futura richiede nuova versione, nuovo documento, nuova validazione

---

**Q-Mentor Framework | Market Detector | Fase LATERAL v2.1 FINAL - FROZEN**
