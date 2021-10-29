cadastro_temporário = dict()
pessoas_cadastradas = list()    
print('')

while True:

    cadastro_temporário['Nome'] = str(input('Nome: '))
    cadastro_temporário['Idade'] = int(input('Idade: '))
    cadastro_temporário['Sexo'] = str(input('[M|F] Masculino | Feminino: ')).capitalize()

    pessoas_cadastradas.append(cadastro_temporário.copy())

    desejo = str(input('[C para encerrar]: ')).capitalize()
    if desejo == "C":
        break
    print('')

print('')
print(f'Foram cadastradas {len(pessoas_cadastradas)} pessoas')

soma_idades = 0
feminino = list()
acima_média = list()

for pessoa in pessoas_cadastradas:

    soma_idades += pessoa['Idade']

    if pessoa['Sexo'] == 'F':
        feminino.append(pessoa['Nome'])

print(f'A média das idades é de: {soma_idades / len(pessoas_cadastradas)} anos')

if feminino != []:

    print('Se declaram do sexo feminino: ',end='')

    for indivíduo in feminino:

        print(indivíduo, end='  ')

print('')

for pessoa in pessoas_cadastradas:

    if pessoa['Idade'] > (soma_idades / len(pessoas_cadastradas)):
        acima_média.append(pessoa['Nome'])


if acima_média != []:

    print('São mais velhos que a média: ',end='')

    for indivíduo in acima_média:

        print(indivíduo, end='  ')

print('')
