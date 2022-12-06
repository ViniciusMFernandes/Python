from time import sleep


def linhas():
    print('-='*20)


def contadorUp():
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')
    linhas()


def contadorDown():
    print('Contagem de 10 até 0 de 2 em 2')
    for d in range(10, -2, -2):
        print(d, end=' ', flush=True)
        sleep(0.5)
    print('FIM')
    linhas()


def contadorUsuario():
    print('Agora é a sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for u in range(i, f, p):
            print(u, end=' ')
            sleep(0.2)
        print('FIM')
    else:
        for u in range(i, f, -p):
            print(u, end=' ')
            sleep(0.2)
        print('FIM')
    linhas()


linhas()
contadorUp()
contadorDown()
contadorUsuario()
print('FIM')

