print('{:-^40}'.format('\033[30;47m NÚMERO PRIMO \033[m'))
n = int(input('Digite um número inteiro: '))
total = 0
print('VAMOS DESCOBRIR SE É UM NÚMERO PRIMO?')
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(n, total))
if total == 2:
    print('E por isso ele é \033[30;42m PRIMO \033[m')
else:
    print('E por isso ele \033[30;41m NÃO é PRIMO \033[m')



