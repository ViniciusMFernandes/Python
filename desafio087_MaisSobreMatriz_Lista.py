matriz = [[], [], [], [], [], [], [], [], []]
i = v = soma = coluna3 = maior = 0
for c in range(0, 9):
    n = (int(input(f'Digite um valor para {[v]}{[i]}: ')))
    if n % 2 == 0:
        soma += n
    if c == 2 or c == 5 or c == 8:
        coluna3 += n
    if c == 3:
        maior = n
    elif c == 4 or c == 5:
        if n > maior:
            maior = n
    matriz[c].append(n)
    i += 1
    if i == 3:
        i = 0
        v += 1
print('-='*30)
for m in range(0, 3):
    print(matriz[m], end='')
print()
for m in range(3, 6):
    print(matriz[m], end='')
print()
for m in range(6, 9):
    print(matriz[m], end='')
print()
print('-='*30)
print(f'Soma dos valores pares: {soma}')
print(f'Soma dos valores da 3ª coluna: {coluna3}')
print(f'Maior valor da 2ª linha: {maior}')
