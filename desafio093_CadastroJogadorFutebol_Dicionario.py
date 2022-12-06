jogador = dict()
partidaslista = list()
total = 0
jogador['Nome'] = str(input('Nome do jogador: ').capitalize())
partidas = int(input(f'Quantas partidadas {jogador["Nome"]} jogou? '))
for c in range(partidas):
    p = int(input(f'Quantos gols na partida {c+1}? '))
    total += p
    partidaslista.append(p)
jogador['Gols'] = partidaslista
jogador['Total'] = total
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for i, pa in enumerate(partidaslista):
    if pa == 1:
        print(f'==> Na partida {i+1}, fez {pa} gol ')
    else:
        print(f'==> Na partida {i + 1}, fez {pa} gols')
if total == 1:
    print(f'Foi um total de {total} gol')
else:
    print(f'Foi um total de {total} gols')
print('FIM')



