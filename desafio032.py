ano = int(input('DIGITE UM ANO QUALQUER (EX:xxxx): '))
b = ano % 4
if b == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
