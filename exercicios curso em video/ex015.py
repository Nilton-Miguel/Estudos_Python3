t = float(input("Informe por quantos dias você alugou o veículo: "))
d = float(input("Informe quantos quilômetros você rodou com o veículo: "))
p = t * 60 + d * 0.15
print("o preço a pagar é de R${}".format(p))
