from random import randint
from time import sleep
lista = list()


def sortear():
    print('Sorteando 5 valores da lista: ')
    while len(lista) != 5:
        num = randint(1, 10)
        if num not in lista:
            print(num, end=' ')
            sleep(0.5)
            lista.append(num)
    print('Pronto !')


def somar():
    soma = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'Somando os valores pares de {lista}, temos {soma}')


sortear()
somar()
print('FIM')
