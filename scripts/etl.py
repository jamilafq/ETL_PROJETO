# ==============================================================================
# PROJETO: Meu Primeiro Pipeline de ETL (Extração, Transformação e Carga)
# Objetivo: Ensinar conceitos de Engenharia de Dados para o Ensino Médio
# ==============================================================================

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

# ------------------------------------------------------------------------------
# ETAPA 2: TRANSFORMAÇÃO (T de Transform) - Limpando e corrigindo os dados
# ------------------------------------------------------------------------------
print("Iniciando a etapa de Transformação...")

# Remove os espaços em branco invisíveis que ficam antes ou depois dos nomes
dados["nome"] = dados["nome"].str.strip()

# Remove o símbolo de '%' da coluna frequência e transforma o texto em número
dados["frequencia"] = dados["frequencia"].str.replace("%", "").astype(int)

# Corrige notas erradas (se a nota for maior que 10, limita o valor máximo para 10)
dados["nota"] = dados["nota"].clip(upper=10.0)

# Cria uma nova coluna para dizer se o aluno foi aprovado (nota >= 6 e frequência >= 75)
dados["status"] = (dados["nota"] >= 6.0) & (dados["frequencia"] >= 75)
# Substitui os valores True/False por palavras mais fáceis de ler: Aprovado ou Reprovado
dados["status"] = dados["status"].map({True: "Aprovado", False: "Reprovado"})

# Exibe na tela como os dados ficaram bonitos e limpos após a transformação
print("Dados Transformados:\n", dados, "\n")

# ------------------------------------------------------------------------------
# ETAPA 3: CARGA (L de Load) - Salvando tudo no banco de dados
# ------------------------------------------------------------------------------
print("Iniciando a etapa de Carga...")

# Conecta ao arquivo do banco SQLite (se o arquivo não existir, ele cria na hora)
conexao = sqlite3.connect("escola.db")

# Salva a tabela final no banco de dados (se já existir uma tabela antiga, ela é substituída)
dados.to_sql("alunos_aprovados", conexao, if_exists="replace", index=False)

# Fecha a conexão com o banco de dados por segurança e boa prática
conexao.close()

# Mensagem final para celebrar o sucesso do pipeline!
print("ETL Finalizado com Sucesso! O arquivo 'escola.db' foi gerado.")
