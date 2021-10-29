n = int(input('Número: '))
resultado = 1
print(f'{n}! = ', end=' ')

while n > 1:
    resultado = resultado * n
    print(n, end=' x ')
    n = n - 1

print(f'1 = {resultado}')
