print('*-'*20)
print('\033[30;44m CÁLCULO IMC \033[m')
peso = float(input('Digite seu peso em KG: '))
alt = float(input('Digite sua altura em m: '))
IMC = peso / (alt**2)
print('{:.2f}'.format(IMC))
if IMC <= 18.5:
    print('\033[30;41m Abaixo do peso ! \033[m')
elif 18.5 < IMC <= 25:
    print('\033[30;42m Peso ideal \033[m')
elif 25 < IMC <= 30:
    print('\033[30;43m Sobrepeso \033[m')
elif 30 < IMC <= 40:
    print('\033[30;45m Obesidade \033[m')
else:
    print('\033[30;46m Obesidade Mórbida \033[m')
