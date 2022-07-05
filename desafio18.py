import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Ângulo {}\nSENO {:.2f}º\nCOSSENO {:.2f}\nTangente {:.2f}ª'.format(ang, sen, cos, tang))

