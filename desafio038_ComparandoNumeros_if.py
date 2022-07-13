n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
maior = n1
menor = n1
if n1 == n2:
    print('Valores Iguais')
elif maior < n2:
    maior = n2
    print('Valores digitados {} e {}.\nMaior número é {} \nMenor número é {}'.format(n1, n2, maior, menor))
elif menor > n2:
    menor = n2
    print('Valores digitados {} e {}.\nMaior número é {} \nMenor número é {}'.format(n1, n2, maior, menor))

