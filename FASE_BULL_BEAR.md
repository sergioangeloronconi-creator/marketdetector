# FASE BULL E BEAR - Documentazione Ufficiale Congelata

**Versione:** 1.0 - Congelata  
**Data:** 2026-02-09  
**Status:** PRODUZIONE - NON MODIFICARE SENZA APPROVAZIONE  
**Q-Mentor Framework - Market Detector**

---

## 📋 Definizione

La **Fase Bull e Bear** è la **FASE 0 - BASELINE** del Market Detector. È sempre presente, sempre calcolata e sempre attiva in background.

### Caratteristiche

- **Stato:** Iniziale del sistema
- **Calcolo:** Sempre calcolato
- **Attività:** Sempre attivo in background
- **Priorità:** 1 (più bassa - layer di base)
- **Colori:**
  - **BULL Market** → Verde RGB(46, 125, 50) con opacità 0.45
  - **BEAR Market** → Rosso RGB(198, 40, 40) con opacità 0.45

**IMPORTANTE - SOVRASCRITTURA DA LATERAL:**
- Quando la fase LATERAL (Priorità 2) è attiva, **sovrascrive Bull/Bear a livello di sistema**
- La fase comunicata al Decision Layer sarà **"LATERAL"**, NON "BULL" o "BEAR"
- Bull/Bear rimangono attivi in background ma non vengono comunicati al Decision Layer
- Questo è un comportamento architetturale, non solo visivo

---

## 🔧 Logica Ufficiale Q-Mentor

### Discriminante Principale

**SMA150** (Simple Moving Average a 150 periodi) è il discriminante principale per determinare il regime di mercato.

### Regole di Classificazione

| Condizione | Fase | Descrizione |
|------------|------|-------------|
| `spy_vs_sma150 > 0` | **BULL** | SPY > SMA150 - Regime rialzista strutturale |
| `spy_vs_sma150 < 0` | **BEAR** | SPY < SMA150 - Regime ribassista strutturale |
| `spy_vs_sma150 == 0` | **BULL** | SPY esattamente su SMA150 - Default conservativo BULL |

### Variabili Calcolate

```javascript
// EMA30 (shock/crash/recovery)
ema30 = EMA(close, 30)

// SMA150 (regime primario) - DISCRIMINANTE PRINCIPALE
sma150 = SMA(close, 150)

// Posizioni relative (percentuali)
spy_vs_ema30 = (Close - EMA30) / EMA30
spy_vs_sma150 = (Close - SMA150) / SMA150  // VARIABILE CHIAVE
ema30_vs_sma150 = (EMA30 - SMA150) / SMA150
```

### Gerarchia di Fallback (Warm-up Period)

Quando SMA150 non è disponibile (primi 150 giorni):

1. **SMA150 disponibile:** Usa `spy_vs_sma150` (classificazione principale)
2. **SMA150 non disponibile (< 150 barre):** Usa `spy_vs_ema30` come proxy
3. **EMA30 non disponibile:** Usa `returns` (percentuale di cambio)
4. **Default:** BULL (conservativo)

---

## 💻 Implementazione Codice

### Funzione di Classificazione

```javascript
function classificaBullBear(row, spy_vs_sma150, spy_vs_ema30, returns) {
    // IMPORTANTE: Restituisce sempre BULL o BEAR, mai NEUTRAL
    
    if (spy_vs_sma150 !== null && spy_vs_sma150 !== undefined) {
        if (spy_vs_sma150 > 0) return 'BULL';
        if (spy_vs_sma150 < 0) return 'BEAR';
        // Se esattamente 0, default conservativo BULL
        return 'BULL';
    } else if (spy_vs_ema30 !== null && spy_vs_ema30 !== undefined) {
        return spy_vs_ema30 > 0 ? 'BULL' : 'BEAR';
    } else if (returns !== null && returns !== undefined) {
        return returns > 0 ? 'BULL' : 'BEAR';
    }
    return 'BULL'; // Default sempre BULL
}
```

### Visualizzazione Grafica

#### Colori Zone

- **BULL Zone:**
  - RGB: `(46, 125, 50)`
  - Opacità: `0.45`
  - Material Design Green 700

- **BEAR Zone:**
  - RGB: `(198, 40, 40)`
  - Opacità: `0.45`
  - Material Design Red 700

#### Regole Visualizzazione

- Zone continue senza gap: ogni punto dati ha un colore
- Zone si sovrappongono leggermente per evitare spazi bianchi
- Background sempre colorato: verde (BULL) o rosso (BEAR)
- Nessuna zona bianca o neutra

---

## 📊 File di Riferimento

### Codice Implementato

1. **Pine Script:**
   - `phases/phase_0_baseline.pine` - Implementazione fase baseline
   - `market_detector.pine` - File master con gestione priorità

2. **HTML/JavaScript:**
   - `market_detector_charts.html` - Visualizzazione grafica interattiva

3. **Python:**
   - `verify_year_by_year.py` - Script di verifica anno per anno

### Documentazione Correlata

- `PHASES.md` - Documentazione generale delle fasi
- `README.md` - Documentazione principale progetto
- `VERIFICATION.md` - Guida agli script di verifica

---

## ✅ Validazione

### Test di Verifica

1. **Coerenza Temporale:**
   - Anni con trend rialzista → principalmente BULL
   - Anni con trend ribassista → principalmente BEAR

2. **Transizioni:**
   - Transizioni Bull→Bear e Bear→Bull coerenti con eventi di mercato noti
   - Esempio: 2008 dovrebbe mostrare transizione a BEAR

3. **Percentuale SMA150:**
   - Valori positivi = BULL
   - Valori negativi = BEAR
   - Magnitudine indica forza del trend

4. **Confronto Eventi Storici:**
   - 2008-2009: Crisi finanziaria → BEAR
   - 2020: Pandemia → Transizione rapida
   - 2021-2022: Recovery/Bull → BULL (con possibili interruzioni)

---

## 🔒 Note Finali

### Versione Congelata

Questa documentazione rappresenta la **versione ufficiale congelata** della Fase Bull e Bear.

**IMPORTANTE:**
- ✅ Logica validata e testata
- ✅ Codice implementato e funzionante
- ✅ Visualizzazione grafica completa
- ✅ Documentazione completa

**NON MODIFICARE SENZA:**
- Approvazione formale
- Test di regressione completi
- Aggiornamento documentazione
- Revisione del codice

---

## 📝 Changelog

### Versione 1.0 (2026-02-09) - CONGELATA

- ✅ Implementazione logica ufficiale Q-Mentor basata su SMA150
- ✅ Sistema di fallback per warm-up period
- ✅ Visualizzazione grafica con zone continue senza gap
- ✅ Colori ottimizzati: verde RGB(46,125,50) e rosso RGB(198,40,40)
- ✅ Opacità 0.45 per buona visibilità
- ✅ Documentazione completa

---

**Q-Mentor Framework | Market Detector | Fase Bull e Bear v1.0 - CONGELATA**
