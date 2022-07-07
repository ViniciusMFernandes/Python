velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('{:.2f}km/h Velocidade da via excedida, você foi multado !\nTotal da multa R${:.2f}'.format(velocidade,
                                                                                                  multa))
else:
    print('Sua velocidade está correta. {:.2f}km/h'.format(velocidade))
