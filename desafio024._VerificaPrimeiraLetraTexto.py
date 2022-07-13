cidade = str(input('Qual sua cidade? ')).strip().upper()
dividido = cidade.split()
print('\n')
print('A Cidade começa com Santo? ')
print('SANTO' in dividido[0])

