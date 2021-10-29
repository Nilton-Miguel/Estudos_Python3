p = 1
while p == 1:

    A = float(input('Primeiro lado: '))
    B = float(input('Segundo lado: '))
    C = float(input('Terceiro lado: '))

    if (A + C) > B > abs(A - C) and (A + B) > C > abs(A - B) and (B + C) > A > abs(B - C):
        possível = True
    else:
        possível = False

    if possível:

        if A == B and A == C:
            print('\033[36mTriângulo equilátero\033[m')

        elif A != B and A != C and B != C:
            print('\033[35mTriângulo escaleno\033[m')

        else:
            print('\033[33mTriângulo isósceles\033[m')

    else:
        print('\033[31mTriângulo impossível\033[m')

    print('')
