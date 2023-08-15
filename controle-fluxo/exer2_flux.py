resultado = 0

while True:
    a = (input("Digite um número decimal (lembrando que se você digitar qualquer valor que não seja número o programa irá dar erro): "))
    op = str(input("Se você quiser somar digite (+), subtrair (-), multiplicar (*) ou dividir (/): "))
    b = (input("Digite um número decimal (lembrando que se você digitar qualquer valor que não seja número o programa irá dar erro): "))

    print(type(a)) # quero checar a classe com if para escrever para o usuário que ele não digitou um valor numérico

    a = float(a)
    b = float(b)

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        resultado = a / b

    print("O resultado da sua operação é: ", resultado)


        
# EXERCÍCIO INCOMPLETO, EM CONTRUÇÃO!