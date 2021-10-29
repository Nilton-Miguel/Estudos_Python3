from random import randint
jogo = 0
while True:

    nj = int(input('Qual seu número? ').strip())
    j = input('Par ou ímpar [P/I]: ').strip().upper()
    if j == 'P':
        j = 1
    elif j == 'I':
        j = 2

    nc = randint(1, 10)
    resultado = (nc + nj) % 2

    if resultado == 0:
        jogo = 1
        """par"""
    elif resultado == 1:
        jogo = 2
        """ímpar"""
    if jogo == j:
        print(f'jogador: {nj} computador: {nc} você ganhou!!')
    elif jogo != j:
        print(f'jogador: {nj} computador: {nc} você perdeu!!')
        break
    print()
