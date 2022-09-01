soma = i = 0
print('\033[30;45m LEITURA DE VÁRIOS NÚMEROS COM PARADA EM FLAG \033[m')
while True:
    n = int(input('Digite um número [999 para SAIR]: '))
    if n == 999:
        break
    i += 1
    soma += n
print(f'\nNúmeros digitados: {i} \nSoma entre os números: {soma}')


