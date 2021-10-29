termos = int((input('Quantos termos você deseja na PA ?')).strip())
primeiro = int(input('Primeiro termo: ').strip())
razão = int((input('Razão: ')).strip())
vez = 0

while vez < termos:
    if vez == termos - 1:
        print('\033[33m', primeiro, '\033[m')
    else:
        print('\033[33m', primeiro, '\033[m', end=' --> ')
    primeiro += razão
    vez += 1
