"""EDA HR

Análise de um dataset de Recursos Humanos. Nesta verificação, pude encontrar 
informações valiosas sobre a relação entre a situação dos funcionários com 
aspectos financeiros, dentre outros insights obtidos. 
"""


import pkg_resources
import pandas as pd
from IPython.display import display
import plotly.express as px
import plotly.graph_objects as go
from ydata_profiling import ProfileReport


database = pd.read_excel('Base Funcionarios.xlsx')

profile = ProfileReport(database, title="Análise de Funcionários")
profile.to_file("database_report.html")

profile

database.drop(columns=['Data Nascimento'], inplace=True)

with pd.option_context('display.max_columns', 23):
    display(database, database.head(5), database.tail(5)) # type: ignore

database.shape

database.info()

database.describe()

nulos = database.isnull().sum(), database.isna().sum()
nulos

database.duplicated().sum()

database.Situação.value_counts()

"""Criando categorias de faixas etárias:"""

bins = [1956, 1970, 1985, 2000]
labels = ["Senior", "Adulto", "Jovem"]

# Criando a nova coluna categorizada
database["Categoria_Etaria"] = pd.cut(database["Ano Nascimento"],
                                      bins=bins, labels=labels, include_lowest=True, right=False)

database

database.Categoria_Etaria.value_counts()

"""Criando categoria Salarial:"""

bins = [0, 2000, 5000, 8000, 12000]
labels = ["Baixo (até 2k)", "Médio (2k-5k)", "Alto (5k-8k)", "Muito Alto (8k-12k)"]

# Criando a nova coluna categorizada
database["Categoria_Salarial"] = pd.cut(database["Valor Salário"], bins=bins, labels=labels, include_lowest=True)

database

"""Análise por Raças:"""

pd.crosstab(database['Cargo'], database['Raça']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Raça'], database['Situação']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Raça'], database['Cód C.Custo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Raça'], database['Sexo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Raça'],
            database['Categoria_Salarial']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Raça'],
            database['Causa Afastamento']).style.background_gradient(cmap="coolwarm")

"""Análise por Genero:"""

pd.crosstab(database['Cargo'], database['Sexo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Sexo'], database['Situação']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Sexo'], database['Cód C.Custo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Salarial'],
            database['Sexo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Causa Afastamento'],
            database['Sexo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Sexo'], database['Raça']).style.background_gradient(cmap="coolwarm")

"""Análise de Faixa Salarial:"""

pd.crosstab(database['Cargo'],
            database['Categoria_Salarial']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Salarial'],
            database['Cód C.Custo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Salarial'],
            database['Escala']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Escolaridade'],
            database['Categoria_Salarial']).style.background_gradient(cmap="coolwarm")

"""DIstribuição dos Pagamentos por Situação:"""

database_ativos = database[database['Situação'] == "Trabalhando"]
soma_salario_ativos = database_ativos['Valor Salário'].sum()
print(f"Pagamentos: Funcionários que estão ativos é R$ {soma_salario_ativos:.2f}")

database_inativos = database[database['Situação'] == "Demitido"]
soma_salario_inativos = database_inativos['Valor Salário'].sum()
print(f"Pagamentos: Funcionários que foram demitidos é de R$ {soma_salario_inativos:.2f}")

database_ferias = database[database['Situação'] == "Férias"]
soma_salario_ferias = database_ferias['Valor Salário'].sum()
print(f"Pagamentos: Funcionários que estão de férias é R$ {soma_salario_ferias:.2f}")

soma_pagamentos_ativos = database_ativos['Valor Salário'].sum() +database_ferias['Valor Salário'].sum()

print(f"Soma de Pagamentos: Funcionários que estão Ativos/Férias é R$ {soma_pagamentos_ativos:.2f}")

"""Pagamentos por Tipo de Motivo de Demissão:"""

pd.crosstab(database['Causa Afastamento'],
            database['Categoria_Salarial']).style.background_gradient(cmap="coolwarm")

pd.pivot_table(database, values='Valor Salário',
               index='Causa Afastamento', aggfunc='sum').style.background_gradient(cmap="coolwarm")

pd.pivot_table(database, values='Valor Salário',
               index='Escala', aggfunc='sum').style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Salarial'],
            database['Escala']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Ano Nascimento'],
            database['Categoria_Salarial']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Escala'],
            database['Funcionário']).style.background_gradient(cmap="coolwarm")

"""Análise nas Categorias de Faixa Etária:"""

pd.crosstab(database['Categoria_Etaria'],
            database['Escala']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Etaria'],
            database['Escolaridade']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Etaria'],
            database['Situação']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Etaria'],
            database['Categoria_Salarial']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Causa Afastamento'],
            database['Categoria_Etaria']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Cargo'],
            database['Categoria_Etaria']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Etaria'],
            database['Sexo']).style.background_gradient(cmap="coolwarm")

pd.crosstab(database['Categoria_Etaria'],
            database['Raça']).style.background_gradient(cmap="coolwarm")

# Próxima Etapa: Visualização

import plotly.express as px
fig = px.scatter(
    database.query("Sexo=='Feminino'"),
    x="Valor Salário",
    y="Situação",
    color="Situação",
    size="Valor Salário",          # controla o tamanho dos pontos
    hover_name="Categoria_Salarial",
    log_x=True,
    size_max=100,                  # aumenta o tamanho máximo permitido
    title="Situação dos Funcionários do Sexo Feminino por Salário"

)
fig.show()

import plotly.express as px
fig = px.scatter(
    database.query("Categoria_Etaria=='Senior'"),
    x="Valor Salário",
    y="Situação",
    color="Situação",
    size="Valor Salário",
    hover_name="Categoria_Salarial",
    log_x=True,
    size_max=100,
    title="Situação dos Funcionários da Categoria Senior por Salário"

)
fig.show()

import plotly.express as px
fig = px.scatter(
    database.query("Categoria_Etaria=='Jovem'"),
    x="Valor Salário",
    y="Situação",
    color="Situação",
    size="Valor Salário",
    hover_name="Categoria_Salarial",
    log_x=True,
    size_max=100,
    title="Situação dos Funcionários da Categoria Jovem por Salário"

)
fig.show()

import plotly.express as px
fig = px.scatter(
    database.query("Categoria_Etaria=='Adulto'"),
    x="Valor Salário",
    y="Situação",
    color="Situação",
    size="Valor Salário",
    hover_name="Categoria_Salarial",
    log_x=True,
    size_max=70,
    title="Situação dos Funcionários da Categoria Adulto por Salário"

)
fig.show()

import plotly.express as px

fig = px.scatter(
    database.query("Sexo=='Masculino'"),
    x="Valor Salário",
    y="Situação",
    color="Situação",
    size="Valor Salário",
    hover_name="Categoria_Salarial",
    log_x=True,
    size_max=100,
    title="Situação dos Funcionários do Sexo Feminino por Salário"

)
fig.show()

grafico_funcionarios = database.groupby(['Raça', 'Escala']).size().reset_index(name='count')

grafico = px.bar(grafico_funcionarios, x="Raça", y="count", color="Escala",
                              title="Funcionarios por Escala e Raça",
                              labels={"Escala": "Escala", "count": "Quantidade", "Raça": "Raça"}

                              )

grafico.show()

sexo_escala_rott = database.groupby(['Sexo', 'Escala']).size().reset_index(name='count')

grafico_divisao = px.bar(sexo_escala_rott, x="Sexo", y="count", color="Escala",
                              title="Funcionarios por Escala e Sexo",
                              labels={"Escala": "Escala", "count": "Quantidade", "Sexo": "Sexo"}

                              )

grafico_divisao.show()

sexo_escala_rott = database.groupby(['Sexo', 'Causa Afastamento']).size().reset_index(name='count')

grafico_divisao = px.bar(sexo_escala_rott, x="Sexo", y="count", color="Causa Afastamento",
                              title="Causa de Afastamento por Sexo",
                              labels={"Causa Afastamento": "Causa Afastamento", "count": "Quantidade", "Sexo": "Sexo"}

                              )

grafico_divisao.show()

sexo_escala_rott = database.groupby(['Categoria_Etaria', 'Causa Afastamento']).size().reset_index(name='count')

grafico_divisao = px.scatter(sexo_escala_rott, x="Categoria_Etaria", y="count", color="Causa Afastamento",
                              title="Rotatividade por Causa do Afastamento",
                              labels={"Causa Afastamento": "Causa Afastamento", "count": "Quantidade", "Categoria_Etaria": "Categoria_Etaria"},
                              size="count",
                              size_max=100

                              )

grafico_divisao.show()

raças_idades_rott = database.groupby(['Raça', 'Sexo'], observed=True).size().reset_index(name='count')

grafico_rotatividade = px.bar(raças_idades_rott, x="Raça", y="count", color="Sexo",
                              title="Distribuição por Raça e Sexo",
                              labels={"count": "Quantidade", "Raça": "Raça", "Sexo": "Sexo"}
                              )

grafico_rotatividade.show()

salario_situacao = database.groupby(['Categoria_Etaria', 'Situação']).size().reset_index(name='count')

grafico_rotatividade_salario_causa = px.bar(salario_situacao, x="Categoria_Etaria", y="count", color="Situação",
                                            title="Rotatividade por Categoria Etaria e Situação",
                                            )
grafico_rotatividade_salario_causa.show()

media_salarial_categoria = database.groupby('Categoria_Salarial')['Valor Salário'].mean().reset_index()


fig = px.bar(media_salarial_categoria , x='Categoria_Salarial', y='Valor Salário',
             title='Media Salarial por Categoria')
fig.show()

media_salarial_etaria = database.groupby('Categoria_Etaria', observed=True)['Valor Salário'].sum().reset_index()
fig = px.bar(media_salarial_etaria , x='Categoria_Etaria', y='Valor Salário',
             title='Média Salarial por Categoria Etária')
fig.show()

media_salarial_etaria = database.groupby('Categoria_Etaria', observed=True)['Valor Salário'].mean().reset_index()
fig = px.bar(media_salarial_etaria , x='Categoria_Etaria', y='Valor Salário',
             title='Média Salarial por Categoria Etária: 🚨 Média sendo puxada pelo Senior (8k - 12k)')
fig.show()

import plotly.express as px
fig = px.scatter_matrix(database, dimensions=["Valor Salário", "Ano Nascimento"], color="Categoria_Salarial",
                        title="Categoria Salarial por Ano de Nascimento")
fig.show()

import plotly.express as px
fig = px.scatter_matrix(database, dimensions=["Valor Salário", "Raça"], color="Categoria_Salarial",
                       title="Categoria Salarial por Raça",
                       size="Valor Salário",
                       size_max=50
)
fig.show()

import plotly.express as px
fig = px.scatter_matrix(database, dimensions=["Situação", "Cód C.Custo"], color="Categoria_Salarial",
                       title="Categoria Salarial Centro de Custo e Situação",
                       size="Valor Salário",
                       size_max=80

)
fig.show()

afastamento_idade_raca_counts = database.groupby(['Causa Afastamento', 'Categoria_Etaria', 'Raça'], observed=True).size().reset_index(name='count')
fig = px.bar(afastamento_idade_raca_counts, x="Causa Afastamento", y="count", color="Raça",
             facet_col="Categoria_Etaria", title="Distribuição de Causa de Afastamento por Categoria Etária e Raça")
fig.show()

afastamento_idade_raca_counts = database.groupby(['Cód C.Custo', 'Categoria_Etaria', 'Raça'], observed=True).size().reset_index(name='count')
fig = px.bar(afastamento_idade_raca_counts, x="Cód C.Custo", y="count", color="Raça",
             facet_col="Categoria_Etaria", title="Distribuição de Raças nos Centros de Custo por Faixa Etaria")
fig.show()

afastamento_idade_raca_counts = database.groupby(['Causa Afastamento', 'Categoria_Etaria', 'Sexo'], observed=True).size().reset_index(name='count')
fig = px.bar(afastamento_idade_raca_counts, x="Causa Afastamento", y="count", color="Sexo",
             facet_col="Categoria_Etaria", title="Distribuição de Causa de Afastamento por Categoria Etária e Sexo")
fig.show()

idade_raca_counts = database.groupby(['Cód C.Custo', 'Categoria_Etaria', 'Raça'], observed=True
                                     ).size().reset_index(name='count')
fig = px.scatter(idade_raca_counts, x="Cód C.Custo", y="count",
                 color="Raça",
                 facet_col="Categoria_Etaria",
                 title="Distribuição de Raças nos Centros de Custo por Faixa Etaria",
                 size="count",
                 size_max=100)
fig.show()

database.profile_report = ProfileReport(database, title="Análise de Funcionários")
database.profile_report.to_file("database_report.html")