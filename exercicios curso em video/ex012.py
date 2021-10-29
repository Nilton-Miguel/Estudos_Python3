p = float(input('digite o valor original do produto em reais: '))
pctg = float(input('digite a porcentagemo do desconto: '))
d = p/100*pctg
np = p-d
print('o novo preço é R$ {}'.format(np))
