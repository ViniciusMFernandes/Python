salario = float(input('Digite seu salário atual R$'))
if salario <= 1250:
    print('Salário atual: R${:.2f}\nCom aumento de 15% R${:.2f}'.format(salario, salario + (salario * 0.15)))
else:
    print('Salario atual R${:.2f}\nCom aumento de 10% R${:.2f}'.format(salario, salario + (salario * 0.10)))
