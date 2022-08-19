print('-'*10, '\033[30;47m PROGRESSÃO ARITMÉTICA WHILE V3 \033[m', '-'*10)
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = 10
continuar = 1
while decimo != 0:
    print('{}'.format(primeirotermo), end=' -> ')
    primeirotermo += razao
    decimo -= 1
    while decimo == 0:
        if continuar == 0:
            break
        print('ACABOU!')
        while decimo == 0:
            print('\n [ 0 ] SAIR')
            print(' [ 1 ] MOSTRAR MAIS TERMOS')
            continuar = int(input('\n ESCOLHA UMA OPÇÃO: '))
            if continuar == 0:
                break
            elif continuar == 1:
                decimo = int(input('Quantidade de termos: '))
                print('{}'.format(primeirotermo), end=' -> ')
                primeirotermo += razao
                decimo -= 1
            else:
                print('Opção Inválida!')
print('\nFIM')





