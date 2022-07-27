maior = 0
menor = 0
for c in range(0, 5, 1):
    peso = float(input('Digite {}º peso (kg): '.format(c + 1)))
    if menor == 0:
        menor = peso
    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso
print('\nMaior peso digitado: {}'.format(maior))
print('Menor peso digitado: {} '.format(menor))
