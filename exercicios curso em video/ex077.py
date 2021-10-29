lista = ("aprender", "estudar", "formatura", "carro", "estacionamento")

for n in lista:

    n.capitalize()
    vogais = n.count("a") + n.count("e") + n.count("i") + n.count("o") + n.count("u")

    print(f"A palavra {n} tem {vogais} vogais")
