print('*'*10, 'Tabela Conversão', '*'*10)
n = float(input('Digite um número em metros a ser convertido: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n * 10
cm = n * 100
mm = n * 1000
print('\n')
print('*'*10, 'Tabela Conversão', '*'*10)
print('{}m corresponde a:\n{:.3f}km\n{:.3f}hm\n{}dam\n{}dm\n{:.0f}cm\n{:.0f}mm'.format(n, km, hm, dam, dm, cm, mm))


