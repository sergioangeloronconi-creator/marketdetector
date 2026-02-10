# Gerarchia Fasi Bull/Bear - Lateralità

**Versione:** 1.0 - Congelata  
**Data Congelamento:** 2026-02-09  
**Status:** FROZEN - PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE  
**Q-Mentor Framework - Market Detector**

**🔒 DOCUMENTO CONGELATO**

Questo documento descrive la gerarchia tra le fasi attualmente congelate:
- Fase Bull/Bear (Priorità 1)
- Fase Lateralità (Priorità 2)

Il documento verrà esteso man mano che altre fasi verranno congelate.

---

## 📊 Gerarchia di Priorità (Vincolante)

**Fasi Attualmente Congelate:**

| Priorità | Fase | Nome | Colore | Status |
|----------|------|------|--------|--------|
| 1 | Fase 0 | **Bull / Bear** (Baseline) | Verde/Rosso | ✅ CONGELATA |
| 2 | Fase 1 | **Lateralità** (LATERAL) | Grigio | ✅ CONGELATA |

**Regola fondamentale:** In caso di conflitto, **vince sempre la fase con priorità più alta**.

**Nota:** Questo documento verrà aggiornato man mano che le fasi successive verranno congelate.

---

## 🔄 Comportamento di Sovrascrittura

### Principio Architetturale

Il Market Detector è costruito per **layer successivi**, non per classificazione piatta.

- Le fasi **non sono mutualmente esclusive**
- Le fasi **si stratificano**
- Le fasi **sovrascrivono** visivamente e logicamente quelle precedenti

### Due Livelli di Sovrascrittura

#### 1. Sovrascrittura Visiva

- Il **colore di background** viene determinato dalla fase con priorità più alta
- Le fasi con priorità più bassa rimangono "sotto" visivamente

**Esempio:**
- Se LATERAL (Priorità 2) è attiva → Background grigio
- Bull/Bear (Priorità 1) rimangono attivi in background ma non visibili

#### 2. Sovrascrittura a Livello di Sistema

- La **fase comunicata al Decision Layer** è quella con priorità più alta
- Le fasi con priorità più bassa **non vengono comunicate** al Decision Layer

**Esempio:**
- Se LATERAL (Priorità 2) è attiva → Decision Layer riceve `md_phase = "LATERAL"`
- Bull/Bear (Priorità 1) sono attivi ma **NON** vengono comunicati

---

## 🎯 Regole di Priorità per Decision Layer

### Comportamento Sistema

```pine
// Logica di determinazione fase per Decision Layer
// (Solo fasi congelate al momento)
if not na(lateralColor)
    md_phase := "LATERAL"           // Priorità 2 ← SOVRASCRIVE Bull/Bear
else
    md_phase := isBull ? "BULL" : "BEAR"  // Priorità 1
```

**Nota:** Quando altre fasi verranno congelate, questa logica verrà estesa con le priorità corrispondenti.

### Esempi Pratici

#### Esempio 1: LATERAL attiva su Bull Market

**Situazione:**
- Bull Market attivo (SPY > SMA150)
- LATERAL attiva (condizioni soddisfatte)

**Risultato:**
- ✅ Background: **Grigio** (LATERAL)
- ✅ Decision Layer riceve: `md_phase = "LATERAL"`
- ⚠️ Bull Market: Attivo in background ma **NON comunicato**

**Motivazione:** LATERAL funge da gate di contesto che impedisce decisioni direzionali.

---


#### Esempio 3: Solo Bull Market attivo

**Situazione:**
- Bull Market attivo (SPY > SMA150)
- Nessuna altra fase attiva

**Risultato:**
- ✅ Background: **Verde** (Bull)
- ✅ Decision Layer riceve: `md_phase = "BULL"`
- ✅ Nessuna sovrascrittura

---

## 🔒 Fasi Congelate

### Fase Bull/Bear (Priorità 1)

- **Versione:** 1.0 - Congelata
- **Documentazione:** `FASE_BULL_BEAR.md`
- **Codice:** `phases/phase_0_baseline.pine`
- **Comportamento:** Sempre attiva in background, comunicata solo se nessuna altra fase attiva

### Fase LATERAL (Priorità 2)

- **Versione:** v2.1 FINAL - FROZEN
- **Documentazione:** `FASE_LATERAL_v2.1_FROZEN.md`
- **Codice:** `phases/phase_1_lateralita.pine`
- **Comportamento:** Sovrascrive Bull/Bear quando attiva (sia visivo che sistema)

---

## 📋 Regole di Comunicazione al Decision Layer

### Regola 1: Una Sola Fase

Il Decision Layer riceve **una sola fase** per barra:
- La fase con **priorità più alta** tra quelle attive
- Le altre fasi, anche se attive, **non vengono comunicate**

### Regola 2: Priorità Assoluta

La priorità è **assoluta** e **non negoziabile**:
- Non ci sono "fasi multiple" comunicate
- Non ci sono "fasi parziali"
- La gerarchia è **deterministica**

### Regola 3: Background vs Sistema

- **Background:** Può mostrare solo la fase con priorità più alta
- **Sistema:** Comunica solo la fase con priorità più alta
- **Coerenza:** Background e sistema sono sempre allineati

---

## 🎨 Visualizzazione

### Colori per Priorità (Fasi Congelate)

| Priorità | Fase | Colore RGB | Opacità |
|----------|------|------------|---------|
| 1 | Bull/Bear | Verde: (46,125,50) / Rosso: (198,40,40) | 0.45 |
| 2 | LATERAL | Grigio | 0.60 |

**Nota:** Colori per fasi future verranno aggiunti quando congelate.

### Comportamento Background

- Solo **un colore** per barra (quello della fase con priorità più alta)
- Nessuna ambiguità cromatica
- Colori sovrapposti non visibili (sostituiti, non mescolati)

---

## ⚠️ Note Importanti

### Per Sviluppatori

1. **Non modificare la gerarchia** senza approvazione formale
2. **Rispettare la priorità** in tutte le implementazioni
3. **Coerenza:** Background e sistema devono essere allineati
4. **Test:** Verificare sovrascrittura in tutti i casi d'uso

### Per Decision Layer

1. **Riceve sempre una fase** (non può essere vuota)
2. **La fase ricevuta è quella con priorità più alta**
3. **Non assumere** che fasi con priorità più bassa siano attive
4. **LATERAL sovrascrive Bull/Bear** - questo è intenzionale e documentato

---

## 📝 Changelog

### Versione 1.0 (2026-02-09) - Ufficiale

- ✅ Documentata gerarchia fasi congelate (Bull/Bear, LATERAL)
- ✅ Chiarito comportamento sovrascrittura (visivo e sistema)
- ✅ Documentate regole di comunicazione al Decision Layer
- ✅ Esempi pratici di sovrascrittura
- ✅ Tabella priorità fasi congelate
- ✅ Note per sviluppatori e Decision Layer
- 📝 Documento verrà esteso man mano che altre fasi verranno congelate

---

## 🔗 Riferimenti

- `FASE_BULL_BEAR.md` - Documentazione fase Bull/Bear
- `FASE_LATERAL_v2.1_FROZEN.md` - Documentazione fase LATERAL
- `market_detector.pine` - Implementazione gerarchia
- `PHASES.md` - Documentazione generale fasi

---

**Q-Mentor Framework | Market Detector | Gerarchia Fasi v1.0 - UFFICIALE**
