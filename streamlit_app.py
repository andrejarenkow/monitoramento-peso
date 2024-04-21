import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="MOnitoramento peso",
    layout="centered")

dados = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSiXIJe-xpjsJCAG8RX38_QFNe9-b0RHmu0KbE7n942AQ7ssD9yyWHjc8vMBUD7pZLkwW_rP3E5nxUU/pub?output=csv')
dados['Qual o peso?'] = pd.to_numeric(dados['Qual o peso?'].str.replace(',','.'))
dados['Carimbo de data/hora'] = pd.to_datetime(dados['Carimbo de data/hora'])

col1, col2 = st.columns(2)
col1.metric('Peso médio Lisi', round(dados[dados['Quem é você?']=='Lisi']['Qual o peso?'].mean(),1))
col2.metric('Peso médio André', round(dados[dados['Quem é você?']=='André']['Qual o peso?'].mean(),1))

fig = px.line(dados, x='Carimbo de data/hora', y='Qual o peso?', color='Quem é você?', markers=True, title='Monitoramento de peso',
             labels={'x': 'Eixo X Personalizado', 'y': 'Eixo Y Personalizado'})
st.plotly_chart(fig, use_container_width=True)

