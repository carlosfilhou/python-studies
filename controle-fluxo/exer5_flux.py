i = 0

while True:
    n = int(input("Digite um número inteiro: "))

    while i < n:
        i = i + 1
        if i % 2 == 0:
            print(i)