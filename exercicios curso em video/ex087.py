valores = []

for linha in range(0, 3):
    for coluna in range(0, 3):
        valores.append(int(input(f'Digite um valor para [{linha + 1}, {coluna + 1}]: ')))

cont = 0
print('')

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {valores[cont]} ]',end=' ')
        cont += 1
    print('')
print('')

soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = valores[3]

for numero in valores:
    if numero%2 == 0:
        soma_pares += numero

for numero in range(0, 9):
    if (numero+1)%3==0:
        soma_terceira_coluna += valores[numero]
    
for numero in range(4, 6):
    if valores[numero] > maior_valor_segunda_linha:
        maior_valor_segunda_linha = valores[numero]
    
print(f'A soma de todos os valores pares da matriz é: {soma_pares}')
print(f'A soma de todos os valores pares da terceira coluna é: {soma_terceira_coluna}')
print(f'O maior valor da segunda linha é: {maior_valor_segunda_linha}')
