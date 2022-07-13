print('Cálculo de Tinta Necessária')
a = float(input('Digite a altura, em metros, da parede: '))
l = float(input('Digite a largura, em metros, da parede: '))
area = a * l
tinta = area / 2
print('A sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(a, l, area))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))

