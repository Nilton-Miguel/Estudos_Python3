p = 1
while p == 1:

    nA = float(input('Primeira nota: '))
    nB = float(input('Segunda nota: '))
    m = (nA + nB) / 2

    print(f'\033[36mmédia: {m:.1f}')

    if m > 7.0:
        print('\033[34mAprovado\033[m')
    elif 5.0 < m < 7.0:
        print('\033[33mRecuperação\033[m')
    else:
        print('\033[31mReprovado\033[m')
