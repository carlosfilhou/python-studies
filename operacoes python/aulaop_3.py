# OPERADORES LÓGICOS

# not

idade = 16

maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade

print(idade)
print(maior_de_idade)
print(menor_de_idade)

# and

usuario_correto = True
senha_correta = True

sucesso = usuario_correto and senha_correta

print("Login bem sucedido", sucesso)

# or

altura = 1,30
altura_minima = 1,50
acompanhado_pais = True

pode_entrar = altura >= altura_minima or acompanhado_pais

print("essa criança pode entrar no brinquedo?", pode_entrar)