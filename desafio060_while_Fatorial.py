import math
print('-'*10, '\033[30;47m NÚMERO FATORIAL \033[m', '-'*10)
n = int(input('Digite um número: '))
w = 2
fatorial = n
print('Calculando {}! '.format(n), end='')
print('\n')
while w != 1:
    w = n
    n -= 1
    print('{}'.format(w), end='')
    print(' x ' if n > 0 else ' = ', end='')
fatorial = math.factorial(fatorial)
print(fatorial, end='')
print('\n')




