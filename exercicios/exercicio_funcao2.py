'''
Implemente uma função que recebe uma lista de números inteiros e retorna uma
tupla (pos, num) , onde pos é a posição (ou índice) do maior número na lista e num
é o valor desse número.
'''

minha_lista = [4, 6, 1, 7, 9]


def maior_numero(lista):
    num = max(lista)
    pos = lista.index(num)

    tupla = (pos, num)

    return tupla


maior_numero(minha_lista)
print(maior_numero(minha_lista))
