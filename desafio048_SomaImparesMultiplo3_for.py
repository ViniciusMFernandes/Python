s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('Números entre \033[30;43m 0 \033[m até \033[30;45m 500 \033[m')
print('Soma dos {} números multiplos de 3: {}'.format(cont, s))
