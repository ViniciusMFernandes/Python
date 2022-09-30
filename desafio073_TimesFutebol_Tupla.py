tabela = ('Cruzeiro', 'Bahia', 'Vasco da Gama', 'Grêmio', 'Londrina', 'Sport Recife', 'Tombense', 'Ituano',
          'Criciúma', 'Ponte Preta', 'CRB', 'Sampaio Corrêa', 'Novorizontino', 'CSA', 'Chapecoense', 'Brusque', 'Vila Nova',
          'Operário', 'Guarani', 'Náutico')
print('{:^30}'.format('\033[30;44m Tabela Série B 2022 \033[m'))
print('-'*20)
print(f'Os cinco primeiros colocados: {tabela[0:5]}')
print('-'*20)
ultimo = len(tabela) - 1
print('Os quatro últimos times: ', end='')
for c in range(0, 4):
    print(tabela[ultimo], end=', ')
    ultimo -= 1
print('\n')
print('-' * 20)
print('Times em ordem alfabética: {}'.format(sorted(tabela)))
print('-'*20)
print('A Ponte Preta está na {}ª posição'.format(tabela.index('Ponte Preta')+1))

