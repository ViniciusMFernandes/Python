print('-=-'*20)
print('\033[30;45mEmprestimo Bancário\033[m')
print('-=-'*20)
casa = float(input('Valor da Casa R$'))
salario = float(input('Salário R$'))
anos = int(input('Quantidade de anos para pagar ?'))
meses = anos * 12 #Calculo anos para meses
prestação = casa / meses
trinta = salario * 0.3
print('\n')
print('Salário R${:.2f}'.format(salario))
print('Tempo a pagar: {} anos ou {} meses'.format(anos, meses))
print('Prestação R${:.2f}'.format(prestação))
print('30% do salário R${:.2f}'.format(trinta))
if prestação >= trinta:
    print('Emprestimo \033[30;41mNEGADO\033[m')
    print('MOTIVO: Valor da parcela excede 30% do seu salário')
else:
    print('Emprestimo \033[30;42mAPROVADO\033[m')
