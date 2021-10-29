p = 1
pt = 0
dr = 0
em = 0

while p == 1:
    from random import randint
    from time import sleep
    import emoji

    j = input(emoji.emojize('''[ 1 ] pedra :raised_fist:
[ 2 ]papel :raised_hand:
[ 3 ]tesoura :victory_hand:

sua opção: ''')).strip()

    while not (((('1' in j) or ('2' in j) or ('3' in j)) and j.isnumeric()) and len(j) == 1):
        j = input('digite uma opção válida: ').strip()
    j = int(j)

    sleep(0.5)
    print('')
    c = randint(1, 3)

    print('pedra'), sleep(0.5), print('papel'), sleep(0.5), print('tesoura'), sleep(0.5)

    if j == 1:
        jogadaj = 'pedra'
    elif j == 2:
        jogadaj = 'papel'
    elif j == 3:
        jogadaj = 'tesoura'

    if c == 1:
        jogadac = 'pedra'
    elif c == 2:
        jogadac = 'papel'
    elif c == 3:
        jogadac = 'tesoura'
    print('')

    if j == c:
        print(f'\033[36m{jogadaj} e {jogadac}, EMPATE \033[m')
        em = em + 1

    else:
        if j == 1 and c == 2:
            print(f'\033[31m{jogadaj} e {jogadac}, VOCÊ PERDEU\033[m')
            dr = dr + 1
        elif j == 1 and c == 3:
            print(f'\033[32m{jogadaj} e {jogadac}, VOCÊ VENCEU\033[m')
            pt = pt + 1
        elif j == 2 and c == 1:
            print(f'\033[32m{jogadaj} e {jogadac}, VOCÊ VENCEU\033[m')
            pt = pt + 1
        elif j == 2 and c == 3:
            print(f'\033[31m{jogadaj} e {jogadac}, VOCÊ PERDEU\033[m')
            dr = dr + 1
        elif j == 3 and c == 1:
            print(f'\033[31m{jogadaj} e {jogadac}, VOCÊ PERDEU\033[m')
            dr = dr + 1
        elif j == 3 and c == 2:
            print(f'\033[32m{jogadaj} e {jogadac}, VOCÊ VENCEU\033[m')
            pt = pt + 1

    print('')
    sleep(1)
    print(f'você tem {pt} vitórias, {dr} derrotas e {em} empates')
    sleep(1)
    print('\n'*4)
