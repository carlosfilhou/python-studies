'''
6. DESAFIO. Escreva um programa que dado uma lista de números inteiros, imprime
o maior número dessa lista.
lista = [1, 6, 2, 5]
...
# Deve imprimir 6
# '''

lista = [1, 6, 2, 5]

maior_numero = 0

for num in lista:
    if maior_numero < num:
        maior_numero = num

print(maior_numero)
