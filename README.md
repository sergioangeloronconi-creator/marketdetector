# Market Detector (MD) — Phase Stratification Framework

## Contesto Generale

Progetto dedicato esclusivamente al Market Detector del framework Q-Mentor.

**Obiettivo istituzionale:**
- Pochi documenti
- Pochi codici
- Tutti ufficiali
- Nessuna duplicazione
- Nessuna sperimentazione non tracciata

Il progetto serve a congelare la definizione finale delle fasi di mercato e la loro rappresentazione grafica stratificata.

## Obiettivo Strutturale

Costruire un Market Detector a fasi progressive, dove:
- Le fasi **non sono mutualmente esclusive**
- Le fasi **si stratificano**
- Le fasi possono **sovrascrivere visivamente e logicamente** quelle precedenti

**Risultato finale:**
- Un contesto di mercato completamente colorato
- Ogni colore rappresenta una fase dominante o subordinata
- Le fasi più "forti" o "rare" hanno priorità di sovrascrittura

## Principio Architetturale Chiave

Il Market Detector è costruito per **layer successivi**, non per classificazione piatta.

Ogni nuova fase:
- **NON sostituisce** le precedenti
- **Ridefinisce** quando le condizioni sono soddisfatte

**Concetto chiave:** Le fasi avanzate hanno priorità semantica e visiva sulle fasi base.

## Gerarchia Costituzionale (Vincolante)

**📖 Riferimento Ufficiale:** `MANIFESTO_GERARCHIA.md` (FROZEN)

La gerarchia del Market Detector è organizzata in 5 livelli + transizione derivata:

- **🔴 LIVELLO 0:** Eventi Sistemici (CRASH, CAPITULATION) - Autorità assoluta
- **🟠 LIVELLO 1:** Regime Strutturale (BULL, BEAR, LATERAL, RECOVERY) - Mutualmente esclusivi
- **🟡 LIVELLO 2:** Eventi Locali di Stress (LoCE, Capitulation locale)
- **🟢 LIVELLO 3:** Processi di Rischio (ACCUMULATION, DISTRIBUTION) - **NON sono fasi**
- **🔵 LIVELLO 4:** Rotazione Settoriale
- **⚪ LIVELLO 5:** Qualificatori
- **Derivato:** md_transition (Bull+Distribution, Bear+Accumulation)

**Fasi Congelate:**
- ✅ Bull/Bear (LIVELLO 1) - CONGELATA
- ✅ LATERAL (LIVELLO 1) - CONGELATA v2.1 FINAL

**Regola fondamentale:** Nessun livello può sovrascrivere un livello superiore.

**Forma comunicazione:** Regime → Processo → Rotazione → Transition

## Struttura del Progetto

```
Market Detector/
├── README.md (questo file)
├── PHASES.md (documentazione ufficiale delle fasi)
├── market_detector.pine (file master)
└── phases/
    ├── phase_0_baseline.pine
    ├── phase_1_lateralita.pine
    ├── phase_2_crash.pine
    ├── phase_3_capitulation.pine
    ├── phase_4_recovery.pine
    ├── phase_5_accumulazione.pine
    └── phase_6_distribuzione.pine
```

## Note Finali

Questo progetto **NON è sperimentale**. È un repository di verità operative.

Ogni modifica:
- Deve essere motivata
- Deve rispettare la stratificazione
- Non deve rompere la gerarchia
