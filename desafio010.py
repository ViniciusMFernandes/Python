dinheiro = float(input('Digite o valor em R$'))
dolar2016 = float(3.17)
dolar2022 = float(5.21)
d1 = (dinheiro / dolar2016)
d2 = (dinheiro / dolar2022)
print('R$ => $')
print('Em 2016 R${} compraria ${}'.format(dinheiro, d1))
print('Em 2022 R${} compra ${}'.format(dinheiro, d2))
print('-'*10)




