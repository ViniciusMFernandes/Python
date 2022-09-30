print('\033[30;45m ESTATISTICAS DE PRODUTOS \033[m')
print('-'*20)
print('{:^20}'.format('LOJA'))
print('-'*20)
menorpreco = total = maiormil = 0
menornome = ''
while True:
    continuar = 'T'
    produto = str(input('Nome do Produto: ')).title()
    preco = float(input('R$'))
    if menorpreco == 0 or preco <= menorpreco:
        menorpreco = preco
        menornome = produto
    if preco > 1000:
        maiormil += 1
    total += preco
    while continuar not in 'NS':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('\n')
print('-'*20, 'FIM DO PROGRAMA', '-'*20)
print(f'Total da compra R${total:.2f}')
if maiormil > 1:
    print(f'Temos {maiormil} produtos custando mais de R$1.000')
else:
    print(f'Temos {maiormil} produto custando mais de R$1.000')
print(f'O produto mais barato foi {menornome} que custa R${menorpreco:.2f}')

