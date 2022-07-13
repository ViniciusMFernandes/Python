import datetime
date = datetime.datetime.now()
anoatual = int(date.strftime('%Y'))
print('*'*20)
print('\033[30;42m CÁLCULO ALISTAMENTO MILITAR \033[m')
print('*'*20)
anonascimento = int(input('Qual seu ano de nascimento? '))
idade = (anoatual - anonascimento)
falta = 18 - idade
passa = idade - 18

if idade == 18:
    print('Você já tem 18 anos, Precisa realizar seu alistamento militar imediatamente!')
elif idade < 18:
    print('Você tem {} anos.\nFalta {} anos para seu alistamento militar\nSeu alistamento será em {} !'.format(idade, falta, anoatual + falta))


elif idade > 18:
    print('Você tem {} anos \nSeu alistamento militar deveria ter sido feito há {} ano(s) atrás\nSeu alistamento foi '
          'em {}'.format(idade, passa, anoatual - passa))
