from random import shuffle
n1 = str(input('Digite o 1º aluno: '))
n2 = str(input('Digite o 2º aluno: '))
n3 = str(input('Digite o 3º aluno: '))
n4 = str(input('Digite o 4º aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('Ordem de apresentação de alunos: ')
print(lista)







