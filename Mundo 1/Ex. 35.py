A = float(input('Comprimento do primeiro seguimento: '))
B = float(input('Comprimento do segundo seguimento: '))
C = float(input('Comprimneto do terceiro seguimento: '))
if A < B + C and B < A + C and C < A + B:
    print('Os seguimentos a cima podem formar um triangulo.')
else:
    print('Os seguimentos a cima não podem formar um triangulo.')
