# tuplas são imutáveis, ou seja, você não pode depois de ter criado uma 'tupla', adicionar, remover ou alterar os seus elementos

x = (1, 50, 20) # tuplas podem ser criadas com parenteses
z = 1, 50, 20 # ou sem parenteses

print(x)

print(type(z))



# tuplas podem armazenar tuplas e listas como no exemplo abaixo.

turma = (
    ("primeiro ano", 3),
    [10, 2, 7.5],
    "nome da escola"
)