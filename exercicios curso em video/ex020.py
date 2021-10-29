from random import shuffle
n1 = str(input('digite um nome: '))
n2 = str(input('digite outro nome: '))
n3 = str(input('digite mais um nome: '))
n4 = str(input('digite um último nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('a ordem será: {}'.format(lista))
