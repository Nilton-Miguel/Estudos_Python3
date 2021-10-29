ns = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
      'quatroze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:

    n = ' '
    while True:
        while not n.isnumeric():
            n = input('Digite um número de 0 a 20: ').strip()
        n = int(n)
        if 0 <= n <= 20:
            break
        else:
            n = ' '

    print(f'{n} escrito por extenso é {ns[n]}')
    resposta = input('Continuar ?').upper().strip()
    if resposta == 'N':
        break
    print()
