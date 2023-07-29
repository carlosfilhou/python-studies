idade = input("Digite sua idade: ")

idade = int(idade)

if idade >= 18 and idade <= 69:
    print("adulto")
elif idade >= 12 and idade < 18:
    print("adolescente")
elif idade >= 70:
    print("idoso")
else:
    print("criançaa")