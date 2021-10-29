n = int(input('Número: '))
divisões = 0

for tries in range(1, n+1):
    if n % tries == 0:
        print(f'\033[32m{tries}\033[m', end=' ')
        divisões += 1
    else:
        print(f'\033[31m{tries}\033[m', end=' ')

print('')

if divisões == 2:
    print('é primo')
else:
    print('não é primo')
