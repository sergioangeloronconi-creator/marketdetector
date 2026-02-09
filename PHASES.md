# Documentazione Ufficiale delle Fasi - Market Detector

## FASE 0 — BASELINE (SEMPRE PRESENTE)

**Bull / Bear Market**

- **Stato:** Iniziale del sistema
- **Calcolo:** Sempre calcolato
- **Attività:** Sempre attivo in background
- **Colori:**
  - Bull Market → **Verde**
  - Bear Market → **Rosso**
- **Priorità:** 1 (più bassa)
- **Note:** Questa fase è il layer di base.

---

## FASE 1 — LATERALITÀ / RANGE

**Caratteristiche:**
- Può comparire sopra Bull o Bear
- Sovrascrive visivamente il colore sottostante
- **Colore:** **Grigio**
- **Priorità:** 2

**Logica:**
- Mercato non direzionale
- Compressione
- Perdita di trend

**Regole:**
- Priorità superiore a Bull/Bear
- Priorità inferiore a Crash/Capitulation

---

## FASE 2 — CRASH

**Caratteristiche:**
- Evento violento, rapido, direzionale, raro
- **Colore:** **Giallo**
- **Priorità:** 6

**Regole:**
- Sovrascrive Bull, Bear e Lateralità
- **NON persistente** - transitorio

---

## FASE 3 — CAPITULATION

**Caratteristiche:**
- Evento distinto dal crash
- Panico finale, climax, esaurimento vendite
- **Colore:** **Viola**
- **Priorità:** 7 (MASSIMA)

**Regole:**
- Può avvenire solo dopo Crash o Bear prolungato
- Sovrascrive **tutte** le fasi precedenti

---

## FASE 4 — RECOVERY

**Caratteristiche:**
- Fase di uscita dal panico
- Non è Bull Market
- È una fase di transizione fragile
- **Colore:** **Azzurro**
- **Priorità:** 4

**Regole:**
- Recovery può convivere con Bear di fondo
- Recovery non riaccende Bull

---

## FASE 5 — ACCUMULAZIONE

**Caratteristiche:**
- Fase post-recovery
- Costruzione, assorbimento supply
- **Colore:** **Blu**
- **Priorità:** 5

**Regole:**
- Sovrascrive Recovery
- Ancora distinta da Bull Market

---

## FASE 6 — DISTRIBUZIONE

**Caratteristiche:**
- Fase terminale del Bull
- Perdita di efficienza, rotazione
- **Colore:** **Arancione**
- **Priorità:** 3

**Regole:**
- Può avvenire solo in Bull o Accumulation avanzata
- Sovrascrive Bull visivamente

---

## Tabella Riassuntiva Priorità

| Fase | Nome | Colore | Priorità |
|------|------|--------|----------|
| 0 | Baseline (Bull/Bear) | Verde/Rosso | 1 |
| 1 | Lateralità | Grigio | 2 |
| 6 | Distribuzione | Arancione | 3 |
| 4 | Recovery | Azzurro | 4 |
| 5 | Accumulazione | Blu | 5 |
| 2 | Crash | Giallo | 6 |
| 3 | Capitulation | Viola | 7 |
