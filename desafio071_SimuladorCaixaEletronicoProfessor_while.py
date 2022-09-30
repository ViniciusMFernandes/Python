print('-'*30)
print('{:^30}'.format('Simulador Caixa Eletrônico'))
print('-'*30)
qnt = total = 0
valor = int(input('Qual valor deseja sacar? R$'))
total = valor
ced = 50
qnt = 0
while True:
    if total >= ced:
        total -= ced
        qnt += 1
    else:
        if qnt > 0:
            print(f'Total de {qnt} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        qnt = 0
        if total == 0:
            break
print('-'*30)