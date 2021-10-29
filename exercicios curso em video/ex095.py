from time import sleep as slp
import colorama
import os

os.system("")

colorama.init()

cyane = colorama.Fore.CYAN
magenta = colorama.Fore.MAGENTA
green = colorama.Fore.GREEN
yellow = colorama.Fore.YELLOW
normal = colorama.Fore.RESET

jogadores = list()

cadastro_jogador = dict()

divisas = 125

while True:

    print('')
    print('='*divisas)
    print('')

    cadastro_jogador['Nome'] = str(input(cyane + 'Nome do jogador: ' + normal))

    cadastro_jogador['Jogos'] = int(input(cyane + 'Quantidade de jogos: ' + normal))

    cadastro_jogador['Total de gols'] = 0
    cadastro_jogador['Gols'] = []
    print('')

    for cont in range(0, cadastro_jogador['Jogos']):

        cadastro_jogador['Gols'].append(int(input(cyane + f'Quantidade de gols no {cont + 1}° jogo: ' + normal))) 
        cadastro_jogador['Total de gols'] += cadastro_jogador['Gols'][cont]
    
    jogadores.append(cadastro_jogador.copy())
    
    procedência = str(input(magenta + '[C para encerrar]: ' + normal)).capitalize()
    if procedência == 'C':
        break

print('')
print('='*divisas)
print('')

# print da borda guia da tabela

print(magenta + "Jogador".ljust(15, ' '),"|", "Jogos em campo".ljust(15, ' '),
         "|", "Gols".ljust(25, ' '), "|", "Total do Campeonato")

# print das informações da tabela

for jogador in jogadores:

    print(green + f"{jogador['Nome']}".ljust(15, ' '), "|", f"{jogador['Jogos']}".ljust(15, ' '),
          "|", f"{jogador['Gols']}".ljust(25, ' '), "|", str(jogador['Total de gols']) + normal)

print('')
print('='*divisas)
print('')

while True:

    n = int(input(yellow + '[999 encerra] Dados a exibir: ' + normal)) - 1
    print('')

    if (n + 1) == 999:
        break

    else:

        # print da borda guia da tabela

        print(magenta + "Jogador".ljust(15, ' '),"|", "Jogos em campo".ljust(15, ' '),
                 "|", "Gols".ljust(25, ' '), "|", "Total do Campeonato")
        
        # print das informações da tabela

        print(green + f"{jogadores[n]['Nome']}".ljust(15, ' '), "|", f"{jogadores[n]['Jogos']}".ljust(15, ' '),
          "|", f"{jogadores[n]['Gols']}".ljust(25, ' '), "|", str(jogadores[n]['Total de gols']) + normal)

    print('')
    print('='*divisas)