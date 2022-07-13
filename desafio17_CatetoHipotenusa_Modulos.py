from math import hypot
catop = float(input('Digite o valor do Cateto Oposto: '))
catadj = float(input('Digite o valor do Cateto Adjacente: '))
'''hip = (catadj ** 2 + catop ** 2) ** (1/2)'''
hip = hypot(catop, catadj)
print('A hipotenusa será {:.2f}'.format(hip))

