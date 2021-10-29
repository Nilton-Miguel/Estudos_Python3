C = {'limpa': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'azul': '\033[1;36m'}
n = float(input(('{}Digite um número natural qualquer: '.format(C['azul']))))

if n % 2 == 0:
    print('{} é um número {}PAR'.format(n, C['verde']))
else:
    print('{} é um número {}ÍMPAR'.format(n, C['vermelho']))

