'''
Escreva uma função chamada contar_vogais que recebe uma string 
como argumento e retorna o número de vogais presentes nessa string.
'''


def contar_vogais(palavra):
    numero_vogais = 0
    for element in palavra:
        if element == "a":
            numero_vogais = numero_vogais + 1
        elif element == "e":
            numero_vogais = numero_vogais + 1
        elif element == "i":
            numero_vogais = numero_vogais + 1
        elif element == "o":
            numero_vogais = numero_vogais + 1
        elif element == "u":
            numero_vogais = numero_vogais + 1

    return numero_vogais


print(contar_vogais("abacaxi"))
