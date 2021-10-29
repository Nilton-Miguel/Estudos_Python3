lista = ("aprender", "estudar", "formatura", "carro", "estacionamento")

for n in lista:

    print(f"\n\033[mA palavra {n} tem:  ", end="")

    for letra in n:
        if letra in "aeiou":
            print(f"\033[32m{letra}", end=" ")