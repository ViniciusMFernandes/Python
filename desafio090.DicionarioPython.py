aluno = {'Nome': 'Vinicus', 'Média': 7, 'Situação': 'Reprovado'}
aluno['Nome'] = str(input('Nome do aluno: ').capitalize())
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print()
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Média'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
print('FIM')



