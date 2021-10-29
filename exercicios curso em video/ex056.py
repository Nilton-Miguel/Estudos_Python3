maisvelho = ''

mulheres = 0
maior = 0
total = 0

quantidade = int(input('Quantas pessoas para analisar? \n'))

for cont in range(1, quantidade + 1):

    nome = (input(f'{cont}º Nome: ')).strip()
    idade = int(input(f'{cont}º Idade: '))
    sexo = (input(f'{cont}º Sexo (F/M): ').upper()).strip()
    print('')

    total += idade

    if (sexo == 'F') and (idade <= 20):
        mulheres += 1

    elif sexo == 'M':
        if cont == 1:
            maisvelho = nome
            maior = idade

        elif idade > maior:
            maisvelho = nome
            maior = idade

if mulheres > 1:
    mensagem = 'mulheres'
else:
    mensagem = 'mulher'

if mulheres > 0:
    print(f'Há {mulheres} {mensagem} com 20 anos ou menos')
else:
    print('não há mulheres listadas')

print(f'A média das idades foi de {total / quantidade}')

if maisvelho != '':
    print(f'O homem mais velho é {maisvelho} com {maior} anos')
else:
    print('não há homens listados')
