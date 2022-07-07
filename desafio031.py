distancia = float(input('Digite a distância, em KM, que deseja percorrer: '))
if distancia <= 200:
    print('Valor digitado: {:.1f}KM'.format(distancia))
    print('R${:.2f}'.format(distancia * 0.5))
else:
    print('Valor digitado {}KM'.format(distancia))
    print('R${:.2f}'.format(distancia * 0.45))


