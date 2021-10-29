n = int(input('digite um número inteiro: '))

op = int(input('''escolha uma opção de conversão: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal'''))

if op == 1:
    print(bin(n)[2:])

elif op == 2:
    print(oct(n)[2:])

elif op == 3:
    print(hex(n)[2:])
