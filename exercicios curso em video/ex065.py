cont = 1
número = int(input('Valor: ').strip())
maior = menor = soma = número
resposta = (input('Quer continuar ? (S/N): ').upper().strip())

while resposta == 'S':
    número = int(input('Valor: ').strip())

    if número > maior:
        maior = número
    elif número < menor:
        menor = número

    soma += número
    cont += 1
    resposta = (input('Quer continuar ? (S/N): ').upper().strip())

print(f'a média foi dos {cont} números foi {soma/cont}')
print(f'o maior foi {maior} e o menor foi {menor}')
