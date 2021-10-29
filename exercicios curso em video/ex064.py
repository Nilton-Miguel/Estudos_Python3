soma = cont = n = 0
while n != 999:
    soma += n
    n = int(input('Valor: '))
    if n != 999:
        cont += 1
print(f'a soma foi {soma} e foram informados {cont} números')
