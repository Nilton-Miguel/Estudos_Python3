valor = str(input('Valor para saque: ').strip())
last = valor[len(valor) - 1]
valor = int(valor)

if last == '1':
    valor += 1
    print(f'o valor precisou ser corrigido para R${valor},00 pois não há notas de R$ 1,00 disponíveis')
    print()

tot100 = tot50 = tot20 = tot10 = tot5 = tot2 = 0

while True:
    if valor // 100 > 0:
        tot100 += 1
        valor -= 100

    elif valor // 50 > 0:
        tot50 += 1
        valor -= 50

    elif valor // 20 > 0:
        tot20 += 1
        valor -= 20

    elif valor // 10 > 0:
        tot10 += 1
        valor -= 10

    elif valor // 5 > 0 and ((valor % 2) == 1):
        tot5 += 1
        valor -= 5

    elif valor // 2 > 0 and ((valor % 2) == 0):
        tot2 += 1
        valor -= 2
    else:
        break

if tot100 > 0:
    if tot100 == 1:
        A = 'nota'
    else:
        A = 'notas'
    print(f'{tot100} {A} de R$ 100,00')
if tot50 > 0:
    if tot50 == 1:
        A = 'nota'
    else:
        A = 'notas'
    print(f'{tot50} {A} de R$ 50,00')

if tot20 > 0:
    if tot20 == 1:
        A = 'nota'
    else:
        A = 'notas'
    print(f'{tot20} {A} de R$ 20,00')

if tot10 > 0:
    if tot10 == 1:
        A = 'nota'
    else:
        A = 'notas'
    print(f'{tot10} {A} de R$ 10,00')

if tot5 > 0:
    if tot5 == 1:
        A = 'nota'
    else:
        A = 'notas'
    print(f'{tot5} {A} de R$ 5,00')

if tot2 > 0:
    if tot2 == 1:
        A = 'nota'
    else:
        A = 'notas'
    print(f'{tot2} {A} de R$ 2,00')
print()
