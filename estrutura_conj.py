# CONJUNTOS (SET) (estrutura de dados NÃO ORDENADA, sem duplicatas)
# PARTICULARIDADE: NÃO POSSUEM E NÃO RECEBEM ELEMENTOS REPETIDOS

# pode ser declarado de duas formas
usuarios = {"Admin", "Carlos"}
usuarios_2 = set(["Admin", "Carlos", "Rafael", "Lucas"])

print("Aqui o primeiro conjunto: ", usuarios)
print("Aqui o segundo conjunto: ", usuarios_2)

# MÉTODOS

# adicionar elemento
usuarios.add("Joao")
print("Joao adicionado ao primeiro conjunto:", usuarios)

usuarios.add("Admin")  # não será adicionado, "Admin" ja existe no conjunto

# união de dois conjuntos, unir os dois (2 opções)
usuarios.union(usuarios_2)  # primeira opção
usuarios | usuarios_2  # segunda opção
print("A união dos dois conjuntos", usuarios.union(usuarios_2))

# interseção de dois conjuntos, o que tem igual entre os dois (2 opções)
usuarios.intersection(usuarios_2)  # primeira opção
usuarios & usuarios_2  # segunda opção
print("A interseção dos dois conjuntos", usuarios.intersection(usuarios_2))

# diferença de dois conjuntos, o que está em um e não no outro (2 opções)
usuarios.difference(usuarios_2)  # primeira opção
usuarios - usuarios_2  # segunda opção
print("A diferença dos dois conjuntos", usuarios.difference(usuarios_2))
