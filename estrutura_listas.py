# LISTAS (estrutura de dados ORDENADAS, ordenação de inserção)

# lista homogênea, com elementos do mesmo tipo
notas = [2, 4, 3, 1]
#        0  1  2  3

# lista heterogênea, com elementos de tipos diferentes
pessoa = ["carlos", 29, 1.88]  # string, int, float
#             0      1     2

# Listas de listas (lista 2D ou matrizes)
pessoas = [
    ["Lucas", 28],
    ["Gabriel", 29]
]

print("Essa é sua lista: ", notas)

print("Aqui printando apenas o elemento do índice 2:", notas[2])


# MÉTODOS

notas.append(5)  # adicionar elemento ao final da lista
print("Foi adicionado o elemento 5 ao final da lista:", notas)

notas.sort()  # ordenação de valores
print("Aqui a sua lista foi ordenada em sequência de valores:", notas)

notas.sort(reverse=True)  # ordenação de valores ao contrário
print("Aqui a sua lista foi ordenada em sequência reversa de valores:", notas)

# removendo o último elemento da lista e salvando em uma variável
elemento_removido = notas.pop()
print("Foi removido o último elemento da lista:", notas)
print("Aqui printando apenas o elemento que foi removido:", elemento_removido)

notas.pop(1)  # remover o elemento do índice 1
print("Foi removido o elemento do índice 1:", notas)

notas.insert(0, 6)  # adicionar elemento 6 no índice 0
print("Foi adicionado o elemento 6 no índice 0:", notas)

quantidade = len(notas)  # saber a quantidade de elementos na lista
print("Essa é a quantidade de elementos que existem na lista:", quantidade)


# ---------------------------------

# CALCULANDO A MÉDIA (soma total de todas as notas, dividido pela quantidade)

i = 0
total = 0
qtd = len(notas)

# somando o total de todas as notas
while i < qtd:
    total = total + notas[i]
    i = i + 1

print("A soma de todas das notas é:", total)

media = total / qtd
print("A média das notas é:", media)
