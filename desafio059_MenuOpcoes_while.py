opcao = 0
sair = ''
n1 = int(input('DIGITE 1º NÚMERO: '))
n2 = int(input('DIGITE 2º NÚMERO: '))
while opcao != 5:
    print('\n', '-' * 10, 'MENU OPÇÕES', '-' * 10)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR')
    print('-' * 35)
    opcao = int(input('ESCOLHA UMA OPÇÃO: '))
    if opcao > 5:
        print('Opção Inválida. Tente novamente!')
    if opcao == 1:
        soma = n1 + n2
        print('\n\033[30;46m [ 1 ] SOMAR \033[m')
        print('{} + {} = {}'.format(n1, n2, soma))
    if opcao == 2:
        mult = n1 * n2
        print('\n\033[30;46m [ 2 ] MULTIPLICAR \033[m')
        print('{} x {} = {}'.format(n1, n2, mult))
    if opcao == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('\n\033[30;46m [ 3 ] MAIOR \033[m')
        print('Valores Digitados {} e {}'.format(n1, n2))
        print('MAIOR NÚMERO {}'.format(maior))
    if opcao == 4:
        print('\n\033[30;46m [ 4 ] NOVOS NÚMEROS \033[m')
        n1 = int(input('DIGITE 1º NÚMERO: '))
        n2 = int(input('DIGITE 2º NÚMERO: '))
    if opcao == 5:
        print('\n\033[30;46m [ 5 ] SAIR \033[m')
        print('ATÉ BREVE')






