'''
4. Suponha o seguinte programa:
# Alunos e suas respectivas notas
alunos = [
("Alice"
, 8),
("Bob"
, 7),
("Carlos"
, 9),
]
Escreva uma programa que calcula a média das notas de todos os alunos.
'''

# declarando a tupla
alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]
quantidade_elementos = len(alunos)

# declarando variáveis
soma_parcial = 0
soma_total = 0
media = 0

# calculando a soma de todos os elementos
for i in alunos:
    soma_total = i[1] + soma_parcial
    soma_parcial = soma_total

media = soma_total / quantidade_elementos

print(media)
