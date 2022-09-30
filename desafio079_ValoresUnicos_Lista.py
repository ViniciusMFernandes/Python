lista = []
continuar = ' '
while continuar not in 'N':
    a = int(input('Digite um valor: '))
    if a in lista:
        print('Valor Duplicado. Valor não adicionado...')
    else:
        lista.append(a)
        print('Valor adicionado com sucesso...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]').upper()[0])
    if continuar == 'N':
        break
print('-='*20)
print(f'Você digitou os valores {sorted(lista)}')