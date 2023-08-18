while True:

    n = int(input("Digite um número inteiro: "))

    if n < 2:
        print(n, "não é primo!")
    else:
        primo = 1  # Usaremos 1 para representar 'primo' e 0 para 'não primo'
        divisor = 2
        while divisor < n:
            if n % divisor == 0:
                primo = 0
                break
            divisor += 1

        if primo == 1:
            print(n, "é primo!")
        else:
            print(n, "não é primo!")

# Finalizado