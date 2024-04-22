import pandas as pd
import plotly.express as px
import streamlit as st

# Configurações da página do Streamlit
st.set_page_config(
    page_title="Monitoramento peso",
    page_icon="🍽️",
    layout="centered")  # Define o título da página e a layout centralizada

# Carrega os dados do CSV online
dados = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSiXIJe-xpjsJCAG8RX38_QFNe9-b0RHmu0KbE7n942AQ7ssD9yyWHjc8vMBUD7pZLkwW_rP3E5nxUU/pub?output=csv')
dados['Qual o peso?'] = pd.to_numeric(dados['Qual o peso?'].str.replace(',','.'))  # Converte para numérico e substitui vírgula por ponto
dados['Carimbo de data/hora'] = pd.to_datetime(dados['Carimbo de data/hora'])  # Converte para formato de data e hora

# Cria o gráfico de linha com Plotly Express
fig = px.line(dados, x='Carimbo de data/hora', y='Qual o peso?', color='Quem é você?', markers=True, 
             labels={'Carimbo de data/hora': 'Data e hora', 'Qual o peso?': 'Peso (kg)'},  # Define os rótulos dos eixos
             template='plotly_dark',  # Escolhe o tema escuro
             range_y=[0, 150])  # Define o intervalo do eixo y

# Ajusta a legenda para ser horizontal e centralizada
fig.update_layout(legend=dict(orientation='h', y=1.1, x=0.5, xanchor='center'))
# Ajusta as margens para diminuir as bordas
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

# Exibe o gráfico no Streamlit, desabilitando todas as interações
st.plotly_chart(fig, use_container_width=True, theme=None, config={})

# Métricas de peso médio
col1, col2 = st.columns(2)
col1.metric('Média Lisi', f"{round(dados[dados['Quem é você?']=='Lisi']['Qual o peso?'].mean(),1)}")
col2.metric('Média André', f"{round(dados[dados['Quem é você?']=='André']['Qual o peso?'].mean(),1)}")
