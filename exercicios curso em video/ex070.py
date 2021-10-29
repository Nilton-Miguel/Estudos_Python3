total = totmil = menor = barato = 0

while True:
    nome = input('Produto: ')
    preço = float(input('Valor: '))
    total += preço
    if menor == 0 or preço < menor:
        menor = preço
        barato = nome

    if preço > 1000:
        totmil += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('continuar? ').strip().upper()
    if resposta == 'N':
        break
    print()

print()
print(f'foram gastos R${total:.2f}')
print(f'o mais barato foi {barato} e custou R${menor:.2f}')
print(f'{totmil} produtos custaram mais de R$ 1000,00')
