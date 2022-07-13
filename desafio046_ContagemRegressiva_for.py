from time import sleep
print('{:-^40}'.format(' CONTAGEM REGRESSIVA '))
for c in range(10, -1, -1):
    print('{}'.format(c))
    sleep(1)
print('\033[30;46m BOOOOM \033[m')
