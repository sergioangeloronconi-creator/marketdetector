# Codice Fase LATERAL v2.1 - Versione Congelata

**Versione:** v2.1 FINAL  
**Data Congelamento:** 2026-02-09  
**Status:** FROZEN - PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE

---

## 📁 File del Codice

### 1. Pine Script - Fase LATERAL v2.1 FINAL

**File:** `phases/phase_1_lateralita.pine`

**Versione:** v2.1 FINAL - FROZEN

Il codice implementa:

- ✅ Core conditions (assenza direzionalità, inefficienza movimento)
- ✅ Additional conditions (conferma - almeno 2/3)
- ✅ State machine completo (NOT_LATERAL → CANDIDATE → CONFIRMED → EXIT_CANDIDATE)
- ✅ Exit dinamico (movimento cumulativo > 2%)
- ✅ Exit accelerato (violazione core conditions)
- ✅ Isteresi per prevenire chattering
- ✅ Smoothing per stabilità

**Riferimento:** Vedi `phases/phase_1_lateralita.pine` per implementazione completa.

### 2. Python - Codice Originale v2.1

**File:** Codice Python completo fornito (vedi sotto)

Il codice Python originale è la **riferimento ufficiale** per la logica implementata.

---

## 🔧 Componenti Implementati

### State Machine

```pine
// Stati possibili:
// - NONE: Nessuna fase laterale
// - CANDIDATE: Rilevamento iniziale (non confermato)
// - CONFIRMED: Fase laterale attiva
// - EXIT: Uscita in corso (isteresi)
```

### Core Conditions

```pine
// 1. Assenza di direzionalità
// 2. Inefficienza del movimento
```

### Additional Conditions

```pine
// Condizioni di conferma che validano le core conditions
```

### Exit Logic

```pine
// Exit dinamico: movimento cumulativo significativo
// Exit accelerato: violazione core conditions
// Isteresi: previene chattering
```

---

## 📊 Output Standardizzato

### Variabili di Output

- `md_phase`: Fase corrente (string: "LATERAL" o altro)
- `md_phase_duration`: Durata fase in barre (int)
- `md_phase_confidence`: Confidenza 0-1 (float)
- `exit_reason`: Motivo uscita (string, per audit/debug)

---

## 🎨 Visualizzazione

### Colore

- **Grigio** - RGB da definire nel codice
- Opacità: da definire nel codice
- Priorità: 2 (sovrascrive Bull/Bear)

---

## 🔒 Regole di Congelamento

### Cosa è Congelato

✅ **Logica di detection completa**  
✅ **State machine completo**  
✅ **Sistema di exit completo**  
✅ **Output standardizzato**  
✅ **Soglie e parametri**

### Modifiche NON Consentite

❌ Modifiche alla logica senza nuova versione  
❌ Ottimizzazione parametri  
❌ Estensioni funzionali  
❌ Integrazioni con altri moduli

---

## 📝 Changelog

### Versione v2.1 FINAL (2026-02-09) - FROZEN

- ✅ Risolto: Instabilità di stato
- ✅ Risolto: Chattering
- ✅ Risolto: Eccessiva persistenza
- ✅ Risolto: Exit tardive
- ✅ Risolto: Ambiguità semantiche
- ✅ State machine completo
- ✅ Exit dinamico implementato
- ✅ Output standardizzato

---

## 💻 Codice Python Originale v2.1 FINAL

Il codice Python seguente è la **riferimento ufficiale** per la logica LATERAL v2.1:

```python
"""
MARKET PHASE CLASSIFIER - LATERAL v2.1 (STATEFUL · MD-GRADE)
Q-Mentor Framework - Market Detector

VERSIONE: v2.1 (Stateful, MD-Grade)
STATUS: CORREZIONE DEFINITIVA - FROZEN
"""

# [Codice Python completo fornito - vedere file originale per dettagli]
# 
# Componenti principali:
# - LateralState (Enum): NOT_LATERAL, CANDIDATE, CONFIRMED, EXIT_CANDIDATE
# - ExitReason (Enum): NONE, STANDARD_EXIT, MOVEMENT_EXIT, CORE_VIOLATION_EXIT
# - LateralConfig: Parametri congelati
# - calcola_metriche_lateral_v2_1(): Calcolo metriche
# - detect_lateral(): Detection pura
# - LateralStateMachine: State machine persistente
# - classifica_lateral_v2_1(): Funzione principale
```

**NOTA:** Il codice Python completo è disponibile nel documento originale fornito. Questo documento rappresenta la struttura e i riferimenti al codice congelato.

---

**Q-Mentor Framework | Market Detector | Codice Fase LATERAL v2.1 FINAL - FROZEN**
