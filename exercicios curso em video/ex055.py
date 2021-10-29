maior = 0
menor = 0

for t in range(1, 6):
    valor = int(input(f'{t}º valor: '))
    if t == 1:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
print(f'O maior é {maior} e o menor é {menor}')
