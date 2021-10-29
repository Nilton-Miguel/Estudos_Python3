from time import sleep

primeiro = int(input('Primeiro termo: ').strip())
razão = int((input('Razão: ')).strip())
vez = 0
resposta = int(input('Quantos termos inicialmente ?').strip())
vezes = resposta
números = 0

while resposta != 0:
    while vez < vezes:
        if vez == vezes - 1:
            print('\033[33m', primeiro, '\033[m')
        else:
            print('\033[33m', primeiro, '\033[m', end='-->')

        primeiro += razão
        vez += 1
        números += 1

    resposta = int(input('Quantos termos a mais ? ').strip())
    vez = 0
    vezes = resposta

print(f'\033[34mforam solicitados {números} números\033[m')
