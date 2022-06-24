a = input('Digite algo: ')
print('O tipo primitivo é: ', type(a))
print('Só tem espaços? {}\n''É um número? {}\n''É alfabetico? {}\n''É alfanumérico? {}\n''Está em maiúscula? {}\n'
      'Está em minúscula? {}\n''Está capitalizada? {} '.format(a.isspace(), a.isnumeric(), a.isalpha(), a.isalnum(),
                                                            a.islower(), a.isupper(), a.istitle()))


