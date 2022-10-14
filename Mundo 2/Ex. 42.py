A = float(input('Comprimento do primeiro seguimento: '))
B = float(input('Comprimento do segundo seguimento: '))
C = float(input('Comprimneto do terceiro seguimento: '))
if A < B + C and B < A + C and C < A + B:
    print('Os seguimentos a cima podem formar um triangulo, ', end='')
    if A == B != C and A != B == C and A == C != B and C != A == B:
        print('e este quadrado é ISÓCELES!')
    elif A == B == C and A == C:
        print('e este quadrado é EQUILÁTERO!')
    elif A != B != C and C != A:
        print('e este quadrado é ESCALENO!')
else:
    print('Os seguimentos a cima não podem formar um triangulo.')
