nome = str(input('Digite seu nome completo: ').strip())
print('LETRAS MAIUSCULAS: ', nome.upper())
print('letras minusculas: ', nome.lower())
print('Seu nome tem ao todo: {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('Número de letras do 1º nome: {}'.format(len(dividido[0])))


