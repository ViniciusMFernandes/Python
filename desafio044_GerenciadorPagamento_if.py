print('{:-^40}'.format('\033[30;45m EXERCÍCIO LOJA \033[m'))
valor = float(input('Digite o Valor do Produto R$'))
pagamento = int(input(
    'Digite a forma de pagamento: \n1- À VISTA (Dinheiro ou Cheque)\n2- À VISTA (Cartão)\n3- 2x (Cartão)\n4- 3x ou '
    'mais (Até 10x)'))
print('\nOpção escolhida {}'.format(pagamento))
print('Valor Inicial R${:.2f}'.format(valor))
if pagamento == 1:
    print('Pagamento À Vista (Dinheiro ou Cheque) 10% de Desconto \nR${:.2f}'.format(valor - (valor * 0.1)))
elif pagamento == 2:
    print('Pagamento À Vista (Cartão) 5% de Desconto \nR${:.2f}'.format(valor - (valor * 0.05)))
elif pagamento == 3:
    print('Pagamento 2x (Cartão) \n2x R${:.2f}'.format(valor / 2))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas (Até 10x)?'))
    print('\nNovo valor R${:.2f}'.format(valor + (valor * 0.2)))
    print('Pagamento 3x ou mais (Cartão) \n{}x R${:.2f}'.format(parcela, (valor + (valor * 0.2)) / parcela))
else:
    print('Opção Inválida!')
