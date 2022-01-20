# ------------------- ADVENT OF CODE 2021 - DAY 3 ------------------------------

# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report
# just in case.

# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded
# properly, can tell you many useful things about the conditions of the submarine. The first parameter to
# check is the power consumption.

# You need to use the binary numbers in the diagnostic report to generate two new binary numbers
# (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying
# the gamma rate by the epsilon rate.

# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding
# position of all numbers in the diagnostic report.

# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit
# from each position is used.

# PARTE 1:

# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then
# multiply them together. What is the power consumption of the submarine? (Be sure to represent your
# answer in decimal, not binary.)

def transforma_decimal(lista):

    lista_string = [str(k) for k in lista]   # transforma a lista em string
    numero_binario = "".join(lista_string)   # concatena as strings em uma unica string
    numero_decimal = int(numero_binario, 2)  # função int também transforma binário (tipo str) em decimal
                                             # o segundo argumento é a base do numero
    return numero_decimal

def parte_1():

    mais_comum = []
    menos_comum = []

    with open("numeros_binarios.csv") as arquivo:
        comprimento = len(arquivo.readline().strip())

        for i in range(0, comprimento):
            arquivo.seek(0)   # vai pro inicio do arquivo
            contador_0 = 0
            contador_1 = 0

            for linha in arquivo:
                elemento = int(linha[i])

                if elemento == 0:
                    contador_0 += 1
                else:
                    contador_1 += 1

            if contador_0 > contador_1:
                mais_comum.append(0)
                menos_comum.append(1)
            else:
                mais_comum.append(1)
                menos_comum.append(0)

        taxa_gama = transforma_decimal(mais_comum)
        taxa_epsilon = transforma_decimal(menos_comum)

        multiplicacao = taxa_gama * taxa_epsilon
        print(f"PARTE 1: \n"
              f"O consumo de energia do submarino é {multiplicacao}\n")

# PARTE 2:

# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator
# rating by the CO2 scrubber rating.

# Start with the full list of binary numbers from your diagnostic report and consider just the first bit
# of those numbers. Then:

# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching.
# Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.

# Oxygen generator rating is calculated by considering the most common bits and the CO2 scrubber rating by the
# least common bits

def oxigenio(comprimento, lista):

    for i in range(1, comprimento):
        if len(lista) == 1:
            break

        elemento_0 = []
        elemento_1 = []

        for numero in lista:
            elemento = int(numero[i])

            if elemento == 0:
                elemento_0.append(numero)
            else:
                elemento_1.append(numero)

        if len(elemento_0) > len(elemento_1):
            lista = elemento_0
        elif len(elemento_1) > len(elemento_0):
            lista = elemento_1
        elif len(elemento_0) == len(elemento_1):
            lista = elemento_1

    return lista


def gas_carb(comprimento, lista):

    for i in range(1, comprimento):
        if len(lista) == 1:
            break

        elemento_0 = []
        elemento_1 = []

        for numero in lista:
            elemento = int(numero[i])

            if elemento == 0:
                elemento_0.append(numero)
            else:
                elemento_1.append(numero)

        if len(elemento_0) < len(elemento_1):
            lista = elemento_0
        elif len(elemento_1) < len(elemento_0):
            lista = elemento_1
        elif len(elemento_0) == len(elemento_1):
            lista = elemento_0

    return lista

def parte_2():

    lista_0 = []
    lista_1 = []

    with open("numeros_binarios.csv") as arquivo:

        comprimento = len(arquivo.readline().strip())
        arquivo.seek(0)

        for linha in arquivo:
            elemento = int(linha[0])

            if elemento == 0:
                lista_0.append(linha.strip())
            else:
                lista_1.append(linha.strip())


    # as taxas de oxigenio e CO2 são separadas a partir do primeiro bit (linha[0])
    if len(lista_0) > len(lista_1):
        Ox = lista_0
        CO2 = lista_1
    else:
        Ox = lista_1
        CO2 = lista_0

    Ox = oxigenio(comprimento, Ox)
    CO2 = gas_carb(comprimento, CO2)

    Ox_decimal = transforma_decimal(Ox)
    CO2_decimal = transforma_decimal(CO2)

    multiplicacao = Ox_decimal * CO2_decimal

    print(f"PARTE 2: \n"
          f"A taxa de suporte à vida é {multiplicacao}\n")

parte_1()
parte_2()