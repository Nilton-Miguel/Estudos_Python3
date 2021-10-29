resultado = 1

while True:
    n = int(input('Valor para tabuada: ').strip())
    if n < 0:
        break
    for fator in range(1, 11):
        resultado = n * fator
        print(f'{n} x {fator} = {resultado}')
