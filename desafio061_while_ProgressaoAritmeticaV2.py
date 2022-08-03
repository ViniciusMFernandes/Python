print('-'*10, '\033[30;47m PROGRESSÃO ARITMÉTICA WHILE \033[m', '-'*10)
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = 10
while decimo != 0:
    print('{}'.format(primeirotermo), end=' -> ')
    primeirotermo += razao
    decimo -= 1
print('ABACOU')