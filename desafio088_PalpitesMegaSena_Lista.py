from time import sleep
from random import randint
lista = []
numerosaleatorios = []
c = b = 0
print('-'*20)
print('Jogo Mega Sena')
print('-'*20)
n = int(input('Quantos jogos deseja sortear? '))
print('-'*20)
print('-'*20)
print('-='*5, f'SORTEANDO {n} JOGOS', '-='*5)
while c != n:
    for a in range(0, 6):
        b = randint(1, 60)
        if b not in numerosaleatorios:
            numerosaleatorios.append(b)
        else:
            b = randint(1, 60)
            numerosaleatorios.append(b)
    lista.append(numerosaleatorios[:])
    numerosaleatorios.clear()
    print(f'Jogo {c+1}: ', end='')
    print(sorted(lista[c]))
    sleep(0.7)
    c += 1
print('-='*7, 'BOA SORTE', '-='*7)
