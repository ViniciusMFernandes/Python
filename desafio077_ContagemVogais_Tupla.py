lista = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
          'trabalhar', 'mercado', 'programador', 'futuro')
for l in lista:
    print(f'\nNa palavra \033[30;45m{l}\033[m temos', end=' ')
    for letra in l:
        if letra in 'aeiou':
            print(letra, end=' ')






