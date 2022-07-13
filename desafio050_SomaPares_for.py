print('{:-^40}'.format(' SOMA NÚMEROS PARES '))
s = 0
for c in range(0, 7):
    n = int(input('Digite número').format(c + 1))
    if n % 2:
        s += c + 1
print(s)

