# DEF (função para DEFINIR funções)
# É MAIS USADO PARA CRIAR UM BLOCO DE CÓDIGO REUTILIZÁVEL QUE PODE SER CHAMADO VÁRIAS VEZES.
# ARMAZENA UMA LÓGICA OU REGRA DE NEGÓCIO

# definindo uma função antes de executa-la
def dar_boas_vindas():
    print("Olá")
    print("Mundo!")
    # por baixo dos panos toda função tem um "return" que retorna um none


# executar uma função previamente definida
dar_boas_vindas()


# -----------------------------------------


# definindo uma função com parâmetro
def bem_vindo_ao_time(nome, sobrenome, cidade):  # PARÂMETRO
    print("Olá,", nome, sobrenome)
    print("Bem-vindo a", cidade)


# ARGUMENTOS POSICIONAIS: ATENÇÃO NA SEQUÊNCIA OU POSIÇÃO DOS ARGUMENTOS!
bem_vindo_ao_time("Carlos", "Augusto", "Dublin")  # ARGUMENTO

# ARGUMENTOS NOMEADOS (keyword arguments):
bem_vindo_ao_time(sobrenome="Paulo", nome="João", cidade="Florianópolis")


# ----------------------------------------


# definindo uma função que retorna
def calcular_conta(consumo, taxa_servico):
    # early return ou retorno antecipado
    if taxa_servico == 0:
        return consumo

    servico = consumo * taxa_servico
    valor = consumo + servico
    return valor


# variável recebendo uma função que retorna algo
valor_final = calcular_conta(consumo=100, taxa_servico=0.1)

# printando a variável
print("O valor calculado é da função que retorna é:", valor_final)


# -----------------------------------------


# definindo uma função com parâmetro padrão
# (ATENÇÃO PRIMEIRO ARG POSICIONAL E DEPOIS ARG NOMEADO)
def calcular_conta(consumo, taxa_servico=0.1):
    servico = consumo * taxa_servico
    valor = consumo + servico
    return valor


# passar o argumento é opcional pois ele ja tem um valor padrão no parâmetro
valor_final = calcular_conta(consumo=200)

# printando a variável
print("O valor calculado com taxa de servico padrão é:", valor_final)
