total = 0

while True:
    valor = float(input("Digite o valor da compra: \n")) # aqui estamos "envelopando" o input para que ele seja do tipo float
    total = total + valor

    continuar = input("Deseja continuar? (s/n)")

    if continuar != "s":
        break # esse é um comando para parar o loop

print("O valor total da compra é: ", total)