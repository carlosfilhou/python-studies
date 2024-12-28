'''
1. Escreva um programa que lê números inteiros positivos do usuário, um após o
outro, e monta uma lista a partir desses números e depois imprime a lista montada.
O programa deve continuar solicitando por números até que o elemento digitado
seja um número negativo (que não deve ser inserido na lista).
'''

num = 0
list = []

while num >= 0:
    num = int(input("Digite um número inteiro: "))
    if num >= 0:
        list.append(num)
    else:
        print(list)
        break
