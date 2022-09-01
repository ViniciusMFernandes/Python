from random import randint
print('\033[30;45m JOGO PAR OU ÍMPAR \033[m')
computador = randint(0, 10)

n = total = i = 0
print('=-'*15)
print('VAMOS JOGAR \033[30;45m PAR \033[m OU \033[30;46m ÍMPAR \033[m')
print('=-'*15)
while True:
    n = int(input('Digite um valor: '))
    escolha = 'a'
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]')).strip()[0].upper()
    total = n + computador
    print(f'Jogador: {n}\nComputador: {computador}')
    print(f'Total: {total}')
    print('\nJogador pediu:', 'PAR' if escolha == 'P' else 'ÍMPAR')
    print('Resultado: ', 'PAR' if total % 2 == 0 else 'ÍMPAR')
    if total % 2 == 1 and escolha == 'I':
        print('\033[30;46m Ímpar \033[m. Você \033[30;42m Venceu ! \033[m')
        i += 1
    elif total % 2 == 0 and escolha == 'P':
        print('\n\033[30;45m Par \033[m. Você \033[30;42m Venceu ! \033[m')
        i += 1
    else:
        print('\nVocê \033[30;41m Perdeu \033[m')
        break
if i == 1:
    print(f'GAME OVER! Você venceu {i} vez')
elif i == 0:
    print(f'GAME OVER! Você não venceu nenhuma vez')
else:
    print(f'GAME OVER! Você venceu {i} vezes')
