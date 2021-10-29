num = (input('primeiro valor: '), input('segundo valor: '), input('terceiro valor: '), input('quarto valor: '))
for n in num:
    print(f'{n}', end='')

texto = "vez" if (num.count('9') == 1) else "vezes"

print(f"\no número 9 apareceu {num.count('9')} {texto}")

if '3' in num:
    print(f'o valor 3 apareceu primeiramente na posição {num.index("3") + 1}')
elif '3' not in num:
    print('não há um número 3 na tupla')

cont_pares = 0

for n in num:
    if int(n) % 2 == 0:
        print(f'{n}  ',end='')
        cont_pares += 1

if cont_pares != 0:
    print('é o número par') if cont_pares == 1 else print('são os números pares')
