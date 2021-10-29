valores = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        valores.append(int(input(f'Digite um valor para [{linha + 1}, {coluna + 1}]: ')))

cont = 0
print('')

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {valores[cont]} ]',end=' ')
        cont += 1
    print('')
print('')
