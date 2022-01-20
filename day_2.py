#                   --------------- ADVENT OF CODE --- DAY 2 ---------------------

# PARTE 1:

# Now, you need to figure out how to pilot this thing.

# It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

# Note that since you're on a submarine, down and up affect your depth, and so they have the
# opposite result of what you might expect.

# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

# PARTE 2:

# Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine
# manual and discover that the process is actually slightly more complicated.

# In addition to horizontal position and depth, you'll also need to track a third value, aim, which also
# starts at 0. The commands also mean something entirely different than you first thought:

# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
#   It increases your horizontal position by X units.
#   It increases your depth by your aim multiplied by X.

# Using this new interpretation of the commands, calculate the horizontal position and depth you would have
# after following the planned course. What do you get if you multiply your final horizontal position by your
# final depth?

def soma_multiplicacao(horizontal, profundidade):

    soma_horizontal = sum(horizontal)
    soma_profundidade = sum(profundidade)
    resultado = soma_profundidade * soma_horizontal

    return resultado


def parte_1(dados, horizontal, profundidade):

    for linha in dados:
    # agora vamos colocar em listas separadas os valores correspondentes ao deslocamento horizontal e profundidade
        if linha[0] == "forward":
            horizontal.append(linha[1])

        if linha[0] == "down":
            profundidade.append(linha[1])          # down aumenta a profundidade

        if linha[0] == "up":
            profundidade.append(linha[1] * (-1))   # up diminui profundidade, por isso vamos colocar o valor negativo,
                                                # já que queremos somá-los depois

    resultado = soma_multiplicacao(horizontal, profundidade)

    print("PARTE 1: \n"
          f"A multiplicação entre as posições finais horizontal e de profundidade retorna um valor de {resultado}.\n")


def parte_2(dados, horizontal, profundidade, aim):
    for linha in dados:

        if linha[0] == "down":
            aim += linha[1]

        if linha[0] == "up":
            aim -= linha[1]

        if linha[0] == "forward":
            horizontal.append(linha[1])
            profundidade.append(linha[1] * aim)

    resultado = soma_multiplicacao(horizontal, profundidade)

    print("PARTE 2: \n"
          f"A multiplicação entre as posições finais horizontal e de profundidade retorna um valor de {resultado}.\n")


# -----------------------------------------------------------------------------------------------------------

dados = []

profundidade_parte_1 = []
horizontal_parte_1 = []

profundidade_parte_2 = []
horizontal_parte_2 = []
aim = 0

with open("posicao.csv") as arquivo:
    for linha in arquivo:
        comando, valor = linha.split()  # separa cada linha do arquivo em uma tupla, mas transforma em string
        valor = int(valor)  # transforma a variavel valor de cada tupla em inteiro
        dados.append((comando, valor))

parte_1(dados, horizontal_parte_1, profundidade_parte_1)
parte_2(dados, horizontal_parte_2, profundidade_parte_2, aim)



