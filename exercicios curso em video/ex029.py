v = float(input('Digite sua velocidade em Km/h: '))
c = (v-80)*7


if 80 >= v:
    print('Você está dentro do limite tolerado')
else:
    print('Você foi multado e deverá pagar R${}'.format(c))
