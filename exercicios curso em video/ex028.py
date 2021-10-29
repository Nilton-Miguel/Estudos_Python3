from random import randint

N = randint(1, 3)
n = int(input('Pensei em um número entre 1 e 3, tente adivinhar qual\nDigite seu palpite: '))

if n == N:
    print('Parabéns, você acertou!!!')
else:
    print('AAAAAH, que pena, eu pensei no {}'.format(N))
