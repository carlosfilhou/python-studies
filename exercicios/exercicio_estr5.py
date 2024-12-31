'''
5. Suponha o seguinte programa:
# Alunos e suas notas representados através de dicionários
alunos = [
{
"nome": "Alice",
"nota": 8
},
{
"nome": "Bob",
"nota": 7
},
{
"nome": "Carlos",
"nota": 9
}
]
Escreva uma programa que calcula a média das notas de todos os alunos.
'''

alunos = [
    {
        "nome": "Alice",
        "nota": 8
    },
    {
        "nome": "Bob",
        "nota": 7
    },
    {
        "nome": "Carlos",
        "nota": 9
    }
]
quantidade_elementos = len(alunos)

media = 0
soma_parcial = 0
soma_total = 0

# desempacotando uma lista de dicionário e somando os elementos
for aluno in alunos:
    soma_parcial = aluno["nota"] + soma_total  # acessando a chave "nota"
    soma_total = soma_parcial

media = soma_total / quantidade_elementos

print(media)
