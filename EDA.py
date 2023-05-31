import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# plt.style.use('seaborn-v0_8-whitegrid')
plt.style.use('default')
# asdf
st.title('Análise dos dados:')

# Importando dados
df = pd.read_csv('./dataset/predictive_maintenance.csv')
colunas = df.columns

st.write('Conjunto de dados:')
# Explicar variáveis?

# Data Frame
st.write(df)

# Dados de df.info()
st.write('Verificando as observações de cada coluna `df.info()`:')

df_info = pd.DataFrame({'Colunas': df.columns,
                        'Observações não nulas': [len(df) for x in df.columns],
                        'Nulos': [df[x].isnull().sum() for x in df.columns],
                        'Dtype': [np.dtype(df[x]) for x in df.columns]})
st.write(df_info)

# Dados de df.describe()
st.write('Principais métricas dos dados:')
st.write(df.describe())

# Contagem com value_counts()
st.write(df.value_counts('Type'))
st.write(df.value_counts('Failure Type'))

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
with st.container():
    
    fig = plt.figure(constrained_layout = True, figsize=(16,9))
    gs = fig.add_gridspec(1, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    sns.histplot(df, x = col_escolhida, bins = 'auto', hue = 'Type')
    ax1.set_title(f'Histograma da variável `{col_escolhida}` por tipo de máquina')

    ax2 = fig.add_subplot(gs[0, 1])
    sns.boxplot(df, y = 'Type', x = col_escolhida, orient = 'h')
    ax2.set_title(f'Boxplot da variável `{col_escolhida}` por tipo de máquina')

    st.pyplot(fig)

# Construção dos histogramas e boxplots por variáveis
df_failures = df[df.loc[:, 'Failure Type'] != 'No Failure']
with st.container():

    fig = plt.figure(constrained_layout = True, figsize=(16,9))
    gs = fig.add_gridspec(2, 2)

    ax1 = fig.add_subplot(gs[0, 0])
    sns.histplot(df, x = col_escolhida, bins = 'auto', hue = 'Target')
    ax1.set_title(f'Histograma da variável `{col_escolhida}` por ocorrência de falha')


    ax2 = fig.add_subplot(gs[0, 1])
    sns.histplot(df_failures, x = col_escolhida, hue = 'Failure Type')
    ax2.set_title(f'Histograma da variável `{col_escolhida}` por tipo de falha')

    ax3 = fig.add_subplot(gs[1, 0])
    sns.boxplot(df, y = 'Target', x = col_escolhida, orient = 'h')
    ax3.set_title(f'Boxplot da variável `{col_escolhida}` por ocorrência de falha')

    ax4 = fig.add_subplot(gs[1, 1])
    sns.boxplot(df_failures, y = 'Failure Type', x = col_escolhida, orient = "h")
    ax4.set_title(f'Boxplot da variável `{col_escolhida}` por tipo de falha')

    st.pyplot(fig)
