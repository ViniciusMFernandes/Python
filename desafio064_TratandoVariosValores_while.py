print('-'*10, '\033[30;43m TRATANDO VÁRIOS DADOS \033[m', '-'*10)
n = soma = cont = 0
print('999 para SAIR')
n = int(input('Digite um número inteiro: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro: '))
print('Você digitou {} números e a soma dos número digitados: {}'.format(cont, soma))
