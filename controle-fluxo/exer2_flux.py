resultado = 0

while True:
    a = input(
        "Digite um número decimal (lembrando que se você digitar qualquer valor que não seja número o programa irá dar erro): "
    )
    op = str(
        input(
            "Digite um operador, somar (+), subtrair (-), multiplicar (*) ou dividir (/): "
        )
    )
    b = input(
        "Digite um número decimal (lembrando que se você digitar qualquer valor que não seja número o programa irá dar erro): "
    )

    if op == "+":
        resultado = a + b
        print("O resultado da sua operação é: ", resultado)
    elif op == "-":
        resultado = a - b
        print("O resultado da sua operação é: ", resultado)
    elif op == "*":
        resultado = a * b
        print("O resultado da sua operação é: ", resultado)
    elif op == "/" and b == 0:
        print("Não é possível realizar divisão por zero!")
    elif op == "/":
        resultado = a / b
        print("O resultado da sua operação é: ", resultado)
    else:
        print("A opção que você digitou no seu operador não é válida!")
