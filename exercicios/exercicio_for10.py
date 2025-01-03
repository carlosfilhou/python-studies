# Dada uma lista de palavras, crie um programa que remova todas as palavras duplicadas e as organize em ordem alfabética.
# Resultado esperado: ['banana', 'laranja', 'maçã', 'uva']

lista = ["maçã", "banana", "laranja", "banana", "maçã", "uva"]
nova_lista = [lista[0]]

for element in lista:
    if element not in nova_lista:
        nova_lista.append(element)

nova_lista.sort()

print(nova_lista)
