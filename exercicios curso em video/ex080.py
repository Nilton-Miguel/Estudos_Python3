lista = []
for n in range(0, 5):

    num = int(input("Digite um número: "))
    if n == 0:
        lista.append(num)
        print('primeiro número, única posição')
    elif num > lista[-1]:
        lista.append(num)
        print("adicionei o número no final")

    for g in range(0, len(lista)):
        if num < lista[g]:
            lista.insert(g, num)
            print(f'adicionei o número na posição {g}')
            break

print(lista)
