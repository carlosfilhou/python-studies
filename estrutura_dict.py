# DICIONÁRIOS (estrutura de dados NÃO ORDENADA, chave-valor)
# É MAIS USADO PARA ARMAZENAR DADOS COM UMA RELAÇÃO DE CHAVE E VALOR, COMO EM UM REGISTRO DE INFORMAÇÕES.

# {key: value}
notas = {
    "Carlos": 9,
    "Lucas": 7,
    "Joao": 10
}

janeiro = {
    1: "Sábado",
    2: "Domingo",
}

# o objeto carlos tem os atributos representados pelas chaves do dict
carlos = {
    "nome": "Carlos",
    "idade": 29,
    "admin": True
}

# dicionário dentro de um dicionário
joao = {
    "nome": "Joao",
    "idade": 28,
    "admin": False,
    "endereço": {
        "rua": "Álvaro de Carvalho",
        "número": 4
    }
}

# acessando o dia pela chave
print("Aqui está a nota de Carlos no dicionário:", notas["Carlos"])
print("Aqui o dia 1 de janeiro será", janeiro[1])

# acessando o atributo do usuário pela chave
print("Aqui é a idade de Carlos:", carlos["idade"])

# acessando uma chave dentro de uma chave no dicionário
print("Aqui está o nome da rua do Joao:", joao["endereço"]["rua"])
