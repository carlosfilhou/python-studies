'''
3. Implemente uma função maior_idade(pessoa) que receba uma tupla representando
uma pessoa com nome e idade e imprime na tela se a pessoa é maior de idade ou
não.
'''

pessoa = ("Carlos", 29)


def maior_idade(tupla):
    if tupla[1] < 18:
        print("Essa pessoa é menor de idade!")
    else:
        print("Essa pessoa é maior de idade!")


maior_idade(pessoa)
