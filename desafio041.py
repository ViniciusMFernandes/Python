from datetime import date
anoatual = date.today().year
print('\033[30;47m CONFEDERAÇÃO NACIONAL DE NATAÇÃO \033[m')
ano = int(input('DIGITE O ANO DE NASCIMENTO DO ATLETA: '))
idade = anoatual - ano
print('IDADE: {} anos'.format(idade))
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
