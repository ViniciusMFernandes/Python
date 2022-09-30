matriz = [[], [], [], [], [], [], [], [], []]
i = v = 0
for c in range(0, 9):
    matriz[c].append(int(input(f'Digite um valor para {[v]}{[i]}: ')))
    i += 1
    if i == 3:
        i = 0
        v += 1
for m in range(0, 3):
    print(matriz[m], end='')
print()
for m in range(3, 6):
    print(matriz[m], end='')
print()
for m in range(6, 9):
    print(matriz[m], end='')

