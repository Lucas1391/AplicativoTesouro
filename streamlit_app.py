#Biblioteca para Carregar dados do yahoo Finance
import yfinance as yf
#Instalando Pandas
import pandas as pd
#Instalando Numpy
import numpy as np
import pandas_ta as ta
import streamlit as st


def Operacoes(dicionario):
        resultado_ifr2 = {}
        for indice in dicionario:
            if (dicionario[indice]['Sinal'] == 'compra') or (dicionario[indice]['Sinal'] == 'venda'):
                resultado_ifr2.update({indice:dicionario[indice]})
        return resultado_ifr2

def IFR2(ativo):
        df=yf.download(ativo,period='5d')
        #Cálculo do IFR
        df['IFR2'] = ta.rsi(df['Close'],2)
        #Calculando máxima dos dois ultimos dias
        df['highest_2'] = df['High'].rolling(2).max()
        highest_2 = df['highest_2'].iloc[3]
        fechamento_atual  = df['Close'].iloc[-1]
        ifr_2 = df['IFR2'].iloc[-1]
        maxima = df['High'].iloc[-1]
        #CALCULANDO CONDIÇÕES DE COMPRA,VENDA OU NEUTRALIDADE
        operacao = 'nenhuma'
        if ifr_2 <  25.00:
                operacao = 'compra'
        elif highest_2 < maxima:
                operacao = 'venda'
        else:
                operacao = operacao
        #ALOCANDO RESULTADO EM UM DICIONÁRIO
        resultado_ifr2 = ({'Preço':fechamento_atual,
                        'Sinal':operacao
                        })
        return resultado_ifr2
ativos = ["WEGE3.SA","MGLU3.SA","AZUL4.SA"]
def IFR2_ATIVOS(ativos):
    #Gerando Dicionário para todos os ativos
    resultado_ifr2 = {}
    for ativo in ativos:
        resultado_ifr2.update({ativo:IFR2(ativo)})
    return resultado_ifr2
#==============================MENSAGEM TELEGRAM=====================================================
st.title("APLICATIVO DE SINAIS")
lista= ["","IFR2","9.1","TUTLE"]
estrategia = st.selectbox("SELECIONE O SETUP DESEJADO!",lista)
if estrategia==lista[1]:
    dicionario = IFR2_ATIVOS(ativos)
    Operacoes = Operacoes(dicionario)
    operacoes = pd.DataFrame()
    operacoes['ativos'] = ativos
    operacoes = pd.DataFrame(operacoes.values())
    st.dataframe(operacoes)                      
    

