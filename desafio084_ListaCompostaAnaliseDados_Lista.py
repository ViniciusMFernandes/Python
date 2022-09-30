lista = list()
temp = list()
menor = maior = 0
while True:
    temp.append(str(input('Nome: ')).capitalize())
    temp.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
           maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    lista.append(temp[:])
    temp.clear()
    continuar = str(input('Quer continuar ? [S/N]')).upper()[0]
    if continuar in 'N':
        break
print(f'Você cadastrou {len(lista)}')
print(f'Maior peso registrado: {maior}. Peso de ', end='')
for l in lista:
    if l[1] == maior:
        print(f'[{l[0]}]', end='')
print()
print(f'\nMenor peso registrado: {menor}. Peso de ', end=' ')
for l in lista:
    if l[1] == menor:
        print(f'[{l[0]}]', end=' ')





