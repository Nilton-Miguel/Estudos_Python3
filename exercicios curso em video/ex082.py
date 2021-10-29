total = []
pares = []
impares = []

while True:
    n = int(input("Digite um número: "))
    total.append(n)
    if (n % 2) == 0:
        pares.append(n)
    elif (n % 2) == 1:
        impares.append(n)
    r = input("Quer continuar ? [S/N]")
    if r in "nN":
        break
print(f'os números digitados foram {total}')
print(f'{pares} são pares e {impares} são ímpares')
