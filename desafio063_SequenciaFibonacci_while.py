print('-'*10, '\033[30;47m SEQUÊNCIA FIBONACCI \033[m', '-'*10)
fibo = 0
n = int(input('DIGITE UM NÚMERO INTEIRO: '))
i = 0
while fibo != n:
    print('{}'.format(i), end=' -> ')
    i += 1
    i = (i + 1) + (i + 2)
    fibo += 1




