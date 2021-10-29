C = {'azul': '\033[1;36m', 'verde': '\033[1;32m'}
d = int(input('{}Digite a distância da viagem em Km: '.format(C['azul'])))

if d > 200:
    p = d*0.45
    print('{}Sua viagem custará {}R${:.2f}'.format(C['azul'], C['verde'], p))
else:
    p = d*0.5
    print('{}Sua viagem custará {}R${:.2f}'.format(C['azul'], C['verde'], p))
