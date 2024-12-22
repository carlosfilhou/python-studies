# INPUT

# REBENDO INPUT DO USUARIO
idade = input("Digite a idade: ")
# idade automaticamente será uma STRING
print("sua idade é: ", idade, " (esse valor é uma STRING)")

# EM PYTHON O VALOR RETORNADO NO INPUT SEMPRE SERÁ UMA STRING
# PARA ALTERAR, SERÁ NECESSÁRIO USAR O MÉTODO (INT)
# usando método (int), também podemos usar o float)
dias = int(input("Digite a quantidade de dias: "))
print("o número de dias é: ", dias, " (esse valor é do tipo INT)")


# PARA INSERIR UMA QUEBRA DE LINHA É USADO O CARACTER ESPECIAL \n
print("sua idade está uma linha abaixo \n", idade)
