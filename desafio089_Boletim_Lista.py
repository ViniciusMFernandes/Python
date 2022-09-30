lista = []
m = 0
while True:
    nome = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    m = (n1 + n2)/2
    lista.append([nome, [n1, n2], m])
    continuar = str(input('Deseja continuar? [S/N]')).upper()[0]
    if continuar in 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
