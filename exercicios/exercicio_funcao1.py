'''
1. Escreva uma função que recebe um número inteiro positivo e retorna True caso ele
seja primo e False , caso contrário.
Sugestão:
def e
_primo(n):
# Sua implementação aqui
print(e
_primo(1))
# False
print(e
_primo(2))
# True
'''

n = int(input("Digite um número inteiro positivo: "))


def e_primo(n):
    primo = True
    contador = 2

    if n <= 1:
        primo = False  # 1 e números menores que 1 não são primos
    if n == 2:
        primo = True  # 2 é primo

    while contador < n:
        if n % contador == 0:  # condição ira testar o resto com todos os numeros
            primo = False
            break
        else:
            contador += 1  # igual a (contador = contador + 1)

    return primo


print(e_primo(n))
