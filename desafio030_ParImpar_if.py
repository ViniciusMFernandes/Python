n = int(input('Digite um número: '))
r = n % 2
if r == 0:
    print('Você digitou {}. Esse é um número par!'.format(n))
else:
    print('Você digitou {}. Esse número é ímpar!'.format(n))
