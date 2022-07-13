n1 = float(input('1ª NOTA: '))
n2 = float(input('2ª NOTA: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[30;41m REPROVADO! \033[m \nMédia Final \033[30;41m {:.2f} \033[m'.format(media))
elif media == 5 or media <= 6.9:
    print('\033[30;43m Recuperação! \033[m \nMédia Final \033[30;43m {:.2f} \033[m'.format(media))
elif media >= 7:
    print('\033[30;42m APROVADO! \033[m \nMédia Final \033[30;42m {} \033[m'.format(media))
