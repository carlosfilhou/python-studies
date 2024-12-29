'''
3. Data uma lista de números inteiros, escreva um programa que calcula a média dos
números na lista. O resultado não deve incluir números decimais. Exemplo: 12.3
deve imprimir apenas 12.
Se preferir, pode utilizar a lista abaixo como exemplo:
lista = [1, 10, 20, 35, 22, 12]
# Resultado deve ser 16
P.S.: Pode utilizar o operador // (divisão inteira)
'''

# declarando a lista
lista = [1, 10, 20, 35, 22, 12]
qtd_elementos = len(lista)

# declarando as variáveis
soma_total = 0
soma_parcial = 0

# somando todos o elementos da lista
for i in lista:
    soma_parcial = soma_total + i
    soma_total = soma_parcial

# calculando a média
media = soma_total // qtd_elementos  # sempre TOTAL dividido pela QUANTIDADE

print(media)
