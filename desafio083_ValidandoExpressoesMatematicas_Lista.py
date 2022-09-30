lista = []
abre = fecha = 0
lista.append(str(input('Digite uma expressão: ')))
abre = lista[0].count('(')
fecha = lista[0].count(')')
if abre != fecha:
    print('Expressão inválida')
else:
    print('Expressão válida')