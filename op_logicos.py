# OPERADORES LÓGICOS

# not NEGAÇÃO
idade = 16
maior_de_idade = idade >= 18
menor_de_idade = not maior_de_idade  # invertendo o valor booleano

# and CONJUNÇÃO
usuario_correto = True
senha_correta = True
sucesso = usuario_correto and senha_correta  # True se ambos sejam verdadeiros

# or DIJUNÇÃO
idade = 14
idade_minima = 16
acompanhada_pelos_pais = True
pode_assistir_o_filme_cinema = idade >= idade_minima or acompanhada_pelos_pais
# False se ambos sejam falsos
