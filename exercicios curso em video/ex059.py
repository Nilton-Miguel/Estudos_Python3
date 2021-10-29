from time import sleep
continuar = True
mesmos = True

while continuar:
    a = int(input('Primeiro número: '))
    b = int(input('Segundo número: '))
    mesmos = True
    print('')
    while mesmos:
        sleep(0.5)
        op = int(input('''Qual opção deseja ?
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Informar maior
[ 4 ] Digitar novos números
[ 5 ] Sair do programa

'''))

        sleep(0.5)
        while 5 < op or op < 1:
            op = int(input('Digite um valor válido: '))

        if op == 1:
            print(f'{a} + {b} = {a + b}')
        elif op == 2:
            print(f'{a} x {b} = {a * b}')
        elif op == 3:
            if a > b:
                print(f'{a} é maior que {b}')
                print('')
            elif a < b:
                print(f'{b} é maior que {a}')
                print('')
            else:
                print(f'{a} é igual a {b}')
                print('')
        elif op == 4:
            mesmos = False
            print('')
        elif op == 5:
            mesmos = False
            continuar = False
            print('')
