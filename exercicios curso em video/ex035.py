A = float(input('Primeiro lado: '))
B = float(input('Segundo lado: '))
C = float(input('Terceiro lado: '))

if (A + C) > B > abs(A - C) and (A + B) > C > abs(A - B) and (B + C) > A > abs(B - C):
    possível = True
else:
    possível = False

if possível:
    print('possível')
else:
    print('impossível')
