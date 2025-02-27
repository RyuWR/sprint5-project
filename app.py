import streamlit as st
import pandas as pd
import plotly.express as px

# Ler o arquivo CSV
df = pd.read_csv('vehicles_us.csv')  # Substitua pelo nome do seu arquivo CSV

# Criar cabeçalho do aplicativo
st.header('Dashboard Interativo com Streamlit')

# Criar caixas de seleção para exibir gráficos
show_histogram = st.checkbox('Gerar histograma')
show_scatter = st.checkbox('Gerar gráfico de dispersão')

if show_histogram:
    st.write('Criando um histograma baseado no conjunto de dados')

    # Criar histograma
    # Substitua "odometer" pela coluna desejada
    fig = px.histogram(df, x="odometer")

    # Exibir gráfico interativo
    st.plotly_chart(fig, use_container_width=True)

if show_scatter:
    st.write('Criando um gráfico de dispersão baseado no conjunto de dados')

    # Criar gráfico de dispersão
    # Substitua "odometer" e "price" pelas colunas desejadas
    fig = px.scatter(df, x="odometer", y="price")

    # Exibir gráfico interativo
    st.plotly_chart(fig, use_container_width=True)
