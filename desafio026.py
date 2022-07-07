frase = str(input('Digite uma frase: ')).strip().upper()
print('Número de letras A na frase: ', frase.count('A'))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A Última letra A aparece na posição {}'.format(frase.rfind('A')+1))

