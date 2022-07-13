dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodado?'))
total = (dias * 60) + (km * (0.15))
print('O total a pagar R${:.2f}'.format(total))
