import datetime

dados = dict()

print('')
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = datetime.datetime.now().year - int(input('Ano de nascimento: '))
dados['Número da CTS'] = int(input('[0 se não possui] Número da carteira de trabalho: '))

if dados['Número da CTS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria prevista'] = datetime.datetime.now().year + 35 - (datetime.datetime.now().year - dados['Ano de contratação'])

print('')

for k,v in dados.items():
    print(f"{k} foi cadastrado como: {v}")

print('')
