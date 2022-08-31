print('\033[30;47m SIMULADOR CAIXA ELETRÔNICO \033[m')
print('='*10, 'Simulador Banco', '='*10)
valor = int(input('Qual valor você quer sacar? R$'))
nota50 = 50
nota20 = 20
nota10 = 10
nota1 = 1
resultado50 = resultado20 = resultado10 = resultado1 = resto50 = resto20 = resto10 = resto1 = 0
#Calculando resto da divisão NOTA 50
resto50 = valor % nota50
#Divisor inteiro NOTA 50
resultado50 = valor // nota50
#Divisor inteiro NOTA 20
resultado20 = resto50 // nota20
#Calculando resto da divisão NOTA 10
resto10 = resto50 % nota20
resultado10 = resto10 // nota10

resto1 = resto10 % nota10
resultado1 = resto1 // nota1

print('Notas de 50: {}'.format(resultado50))
print(f'Notas de 20: {resultado20}')
print(f'Notas de 10: {resultado10}')
print(f'Notas de 1: {resultado1}')
