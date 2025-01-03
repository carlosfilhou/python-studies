# Dada uma lista de números, escreva um programa que crie uma nova lista contendo os mesmos números, mas sem duplicatas. A ordem dos números deve ser mantida

lista = [1, 2, 2, 3, 4, 4, 5, 1]

nova_lista = []

for element in lista:
    if element not in nova_lista:
        nova_lista.append(element)

nova_lista.sort()

print("Essa é a lista atualizada sem valor duplicados: ", nova_lista)
