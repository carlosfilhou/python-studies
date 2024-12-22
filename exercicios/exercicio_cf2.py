'''
2. Implemente uma calculadora que recebe 3 valores do usuário:
a. Operando a (pode ser um inteiro ou float).
b. Operando b (pode ser um inteiro ou float).
c. Operador op.
i. op pode ser uma string representando o operador, por exemplo, "+" ou "
-
"
. Outra opção é utilizar números, por exemplo, 1 para soma , 2 para
subtração , etc.
O seu programa deve receber esses 3 valores e imprimir o resultado da operação.
Caso o operador seja de divisão e o segundo operando seja o valor zero, o
programa deve imprimir uma mensagem: “Não é possível realizar divisão por
zero!”.
'''

a = float(input("Digite o primeiro operando: "))
b = float(input("Digite o segundo operando: "))
op = input("Digite um operador: ")
resultado = 0

if op == "+":
    resultado = a + b
    print("O resultado da soma é: ", resultado)
elif op == "-":
    resultado = a - b
    print("O resultado da subtração é: ", resultado)
elif op == "/":
    if b == 0:
        print("Não é possível realizar divisão por zero!")
    else:
        resultado = a / b
        print("O resultado da divisão é: ", resultado)
elif op == "*":
    resultado = a * b
    print("O resultado da multiplicação é: ", resultado)
