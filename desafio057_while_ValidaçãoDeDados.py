r = 's'
while r not in 'MF':
    r = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
    if r not in 'MF':
        print('Opção Errada. Tente Novamente')
print('\nOpção escolhida {}'.format(r))
print('FIM')
