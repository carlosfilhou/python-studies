num = 8
i = 0

while i < 3:
    i = i + 1
    print("Essa é a tentativa de número ", i)
    user_num = int(input("Esse é o jogo 'ACERTE O NÙMERO' você tem 3 tentativas para descobrir o número pré-escolhido pelo sistema, boa sorte: "))

    if user_num < num:
        print("Esse número é menor que o número pré-definido pelo sistema.")
    elif user_num > num:
        print("Esse número é maior que o número pré-definido pelo sistema.")
    else:
        print("VOCÊ ACERTOU, ESSE É NÚMERO CORRETO! \n" "O jogo terminou." )