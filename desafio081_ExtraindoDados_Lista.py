lista = []
continuar = ' '
i = 0
while continuar not in 'N':
    lista.append(int(input('Digite um valor: ')))
    i += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ').upper()[0])
print('-='*20)
lista.sort(reverse=True)
if i == 1:
    print(f'Você digitou {i} elemento na lista')
else:
    print(f'Você digitou {i} elementos na lista')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')




