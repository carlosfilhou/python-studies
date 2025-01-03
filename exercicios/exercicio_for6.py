# Dada uma lista de palavras, escreva um programa que crie um dicionário contando quantas vezes cada palavra aparece na lista

lista = ["maçã", "banana", "maçã", "laranja", "banana", "banana"]
dicionario = {}

for element in lista:
    if element in dicionario:
        dicionario[element] += 1  # Incrementar o valor
    else:
        dicionario[element] = 1  # Adicionar a chave com valor inicial

print(dicionario)
