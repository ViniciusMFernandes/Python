import random
from random import randint
print('{:^30}'.format('\033[30;45m Maior e Menor Valores em Tupla \033[m'))
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Eu sortiei os valores {tupla}')
print(f'Maior número sorteado: {max(tupla)}')
print(f'Menor número sorteado: {min(tupla)}')



