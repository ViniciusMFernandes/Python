from random import choice
from time import sleep

lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)

print('{:-^40}'.format(' JOKENPÔ '))

usuario = int(input('Escolha uma opção:\n[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\n'))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.5)
print('\nComputador: {}'.format(computador))
if usuario == 1:
    print('Usuário: PEDRA')
    if computador == 'TESOURA':
        print('PARABÉNS, Você \033[30;42m VENCEU! \033[m')
    elif computador == 'PAPEL':
        print('Você \033[30;41m PERDEU! \033[m')
    else:
        print('\033[30;43m EMPATE! \033[m')
elif usuario == 2:
    print('Usuário: PAPEL')
    if computador == 'TESOURA':
        print('Você \033[30;41m PERDEU! \033[m')
    elif computador == 'PEDRA':
        print('PARABÉNS, Você \033[30;42m Venceu! \033[m')
    else:
        print('\033[30;43m EMPATE! \033[m')
elif usuario == 3:
    print('Usuário: TESOURA')
    if computador == 'PEDRA':
        print('Você \033[30;41m Perdeu! \033[m')
    elif computador == 'PAPEL':
        print('PARABÉNS, Você \033[30;42m Venceu! \033[m')
    else:
        print('\033[30;43m EMPATE \033[m')
else:
    print('Opção Inválida')

