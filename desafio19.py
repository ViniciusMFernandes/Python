import random
n1 = input('Digite o 1º aluno: ')
n2 = input('Digite o 2º aluno: ')
n3 = input('Digite o 3º aluno: ')
n4 = input('Digite o 4º aluno: ')
lista = [n1, n2, n2, n4]
escolhido = random.choice(lista)
print('\n')
print('*'*10)
print('O aluno escolhido foi {}'.format(escolhido))




