# Comunicazione Multilivello - Market Detector

**Versione:** 1.0 - Ufficiale  
**Data:** 2026-02-09  
**Status:** PRODUZIONE - RIFERIMENTO UFFICIALE  
**Q-Mentor Framework - Market Detector**

**📖 Riferimento:** Vedi `MANIFESTO_GERARCHIA.md` per la gerarchia costituzionale completa.

---

## 🎯 Principio Fondamentale

Il Market Detector comunica attraverso una **comunicazione multilivello gerarchica**, non un'etichetta unica.

Questo approccio:
- ✅ Evita ambiguità
- ✅ È spiegabile a livelli diversi
- ✅ È coerente con la gerarchia delle fasi
- ✅ Fornisce contesto operativo completo

---

## 📊 Struttura del Messaggio (Vincolante)

Ogni stato di mercato viene comunicato **sempre** in questo ordine:

### 🔴 LIVELLO 0: Eventi Sistemici (Autorità Assoluta)
**Variabile:** `md_level_0_event`  
**Tipo:** String  
**Valori:** `"CRASH"`, `"CAPITULATION"`, `"NONE"`

**Definizione:** Shock rari, violenti, price-driven. Se attivo, tutti gli altri livelli sono informativi ma non rilevanti.

### 🟠 LIVELLO 1: Regime Strutturale (Spina Dorsale)
**Variabile:** `md_phase`  
**Tipo:** String  
**Valori:** `"BULL"`, `"BEAR"`, `"LATERAL"`, `"RECOVERY"`

**Definizione:** Cosa fa il prezzo. Mutualmente esclusivi - solo uno stato può essere attivo alla volta.

### 🟡 LIVELLO 2: Eventi Locali di Stress
**Variabile:** `md_level_2_event`  
**Tipo:** String  
**Valori:** `"LoCE"`, `"LOCAL_CAPITULATION"`, `"NONE"`

**Definizione:** Perdita temporanea di controllo del flusso. Possono apparire in Bull, Bear o Lateral.

### 🟢 LIVELLO 3: Processi di Rischio Sistemico
**Variabile:** `md_process`  
**Tipo:** String  
**Valori:** `"DISTRIBUTION"`, `"ACCUMULATION"`, `"NONE"`

**⚠️ IMPORTANTE:** Accumulation/Distribution **NON sono fasi**, sono **processi**.  
**Definizione:** Se il rischio sta entrando o uscendo dal sistema. Inferiti dalla partecipazione (breadth).

### 🔵 LIVELLO 4: Rotazione Settoriale
**Variabili:**
- `sector_rotation`: Boolean - Rotazione settoriale in atto
- `sector_rotation_type`: String - Tipo rotazione (`"ciclica"`, `"difensiva"`, `"growth"`, `"none"`)

**Definizione:** Dove il rischio si rialloca all'interno del regime.  
**Regola:** La rotazione NON implica né accumulazione né distribuzione.

### ⚪ LIVELLO 5: Qualificatori
**Definizione:** Intensità, persistenza, confidence (da implementare)

### Derivato: Stato di Transizione
**Variabile:** `md_transition`  
**Tipo:** Boolean

**Definizione:** Derivato logicamente. `TRUE` se LIVELLO 3 ≠ NONE e incoerente con LIVELLO 1.

---

## 🔄 Ordine di Comunicazione (Vincolante)

**Mai il contrario.** L'ordine è sempre:

1. **Regime strutturale** (prezzo) → `md_phase`
2. **Processo latente** (rischio) → `md_process`
3. **Dinamica interna** (riallocazione) → `sector_rotation`, `md_transition`

---

## 📝 Esempi di Comunicazione

### Esempio 1: Bull sano con distribuzione

**Narrativa:** "Bull market, distribuzione in atto, rotazione verso settori difensivi."

**Output strutturato:**
```json
{
  "md_phase": "BULL",
  "md_process": "DISTRIBUTION",
  "sector_rotation": true,
  "sector_rotation_type": "difensiva",
  "md_transition": true
}
```

**Interpretazione operativa:**
- ✅ Trend ancora positivo
- ⚠️ Rischio sistemico che inizia a uscire
- ⚠️ Capitale che si sposta verso difensivi
- ⚠️ Fase di attenzione massima
- ❌ Non è ancora Bear
- ❌ Non è un contesto aggressivo

---

### Esempio 2: Bull sano con rotazione ciclica

**Narrativa:** "Bull market, nessun processo di distribuzione, rotazione verso settori ciclici."

**Output strutturato:**
```json
{
  "md_phase": "BULL",
  "md_process": "NONE",
  "sector_rotation": true,
  "sector_rotation_type": "ciclica",
  "md_transition": false
}
```

**Interpretazione operativa:**
- ✅ Bull rafforzato
- ✅ Rischio riallocato ma non ridotto
- ✅ Rotazione ciclica = segnale positivo

---

### Esempio 3: Bear con accumulazione nascente

**Narrativa:** "Bear market, accumulazione in corso, nessuna rotazione significativa."

**Output strutturato:**
```json
{
  "md_phase": "BEAR",
  "md_process": "ACCUMULATION",
  "sector_rotation": false,
  "sector_rotation_type": "none",
  "md_transition": true
}
```

**Interpretazione operativa:**
- ⚠️ Possibile preparazione a recovery
- ⚠️ Ma non ancora segnale operativo
- ⚠️ Monitorare evoluzione

---

### Esempio 4: Lateral neutra

**Narrativa:** "Mercato laterale, nessun processo dominante, rotazione episodica."

**Output strutturato:**
```json
{
  "md_phase": "LATERAL",
  "md_process": "NONE",
  "sector_rotation": false,
  "sector_rotation_type": "none",
  "md_transition": false
}
```

**Interpretazione operativa:**
- ⏸️ Attesa
- ⏸️ Nessun bias direzionale
- ⏸️ Nessuna azione direzionale

---

## 🎯 Perché Questa Comunicazione è Superiore

### 1. Evita Ambiguità

**Non dici mai:**
- ❌ "mercato debole"
- ❌ "mercato confuso"
- ❌ "fase di transizione"

**Dici sempre:**
- ✅ Cosa (regime)
- ✅ Perché (processo)
- ✅ Dove si muove il capitale (dinamica)

### 2. È Spiegabile a Livelli Diversi

- **Comitato investimenti** → Capisce subito il quadro completo
- **Decision Layer** → Sa cosa fare o non fare
- **Report clienti** → Riceve una narrativa coerente

### 3. È Coerente con la Gerarchia

- ✅ Nulla viene sovrascritto
- ✅ Tutto viene qualificato
- ✅ Ogni informazione ha il suo posto

---

## 🔒 Regola di Comunicazione (Vincolante)

**Il Market Detector comunica sempre per strati:**

1. **Prima** il regime (md_phase)
2. **Poi** il processo (md_process)
3. **Infine** la dinamica interna (sector_rotation, md_transition)

**Mai una sintesi unica.**

---

## 💻 Implementazione Tecnica

### Struttura Output Standardizzato

```pine
// Output multilivello per Decision Layer
md_phase          // Regime strutturale (BULL/BEAR/LATERAL)
md_process        // Processo latente (DISTRIBUTION/ACCUMULATION/NONE)
sector_rotation   // Rotazione settoriale (true/false)
sector_rotation_type  // Tipo rotazione (ciclica/difensiva/none)
md_transition     // Transizione in atto (true/false)
```

### Priorità e Sovrascrittura

- **md_phase:** Determinata dalla gerarchia delle fasi (vedi `GERARCHIA_FASI_BULL_BEAR_LATERALITA.md`)
- **md_process:** Determinata dalle fasi di processo (Distribuzione, Accumulazione)
- **sector_rotation:** Calcolata separatamente, non sovrascrive md_phase
- **md_transition:** Flag booleano, non sovrascrive md_phase

**Importante:** md_phase e md_process possono coesistere. Non si escludono a vicenda.

---

## 📋 Esempi di Combinazioni Valide

| md_phase | md_process | sector_rotation | md_transition | Significato |
|----------|------------|-----------------|---------------|-------------|
| BULL | NONE | false | false | Bull sano, nessun processo |
| BULL | DISTRIBUTION | true | true | Bull con distribuzione, rotazione difensiva |
| BEAR | ACCUMULATION | false | true | Bear con accumulazione nascente |
| LATERAL | NONE | false | false | Lateral neutra |
| BULL | NONE | true | false | Bull con rotazione ciclica |

---

## ⚠️ Note Importanti

### Per Sviluppatori

1. **Sempre comunicare tutti i livelli** - Non omettere variabili
2. **Rispettare l'ordine** - Regime → Processo → Dinamica
3. **Coerenza:** md_phase e md_process devono essere coerenti (es. DISTRIBUTION solo in BULL)
4. **Validazione:** Verificare che le combinazioni siano logiche

### Per Decision Layer

1. **Leggere sempre tutti i livelli** - Non basarsi solo su md_phase
2. **Interpretare il contesto completo** - Regime + Processo + Dinamica
3. **Rispettare la gerarchia** - md_phase ha priorità su tutto
4. **Usare md_transition** per identificare cambiamenti imminenti

---

## 📝 Changelog

### Versione 1.0 (2026-02-09) - Ufficiale

- ✅ Formalizzata comunicazione multilivello gerarchica
- ✅ Definita struttura messaggio vincolante
- ✅ Documentati esempi operativi
- ✅ Chiariti vantaggi comunicazione multilivello
- ✅ Definita regola di comunicazione vincolante
- ✅ Documentata implementazione tecnica

---

## 🔗 Riferimenti

- `GERARCHIA_FASI_BULL_BEAR_LATERALITA.md` - Gerarchia fasi
- `FASE_BULL_BEAR.md` - Documentazione fase Bull/Bear
- `FASE_LATERAL_v2.1_FROZEN.md` - Documentazione fase LATERAL
- `market_detector.pine` - Implementazione codice

---

**Q-Mentor Framework | Market Detector | Comunicazione Multilivello v1.0 - UFFICIALE**
