print('{:-^50}'.format('\033[30;42m PROGRESSÃO ARITMETICA FOR \033[m'))
primeirotermo = int(input('Digite o primeiro termo desejado: '))
razao = int(input('Digite a Razão desejado: '))
decimo = primeirotermo + (10 - 1) * razao
for c in range(primeirotermo, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
