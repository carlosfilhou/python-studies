'''
4. Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto uma
tupla quanto um dicionário. Dica: método type pode te ajudar.
'''

pessoa = ("Carlos", 29)
pessoa_dicionario = {
    "nome": "João",
    "idade": 17
}


def maior_idade(lista):
    if type(lista) == tuple:
        if lista[1] < 18:
            print("Essa pessoa é menor de idade!")
        else:
            print("Essa pessoa é maior de idade!")
    else:
        if lista["idade"] < 18:
            print("Essa pessoa é menor de idade!")
        else:
            print("Essa pessoa é maior de idade!")


maior_idade(pessoa_dicionario)
