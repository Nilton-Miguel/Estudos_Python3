print('='*182)
print('Cadastro de alunos')
print('='*182)

continuar = True
lista_de_alunos = list()
quantidade_alunos_cadastrados = 0

while continuar:

    lista_de_alunos.append(list())
    lista_de_alunos[quantidade_alunos_cadastrados].append(str(input('\nNome do aluno: ')))
    lista_de_alunos[quantidade_alunos_cadastrados].append(list())
    lista_de_alunos[quantidade_alunos_cadastrados][1].append(float(input('Primeira nota: ')))
    lista_de_alunos[quantidade_alunos_cadastrados][1].append(float(input('Segunda nota: ')))

    quantidade_alunos_cadastrados += 1

    desejo = input('Para encerrar digite [C]: ').capitalize()
    if desejo == 'C':
        continuar= not continuar

print('')
print('='*182)
print(f'Foram cadastrados {quantidade_alunos_cadastrados} alunos, seguem as médias')
print('='*182)
print('')

for aluno in lista_de_alunos:
    print(aluno[0].ljust(30, ' '), end='média: ')
    print((aluno[1][0] + aluno[1][1])/2)
    print('')

print('='*182)

continuar = not continuar

while continuar:

    aluno = int(input('\n[999 para encerrar] De qual aluno mostrar as notas? '))
    
    if aluno == 999:
        continuar= not continuar
    
    else:
        print(f'\nNotas de {lista_de_alunos[aluno-1][0]}:'.ljust(30, ' '), f'{lista_de_alunos[aluno-1][1]}')

print('')
print('='*182)