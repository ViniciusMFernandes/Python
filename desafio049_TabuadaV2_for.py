print('{:*^40}'.format(' TABUADA 2.0 '))
n = int(input('Tabuada do número: '))
for c in range(1, 11):
    s = n * c
    print('{}x{} = {}'.format(n, c, s))
print('FIM')

