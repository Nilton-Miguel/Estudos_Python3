jogador = dict()

print('')
jogador['Nome'] = str(input('Nome do jogador: '))
jogador['Jogos'] = int(input('Quantidade de jogos: '))
jogador['Gols'] = []
jogador['Total de gols'] = 0
print('')

for cont in range(0, jogador['Jogos']):

    jogador['Gols'].append(int(input(f'Quantidade de gols no {cont + 1}° jogo: '))) 
    jogador['Total de gols'] += jogador['Gols'][cont]

print('')

print(f"O jogador {jogador['Nome']} participou de {jogador['Jogos']} jogos")

print('')

for numero, gol in enumerate(jogador['Gols']):
    print(f'{numero + 1}° Jogo: {gol} gols')

print('')

print(f"Totalizando {jogador['Total de gols']} gols no campeonato")

print('')
