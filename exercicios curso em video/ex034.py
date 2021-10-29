s = float(input('Digite seu salário: '))
if s > 1250.00:
    a = (s / 100) * 10
else:
    a = (s / 100) * 15
print('O novo salário é de R$ {:.2f}'.format(s + a))
