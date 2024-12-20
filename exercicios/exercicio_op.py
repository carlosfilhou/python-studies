'''
1. Escreva um programa que receba um número inteiro do usuário e imprima True
caso o número seja par e False, caso o número seja ímpar.
'''

num = input("Digite um número e descubra se ele é par (True) ou ímpar (False): ")
num = int(num)

num = num % 2

result = num == 0  # a operador relacional irá me retornar um booleano

print(result)



