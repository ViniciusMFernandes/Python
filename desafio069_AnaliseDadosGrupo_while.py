print('='*20, '\033[30;41m ANÁLISE DE DADOS DE GRUPO \033[m', '='*20)
print('-'*20)
print('CADASTRE UMA PESSOA')
print('-'*20)
i = masculino = feminino = 0
while True:
    continuar = 'M'
    idade = 0
    sexo = 'S'
    idade = int(input('Idade: '))
    if idade > 18:
        i += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()
        if sexo == 'M':
            masculino += 1
    if idade < 20 and sexo == 'F':
        feminino += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Pessoas com mais de 18 anos: {i}')
print(f'Homens cadastrados: {masculino}')
print(f'Mulheres com menos de 20 anos: {feminino}')