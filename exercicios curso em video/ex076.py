lista = ("Lápis", 1.00, "Borracha", 2.50, "Caneta BIC", 1.00, "Resma de papel", 20.00, "Elásticos", 0.50)

print("")

for g in range(0, len(lista), 2):

    print(f"{lista[g]:.<40}", end=" ")
    print("R$", end="")
    print(f"{lista[g + 1]:>6.2f}")
