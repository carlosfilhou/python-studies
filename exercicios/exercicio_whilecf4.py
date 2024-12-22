'''
4. O jogo “Acerte o número” funciona da seguinte maneira:
a. Existe um certo número inteiro declarado dentro do programa que o usuário
desconhece. Por exemplo: numero = 8
b. O usuário tem 3 tentativas para acertar o número.
c. A cada tentativa, é informado ao usuário se o número que ele digitou é maior,
menor, ou igual ao número correto.
d. O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário
acerta o número (ganhou).
Implemente o jogo “Acerte o número”.
'''

numero = 6
rodada = 0

while rodada < 3:
    numero_usuario = int(input("Acerte o número, você tem 3 tentativas: "))
    if numero_usuario < numero:
        print("Esse número é menor que o número correto")
    elif numero_usuario > numero:
        print("Esse número é maior que o número correto")
    else:
        print("Parabéns você acertou!")
        break

    rodada += 1

if rodada >= 3:
    print("Você perdeu o jogo!")
