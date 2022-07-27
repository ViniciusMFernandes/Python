maioridade = f = media = 0
nomemaioridade = ''
for c in range(0, 4, 1):
    print('---------- {}º PESSOA ---------'.format(c + 1))
    nome = str(input('Nome: ')).capitalize().strip()
    idade = int(input('Idade: '))
    media += idade
    sexo = str(input('Sexc (M / F): ').upper().strip())
    if sexo == 'M':
        if idade > maioridade:
            maioridade = idade
            nomemaioridade = nome
    elif sexo == 'F':
       if idade < 20:
        f += 1

print('\nMédia de idade do grupo: {:.1f} anos'.format(media / 4))
print('Homem mais velho: {} com {} anos'.format(nomemaioridade, maioridade))
print('Mulheres abaixo de 20 anos: {}'.format(f))


