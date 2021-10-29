continuar = 's'
lista = []

while continuar not in 'nN':
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
    continuar = input('Continuar? [S/N]')

lista.sort(reverse=True)
print(f'Seus números foram {lista}')
if 5 in lista:
    print('sua lista tem o número 5')
else:
    print('o número 5 não foi achado')
