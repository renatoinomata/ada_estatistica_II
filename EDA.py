import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.button('Botãozinho')

st.title('Análise dos dados:')

# Importando dados
df = pd.read_csv('./dataset/predictive_maintenance.csv')
colunas = df.columns

st.write(df)
st.write('O conjunto de dados tem dimensão', df.shape)

col_escolhida = st.selectbox('Escolha o parâmetro',
                             [
                                #  'UDI',
                                #  'Product ID',
                                #  'Type',
                                 'Air temperature [K]', 
                                 'Process temperature [K]',
                                 'Rotational speed [rpm]', 
                                 'Torque [Nm]',
                                 'Tool wear [min]',
                                #  'Target',
                                # 'Failure Type',
                                 ])
# 
col_hist, col_hist_failures = st.columns(2)

with col_hist:
    fig, ax = plt.subplots()
    # sns.histplot(data = df, x = 'Failure Type')
    sns.histplot(df, x = col_escolhida, bins = 'auto', hue = 'Target')
    st.pyplot(fig)

df_failures = df[df.loc[:, 'Failure Type'] != 'No Failure']
with col_hist_failures:
    fig, ax = plt.subplots()
    sns.histplot(df_failures, x = col_escolhida, hue = 'Failure Type')
    st.pyplot(fig)
    
col_boxplot, col_boxplot_failures = st.columns(2)

with col_boxplot:
    fig, ax = plt.subplots()
    sns.boxplot(df, y = 'Target', x = col_escolhida, orient="h", ax=ax)
    st.pyplot(fig)

with col_boxplot_failures:
    fig, ax = plt.subplots()
    sns.boxplot(df_failures, y = 'Failure Type', x = col_escolhida, orient = "h", ax = ax)

    st.pyplot(fig)
