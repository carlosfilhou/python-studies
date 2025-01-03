'''
Escreva um programa que declare uma lista de números inteiros e calcule o produto 
de todos os números na lista (ou seja, multiplique todos os elementos da lista).
'''

lista = [3, 2, 3, 4]
multipli = 1

for element in lista:
    multipli = multipli * element  # Multiplica o valor de multipli pelo elemento atual

print(multipli)  # O resultado final
