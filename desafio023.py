n = input('Digite um número entra 0 e 9999: ')

print('UNIDADE: ', n.strip()[3:4])
print('DEZENA: ', n.strip()[2:3])
print('CENTENA:', n.strip()[1:2])
print('MILHAR: ', n.strip()[:1])
