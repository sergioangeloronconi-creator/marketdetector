"""
Market Detector - Verification Script
Genera grafico anno per anno per verificare classificazione Bull/Bear
Q-Mentor Framework
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import yfinance as yf

def calcola_variabili_strutturali(df_spy):
    """
    Calcola variabili strutturali necessarie per classificare BULL/BEAR
    """
    df = df_spy.copy()
    
    # EMA30 (shock/crash/recovery)
    df['ema30'] = df['Close'].ewm(span=30, adjust=False).mean()
    
    # SMA150 (regime primario) - DISCRIMINANTE PRINCIPALE
    df['sma150'] = df['Close'].rolling(150).mean()
    
    # Posizioni relative
    df['spy_vs_ema30'] = (df['Close'] - df['ema30']) / df['ema30']
    df['spy_vs_sma150'] = (df['Close'] - df['sma150']) / df['sma150']  # VARIABILE CHIAVE
    df['ema30_vs_sma150'] = (df['ema30'] - df['sma150']) / df['sma150']
    
    return df

def classifica_bull_bear(row):
    """
    Classifica fase BULL o BEAR basata su posizione SPY rispetto a SMA150
    """
    spy_vs_sma150 = row.get('spy_vs_sma150', 0)
    
    # Se SMA150 non disponibile (warm-up period < 150 giorni)
    if pd.isna(spy_vs_sma150):
        # Usa EMA30 come proxy temporaneo
        spy_vs_ema30 = row.get('spy_vs_ema30', 0)
        if not pd.isna(spy_vs_ema30):
            if spy_vs_ema30 > 0:
                return 'BULL'  # Proxy: sopra EMA30 = tendenza rialzista
            else:
                return 'BEAR'  # Proxy: sotto EMA30 = tendenza ribassista
        else:
            # Se anche EMA30 non disponibile, usa return recente
            returns = row.get('returns', 0)
            if not pd.isna(returns):
                if returns > 0:
                    return 'BULL'
                else:
                    return 'BEAR'
            else:
                return 'BULL'  # Default conservativo
    
    # Classificazione principale basata su SMA150
    if spy_vs_sma150 > 0:
        return 'BULL'
    elif spy_vs_sma150 < 0:
        return 'BEAR'
    else:
        # spy_vs_sma150 == 0 (esattamente su SMA150) - caso raro
        return 'NEUTRAL'

def classifica_serie_completa(df_spy):
    """
    Classifica tutte le barre come BULL o BEAR
    """
    # Calcola variabili strutturali
    df = calcola_variabili_strutturali(df_spy)
    
    # Aggiungi returns per fallback
    df['returns'] = df['Close'].pct_change()
    
    # Classifica ogni barra
    df['market_phase'] = df.apply(classifica_bull_bear, axis=1)
    
    return df

def riepilogo_anno_per_anno(df):
    """
    Crea riepilogo anno per anno della classificazione
    """
    df['Year'] = df.index.year
    df['Month'] = df.index.month
    
    # Raggruppa per anno
    yearly_summary = df.groupby('Year').agg({
        'market_phase': lambda x: x.value_counts().index[0] if len(x.value_counts()) > 0 else 'UNKNOWN',  # Fase dominante
        'spy_vs_sma150': 'mean',  # Media percentuale
        'Close': ['first', 'last'],  # Prezzo inizio e fine anno
        'market_phase': lambda x: (x == 'BULL').sum() / len(x) * 100  # % giorni BULL
    })
    
    yearly_summary.columns = ['Dominant_Phase', 'Avg_SMA150_Pct', 'Start_Price', 'End_Price', 'Bull_Percentage']
    
    return yearly_summary

def genera_grafico_anno_per_anno(df, save_path='market_detector_verification.png'):
    """
    Genera grafico anno per anno
    """
    fig, axes = plt.subplots(3, 1, figsize=(16, 12))
    fig.suptitle('Market Detector - Verifica Anno per Anno\nQ-Mentor Framework', 
                 fontsize=16, fontweight='bold')
    
    # Grafico 1: Prezzo con classificazione Bull/Bear
    ax1 = axes[0]
    df['Year'] = df.index.year
    
    # Colora le aree in base alla fase
    for year in df['Year'].unique():
        year_data = df[df['Year'] == year]
        if len(year_data) > 0:
            dominant_phase = year_data['market_phase'].value_counts().index[0]
            color = 'green' if dominant_phase == 'BULL' else 'red' if dominant_phase == 'BEAR' else 'gray'
            ax1.axvspan(year_data.index[0], year_data.index[-1], 
                       alpha=0.2, color=color, label=dominant_phase if year == df['Year'].unique()[0] else "")
    
    ax1.plot(df.index, df['Close'], label='SPY Close', linewidth=1.5, color='black')
    ax1.plot(df.index, df['sma150'], label='SMA150', linewidth=2, color='blue', alpha=0.7)
    ax1.plot(df.index, df['ema30'], label='EMA30', linewidth=1, color='orange', alpha=0.7)
    ax1.set_ylabel('Prezzo', fontsize=12)
    ax1.set_title('SPY con Classificazione Bull/Bear (Background Colorato)', fontsize=14)
    ax1.legend(loc='best')
    ax1.grid(True, alpha=0.3)
    
    # Grafico 2: Percentuale rispetto a SMA150
    ax2 = axes[1]
    ax2.plot(df.index, df['spy_vs_sma150'] * 100, label='SPY vs SMA150 (%)', linewidth=1.5, color='purple')
    ax2.axhline(y=0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    ax2.fill_between(df.index, 0, df['spy_vs_sma150'] * 100, 
                     where=(df['spy_vs_sma150'] * 100 > 0), 
                     alpha=0.3, color='green', label='BULL Zone')
    ax2.fill_between(df.index, 0, df['spy_vs_sma150'] * 100, 
                     where=(df['spy_vs_sma150'] * 100 < 0), 
                     alpha=0.3, color='red', label='BEAR Zone')
    ax2.set_ylabel('Percentuale (%)', fontsize=12)
    ax2.set_title('SPY vs SMA150 (Discriminante Principale)', fontsize=14)
    ax2.legend(loc='best')
    ax2.grid(True, alpha=0.3)
    
    # Grafico 3: Riepilogo anno per anno
    ax3 = axes[2]
    yearly = riepilogo_anno_per_anno(df)
    
    years = yearly.index
    bull_pct = yearly['Bull_Percentage']
    
    colors = ['green' if p > 50 else 'red' for p in bull_pct]
    bars = ax3.bar(years, bull_pct, color=colors, alpha=0.7, edgecolor='black')
    
    ax3.axhline(y=50, color='black', linestyle='--', linewidth=1, alpha=0.5)
    ax3.set_ylabel('% Giorni BULL', fontsize=12)
    ax3.set_xlabel('Anno', fontsize=12)
    ax3.set_title('Riepilogo Anno per Anno - % Giorni in Fase BULL', fontsize=14)
    ax3.set_xticks(years[::max(1, len(years)//10)])  # Mostra ogni N anni
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Aggiungi valori sulle barre
    for bar, pct in zip(bars, bull_pct):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{pct:.1f}%',
                ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Grafico salvato in: {save_path}")
    plt.show()
    
    return yearly

def main():
    """
    Funzione principale
    """
    print("Market Detector - Verifica Anno per Anno")
    print("=" * 50)
    
    # Scarica dati SPY
    print("Scaricamento dati SPY...")
    spy = yf.download('SPY', start='2000-01-01', end=None, progress=False)
    
    if spy.empty:
        print("Errore: Impossibile scaricare i dati SPY")
        return
    
    print(f"Dati scaricati: {len(spy)} barre dal {spy.index[0].date()} al {spy.index[-1].date()}")
    
    # Classifica
    print("Classificazione Bull/Bear in corso...")
    df_classified = classifica_serie_completa(spy)
    
    # Riepilogo anno per anno
    print("\nRiepilogo Anno per Anno:")
    print("=" * 50)
    yearly = riepilogo_anno_per_anno(df_classified)
    
    for year, row in yearly.iterrows():
        phase = row['Dominant_Phase']
        avg_pct = row['Avg_SMA150_Pct']
        bull_pct = row['Bull_Percentage']
        start_price = row['Start_Price']
        end_price = row['End_Price']
        change_pct = ((end_price - start_price) / start_price) * 100
        
        print(f"\n{year}:")
        print(f"  Fase Dominante: {phase}")
        print(f"  Media SPY vs SMA150: {avg_pct*100:.2f}%")
        print(f"  % Giorni BULL: {bull_pct:.1f}%")
        print(f"  Prezzo Inizio: ${start_price:.2f}")
        print(f"  Prezzo Fine: ${end_price:.2f}")
        print(f"  Variazione Anno: {change_pct:+.2f}%")
    
    # Genera grafico
    print("\nGenerazione grafico...")
    yearly_summary = genera_grafico_anno_per_anno(df_classified)
    
    # Salva riepilogo CSV
    yearly_summary.to_csv('yearly_summary.csv')
    print("\nRiepilogo salvato in: yearly_summary.csv")
    
    print("\nVerifica completata!")

if __name__ == "__main__":
    main()
