from math import hypot
co = float(input('Comprimento do cateto oposto:' ))
c1 = float(input('Comprimento do ccateto adjaente: '))
hi = hypot(co, c1)
print('A hipotenusa vai medir {:.2f}'.format(hi))
