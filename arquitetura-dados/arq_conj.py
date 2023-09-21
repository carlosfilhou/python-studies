# para declarar um conjunto você irá utilizar 'chaves {}' como no exemplo a baixo

usuarios = {"alice", "bob"}

print(type(usuarios))

# você também pode declarar um conjunto a partir de uma lista como no exemplo a baixo

usuarios_2 = set(["alice", "bob"])

print(type(usuarios_2))

# o conjunto não pode ler valores iguais como no exemplo abaixo
# usuarios = {"alice", "bob", "alice"} --- nesse exemplo alice está repetindo 2 vezes e então será lido apenas 1 vez
