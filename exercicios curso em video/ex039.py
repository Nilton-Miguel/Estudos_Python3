import datetime

nasceu = int(input('Em que ano você nasceu? '))
atualmente = datetime.date.today().year

resposta = int(input('''Já fez aniversário este ano ?
[ 0 ] para não: 
[ 1 ] para sim: '''))

if resposta == 1:
    idade = atualmente - nasceu

elif nasceu == atualmente:
    idade = atualmente - nasceu

else:
    idade = atualmente - nasceu - 1

while idade > 120:
    idade = int(input('Tentando me enganar né ? Digite sua idade, é sério! '))

if idade > 18:
    print('atualmente você tem {} anos'.format(idade))
    certa = idade - 18
    if certa == 1:
        print('Você já devia ter se alistado a {} ano! '.format(certa))
    else:
        print('Você já devia ter se alistado a {} anos! '.format(certa))

elif idade < 18:
    print('atualmente você tem {} anos'.format(idade))
    certa = 18 - idade
    if certa == 1:
        print('Falta {} ano para você se alistar!'.format(certa))
    else:
        print('Faltam {} anos para você se alistar!'.format(certa))

else:
    print('atualmente você tem {} anos'.format(idade))
    print('você deve se alistar imediatamente! ')
