# DEF (função para DEFINIR funções)
# É MAIS USADO PARA CRIAR UM BLOCO DE CÓDIGO REUTILIZÁVEL QUE PODE SER CHAMADO VÁRIAS VEZES.

# definindo uma função antes de executa-la
def dar_boas_vindas():
    print("Olá")
    print("Mundo!")


# executar uma função previamente definida
dar_boas_vindas()


# -----------------------------------------

# função com parâmetro
def bem_vindo_ao_time(nome, sobrenome, cidade):  # PARÂMETRO
    print("Olá,", nome, sobrenome)
    print("Bem-vindo a", cidade)


# ARGUMENTOS POSICIONAIS: ATENÇÃO NA SEQUÊNCIA OU POSIÇÃO DOS ARGUMENTOS!
bem_vindo_ao_time("Carlos", "Augusto", "Dublin")  # ARGUMENTO

# ARGUMENTOS NOMEADOS (keyword arguments):
bem_vindo_ao_time(sobrenome="Paulo", nome="João", cidade="Florianópolis")
