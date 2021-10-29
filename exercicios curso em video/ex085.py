numeros = [[], []]

print('Digite 7 números abaixo: \n')

for n in range(0, 7):
    r = int(input('Número: '))
    if r%2 == 1:
        numeros[0].append(r)
    else:
        numeros[1].append(r)

numeros[0].sort()
numeros[1].sort()

if numeros[0] != []:
    print(f'os números ímpares foram ',end='')
    print(numeros[0])
else:
    print('não foram digitados números ímpares')

if numeros[1] != []:
    print(f'os números pares foram ',end='')
    print(numeros[1])
else:
    print('não foram digitados números pares')
