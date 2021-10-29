n = int(input('Digite um número entre 0 e 9999: '))

m = n//1000 % 10
c = n//100 % 10
d = n//10 % 10
u = n//1 % 10

print('Milhar:  {}\nCentena: {}\nDezena:  {}\nUnidade: {}'.format(m, c, d, u))
