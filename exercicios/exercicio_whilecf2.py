'''
2. Escreva um programa que receba um número inteiro n e imprima todos os
números pares de 1 até n (inclusive n ).
'''
n = int(input("Digite um  número inteiro: "))
contador = 1

while contador <= n:
    if contador % 2 == 0:
        print(contador)
    contador = contador + 1
