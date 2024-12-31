# IF IN (Estrutura de Condicional PARA verificar a presença de elementos em uma sequência)
# O operador "in" é utilizado para verificar se um elemento está presente em uma sequência (como listas, tuplas, strings, dicionários, etc.).

# -------------------------------

# Verificando se um elemento está em uma lista
valores = [1, 2, 3, 4, 5]

# Verificando se o número 3 está na lista
if 3 in valores:
    print("O número 3 está na lista.")
else:
    print("O número 3 não está na lista.")

# Verificando se o número 6 está na lista
if 6 not in valores:
    print("O número 6 não está na lista.")

# -------------------------------

# Verificando se um elemento está em uma tupla
nomes = ("Alice", "Bob", "Carlos")

# Verificando se 'Bob' está na tupla
if "Bob" in nomes:
    print("Bob está na tupla.")
else:
    print("Bob não está na tupla.")

# -------------------------------

# Verificando se uma chave está em um dicionário
cadastro = {
    "Carlos": 123,
    "Admin": 321,
    "Joao": 8451
}

# Verificando se a chave 'Carlos' está no dicionário
if "Carlos" in cadastro:
    print("Carlos está no cadastro.")
else:
    print("Carlos não está no cadastro.")

# Verificando se a chave 'Ana' não está no dicionário
if "Ana" not in cadastro:
    print("Ana não está no cadastro.")

# -------------------------------

# Verificando se um valor está em um dicionário
if 8451 in cadastro.values():
    print("O valor 8451 está no cadastro.")
else:
    print("O valor 8451 não está no cadastro.")

# -------------------------------

# Usando o 'in' para percorrer chaves e valores no dicionário
for chave in cadastro:
    if chave in cadastro:
        print(f"A chave {chave} está no cadastro.")

# Também podemos fazer a verificação no `if` dentro de um loop
for chave, valor in cadastro.items():
    if chave in cadastro:
        print(f"A chave {chave} tem o valor {valor}.")
