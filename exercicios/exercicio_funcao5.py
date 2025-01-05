'''
5. Implemente uma função que recebe dois argumentos, uma lista e um elemento , e
retorna True caso elemento seja encontrado na lista , e False caso contrário. Não
é permitido utilizar o método in .
'''

lista = [9, 2, 4, "Carlos"]


def encontrar_elemento(lista, elemento):
    for element in lista:
        if element == elemento:
            return True

    return False


print(encontrar_elemento(lista, 3))
