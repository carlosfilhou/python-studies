'''
Implemente uma função chamada remover_duplicatas que recebe uma lista de números inteiros e retorna
uma nova lista sem números duplicados, mantendo a ordem dos elementos.
'''

lista = [1, 2, 3, 2, 4, 1]
lista2 = [3, 4, 4, 8, 9, 7, 7]


def remover_duplicatas(lista):
    nova_lista = []
    for element in lista:
        if element not in nova_lista:
            nova_lista.append(element)

    return nova_lista


print(remover_duplicatas(lista))
