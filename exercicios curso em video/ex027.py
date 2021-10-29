nome = str(input('Digite seu nome: ')).strip()

partes = nome.split()
primeiro = partes[0]
último = partes[-1]

print('Olá, prazer te conhecer!\nSeu nome é {} {}!'.format(primeiro, último))



