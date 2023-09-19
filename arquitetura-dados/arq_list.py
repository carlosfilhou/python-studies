# arquitetura de dados, listas

lista = [1, 10, 5, 20, 25] # criando a lista com seus respectivos indices

lista.append(3) # usando o método "append" para adicionar um valor ao final da lista

print("Aqui está a lista \n", lista)

lista.insert(0 ,0) # usando o método insert para inserir um valor no índice desejado

print("Aqui está a lista com um valor inserido no primeiro índice \n", lista)

lista[0] = 0.1 # ou você também pode fazer dessa forma, sem utilizar método

print("Aqui está a lista com um valor inserido no índice '0' sem usar o método insert \n", lista)

lista.sort() # usando o método "sort" para odernar os valores entre sí

print("Aqui está a lista de forma ordenada \n", lista)

lista.sort(reverse=True) # usando o reverse para colocar a lista de forma decrescente

print("Aqui está a lista de forma decrescente \n", lista)

x = lista.pop() # usando o método "pop" para remover o último valor da lista e adicionando ele em uma variável (pode escolher o índice)

print("Aqui está a lista com o último valor removido \n", lista)

print("Aqui está o último valor que foi removido \n", x)

# aqui um exemplo de que no Python você pode armazenar valores de qualquer tipo em uma lista

pessoa = ["José", 32, 1.60] # lembrando que o NOME está na posição/índice 0, a idade está no 1 e assim por diante...

print("Imprimindo a lista pessoa \n", pessoa)

print("Imprimindo a altura da pessoa \n", pessoa[2])


# aqui um exemplo de que no Python você pode criar uma lista dentro de uma lista

cadastro = [
    ["Carlos", 28, 1.88],
    ["João", 27, 1.85],
    ["Rafael", 29, 1.75]
]

print("Imprimindo a lista cadastro \n", cadastro)

print("Imprimindo o índice número 1 da lista cadastro \n",cadastro[1])

# somando a média das notas em uma lista

notas = [1, 10, 30, 9, 40]

i = 0
total = 0

qtd = len(notas) # aqui o médodo 'len' irá dizer quantos elementos existem nessa lista.

while i < qtd:
    total = total + notas[i]
    i = i + 1

print("O total das notas é:", total)

media = total / qtd

print("A média das notas é:", media)