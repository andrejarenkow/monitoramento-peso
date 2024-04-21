import pandas as pd
import plotly.express as px
import streamlit as st

dados = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSiXIJe-xpjsJCAG8RX38_QFNe9-b0RHmu0KbE7n942AQ7ssD9yyWHjc8vMBUD7pZLkwW_rP3E5nxUU/pub?output=csv')
dados['Qual o peso?'] = pd.to_numeric(dados['Qual o peso?'].str.replace(',','.'))
dados['Carimbo de data/hora'] = pd.to_datetime(dados['Carimbo de data/hora'])

fig = px.line(dados, x='Carimbo de data/hora', y='Qual o peso?', color='Quem é você?', markers=True, title='Monitoramento de peso')
st.plotly_chart(fig)

st.line_chart(dados, x='Carimbo de data/hora', y='Qual o peso?', color='Quem é você?', title='Monitoramento de peso')
