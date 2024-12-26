# TUPLAS (são imutáveis, ou seja, depois de criada não será possível alterar seus elementos)
# É MAIS USADA EM UMA LISTA HETEREOGÊNEA (ELEMENTOS DE TIPOS DIFERENTES)

notas = (4, 2, 6)  # uso de parenteses é opcional

# normalmente a gente espera que tuplas representem um objeto, exemplo:
pessoa = ("Carlos", 29, 1.88)  # uma pessoa e suas caracteristicas

# armazenando outras tuplas e listas, exemplo:
turma = (
    ("Primeiro Ano", 3),  # 3 alunos no primeiro ano
    [7, 8, 3]  # 3 notas
)

# DESEMPACOTAR

# declarando variáveis e integrando a tupla a elas direto em cada posição
nome, idade, altura = pessoa  # desempacotamento
print(nome, idade, altura)

# Desempacotando os elementos da tupla "turma"
# 'ano_info' recebe ("Primeiro Ano", 3), e 'notas' recebe [7, 8, 3]
ano_info, notas = turma

# Desempacotando a tupla interna 'ano_info'
ano, qtd_alunos = ano_info  # 'ano' recebe "Primeiro Ano" e 'qtd_alunos' recebe 3

print(ano)  # Saída: Primeiro Ano
print(qtd_alunos)  # Saída: 3
print(notas)  # Saída: [7, 8, 3]
