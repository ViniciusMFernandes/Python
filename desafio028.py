import random
from time import sleep
computador = int(random.randint(1, 5))
print('*'*10, 'Adivinhe o número: ', '*'*10)
usuario = int(input('Tente adivinhar o número que o computador pensou de 1 a 5: '))
print('PROCESSANDO...')
sleep(2)
if usuario == computador:
    print('Parabéns! Você acertou!')
    print('Computador pensou em {}\nVocê digitou {}'.format(computador, usuario))
else:
    print('Você Errou!')
    print('Computador pensou em {}\nVocê digitou {}'.format(computador, usuario))
