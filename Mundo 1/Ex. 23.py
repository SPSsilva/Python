A = int(input('Digite um número: '))
f = A // 1 % 10
g = A // 10 % 10
h = A // 100 % 10
j = A // 1000 % 10
print('Esse número tem {} unidades.'.format(f))
print('{} de dezenas.'.format(g))
print('{} de cemtenas.'.format(h))
print('{} de milhares'.format(j))
