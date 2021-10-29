L = []
while True:
    n = int(input("Adicione um número: "))
    if n not in L:
        L.append(n)
        L.sort()
    else:
        print("número repetido não pode")

    r = input("Quer continuar ? [S/N]")
    if r in "nN":
        break

L.sort()
print(L)
