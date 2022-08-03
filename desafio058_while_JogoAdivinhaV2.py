from random import randint
computador = randint(0, 10)
usuario = -1
i = 0
print('---------- \033[30;44m JOGO DA ADIVINHA V2.0 \033[m----------')
while usuario != computador:
    usuario = int(input('Digite um número entre 0 e 10: '))
    if -1 < usuario > 10:
        print('Opção Errada. Tente novamente')
    elif usuario != computador:
        print('\033[30;41m Errou. Tente novamente \033[m')
        i += 1
print('\n\033[30;42m Você Venceu \033[m !!')
print('\nComputador {}\nUsuário {}'.format(computador, usuario))
print('\nForam necessárias \033[30;43m {} \033[m vezes para vencer esse jogo.'.format(i))

