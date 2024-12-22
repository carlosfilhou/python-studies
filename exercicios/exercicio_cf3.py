'''
3. Escreva um programa de autenticação que receba um nome de usuário e senha
( input ) informe se:
Autenticação foi bem-sucedida.
Se o nome de usuário não existe.
Se a senha está incorreta.
Os valores corretos de nome de usuário e senha devem estar armazenados em
constantes, como no exemplo abaixo:
USUARIO = "admin"
SENHA = "123123"
nome_usuario = input("Digite o nome do usuário:\n")
...
'''

USUARIO = "admin"
SENHA = "123123"

nome_usuario = input("Digite o nome do usuário:\n")
senha_usuario = input("Digite a senha:\n")

if nome_usuario != USUARIO:
    print("O usuário não existe.")
elif senha_usuario != SENHA:
    print("A senha está incorreta.")
else:
    print("Autenticação foi bem-sucedida.")
