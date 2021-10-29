from random import randint

num = (randint(1,9), randint(1,9), randint(1,9), randint(1,9), randint(1,9))

print("os valores sorteados foram: ", end="")

for n in num:
    print(f'{n} ', end='')

maior = menor = num[0]

for a in range(1, len(num)):

    if num[a] > maior:
        maior = num[a]
    elif num[a] < menor:
        menor = num[a]

print(f'\no maior número foi {maior} e o menor foi {menor}')
