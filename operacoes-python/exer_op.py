num = input("Digite um número inteiro: ")

num = int(num)

print("Se esse número for PAR será TRUE, e se for IMPAR será FALSE: ", num % 2 == 0) # ele está dizendo que se o resto da divisão da variável num for 0 o valor será true.

print("AQUI É O SEGUNDO EXERCICIO:")

a = 5
b = 10
x = True 
y = False

print((x or y) and (a < b))
print((x or y) and not (a < b))