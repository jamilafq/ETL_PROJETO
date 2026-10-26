#pip install streamlit


# Importa a biblioteca do Streamlit para criar a página web
import streamlit as st
# Importa o pandas para carregar e manipular as tabelas
import pandas as pd
# Importa o SQLite para abrir o banco de dados que criamos no ETL
import sqlite3

# Configura o título e o ícone que aparecem na aba do navegador
st.set_page_config(page_title="Painel Escolar", page_icon="📊")

# Adiciona um título principal bem bonito na página
st.title("📊 Painel de Desempenho dos Alunos")
# Adiciona uma descrição curta logo abaixo do título
st.markdown("Visualize abaixo os dados limpos e processados pelo nosso pipeline de ETL.")

# Conecta ao banco de dados SQLite onde salvamos as informações
conexao = sqlite3.connect("escola.db")

# Busca todos os dados da tabela 'alunos_aprovados' e transforma em um DataFrame do Pandas
dados = pd.read_sql_query("SELECT * FROM alunos_aprovados", conexao)

# Fecha a conexão com o banco de dados por segurança
conexao.close()

# ------------------------------------------------------------------------------
# ETAPA 1: INDICADORES RÁPIDOS (Cards / Métricas)
# ------------------------------------------------------------------------------
# Cria três colunas lado a lado na página para colocar cartões de informação
col1, col2, col3 = st.columns(3)

with col1:
    # Calcula o total de alunos na tabela e exibe em um card
    st.metric(label="Total de Alunos", value=len(dados))

with col2:
    # Calcula a média de nota de todos os alunos e exibe com uma casa decimal
    st.metric(label="Nota Média", value=f"{dados['nota'].mean():.1f}")

with col3:
    # Conta quantos alunos têm o status "Aprovado" e exibe no card
    st.metric(label="Aprovados", value=len(dados[dados["status"] == "Aprovado"]))

# Adiciona uma linha horizontal para separar as seções do dashboard
st.divider()

# ------------------------------------------------------------------------------
# ETAPA 2: TABELA DE DADOS INTERATIVA
# ------------------------------------------------------------------------------
# Cria um subtítulo para a tabela de dados
st.subheader("📋 Lista Completa de Alunos")
# Exibe a tabela na tela de forma interativa (os alunos podem ordenar clicando nas colunas)
st.dataframe(dados, use_container_width=True)

# ------------------------------------------------------------------------------
# ETAPA 3: GRÁFICO VISUAL
# ------------------------------------------------------------------------------
# Cria um subtítulo para a seção de gráficos
st.subheader("📈 Comparativo: Notas vs Frequência")
# Cria um gráfico de barras mostrando o nome do aluno no eixo X e a nota no eixo Y
st.bar_chart(data=dados, x="nome", y="nota", color="status")

#streamlit run app.py