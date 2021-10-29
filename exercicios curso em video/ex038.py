p = 1
while p == 1:
    a = int(input('Primeiro número: '))
    b = int(input('Segundo número: '))
    if a > b:
        print('{} é maior que {}'.format(a, b))
    elif b > a:
        print('{} é maior que {}'.format(b, a))
    else:
        print('{} é igual a {}'.format(a, b))
