# CONDICIONAIS (estrutura de decisão SE, SENÃO)
# É MAIS USADO PARA DEFINIR FLUXOS DIFERENTES DE EXECUÇÃO BASEADOS EM UMA CONDIÇÃO BOOLEANA.

idade = input("Digite a sua idade: ")
idade = int(idade)

if idade >= 18:
    print("Você é adulto")
elif idade >= 12:  # elif (else if)
    print("Você é adolescente")
else:
    print("Você é criança")


# Lembrando que a condição não precisa ser um valor booleano,
# o Python irá analisar a espressão como se fosse um booleano.
# Então na verdade o interpretador vai aplicar um bool() em volta
# de qualquer expressão que estiver na condicional.

# TRUTHY e FALSY

# 3 VALORES CONSIDERADOS FALSY: 0, " ", None. O restante em sua maioria TRUTHY
