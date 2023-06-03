# ada_estatistica_II
Projeto para o módulo de Estatística II

## Predictive Maintenance

Este notebook contém o trabalho final da disciplina de Estatística II para a turma #970 LM Tech Data Talents do curso de Python e Dados da Ada Tech dos alunos:
* Claudia Cavalcante Fonseca 
* Hevans Vinícius Pereira
* Lucas Voltolini
* Renato Massamitsu Zama Inomata
* Vitor Cunha Cavalcanti Manso
* William James Erthal


## BASE DE DADOS

A análise exploratória a seguir pode ser acompanhada pelo [streamlit](https://lm-ada-estatistica-ii-grupo01.streamlit.app/)

Vamos trabalhar com o dataset [Machine Predictive Maintenance](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification?resource=download) para prever falhas em máquinas, este contém dados fictícios sobre manutenção de máquinas em uma indústria.


Em uma pesquisa realizada pela ABRAMAN - Associação Brasileira de Manutenção e Gestão de Ativos, 5% do faturamento bruto da indústria é gasto com manutenção. Dessa forma, percebe-se a relevância em realizar procedimentos e metodologias que garantam o bom funcionamento dos maquinários, uma vez que o resultado financeiro de uma empresa está diretamente relacionado na operação de seus equipamentos.


Esse dataset pode ser usado para a criação de modelos que prevêem que máquinas apresentarão um problema e precisarão de manutenção (classificação binária) e também pode ser usado para a criação de modelos que prevêem o tipo de erro que ocorre (classificação multiclasse).

O dataset possui 10 000 registros e 14 colunas:
* **UID**: Identificador único das máquinas

* **product ID**: A qualidade do produto que a máquina produz, que pode ser baixa(L, 50% dos produtos), média (M, 30% dos produtos) ou alta (H, 20% dos produtos) e um número de série específico para essa variante.

* **Type**: Apenas o tipo do produto, sem o ID.

* **air temperature [K]**: Indica a temperatura do ar e varia de 2K a 300K.

* **process temperature [K]**: A medida da temperatura durante o processo de fabricação ou operação. 

* **rotational speed [rpm]**: A velocidade de rotação da máquina.
* **torque [Nm]**: Uma medida da força de rotação aplicada pela máquina, expressa em Newton metros (Nm). 

* **tool wear [min]**:  O desgaste da ferramenta é uma medida do tempo acumulado de uso da ferramenta durante o processo de fabricação ou operação, expresso em minutos. O desgaste da ferramenta aumenta gradualmente à medida que a máquina é utilizada, sendo influenciado pela variante de qualidade do produto.


Neste trabalho iremos focar na detecção de binária de ocorrência de falha.
