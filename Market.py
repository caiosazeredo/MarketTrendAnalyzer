import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Função para carregar dados de ações
def carregar_dados(caminho_arquivo):
    dados = pd.read_csv(caminho_arquivo, parse_dates=True, index_col='Date')
    return dados

# Função para calcular o RSI
def calcular_rsi(dados, periodo=14):
    delta = dados['Close'].diff()
    ganhos = delta.where(delta > 0, 0)
    perdas = -delta.where(delta < 0, 0)
    
    media_ganhos = ganhos.rolling(window=periodo).mean()
    media_perdas = perdas.rolling(window=periodo).mean()
    
    rs = media_ganhos / media_perdas
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Função para calcular o MACD
def calcular_macd(dados, span1=12, span2=26, signal=9):
    ema_rapida = dados['Close'].ewm(span=span1, adjust=False).mean()
    ema_lenta = dados['Close'].ewm(span=span2, adjust=False).mean()
    macd = ema_rapida - ema_lenta
    sinal = macd.ewm(span=signal, adjust=False).mean()
    
    return macd, sinal

# Função para identificar padrões de candlestick
def identificar_padroes(dados):
    # Implementação simplificada; considere usar uma biblioteca específica para padrões de candlestick
    padroes_identificados = []
    # Adicione lógica para identificar padrões específicos
    return padroes_identificados

# Função para visualizar os dados e indicadores
def visualizar(dados, rsi, macd, sinal):
    fig, axs = plt.subplots(3, 1, figsize=(14, 10), sharex=True)
    
    # Preços de fechamento
    axs[0].plot(dados.index, dados['Close'], label='Close')
    axs[0].set_title('Preço de Fechamento')
    
    # RSI
    axs[1].plot(dados.index, rsi, label='RSI')
    axs[1].axhline(70, linestyle='--', color='red')
    axs[1].axhline(30, linestyle='--', color='green')
    axs[1].set_title('Índice de Força Relativa (RSI)')
    
    # MACD
    axs[2].plot(dados.index, macd, label='MACD', color='blue')
    axs[2].plot(dados.index, sinal, label='Signal Line', color='orange')
    axs[2].bar(dados.index, macd - sinal, color='gray', alpha=0.5)
    axs[2].set_title('MACD')

    for ax in axs:
        ax.legend()
        ax.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    caminho_arquivo = 'caminho_para_seu_arquivo_de_dados.csv'
    dados = carregar_dados(caminho_arquivo)
    rsi = calcular_rsi(dados)
    macd, sinal = calcular_macd(dados)
    visualizar(dados, rsi, macd, sinal)
