from datetime import date
trabalhador = dict()
atual = date.today().year
while True:
    trabalhador['Nome'] = str(input('Nome: ').capitalize())
    nascimento = int(input('Ano de nascimento: '))
    nascimento = atual - nascimento
    trabalhador['Ano'] = nascimento
    trabalhador['Carteira de Trabalho'] = int(input('Carteira de Trabalho (0 p/ não tem): '))
    if trabalhador['Carteira de Trabalho'] == 0:
        break
    trabalhador['Ano de Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salario'] = int(input('Salário: R$'))
    apostenta = nascimento + (35 - (atual - trabalhador['Ano de Contratação']))
    trabalhador['Aposentadoria'] = apostenta
    break
print('-='*20)
for t, v in trabalhador.items():
    print(f'{t} tem o valor de {v}')
print('FI')




