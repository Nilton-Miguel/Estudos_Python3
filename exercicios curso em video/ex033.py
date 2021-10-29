a = int(input('Digite o primeiro: '))
b = int(input('Digite o segundo: '))
c = int(input('Digite o terceiro: '))

if a > b and a > c:
    if b < c:
        print('O maior foi {} e o menor {}'.format(a, b))
    if c < b:
        print('O maior foi {} e o menor {}'.format(a, c))
if b > a and b > c:
    if a < c:
        print('O maior foi {} e o menor {}'.format(b, a))
    if c < a:
        print('O maior foi {} e o menor {}'.format(b, c))
if c > a and c > b:
    if a < b:
        print('O maior foi {} e o menor {}'.format(c, a))

    if b < a:
        print('O maior foi {} e o menor {}'.format(c, b))
