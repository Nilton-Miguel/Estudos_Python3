v = float(input('Qual o valor da casa ?'))
s = float(input('Quanto você ganha de salário ?'))
t = float(input('Em quantos anos quer pagar ?')) * 12

pc = v / t

pcs = 0.3 * s

if pcs >= pc:
    print('\033[32mo valor da parcela será R$ {:.2f}, o financiamento é possível'.format(v/t))
else:
    print('\033[31mnão vai rolar, foi mal, empréstimo negado')
