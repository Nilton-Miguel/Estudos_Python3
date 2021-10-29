n = int(input('Primeiro número: '))
r = int(input('Razão: '))
valor = n

for c in range(0, 10):
    print(valor, end=' -> ')
    valor += r
print('ACABOU')
