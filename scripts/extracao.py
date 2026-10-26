# Importa a biblioteca para manipulação de tabelas e dados
import pandas as pd
# Importa a biblioteca do banco de dados SQLite (gratuito e já embutido no Python)
import sqlite3

# ------------------------------------------------------------------------------
# ETAPA 1: EXTRAÇÃO (E de Extract) - Buscando os dados da nossa fonte
# ------------------------------------------------------------------------------
print("Iniciando a etapa de Extração...")

# Lê o arquivo CSV com os dados dos alunos e guarda na variável 'dados'
dados = pd.read_csv("dados_brutos.csv")

# Exibe na tela os dados do jeito que foram extraídos do arquivo
print("Dados Extraídos:\n", dados, "\n")