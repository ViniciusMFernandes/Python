r1 = float(input('Digite 1ª reta: '))
r2 = float(input('Digite 2ª reta: '))
r3 = float(input('Digite 3ª reta: '))
if (r1 + r3) > r2 and (r2 + r3) > r1 and (r1 + r2) > r3:
    print('As retas conseguem formar um triângulo entre eles')
    if r1 == r2 == r3:
        print('Triângulo \033[30;41m Equilátero \033[m')
    elif (r1 == r2) or (r2 == r3) or (r1 == r3):
        print('Triângulo \033[30;42m Isósceles \033[m')
    else:
        print('Triângulo \033[30;43m Escaleno \033[m')
else:
    print('Não dá')
