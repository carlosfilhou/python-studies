# Dada uma lista de palavras, escreva um programa que crie uma nova lista contendo apenas as palavras que possuem mais de 5 letras

lista = ["maçã", "banana", "laranja", "abacaxi", "pêra"]
nova_lista = []

for element in lista:
    qtd = len(element)
    if qtd > 5:
        nova_lista.append(element)

print(nova_lista)
