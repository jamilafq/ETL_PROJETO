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