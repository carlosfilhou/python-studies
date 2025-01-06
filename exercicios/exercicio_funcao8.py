'''
Escreva uma função chamada contar_palavras que recebe uma string como argumento
e retorna o número de palavras na frase.Considere que as palavras são separadas por espaços.
'''


def contar_palavras(numero_palavras):
    resultado = 1
    for element in numero_palavras:
        if element == " ":
            resultado = resultado + 1

    return resultado


print(contar_palavras("eu sou"))
