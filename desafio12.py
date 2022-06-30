print('\n')
print('Liquidação da LOJA')
print('-'*5)
p = float(input('Digite o valor R$'))
desc = p - (p * 5/100)
print('R${:.2f} - 5% de desconto'.format(p))
print('O valor com 5% de desconto R${:.2f}'.format(desc))


