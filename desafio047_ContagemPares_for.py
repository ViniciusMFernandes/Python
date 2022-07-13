from time import sleep
print('{:*^40}'.format(' NÚMEROS PARES DE 0 A 50: '))
sleep(1)
for c in range(0, 50):
    if c % 2:
        print(c + 1)

