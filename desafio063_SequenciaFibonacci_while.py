print('-'*10, '\033[30;47m SEQUÊNCIA FIBONACCI \033[m', '-'*10)
n = int(input('DIGITE UM NÚMERO INTEIRO: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')




