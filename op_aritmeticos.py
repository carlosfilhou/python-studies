# OPERADORES ARITMETICOS
a = 10
b = 2

# (SUBTRAÇÃO: -) (MULTIPLICAÇÃO: *) (DIVISÃO: /)
resultado = a + b

print("O resultado é:", resultado)

# ATENÇÃO NA OPERAÇÃO DE DIVISÃO O RESULTADO SERÁ DO TIPO FLOAT
# A NÃO SER QUE VOCÊ USE A DIVISÃO INTEIRA DO PYTHON:
resultado = a // b

print("O resultado da divisão inteira é:", resultado)

# OPERAÇÃO EXPONENCIAL (OU SEJA, UM NUMERO ELEVADO A OUTRO NUMERO)
resultado = a ** b

print("O resultado da exponencial é:", resultado)

# MÓDULO (OU SEJA, O RESTO DA DIVISÃO DE DOIS NÚMEROS)
resultado = a % b

print("O resto da divisão entre os dois números é:", resultado)

# -------------------------------

# OPERAÇÕES SEGUEM AS REGRAS MATEMÁTICAS
# (ONDE POR EXEMPLO A MULTIPLICAÇÃO VEM ANTES DA ADIÇÃO E SUBTRAÇÃO)
# UMA BOA PRÁTICA E MUITO COMUM É USAR OS PARENTESES PARA ESPECIFICAR A ORDEM

# PRIMEIRO A MULTIPLICAÇÃO DEPOIS ADIÇÃO
resultado = 1 + (2 * 2)

print("O resultado da operação matemática é:", resultado)

# TROCANDO A ORDEM
resultado = (1 + 2) * 2

print("O resultado da operação matemática somando primeiro é:", resultado)
