n = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
     'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
usuario = int(input('Digite um número entre 0 e 20: '))
while True:
        while usuario > 20 or usuario < 0:
            usuario = int(input('Digite um número entre 0 e 20: '))
        break
print(f'\nVocê digitou o número {n[usuario]}')
print('Fim')