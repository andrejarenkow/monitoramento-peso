import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Monitoramento peso",
    layout="centered")

dados = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSiXIJe-xpjsJCAG8RX38_QFNe9-b0RHmu0KbE7n942AQ7ssD9yyWHjc8vMBUD7pZLkwW_rP3E5nxUU/pub?output=csv')
dados['Qual o peso?'] = pd.to_numeric(dados['Qual o peso?'].str.replace(',','.'))
dados['Carimbo de data/hora'] = pd.to_datetime(dados['Carimbo de data/hora'])



fig = px.line(dados, x='Carimbo de data/hora', y='Qual o peso?', color='Quem é você?', markers=True, title='Monitoramento de peso',
             labels={'Carimbo de data/hora': 'Data e hora', 'Qual o peso?': 'Peso (kg)'},
             template='plotly_dark',
             range_y=[0, 150])

fig.update_layout(legend=dict(orientation='h', y=1.02, x=0.5, xanchor='center'))
# Ajustando as margens para diminuir as bordas
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))

st.plotly_chart(fig, use_container_width=True, theme=None)

col1, col2 = st.columns(2)
col1.metric('Média Lisi', f"{round(dados[dados['Quem é você?']=='Lisi']['Qual o peso?'].mean(),1)}")
col2.metric('Média André', f"{round(dados[dados['Quem é você?']=='André']['Qual o peso?'].mean(),1)}")
