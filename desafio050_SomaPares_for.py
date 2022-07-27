print('{:-^40}'.format(' SOMA NÚMEROS PARES '))
print('Digite 6 números inteiros')
ni = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite {}º número: '.format(c + 1)))
    s = n % 2
    if s == 0:
        ni += n
        cont += 1
print('\nSoma entre {} números pares digitados: {}'.format(cont, ni))
