from random import randint as ran
from time import sleep as slp

quantidade_de_jogos = int(input('Quantidade de jogos a serem gerados: '))
lista_de_jogos = list()

# crio uma lista vazia de jogos, com uma quantidade de sub listas determinada pelo usuário

for n in range(0, quantidade_de_jogos):
    lista_de_jogos.append(list())

# pra cada um desses jogos eu vou acrescentar os números agora

for jogo in lista_de_jogos:

    # cada jogo tem 6 algarismos

    for algarismo in range(0, 6):

        # o primeiro algarismo nunca vai ter repetição

        if algarismo == 0:
            jogo.append(ran(1, 60))

            # a partir do segundo já pode haver repetição, então preciso usar de um laço pra corrigir

        else:

            # Vou assumir repetido como True para poder iniciar um laço, que vai manter o proóximo algarismo sendo ressorteado
            # até não haver mais repetição

            repetido = True
            while repetido:

                # dentro do laço, eu vou assumir repetido como Falso, assim, se houver repetição, ele vai ser mudado para Verdadeiro
                # e o laço vai recomeçar, porém, se não houver repetição, ele continua sendo Falso, e o laço quebra

                repetido = False
                algarismo_da_vez = ran(1, 60)
                for numero in jogo:
                    if numero == algarismo_da_vez:

                        # se ele achou um repetido, ele muda repetido de False, para True, garantindo a repetição do laço

                        repetido = True
            
            # se algarismo_da_vez não é repetição de nenhum algarismo do Jogo atual, ele quebra o laço e vem parar aqui, logo, é certo que 
            # é um valor novo e pode ser adicionado ao jogo

            jogo.append(algarismo_da_vez)

print('\nSeus jogos são: \n')
slp(1)
            
for jogo in lista_de_jogos:
    jogo.sort()
    print(jogo,'\n')
    slp(1)

print('Boa Sorte!\n')
slp(1)
