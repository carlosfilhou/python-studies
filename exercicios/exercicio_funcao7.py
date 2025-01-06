'''
Escreva uma função chamada reverter_palavra que recebe uma string e retorna essa string de trás para frente.
'''


def reverter_palavra(palavra):
    palavra_invertida = ""
    # Aqui, você está iterando sobre um intervalo de números (os índices da string), gerado pelo range().
    for element in range(len(palavra) - 1, -1, -1):
        # acessar o caracter da string usando o índice
        palavra_invertida = palavra_invertida + palavra[element]

    return palavra_invertida


print(reverter_palavra("carlos"))
