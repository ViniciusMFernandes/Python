print('-'*10, '\033[30;44m MAIOR / MENOR VALOR \033[m', '-'*10)
maior = menor = n = u = media = soma = 0
i = 1
sair = 2
while sair != 0:
    n = int(input('Insira o {}º número: '.format(i)))
    maior = n
    if menor > maior:
        maior = n
    elif maior < menor:
        menor = n
    i += 1
    soma += n
    u += 1
    print('\n[ 0 ] SAIR\n[ 1 ] CONTINUAR')
    sair = int(input('Deseja Continuar ? '))
    media = soma / u
print('Menor número digitado: {}'.format(menor))
print('Maior número digitado: {}'.format(maior))
print('Média números digitados: {:.2}'.format(media))
