# Codice Fase Bull e Bear - Versione Congelata

**Versione:** 1.0 - Congelata  
**Data:** 2026-02-09  
**Status:** PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE

---

## 📁 File del Codice

### 1. Pine Script - Fase Baseline

**File:** `phases/phase_0_baseline.pine`

```pine
//@version=6
// FASE 0 — BASELINE (Bull/Bear Market)
// Sempre presente, sempre calcolato, sempre attivo in background
// Priorità: 1 (più bassa)
// Logica ufficiale Q-Mentor: SMA150 come discriminante principale
// VERSIONE CONGELATA - NON MODIFICARE SENZA APPROVAZIONE

baselinePhase() =>
    // EMA30 (shock/crash/recovery)
    ema30 = ta.ema(close, 30)
    
    // SMA150 (regime primario) - DISCRIMINANTE PRINCIPALE
    sma150 = ta.sma(close, 150)
    
    // Calcolo posizioni relative (percentuali)
    spy_vs_ema30 = na(ema30) ? na : (close - ema30) / ema30
    spy_vs_sma150 = na(sma150) ? na : (close - sma150) / sma150
    
    // Returns per fallback
    returns = ta.change(close) / close[1]
    
    // Classificazione basata su priorità:
    // 1. SMA150 (discriminante principale)
    // 2. EMA30 (proxy durante warm-up period)
    // 3. Returns (fallback)
    // 4. Default: BULL (conservativo)
    
    isBull = false
    isBear = false
    
    if not na(spy_vs_sma150)
        // Classificazione principale basata su SMA150
        if spy_vs_sma150 > 0
            isBull := true
        else if spy_vs_sma150 < 0
            isBear := true
    else if not na(spy_vs_ema30)
        // Proxy: usa EMA30 durante warm-up period (< 150 barre)
        if spy_vs_ema30 > 0
            isBull := true
        else
            isBear := true
    else if not na(returns)
        // Fallback: usa returns
        if returns > 0
            isBull := true
        else
            isBear := true
    else
        // Default conservativo: BULL
        isBull := true
    
    // Colori: Verde per Bull, Rosso per Bear
    phaseColor = isBull ? color.new(color.green, 80) : isBear ? color.new(color.red, 80) : color.new(color.gray, 90)
    
    [isBull, isBear, phaseColor]
```

---

### 2. Pine Script - File Master

**File:** `market_detector.pine`

La funzione `baselinePhase()` è integrata nel file master alle righe 14-62.

**Riferimento:** Vedi `market_detector.pine` righe 8-62 per implementazione completa.

---

### 3. HTML/JavaScript - Visualizzazione Grafica

**File:** `market_detector_charts.html`

#### Funzione di Classificazione

```javascript
// Funzione per classificare Bull/Bear
// IMPORTANTE: Restituisce sempre BULL o BEAR, mai NEUTRAL
// VERSIONE CONGELATA
function classificaBullBear(row, spy_vs_sma150, spy_vs_ema30, returns) {
    if (spy_vs_sma150 !== null && spy_vs_sma150 !== undefined) {
        if (spy_vs_sma150 > 0) return 'BULL';
        if (spy_vs_sma150 < 0) return 'BEAR';
        return 'BULL'; // Forza BULL invece di NEUTRAL
    } else if (spy_vs_ema30 !== null && spy_vs_ema30 !== undefined) {
        return spy_vs_ema30 > 0 ? 'BULL' : 'BEAR';
    } else if (returns !== null && returns !== undefined) {
        return returns > 0 ? 'BULL' : 'BEAR';
    }
    return 'BULL'; // Default sempre BULL
}
```

#### Colori Zone (Congelati)

```javascript
// Zone BULL (verde)
fillcolor: 'rgba(46, 125, 50, 0.45)'  // Material Design Green 700

// Zone BEAR (rosso)
fillcolor: 'rgba(198, 40, 40, 0.45)'  // Material Design Red 700
```

**Riferimento:** Vedi `market_detector_charts.html` righe 247-261 e 580-612.

---

## 🔒 Regole di Congelamento

### Cosa è Congelato

✅ **Logica di classificazione:**
- Discriminante principale: SMA150
- Regole BULL/BEAR basate su `spy_vs_sma150`
- Sistema di fallback per warm-up period

✅ **Colori visualizzazione:**
- Verde BULL: RGB(46, 125, 50) con opacità 0.45
- Rosso BEAR: RGB(198, 40, 40) con opacità 0.45

✅ **Struttura zone:**
- Zone continue senza gap
- Sovrapposizione per evitare spazi bianchi
- Background sempre colorato

### Modifiche Consentite

⚠️ **Solo con approvazione:**
- Modifiche alla logica di classificazione
- Cambiamenti ai colori
- Modifiche alla struttura delle zone
- Aggiornamenti al sistema di fallback

### Processo di Modifica

1. **Richiesta formale** di modifica
2. **Test di regressione** completi
3. **Validazione** con dati storici
4. **Aggiornamento documentazione**
5. **Approvazione** prima del commit

---

## 📊 Test e Validazione

### Test Obbligatori

- ✅ Classificazione corretta su dati storici
- ✅ Zone continue senza gap bianchi
- ✅ Colori corretti (verde/rosso)
- ✅ Fallback funzionante per warm-up period
- ✅ Coerenza con eventi storici noti

### Validazione Storica

- ✅ 2008-2009: Crisi finanziaria → BEAR
- ✅ 2020: Pandemia → Transizione rapida
- ✅ Periodi rialzisti → BULL
- ✅ Periodi ribassisti → BEAR

---

## 📝 Versione

**Versione:** 1.0  
**Data Congelamento:** 2026-02-09  
**Status:** CONGELATA - PRODUZIONE

---

**Q-Mentor Framework | Market Detector | Codice Fase Bull e Bear v1.0 - CONGELATO**
