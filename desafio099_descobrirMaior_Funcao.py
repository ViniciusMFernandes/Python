from time import sleep


def maior(* num):
    cont = maior = 0
    print('Analisando os números:')
    for valor in num:
        if maior == 0:
            maior = valor
        if valor > maior:
            maior = valor
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        cont += 1
    print(f'\nForam informados {cont} números')
    print(f'Maior número é {maior}')
    sleep(0.5)
    print('_-' * 15)


maior(4, 3, 5, 1, 8, 5)
maior(9, 4, 5, 7)
maior(2, 7, 5)
maior(4, 6)
maior(5)
maior()
print('FIM')

