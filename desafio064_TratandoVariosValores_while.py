print('-'*10, '\033[30;43m TRATANDO VÁRIOS DADOS \033[m', '-'*10)
n = soma = 0
print('999 para SAIR')
while n != 999:
    soma += n
    if n == 999:
        break
    n = int(input('Digite um número inteiro: '))
print('Soma dos número digitados: {}'.format(soma))
