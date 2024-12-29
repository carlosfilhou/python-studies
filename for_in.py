# FOR (estrutura de repetição PARA iterar elementos)
# É MAIS USADO PARA PERCORRER ELEMENTOS EM UMA SEQUÊNCIA (LISTAS, TUPLAS, DICIONÁRIOS, ETC.).

# for in
valores = [2, 3, 4]

# O comando da lista vafor percorre cada elemento lores, um de cada vez.
# a cada repetição, ele pega um valor da lista e coloca na variável i.
# A variável i é criada automaticamente pelo Python dentro do laço for.
# O Python entende que você quer usar essa variável i para armazenar os valores da lista enquanto percorre cada elemento

for i in valores:
    print(i)

# Primeiro, ele pega o 2 (primeiro elemento de valores) e coloca na variável i, e imprime.
# Depois, ele pega o 3, coloca em i, e imprime.
# Por último, pega o 4, coloca em i, e imprime.


# --------------------------------------

alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

for aluno in alunos:
    print(aluno[1])  # Isso imprime a segunda posição da tupla (a nota)

cadastro = {
    "Carlos": 123,
    "Admin": 321,
    "Joao": 8451
}

for i in cadastro:
    print(i)  # o for i in cadastro percorre APENAS AS CHAVES
    print(cadastro[i])  # isso imprime o VALOR ASSOCIADO Á CHAVE atual (i)
    print(cadastro)  # aqui, você imprime o DICIONÁRIO INTEIRO em cada iteração


# USANDO MÉTODOS DO DICIONÁRIO:
for i in cadastro.items():  # percorrendo e iterando cada item completo dentro do dicionário
    print(i)

for k, v in cadastro.items():  # percorrendo e iterando em 2 variáveis "k" e "v"
    print(k, v)

for i in cadastro.keys():  # percorrendo e iterando cada chave dentro do dicionário
    print(i)

for i in cadastro.values():  # percorrendo e iterando cada valor dentro do dicionário
    print(i)
