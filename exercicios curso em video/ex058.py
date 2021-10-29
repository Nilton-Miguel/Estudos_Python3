from random import randint
from time import sleep

p = 1

while p == 1:
    tries = 0
    n = randint(1, 10)

    j = int(input('Chute um número de 1 a 10: '))

    while not (j == n):

        tries += 1

        if n > j:
            print('Meu número é maior')
            sleep(0.5)
            j = int(input('Digite outro: '))
            print('')

        elif n < j:
            print('Meu número é menor')
            sleep(0.5)
            j = int(input('Digite outro'))
            print('')

    tries += 1
    print(f'Acertou em {tries} tentativas')
    sleep(0.5)
    print('')
    p = int(input('Continuar [ 1 ], Parar [ 0 ] : '))
    print('')
