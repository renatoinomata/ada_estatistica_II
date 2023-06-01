import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn-v0_8-whitegrid')
# plt.style.use('default')

st.title('Análise dos dados')
st.header('LM Tech Data Talents: Módulo 05 - Estatística II')

# Importando dados
df = pd.read_csv('./dataset/predictive_maintenance.csv')
colunas = df.columns

# Dataset com apenas as falhas
df_failures = df[df.loc[:, 'Failure Type'] != 'No Failure']

# Páginas do dashboard
paginas = ['00 - Introdução',
           '01 - Conjunto de dados', 
           '02 - Contagem de dados', 
           '03 - Distribuições', 
           '04 - Correlações',
           '05 - Scatterplots',]

# Sidebar para escolher a página
with st.sidebar:
    pg_escolhida = st.selectbox('Página', paginas)

st.header(pg_escolhida)

if pg_escolhida == paginas[0]:
    st.markdown('''
## Grupo 01: 
* Claudia Cavalcante Fonseca; 
* Hevans Vinícius Pereira;
* Lucas Voltolini;
* Renato Massamitsu Zama Inomata; 
* Vitor Cunha Cavalcanti Manso;
* William James Erthal.

## O problema

Em uma pesquisa realizada pela 
[ABRAMAN - Associação Brasileira de Manutenção e Gestão de Ativos](https://www.industria40.ind.br/artigo/16472-quais-segmentos-gastam-mais-com-manutencao-de-maquinas-industriais), 
5% do faturamento bruto da indústria é gasto com manutenção. Dessa forma, percebe-se a relevância
em realizar procedimentos e metodologias que garantam o bom funcionamento dos maquinários, uma vez 
que o resultado financeiro de uma empresa está diretamente relacionado na operação de seus equipamentos.

Neste contexto, [a nossa base de dados para este trabalho](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset)
traz informações do funcionamento de máquinas e momentos em que falhas diversas podem ocorrer.
Portanto, o objetivo de nossa análise é determinar um modelo que possa classificar quando as
falhas ocorrem.

Conforme comentado pelos autores do dataset, dados para predição de manutenção em máquinas são
relativamente difíceis de se obter e publicar. O dataset disponibilizado **contém dados sintéticos**
de parâmetros considerados relevantes para problemas reais da indústria.
''')
    

# Conjunto de dados
if pg_escolhida == paginas[1]:
    # Data Frame
    st.subheader('Dataset')

    st.markdown('''
Os atributos do dataset são:

* UID: Identificador único das máquinas
* Product ID: A qualidade do produto que a máquina produz, que pode ser baixa(L, 50% dos produtos), 
média (M, 30% dos produtos) ou alta (H, 20% dos produtos) e um número de série específico para 
essa variante;
* Type: Apenas o tipo do produto, sem o ID;
* Air temperature [K]: Indica a temperatura do ar em K;
* Process temperature [K]: A medida da temperatura durante o processo de fabricação ou operação;
* Rotational speed [rpm]: A velocidade de rotação da máquina;
* Torque [Nm]: Uma medida da força de rotação aplicada pela máquina, expressa em Newton metros (Nm); 
* Tool wear [min]:  O desgaste da ferramenta é uma medida do tempo acumulado de uso da ferramenta 
durante o processo de fabricação ou operação, expresso em minutos. O desgaste da ferramenta aumenta 
gradualmente à medida que a máquina é utilizada, sendo influenciado pela variante de qualidade do 
produto.

    ''')


    st.write(df)

    # Dados de df.info()
    st.subheader('`info()`')
    st.write('Verificando as observações de cada coluna:')

    df_info = pd.DataFrame({'Colunas': df.columns,
                            'Observações não nulas': [len(df) for x in df.columns],
                            'Nulos': [df[x].isnull().sum() for x in df.columns],
                            'Dtype': [np.dtype(df[x]) for x in df.columns]})
    st.write(df_info)

    # Dados de df.describe()
    st.subheader('`describe()`')
    st.write('Principais métricas dos dados:')
    st.write(df.describe())

# Contagem com value_counts()
if pg_escolhida == paginas[2]:
    
    st.markdown('''
Vamos realizar uma contagem dos dados conforme suas categorias:
tipo da máquina, falha, e tipo de falha.
    ''')

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
if pg_escolhida == paginas[3]:

    st.markdown('''
É sempre importante verificar como os dados se distribuem para cada variável, dessa forma
podemos entender como elas se comportam e se existem outliers no dataset. 
Nos gráficos abaixo, foram gerados histogramas e boxplots, por variável, 
e separados por tipo de máquina e falhas ou tipos de falhas detectadas.
    ''')
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
if pg_escolhida == paginas[4]:

    st.markdown('''
Correlacionar as variáveis pode nos ajudar a entender melhor o comportamento das máquinas.
Abaixo está a matriz de correlação e também um pairplot dos dados. 
    ''')

    st.subheader('Matriz de correlações')
    df_numeric = df.select_dtypes(include = np.number).drop(columns = 'UDI')
    matriz_corr = df_numeric.corr()
    # st.write(matriz_corr)
    sns.heatmap(matriz_corr, annot = True, cmap = 'coolwarm')
    st.pyplot(plt.gcf())

    st.subheader('Pairplot')
    sns.pairplot(df.drop(columns = ['Failure Type', 'UDI']), hue = 'Target')
    st.pyplot(plt.gcf())

    st.markdown('''
Pela matriz de correlação percebe-se que a temperatura do ar e a temperatura do processo
são diretamente proporcionais, enquanto que o torque da máquina e sua velocidade de rotação
são inversamente proporcionais.

Fisicamente, este comportamento é explicado pela fórmula da potência, uma vez que
a potência é dada pelo produto entre torque e rotação.
    ''')

if pg_escolhida == paginas[5]:

    st.markdown('''
Na página anterior vimos um pairplot com relação a presença ou não de falhas na máquina.
É interessante também olharmos puramente para as falhas e a classificação de seus tipos,
verificando como se distribuem em um scatterplot de duas variáveis.
    ''')
    st.subheader('Scatterplots selecionando uma variável')
    colunas_numericas = ['Air temperature [K]', 'Process temperature [K]',
                                 'Rotational speed [rpm]', 'Torque [Nm]',
                                 'Tool wear [min]',]    
    col_escolhida = st.selectbox('Histogramas e boxplots da variável', colunas_numericas)
                
    with st.container():
        fig = plt.figure(constrained_layout = True, figsize=(16,9))
        gs = fig.add_gridspec(2, 2)

        grids = [gs[0, 0], gs[0, 1], gs[1, 0], gs[1, 1]]

        colunas_restantes = colunas_numericas.copy()
        colunas_restantes.remove(col_escolhida)
        
        for coluna, grid in zip(colunas_restantes, grids):
            ax = fig.add_subplot(grid)
            sns.scatterplot(df_failures, y = col_escolhida, x = coluna, hue = 'Failure Type')
            ax.set_title(f'Scatterplot `{coluna}` x `{col_escolhida}`')

        st.pyplot(fig)