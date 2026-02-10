"""
MARKET PHASE CLASSIFIER - LATERAL v2.1 (STATEFUL · MD-GRADE)
Q-Mentor Framework - Market Detector

VERSIONE: v2.1 (Stateful, MD-Grade)
STATUS: CORREZIONE DEFINITIVA - FROZEN
VERSIONE PRECEDENTE: market_phase_classifier_lateral_v2_hard.py (v2)

OBIETTIVO:
Recuperare precisione persa senza sacrificare stabilità.
Migliorare solo l'uscita dalla LATERAL, mantenendo:
- Conservatività
- Robustezza
- Auditabilità
- Non ottimizzato per trading

MIGLIORAMENTI v2.1:
1. Exit dinamico basato su movimento (obbligatorio)
2. Exit anticipato su violazione core conditions (obbligatorio)
3. exit_reason per audit/debug

PRINCIPI NON NEGOZIABILI:
- LATERAL resta fase primaria
- Definita da prezzo, inefficienza e disordine
- L'uscita può essere più intelligente dell'ingresso
- Nessuna logica dipende dal futuro (no look-ahead)

DIVIETI:
- NO breadth
- NO accumulazione/distribuzione
- NO ottimizzazione parametri per trading
- NO cambiare Bull/Bear
- NO nuove metriche ibride

CODICE ORIGINALE PYTHON - VERSIONE CONGELATA v2.1 FINAL
"""

# [Il codice Python completo è stato fornito nel prompt precedente]
# Questo file serve come riferimento per il codice originale Python
# L'implementazione Pine Script è in phases/phase_1_lateralita.pine
