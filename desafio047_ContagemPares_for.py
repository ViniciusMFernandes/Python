from time import sleep
print('{:*^40}'.format(' NÚMEROS PARES DE 0 A 50: '))
sleep(1)
for c in range(2, 51):
    if c % 2 == 0:
        print(c, end=' ')

