from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
for j, v in jogadores.items():
    if v == 0:
        v = randint(1, 6)
    print(f'O {j} tirou {v}')
    sleep(0.5)
ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, T in enumerate(ranking):
    print(f'O {i+1}º lugar foi {T[0]} com {T[1]}')
print('FIM')








