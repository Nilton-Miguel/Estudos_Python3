nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúculas á: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('A quantidade de letras de teu nome é: {}'.format(len(nome)-nome.count(' ')))
partes = nome.split()
print('Teu primeiro nome tem {} letras'.format(len(partes[0])))








