# Market Detector - Script di Verifica

Questo documento descrive come utilizzare gli script di verifica per controllare la classificazione Bull/Bear anno per anno.

## Script Disponibili

### 1. `market_detector_verification.pine`

**Script Pine Script per TradingView**

- Mostra la classificazione Bull/Bear in tempo reale
- Visualizza labels all'inizio di ogni anno
- Mostra una tabella con informazioni correnti
- Plot delle medie mobili (EMA30 e SMA150) per riferimento
- Background colorato in base alla fase

**Come usare:**
1. Apri TradingView
2. Carica lo script `market_detector_verification.pine`
3. Applica al grafico SPY (o altro simbolo)
4. Verifica la classificazione anno per anno guardando i labels e il background colorato

**Caratteristiche:**
- Labels mostrano: Anno, Fase, Percentuale SMA150
- Tabella mostra: Anno corrente, Fase, SMA150%, Close, SMA150 value
- Linee verticali tratteggiate indicano il cambio anno

---

### 2. `verify_year_by_year.py`

**Script Python per analisi storica completa**

Genera un grafico completo con:
- Grafico 1: Prezzo SPY con background colorato per fase Bull/Bear
- Grafico 2: Percentuale SPY vs SMA150 (discriminante principale)
- Grafico 3: Riepilogo anno per anno con % giorni in fase BULL

**Prerequisiti:**
```bash
pip install -r requirements_verification.txt
```

**Come usare:**
```bash
python verify_year_by_year.py
```

**Output:**
- Grafico salvato come `market_detector_verification.png`
- Riepilogo CSV salvato come `yearly_summary.csv`
- Output console con dettagli anno per anno

**Esempio output console:**
```
2023:
  Fase Dominante: BULL
  Media SPY vs SMA150: 5.23%
  % Giorni BULL: 78.5%
  Prezzo Inizio: $380.00
  Prezzo Fine: $450.00
  Variazione Anno: +18.42%
```

---

## Interpretazione dei Risultati

### Classificazione Bull/Bear

- **BULL Market:** `spy_vs_sma150 > 0` (SPY > SMA150)
  - Background verde
  - Indica trend rialzista strutturale

- **BEAR Market:** `spy_vs_sma150 < 0` (SPY < SMA150)
  - Background rosso
  - Indica trend ribassista strutturale

- **NEUTRAL:** `spy_vs_sma150 == 0` (SPY esattamente su SMA150)
  - Background grigio
  - Caso raro

### Warm-up Period

Per i primi 150 giorni (quando SMA150 non è disponibile):
- Usa EMA30 come proxy
- Se anche EMA30 non disponibile: usa returns
- Default: BULL (conservativo)

---

## Verifica della Logica

### Cosa controllare:

1. **Coerenza temporale:**
   - Gli anni con trend rialzista dovrebbero essere principalmente BULL
   - Gli anni con trend ribassista dovrebbero essere principalmente BEAR

2. **Transizioni:**
   - Le transizioni Bull→Bear e Bear→Bull dovrebbero essere coerenti con eventi di mercato noti
   - Esempio: 2008 dovrebbe mostrare transizione a BEAR

3. **Percentuale SMA150:**
   - Valori positivi = BULL
   - Valori negativi = BEAR
   - La magnitudine indica la forza del trend

4. **Confronto con eventi storici:**
   - 2008-2009: Crisi finanziaria → BEAR
   - 2020: Pandemia → Transizione rapida
   - 2021-2022: Recovery/Bull → BULL (con possibili interruzioni)

---

## Troubleshooting

### Script Pine Script non mostra labels:
- Verifica di avere abbastanza dati storici (almeno 150 barre)
- Controlla che il simbolo sia corretto (SPY o equivalente)

### Script Python non funziona:
- Verifica di aver installato tutte le dipendenze: `pip install -r requirements_verification.txt`
- Controlla la connessione internet (yfinance scarica dati da internet)
- Verifica di avere Python 3.8+

### Dati non corrispondono:
- Verifica che il simbolo sia lo stesso (SPY)
- Controlla il timeframe (dovrebbe essere giornaliero)
- Verifica che i dati storici siano completi

---

## Note

- Lo script Python scarica dati da Yahoo Finance
- I dati possono avere piccole differenze rispetto a TradingView
- Per analisi più precise, usa dati da fonte ufficiale
- La classificazione è basata sulla logica ufficiale Q-Mentor (SMA150)
