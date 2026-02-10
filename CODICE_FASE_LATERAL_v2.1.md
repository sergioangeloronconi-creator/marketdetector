# Codice Fase LATERAL v2.1 - Versione Congelata

**Versione:** v2.1 FINAL  
**Data Congelamento:** 2026-02-09  
**Status:** FROZEN - PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE

---

## 📁 File del Codice

### 1. Pine Script - Fase LATERAL v2.1

**File:** `phases/phase_1_lateralita.pine`

**NOTA:** Il codice completo v2.1 deve essere fornito e inserito qui.

Il codice implementa:

- ✅ Core conditions (assenza direzionalità, inefficienza movimento)
- ✅ Additional conditions (conferma)
- ✅ State machine (candidato → conferma → uscita)
- ✅ Exit dinamico (movimento cumulativo)
- ✅ Exit accelerato (violazione core)
- ✅ Output standardizzato (md_phase, md_phase_duration, md_phase_confidence, exit_reason)

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

## ⚠️ NOTA IMPORTANTE

**Il codice completo v2.1 deve essere fornito e inserito in questo documento.**

Una volta fornito, questo documento diventerà la **riferimento ufficiale** per il codice congelato.

---

**Q-Mentor Framework | Market Detector | Codice Fase LATERAL v2.1 FINAL - FROZEN**
