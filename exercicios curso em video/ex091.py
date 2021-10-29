# Como eu fiz antes de ver a aula do Guanabara

from random import randint as ran

info = dict()

for dado in range(0, 4):

    info[f'jogador {dado + 1}'] = ran(1, 6)

info_corrigida = sorted(info.items(), key = lambda x: x[1], reverse=True)

print('')

for jogador, valor in info_corrigida:

    print(f'{jogador} conseguiu um {valor} no dado')

print('')
