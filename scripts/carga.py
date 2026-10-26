import pandas as pd  # Adicione isso se for usar o pandas aqui
import sqlite3      # ISSO CORRIGE O ERRO: Avisa o Python para usar o SQLite

print("Iniciando a etapa de Carga...")

# Conecta ao arquivo do banco SQLite
conexao = sqlite3.connect("escola.db")

# Salva a tabela final no banco de dados (certifique-se de que a variável 'dados' existe aqui)
dados.to_sql("alunos_aprovados", conexao, if_exists="replace", index=False)

# Fecha a conexão com o banco de dados
conexao.close 

print("Iniciando a etapa de Carga...")

# Conecta ao arquivo do banco SQLite (se o arquivo não existir, ele cria na hora)
conexao = sqlite3.connect("escola.db")

# Salva a tabela final no banco de dados (se já existir uma tabela antiga, ela é substituída)
dados.to_sql("alunos_aprovados", conexao, if_exists="replace", index=False)

# Fecha a conexão com o banco de dados por segurança e boa prática
conexao.close()

# Mensagem final para celebrar o sucesso do pipeline!
print("ETL Finalizado com Sucesso! O arquivo 'escola.db' foi gerado.")
