cadastrodict = dict()
cadastrolist = list()
mulheres = list()
total = media = resultadomedia = 0
maiorIdade = menorIdade = 0
while True:
    cadastrodict.clear()
    cadastrodict['Nome'] = str(input('Nome: ').capitalize())
    while True:
        cadastrodict['Sexo'] = str(input('Sexo: [M/F] ').upper()[0])
        if cadastrodict['Sexo'] in 'MF':
            break
        print('Erro. Por favor digite apenas M ou F.')
    if cadastrodict['Sexo'] in 'F':
        mulheres.append(cadastrodict.copy())
    cadastrodict['Idade'] = int(input('Idade: '))
    while True:
        continuar = str(input('Quer continuar? [S/N] ').upper()[0])
        if continuar in 'SN':
            break
        print('Erro. Por favor digite apenas S ou N.')
    cadastrolist.append(cadastrodict.copy())
    total += 1
    media += cadastrodict['Idade']
    resultadomedia = media/total
    if continuar in 'N':
        break
print('-='*20)
print(f'O grupo tem {total} pessoas')
print(f'A média de idade é de {resultadomedia:.2f} anos')
print(f'As mulheres cadastradas foram: ', end='')
for m in mulheres:
    print(m["Nome"], end=' ')
    print()
print('Lista de pessoas acima da média:', end='')
for c in cadastrolist:
    if c['Idade'] >= resultadomedia:
        print('     ', end='')
        for k, v in c.items():
            print(f'{k} = {v}', end=' ')
        print()
print('--- FIM ---')
print('FIM')



