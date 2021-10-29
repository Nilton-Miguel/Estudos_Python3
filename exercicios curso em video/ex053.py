frase = ((input('Frase: ').strip()).upper()).split()
frase = ''.join(frase)
contrário = ''

for letra in range(len(frase) - 1, -1, -1):
    contrário = (contrário + frase[letra])
print('')

if contrário == frase:
    print(f'{frase} e {contrário}, é palíndromo')
else:
    print(f'{frase} e {contrário}, não é palíndromo')
