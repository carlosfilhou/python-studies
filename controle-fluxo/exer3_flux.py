while True:

    usuario = "admin"
    senha = "1234"

    usuario_login = input("Digite o USUÁRIO: \n")
    senha_login = input("Digite a SENHA: \n")

    if usuario_login != "admin":
        print("USUÁRIO INCORRETO")
    elif senha_login != "1234":
        print("SENHA INCORRETA")
    else:
        print("Autenticação foi bem-sucedida.")
