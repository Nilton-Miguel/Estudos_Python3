r = input('Sexo:[M / F]: ').lower().strip()

while not ((r == 'm') or (r == 'f')):
    r = input('Digite um dado válido: ').lower().strip()

if r == 'm':
    mensagem = "masculino"
else:
    mensagem = "feminino"

print('')
print(f'{mensagem} registrado')
