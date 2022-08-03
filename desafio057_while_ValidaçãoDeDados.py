r = 's'
while r not in 'MF':
    r = str(input('Digite seu sexo [M/F]: ')).upper()
    if r not in 'MF':
        print('Opção Errada. Tente Novamente')
    if r in 'MF':
        print('\nOpção escolhida {}'.format(r))
print('FIM')
