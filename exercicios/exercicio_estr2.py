'''
2. Dada uma lista de números inteiros, escreva um programa que calcula a soma de
todos os números na lista.
Se preferir, pode utilizar a lista abaixo como exemplo:
list = [1, 10, 20, 35, 22, 12]
# Resultado deve ser = 100
'''

numeros = [1, 10, 20, 35, 22, 12]
soma_parcial = 0
soma_total = 0

for i in numeros:
    soma_total = i + soma_parcial
    soma_parcial = soma_total

print(soma_total)
