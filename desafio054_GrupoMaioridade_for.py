from datetime import date
anoatual = date.today().year
i = 0
u = 0
for c in range(0, 7, 1):
    ano = int(input('Ano de Nascimento {}º aluno (XXXX): '.format(c + 1)))
    if anoatual - ano <= 21:
        i += 1
    else:
        u += 1
print('\n')
print('Alunos MENORES de 21 anos: \033[30;41m {} \033[m '.format(i))
print('\nAlunos MAIORES de 21 anos: \033[30;42m {} \033[m'.format(u))
