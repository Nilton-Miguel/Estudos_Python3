n = [2,2,2,2,3,4,5]
maior = menor = n[0]
pos_maiores = []
pos_menores = []

for v in n:
    if v > maior:
        maior = v
    elif v < menor:
        menor = v

for p, v in enumerate(n):
    if v == maior:
        pos_maiores.append(p)
    elif v == menor:
        pos_menores.append(p)

print(f'Maior: {maior} nas posções {pos_maiores}\nMenor: {menor} nas posições {pos_menores}')
