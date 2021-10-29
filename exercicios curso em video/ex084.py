cadastro = list()
continuar = True
quantidade_cadastrada = 0

grupo_maior_massa = list()
grupo_menor_massa = list()

while continuar:

    # toda vez que esse laço recomeçar uma nova lista é adicionada à lista de cadastros
    # essa nova lista vazia, vai, por sua vez, receber os dados dos cadastrados como itens
    # o primeiro item será o nome, o segundo item será a massa
    # esse método dispena a necessidade de ter uma nova lista temporária onde os dados vão ser guardados e de lá copiados pro cadastro

    cadastro.append([])
    cadastro[quantidade_cadastrada].append(str(input('Nome: ')))
    cadastro[quantidade_cadastrada].append(int(input('Massa corporal: ')))

    quantidade_cadastrada += 1

    desejo = str(input("Para encerrar o cadastro digite [C]: ")).capitalize()
    if desejo == 'C':
        continuar = not continuar
    
    print('')

# massas maiores e menores arbitrárias que serão corrigidas no laço de repetição abaixo

menor_massa = cadastro[0][1]
maior_massa = cadastro[0][1]

for pessoa in cadastro:

    # compara as massas com máximo e mínimo pra atualizar os respectivos valores e grupos

    # o código antes tinha quatro casos: maior que a maior / igual à maior / menor que a menor / igual à menor
    # porém organizados em um if e três elif
    # em casos onde a menor ainda era por definição, igual à maior, um dos elif não acontecia, pois não aparecia brecha para esecução
    # precisei reescrever em dois if com um discernimento interno, e isso resolveram problemas que eu tinha quanto aos grupos

    if pessoa[1] >= maior_massa:
        if pessoa[1] == maior_massa:
            grupo_maior_massa.append(pessoa[0])
        else:
            maior_massa = pessoa[1]
            grupo_maior_massa.clear()
            grupo_maior_massa.append(pessoa[0])

    if pessoa[1] <= menor_massa:
        if pessoa[1] == menor_massa:
            grupo_menor_massa.append(pessoa[0])
        else:
            menor_massa = pessoa[1]
            grupo_menor_massa.clear()
            grupo_menor_massa.append(pessoa[0])

    
print(f'Foram cadastradas {quantidade_cadastrada} pessoas')

print(f'A menor massa cadastrada foi {menor_massa} Kg, de ',end='')
for pessoa in grupo_menor_massa:
    print(pessoa,end=' | ')
print('')

print(f'A maior massa cadastrada foi {maior_massa} Kg, de ',end='')
for pessoa in grupo_maior_massa:
    print(pessoa,end=' | ')
