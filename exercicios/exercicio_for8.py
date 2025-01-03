# Dada uma lista de números, escreva um programa que crie uma nova lista contendo apenas os números que são múltiplos de 3
# Nova lista esperada: [3, 9, 12, 18]

lista = [1, 3, 5, 9, 12, 14, 18, 20]
nova_lista = []

for element in lista:
    if element % 3 == 0:
        nova_lista.append(element)

print(nova_lista)
