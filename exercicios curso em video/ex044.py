preço = float(input('Qual o valor do produto ?'))
print('')

pagamento = int(input('''Selecione a forma de pagamento:
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] mais parcelas no cartão com juros

forma escolhida: '''))

if pagamento == 1:
    ajuste = (preço / 100) * 10
    print('O valor a pagar será R$ {:.2f}'.format(preço - ajuste))
elif pagamento == 2:
    ajuste = (preço / 100) * 5
    print('O valor a pagar será R$ {:.2f}'.format(preço - ajuste))
elif pagamento == 3:
    print('O valor a pagar será R$ {:.2f} em duas parcelas de R$ {:.2f}'.format(preço, preço/2))
elif pagamento == 4:
    p = int(input('Quantas parcelas ? '))
    ajuste = (preço/100) * 20
    print('O valor a pagar será R$ {:.2f} em {} parcelas de R$ {:.2f}'.format(preço + ajuste, p, (preço + ajuste) / p))
else:
    print('Opção inválida')
