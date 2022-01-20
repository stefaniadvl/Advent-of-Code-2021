#                   --------------- ADVENT OF CODE --- DAY 1 ---------------------

#  As the submarine drops below the surface of the ocean, it automatically performs a sonar
#  sweep of the nearby sea floor. On a small screen, the sonar sweep report (your puzzle input)
#  appears: each line is a measurement of the sea floor depth as the sweep looks further and further
#  away from the submarine.

#  The first order of business is to figure out how quickly the depth increases, just so you know what
#  you're dealing with - you never know if the keys will get carried into deeper water by an ocean current'
#  or a fish or something.

# PARTE 1:

#  To do this, count the number of times a depth measurement increases from the previous measurement.
#  (There is no measurement before the first measurement.)

# PARTE 2:

# Your goal now is to count the number of times the sum of measurements in this sliding window increases
# from the previous sum.

def parte_1(profundidade):
    aumenta = 0
    for i in range(1, len(profundidade)):
        # começa do 1 porque não existe medida antes da primeira, então não há como comparar
        if profundidade[i] > profundidade[i - 1]:
            aumenta += 1

    print("PARTE 1:\n"
          f"O número de vezes que a profundidade aumenta em relação à medida anterior é {aumenta}.\n")


def parte_2(profundidade):
    aumenta_soma = 0
    soma_3 = []

    for j in range(2, len(profundidade)):
        soma = profundidade[j] + profundidade[j - 1] + profundidade[j - 2]
        soma_3.append(soma)

    for k in range(1, len(soma_3)):
        if soma_3[k] > soma_3[k - 1]:
            aumenta_soma += 1

    print("PARTE 2:\n"
          "O número de vezes em que a soma de 3 profundidades é maior que a soma anterior é {}.".format(aumenta_soma))

# -------------------------------------------------------------------------------------------

profundidade = []

with open("profundidade.csv") as arquivo:
    for linha in arquivo:
        linha = int(linha)
        profundidade.append(linha)

parte_1(profundidade)
parte_2(profundidade)



