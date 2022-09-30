print('-'*40)
print('{:^50}'.format('\033[30;45m Lista de Preços \033[m'))
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*40)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}',end='')
    else:
        print(f'R${lista[c]:>5.2f}')
print('-'*40)