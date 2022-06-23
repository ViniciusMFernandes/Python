a = input('Digite algo:')
print('O que você digitou é: \n'
      'Apenas letras? {}\n''Apenas números? {}\n''Apenas minusculas? {}\n'
      'Apenas maiusculas? {}\n''Alfanumerico? {}\n''Espaços? {}'.format(a.isalpha(), a.isnumeric(), a.islower(),
                                                                            a.isupper(), a.isalnum(), a.isspace()))
