# arquitetura de dados, listas

lista = [1, 10, 5, 20, 25] # criando a lista com seus respectivos indices

lista.append(3) # usando o método "append" para adicionar um valor ao final da lista

print("Aqui está a lista \n", lista)

lista.insert(0 ,0) # usando o método insert para inserir um valor no índice desejado

print("Aqui está a lista com um valor inserido no primeiro índice \n", lista)

lista.sort() # usando o método "sort" para odernar os valores entre sí

print("Aqui está a lista de forma ordenada \n", lista)

lista.sort(reverse=True) # usando o reverse para colocar a lista de forma decrescente

print("Aqui está a lista de forma decrescente \n", lista)

x = lista.pop() # usando o método "pop" para remover o último valor da lista e adicionando ele em uma variável (pode escolher o índice)

print("Aqui está a lista com o último valor removido \n", lista)

print("Aqui está o último valor que foi removido \n", x)

# aqui um exemplo de que no Python você pode armazenar valores de qualquer tipo em uma lista

cadastro = ["Carlos", 28, 1.88] # lembrando que o NOME está na posição/índice 0, a idade está no 1 e assim por diante...

print("Imprimindo a lista cadastro \n", cadastro)

print("Imprimindo a altura da pessoa cadastrada \n", cadastro[2])
