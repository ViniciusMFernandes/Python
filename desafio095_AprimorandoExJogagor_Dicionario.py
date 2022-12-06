jogador = dict()
jdict = dict()
partidaslista = list()
partidaslista2 = list()
jogadorlista = list()
total = cod = dados = 0
l = 0
d = 0
while True:
    jogador['Codigo'] = cod
    jogador['Nome'] = str(input('Nome do jogador: ').capitalize())
    partidas = int(input(f'Quantas partidadas {jogador["Nome"]} jogou? '))
    for c in range(partidas):
        p = int(input(f'Quantos gols na partida {c+1}? '))
        total += p
        partidaslista.append(p)
        jogador['Gols'] = partidaslista.copy()
        jdict['Partidas'] = c + 1
        jdict['Gols'] = partidaslista2.copy()

    partidaslista.clear()
    jogador['Total'] = total
    jogadorlista.append(jogador.copy())
    p = total = 0
    cod += 1
    continuar = str(input('Quer continuar? [S/N] ').upper()[0])
    if continuar in 'N':
        break
print('-='*20)
print(jdict)
print()
print(jogadorlista)
print()
print(len(jogadorlista))
print(f'{"COD":<4}{"Nome":<10}{"Gols"}{"Total":^25}')
while l != len(jogadorlista):
    print(f'{jogadorlista[l]["Codigo"]:<4}', end='')
    print(f'{jogadorlista[l]["Nome"]:<10}', end='')
    print(f'{jogadorlista[l]["Gols"]}', end='')
    print(f'{jogadorlista[l]["Total"]:^20}')
    l += 1
print('-='*20)
while True:
    dados = int(input('Mostrar dados de qual jogador ? [999 p/ SAIR] '))
    print(f'Levantamento do jogador {jogadorlista[dados]["Nome"]}')
    print(jogadorlista[dados])
    print(jogadorlista[dados]["Gols"])
print('FIM')
    '''for i, pa in enumerate(jogadorlista[dados].items()):
        print(f'==> Na partida {i + 1}, fez {pa[dados]} gols')'''


'''for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
for i, pa in enumerate(partidaslista):
    if pa == 1:
        print(f'==> Na partida {i+1}, fez {pa} gol ')
    else:
        print(f'==> Na partida {i + 1}, fez {pa} gols')
if total == 1:
    print(f'Foi um total de {total} gol')
else:
    print(f'Foi um total de {total} gols')'''