'''
1. Escreva um programa que receba um número inteiro n e imprima a soma de todos
os números de 1 até n (inclusive n ).
'''

n = int(input("Digite um número inteiro: "))

contador = 1
resultado = 0

while contador <= n:
    resultado = resultado + contador
    contador = contador + 1

print("A soma de todos os números de 1 até", n, "é", resultado)
