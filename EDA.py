import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-v0_8-whitegrid')
# plt.style.use('default')
# test
st.title('Análise dos dados')
st.write('Grupo 01: Claudia, Hevans, Voltolini, Renato, Vitor e William')

# Importando dados
df = pd.read_csv('./dataset/predictive_maintenance.csv')
colunas = df.columns

paginas = ['01 - Conjunto de dados', 
           '02 - Contagem de dados', 
           '03 - Distribuições', 
           '04 - Correlações']

df_failures = df[df.loc[:, 'Failure Type'] != 'No Failure']

# Sidebar
with st.sidebar:
    pg_escolhida = st.selectbox('Página', paginas)

st.header(pg_escolhida)
# Conjunto de dados
if pg_escolhida == paginas[0]:
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
if pg_escolhida == paginas[1]:
    
    var1 = st.selectbox('Contagem dos valores da variável:', ['Type', 'Target', 'Failure Type'])
    # st.write('Contagem dos valores da variável:')
    col1, col2 = st.columns([2, 1])
    with col1:
        if var1 == 'Failure Type':
            sns.countplot(df_failures, y = var1)
        else:
            sns.countplot(df, y = var1)
        plt.title('Contagem por categoria da variável')
        plt.xlabel('Contagem')
        st.pyplot(plt.gcf())
    with col2:
        st.write(df.value_counts(var1))

    if st.button('Spoilers'):
        st.write('Como vimos, existe algum tipo de inconsistência nas falhas, vamos descobrir qual o erro:')
        st.write(df.value_counts(['Target', 'Failure Type']))

# Distribuições
if pg_escolhida == paginas[2]:
    col_escolhida = st.selectbox('Histogramas e boxplots da variável',
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
        
        st.subheader('Gráficos por tipo de máquina')

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
 
    with st.container():

        st.subheader('Gráficos por falhas e tipos de falhas')
        
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

# Correlações
if pg_escolhida == paginas[3]:
    st.write('Correlações')
    matriz_corr = df.select_dtypes(include = np.number).drop(columns = 'UDI').corr()
    st.write(matriz_corr)
    if st.button('Spoilers'):
        sns.heatmap(matriz_corr, annot = True, cmap = 'coolwarm')
        st.pyplot(plt.gcf())
 
    