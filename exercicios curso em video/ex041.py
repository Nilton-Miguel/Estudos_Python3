from datetime import date
hoje = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = hoje - nascimento

print(idade)
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
if idade >= 25:
    print('MASTER')
