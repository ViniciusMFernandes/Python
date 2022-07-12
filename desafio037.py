n = int(input('Digite um número qualquer: '))
escolha = int(input(('Escolha qual opção deseja\n1-Binário\n2-Octa\n3-Hexa\n')))
if escolha == 1:
    print('Número {} em BINÁRIO {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('Número {} em Octal {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('Número {} em Hexa {}'.format(n, hex(n)[2:]))
else:
    print('Opção Inválida!')
