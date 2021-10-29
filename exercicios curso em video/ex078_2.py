n = [5, 7, 7, 9, 5]
lista = n[:]
lista.sort()
maior = lista[-1]
menor = lista[0]
maiores = []
menores = []

for pos, num in enumerate(n):
    if num == maior:
        maiores.append(pos)
    elif num == menor:
        menores.append(pos)

print(f'MAIOR: {maior} nas posições: {maiores}\nMENOR: {menor} nas posições: {menores}')
