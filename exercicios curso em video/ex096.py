def area(lado_a, lado_b):

    texto = f'\nA área aproximada do terreno é {(lado_a * lado_b):.2f}\n'

    print(texto)

print('\033[32m')
print('='*90)
print('{:^90}'.format('Cálculo de área'))
print('='*90)
print('\033[m')

a = float(input('Qual a largura do terreno? '))
b = float(input('Qual o comprimento do terreno? '))

print('\033[31m')
area(a, b)
print('\033[m')
