n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))
#número maior
if n1 > n2 and n1 > n3:
    print('Maior número dititado {}'.format(n1))
elif n2 > n1 and n2 > n3:
    print('Maior número dititado {}'.format(n2))
else:
    print('Maior número dititado {}'.format(n3))
#número menor
if n1 < n2 and n1 < n3:
    print('Menor número dititado {}'.format(n1))
elif n2 < n1 and n2 < n3:
    print('Menor número dititado {}'.format(n2))
else:
    print('Menor número digitado {}'.format(n3))

