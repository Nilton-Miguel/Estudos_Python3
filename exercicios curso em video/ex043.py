h = float(input('Digite sua altura (m): '))
m = float(input('Digite sua massa (Kg): '))

imc = m/(h ** 2)
print(f'IMC: {imc}')

if imc < 18.5:
    print('Abaixo do peso')

elif imc < 25:
    print('Peso ideal')

elif imc < 30:
    print('Sobrepeso')

elif imc < 40:
    print('Obesidade')

elif imc > 40:
    print('Obesidade mórbida')
