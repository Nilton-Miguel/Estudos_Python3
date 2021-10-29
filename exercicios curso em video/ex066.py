soma = cont = 0

while True:
    n = int(input('Número: ').strip())
    if n == 999:
        break
    else:
        soma += n
        cont += 1

print(f'a soma dos {cont} números é {soma}')
