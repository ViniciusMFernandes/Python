tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print('\n')
for a in tupla:
    print(a, end=' ')
print(f'\nO número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'\nO número 3 apareceu na posição {tupla.index(3)}')
else:
    print('\nO valor 3 não foi digitado em nenhuma posição')
print(f'\nOs valores pares foram', end=' ')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')
