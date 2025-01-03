# Dada uma lista de números, escreva um programa que calcule a soma de todos os números pares e a soma
# de todos os números ímpares da lista. Em seguida, imprima as duas somas separadamente.
# Soma dos pares: 30 (2 + 4 + 6 + 8 + 10)
# Soma dos ímpares: 25 (1 + 3 + 5 + 7 + 9)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado_par = 0
resultado_impar = 0

for element in lista:
    if element % 2 == 0:
        resultado_par = resultado_par + element
    else:
        resultado_impar = resultado_impar + element

print("Resultado da soma dos números pares: ", resultado_par)

print("Resultado da soma dos números impar: ", resultado_impar)
