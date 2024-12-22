'''
3. Um número primo é um número que é divisível apenas por 1 e por ele mesmo.
Escreva um programa que receba um número n e informe se esse número é primo
ou não.
'''

n = int(input("Digite um número inteiro: "))
contador = 2
primo = True

if n <= 1:
    print("Esse não é um número primo")

while contador < n:
    if n % contador == 0:  # condição ira testar o resto com todos os numeros
        primo = False
        break
    contador += 1  # igual a (contador = contador + 1)

if primo == True:
    print("Esse é um número primo")
else:
    print("Esse não é um número primo")
