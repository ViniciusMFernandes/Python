print('{:*^40}'.format(' FRASE PALINDROMA '))
frase = str(input('Digite uma frase: ')).upper().strip()
separa = frase.split()
junto = ''.join(separa)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print('O inverso da palavra {} é {}'.format(junto, inverso, end=''))
if junto == inverso:
    print('PALINDROMA')
else:
    print('NÃO PALINDROMA')
