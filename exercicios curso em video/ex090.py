aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input('Média: '))

if aluno['média'] >= 6:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'

for key, value in aluno.items():

    print(f'Em {key} foi cadastrado: {value}')
