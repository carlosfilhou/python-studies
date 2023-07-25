valor_compra = input("Digite o valor da compra: ")

valor_compra = float(valor_compra)

valor_frete = input("Digite o valor do frete: ")

valor_frete = float(valor_frete)

fidelidade = input("Cliente é cadastrado no programa de fidelidade? (s/n): ")

print(valor_compra + valor_frete > 100 or fidelidade == "s")