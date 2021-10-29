from time import sleep

termos = int(input('Quantos termos? ').strip())

n = 0
nA = 0
nB = 1

rodada = 0
while rodada < termos:
    if rodada == 0:
        print(f'\033[36m{nA}\033[m')
    elif rodada == 1:
        print(f'\033[36m{nB}\033[m')
    else:
        n = nA + nB
        print(f'\033[36m{n}\033[m é igual a \033[36m{nA}\033[m + \033[36m{nB}\033[m')
        nA = nB
        nB = n

    rodada += 1
    sleep(0.5)
