'''
Escreva um programa que declare uma lista de números inteiros e crie uma 
nova lista contendo apenas os números ímpares da lista original.
'''

lista = [1, 2, 3, 4, 5, 6, 7, 8]
nova_lista = []

for element in lista:
    if element % 2 != 0:
        nova_lista.append(element)

print(nova_lista)
