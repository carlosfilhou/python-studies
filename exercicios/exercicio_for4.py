# Dada uma lista de números, escreva um programa que encontre o menor número da lista sem usar a função min

lista = [5, 2, 8, 1, 3]
resultado = lista[0]

for element in lista:
    if element < resultado:
        resultado = element

print("O menorvalor da lista é: ", resultado)
