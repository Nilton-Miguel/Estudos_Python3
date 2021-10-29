tot20 = homens = tot = menores = 0

while True:
    idade = int(input('idade: ').strip())
    tot += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = input('sexo:').strip().upper()

    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        tot20 += 1
    if idade < 18:
        menores += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = input('continuar ?').strip().upper()

    if resposta == "N":
        break

print()
print(f'{tot} pessoas cadastradas')
print(f'{tot20} mulheres com menos de 20 anos')
print(f'{homens} homens cadastrados')
print(f'{menores} menores de idade cadastrados')
