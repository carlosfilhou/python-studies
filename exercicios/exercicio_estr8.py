'''
8. DESAFIO. Escreva um programa que declara uma lista com elementos de
diferentes tipos e imprime na tela essa lista invertida. Não é permitido utilizar
métodos como reverse ou sort.
def inverte
...
_
lista(lista):
lista = ["a"
, 5, {1}]
lista
invertida = inverte
_
_
lista(lista)
print(lista
_
invertida)
# [{1}, 5, "a"]
'''

lista = ["a", 5, {1}, "abc"]


def inverte_lista(lista):
    lista_invertida = []  # Lista para armazenar os elementos invertidos
    for elemento in lista:  # Itera sobre os elementos da lista original
        # Insere cada elemento no início da nova lista
        lista_invertida.insert(0, elemento)
    return lista_invertida  # Retorna a lista invertida


lista_invertida = inverte_lista(lista)

print(lista_invertida)
