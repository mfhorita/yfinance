"""
# Data App - Dashboard Financeiro Interativo e em Tempo Real
"""

import yfinance as yf
import streamlit as st
from datetime import date
from plotly import graph_objs as go

import warnings
warnings.filterwarnings("ignore")

# Define a data de início para coleta  de dados
INICIO = "2015-01-01"

# Define a data de fim para coleta de dados (data de hoje, execução do script)
HOJE = date.today().strftime("%Y-%m-%d")

# Define o título do Dashboard
st.title("Dashboard Financeiro Interativo")

# Define o código das empresas para coleta dos dados de ativos financeiros
# https://finance.yahoo.com/most-active
empresas = ('PBR', 'GOOG', 'UBER', 'PFE')

# Define de qual empresa usaremos os dados por vez
empresa_selecionada = st.selectbox('Selecione a Empresa Para as Previsões de Ativos Financeiros:', empresas)


# Função para extrair e carregar os dados
@st.cache
def carrega_dados(ticker):
    dados = yf.download(ticker, INICIO, HOJE)
    dados.reset_index(inplace=True)
    return dados


# Mensagem de carga dos dados
mensagem = st.text('Carregando os dados...')

# Carrega os dados
dados = carrega_dados(empresa_selecionada)

# Mensagem de encerramento da carga dos dados
mensagem.text('Carregando os dados...Concluído!')

# Sub-título
st.subheader('Visualização dos Dados Brutos')
st.write(dados.tail())


# Função para o plot dos dados brutos
def plot_dados_brutos():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dados['Date'], y=dados['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=dados['Date'], y=dados['Close'], name="stock_close"))
    fig.layout.update(title_text='Preço de Abertura e Fechamento das Ações', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


# Executa a função
plot_dados_brutos()
