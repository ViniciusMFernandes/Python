import math
print('-'*10, '\033[30;47m NÚMERO FATORIAL \033[m', '-'*10)
n = int(input('Digite um número: '))
w = 2
fatorial = n
print('{}!'.format(n), end='')
while w != 1:
    w = n
    n -= 1
    print('\n{}'.format(w), end='')
print('\n')
print('-'*20)
fatorial = math.factorial(fatorial)
print(fatorial)




