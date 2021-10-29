from random import randint as ran
from operator import itemgetter

info = dict()

for dado in range(0, 4):

    info[f'jogador {dado + 1}'] = ran(1, 6)

    # itemgetter(1) indica que a chave que vamos usar para ordenar os objetos na função sorted() serão os valores do dicionário

info_corrigida = sorted(info.items(), key = itemgetter(1), reverse=True)

    # sorted retorna uma lista, porque dicionários são variáveis compostas não oordenadas, só podemos ordená-las numa lista

print('')

for jogador, valor in info_corrigida:

    print(f'{jogador} conseguiu um {valor} no dado')

print('')
