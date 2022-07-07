import random
computador = int(random.randint(1, 5))
print('*'*10, 'Adivinhe o número: ', '*'*10)
usuario = int(input('Tente adivinhar o número que o computador pensou de 1 a 5: '))
if usuario == computador:
    print('Parabéns! Você acertou!')
    print('Computador {}\nVocê {}'.format(computador, usuario))
else:
    print('Você Errou!')
    print('Computador {}\nVocê {}'.format(computador, usuario))
