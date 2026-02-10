# Manifesto di Gerarchia - Market Detector

**Documento:** Costituzione del Market Detector  
**Versione:** 1.0 FINAL  
**Stato:** FROZEN / CONGELATO  
**Data Congelamento:** 2026-02-09  
**Q-Mentor Framework - Market Detector**

**🔒 COSTITUZIONE DEL SISTEMA - VERSIONE DEFINITIVA CONGELATA**

**⚠️ IMPORTANTE:** Questa versione sostituisce tutte le versioni precedenti della gerarchia.  
**NON MODIFICABILE SENZA DECISIONE ARCHITETTURALE ESPLICITA.**

---

## 1. SCOPO DEL MARKET DETECTOR

Il Market Detector **non prevede, non ottimizza, non decide trade**.

Il suo unico compito è:

**Descrivere lo stato del mercato con autorità gerarchica,**
**separando ciò che è osservabile dal prezzo**
**da ciò che è inferito dai comportamenti interni.**

---

## 2. PRINCIPIO CARDINE (VINCOLANTE)

**Le informazioni di mercato non hanno tutte la stessa autorità.**

Il sistema deve riconoscerle in un ordine preciso.

**Ciò che viene identificato a un livello superiore**
**non può essere sovrascritto da un livello inferiore.**

---

## 3. GERARCHIA UFFICIALE DEI LIVELLI

### 🔴 LIVELLO 0 — EVENTI SISTEMICI (AUTORITÀ ASSOLUTA)

**Cosa sono:**
- Shock rari, violenti, price-driven
- Non ambigui

**Stati:**
- **CRASH**
- **CAPITULATION** (sistemica)

**Regola:**
- Se LIVELLO 0 è attivo → tutti gli altri livelli sono informativi ma non rilevanti

---

### 🟠 LIVELLO 1 — REGIME STRUTTURALE (SPINA DORSALE)

**Cosa descrive:**
- Cosa fa il prezzo

**Stati:**
- **BULL**
- **BEAR**
- **LATERAL**
- **RECOVERY**

**Proprietà:**
- Mutualmente esclusivi
- Persistenti
- Auditabili

**Regola:**
- Solo uno stato di LIVELLO 1 può essere attivo alla volta

**Status:**
- ✅ BULL/BEAR: CONGELATE
- ✅ LATERAL: CONGELATA (v2.1 FINAL)
- ✅ RECOVERY: CONGELATA (Concetto v1.0 FINAL) - Vedi FASE_RECOVERY_FROZEN.md

---

### 🟡 LIVELLO 2 — EVENTI LOCALI DI STRESS

**Cosa descrive:**
- Perdita temporanea di controllo del flusso

**Stati:**
- **LoCE** (Loss of Control Event)
- **Capitulation locale**

**Regola:**
- Possono apparire in Bull, Bear o Lateral
- Non cambiano il regime

**Status:**
- ⚠️ In sviluppo

---

### 🟢 LIVELLO 3 — PROCESSI DI RISCHIO SISTEMICO

**Cosa descrive:**
- Se il rischio sta entrando o uscendo dal sistema

**Stati:**
- **ACCUMULATION**
- **DISTRIBUTION**
- **NONE**

**Caratteristiche:**
- Inferiti dalla partecipazione (breadth)
- Non osservabili direttamente dal prezzo
- Possono coesistere con Bull, Bear o Lateral

**⚠️ IMPORTANTE:** Accumulation/Distribution **NON sono fasi**, sono **processi**.

**Status:**
- ⚠️ In sviluppo

---

### 🔵 LIVELLO 4 — ROTAZIONE SETTORIALE

**Cosa descrive:**
- Dove il rischio si rialloca all'interno del regime

**Stati (esempi):**
- **ROTATION_TO_CYCLICAL**
- **ROTATION_TO_DEFENSIVE**
- **ROTATION_TO_GROWTH**
- **NONE**

**Regola chiave:**
- La rotazione **non implica** né accumulazione né distribuzione.

**Status:**
- ⚠️ In sviluppo

---

### ⚪ LIVELLO 5 — QUALIFICATORI

**Cosa descrive:**
- Intensità
- Persistenza
- Confidence

**Autorità:**
- Descrittiva

**Status:**
- ⚠️ In sviluppo

---

## 4. STATO DI TRANSIZIONE (DERIVATO)

Lo stato di transizione **non è un livello**, ma una **condizione logica**.

```
md_transition = TRUE
se:
  LIVELLO 3 ≠ NONE
  e LIVELLO 3 è incoerente con LIVELLO 1
```

### Esempi

- **Bull + Distribution** → Transition
- **Bear + Accumulation** → Transition

**Regola:**
- La transizione è **derivata**, non decisa direttamente

---

## 5. REGOLA D'ORO (CHIUSURA)

**Il regime dice dove siamo.**
**I processi dicono cosa il mercato prepara.**
**La rotazione dice dove il capitale si sposta.**
**Nessuno di questi può sostituire l'altro.**

Questo principio è **vincolante** per tutto il framework Q-Mentor.

---

## 6. FORMA STANDARD DI COMUNICAZIONE

Ogni output del Market Detector deve essere espresso come:

**Regime → Processo → Rotazione (+ eventuale Transizione)**

### Esempio

**"Bull market, distribuzione in atto, rotazione verso settori difensivi."**

**Traduzione interna:**
```
md_phase          = BULL
md_process        = DISTRIBUTION
sector_rotation   = TRUE (difensiva)
md_transition     = TRUE
```

**Interpretazione operativa:**
- ✅ Trend ancora positivo
- ⚠️ Rischio sistemico che inizia a uscire
- ⚠️ Capitale che si sposta verso difensivi
- ⚠️ Fase di attenzione massima
- ❌ Non è ancora Bear
- ❌ Non è un contesto aggressivo

---

## 7. VINCOLI ASSOLUTI

### Vincoli Gerarchici

1. **Nessun livello può sovrascrivere un livello superiore**
2. **Accumulation / Distribution NON sono fasi** (sono processi - LIVELLO 3)
3. **Rotazione settoriale NON implica transizione**
4. **Lo stato di Transizione è derivato, non deciso**
5. **La LATERAL v2.1 resta intoccabile**

### Divieti

- ❌ Non semplificare la gerarchia
- ❌ Non fondere livelli
- ❌ Non introdurre shortcut decisionali
- ❌ Non usare sotto-livelli come trigger

---

## 8. STATO DEL DOCUMENTO

**Documento:** Costituzione del Market Detector  
**Stato:** FROZEN  
**Modificabile solo con decisione architetturale esplicita**

---

## 📋 OUTPUT STANDARDIZZATO

### Struttura Messaggio (Vincolante)

```json
{
  "md_phase": "BULL|BEAR|LATERAL|RECOVERY",      // LIVELLO 1
  "md_process": "ACCUMULATION|DISTRIBUTION|NONE", // LIVELLO 3
  "sector_rotation": true|false,                  // LIVELLO 4
  "sector_rotation_type": "ciclica|difensiva|none", // LIVELLO 4
  "md_transition": true|false,                     // Derivato
  "md_level_0_event": "CRASH|CAPITULATION|NONE",  // LIVELLO 0 (se attivo)
  "md_level_2_event": "LoCE|LOCAL_CAPITULATION|NONE" // LIVELLO 2 (se attivo)
}
```

### Ordine di Comunicazione

**Sempre in questo ordine:**
1. LIVELLO 0 (se attivo) - Eventi Sistemici
2. LIVELLO 1 - Regime Strutturale
3. LIVELLO 2 (se attivo) - Eventi Locali di Stress
4. LIVELLO 3 - Processi di Rischio
5. LIVELLO 4 - Rotazione Settoriale
6. md_transition (derivato)

---

## 🔗 Riferimenti

- `GERARCHIA_FASI_BULL_BEAR_LATERALITA.md` - Gerarchia fasi congelate
- `FASE_BULL_BEAR.md` - Documentazione fase Bull/Bear
- `FASE_LATERAL_v2.1_FROZEN.md` - Documentazione fase LATERAL
- `COMUNICAZIONE_MULTILIVELLO.md` - Comunicazione multilivello
- `market_detector.pine` - Implementazione codice

---

**Q-Mentor Framework | Market Detector | Manifesto Gerarchia - COSTITUZIONE FROZEN**
