from datetime import date
ano = date.today().year
maiores = 0
menores = 0

for p in range(1, 8):
    nasceu = int(input(f'{p}º data de nascimento: '))
    if ano - nasceu >= 18:
        maiores += 1
    else:
        menores += 1

if maiores > 1:
    mensagemA = 'maiores'
else:
    mensagemA = 'maior'

if menores > 1:
    mensagemB = 'menores'
else:
    mensagemB = 'menor'

print(f'{maiores} {mensagemA} e {menores} {mensagemB}')
