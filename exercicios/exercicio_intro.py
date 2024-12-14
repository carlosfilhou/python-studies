# 1. Escreva um programa que contenha 4 variáveis e que imprima na tela o tipo decada uma delas.
# A saída do seu programa deve ser na seguinte ordem:
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

name = "Carlos"
age = 29
height = 1.88
studying = True

print(type(name))
print(type(age))
print(type(height))
print(type(studying))

# 2. Escreva um programa com as seguintes especificações:
# Uma variável “valor_compras” que receba um valor do tipo float, representando
# o valor total das compras.
# Uma variável “desconto” que receba um valor do tipo float, representando o
# desconto a ser aplicado sobre o valor total das compras.
# Uma variável “quantidade_itens”, que represente a quantidade de itens que
# foram comprados.
# Seu programa deve imprimir dois resultados:
# 1. O valor final das compras, considerando o desconto aplicado.
# 2. O custo médio de cada item (considerando o valor final das compras).

valor_compras = 9.99
valor_desconto = 0.1  # 10% de desconto
quantidade_itens = 4

desconto_total = valor_compras * valor_desconto
valor_final = valor_compras - desconto_total
custo_medio = valor_final / quantidade_itens

print(valor_final)
print(custo_medio)
