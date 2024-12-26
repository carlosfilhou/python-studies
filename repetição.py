# WHILE (estrutura de repetição ENQUANTO a condição for verdadeira)
# É MAIS USADO PARA EXECUTAR UM BLOCO DE CÓDIGO REPETIDAMENTE ATÉ QUE UMA CONDIÇÃO BOOLEANA SEJA FALSA.

i = 1
while i < 51:
    print(i)
    i = i + 1

print("Fim.")

# ----------------------------------------

total = 0
while True:
    valor_compra = float(input("Digite o valor da compra: "))
    total = total + valor_compra

    if total > 50:
        break

print("As suas compras ultrapassaram o valor de 50 reais, valor total: ", total)
