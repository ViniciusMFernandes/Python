print('\033[30;46m TABUADA V3.0 \033[m')
print('-'*40)
r = 0
while True:
    n = int(input('DESEJA VER A TABUADA DE QUAL NÚMERO? '))
    if n < 0:
        break
    print('-' * 40)
    i = 1
    while i != 11:
        r = n * i
        print(f'{n} X {i} = {r}')
        i += 1
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')

