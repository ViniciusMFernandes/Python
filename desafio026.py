frase = 'meu nome agora e johnny'
print('Número de letras A na frase: ', frase.count('a'))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')))
dividido = frase.split()
quantidade = len(dividido)
print('A Última letra A aparece na posição {}'.format(dividido[quantidade - 1].find('a')))

