times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético - PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético - GO')

print('\033[32mOS PRIMEIROS CINCO COLOCADOS:\033[m')

for g in range(0, 5):
    print(times[g])

print('\n\033[31mOS ÚLTIMOS QUATRO COLOCADOS:\033[m')

for g in range(0, 4):
    print(times[(len(times) - 1) - g])

print('\nTIMES EM ORDEM ALFABÉTICA:')
print(sorted(times))

print('\033[36mCOLOCAÇÃO DO CHAPECOENSE:\033[m')

print(times.index('Chapecoense') - 1)
