S = int(input('Digite um número: '))
E = S + 1
P = 0
for c in range(1, E):
    if S % c == 0:
        print('\033[31m{}'.format(c), end=" ")
        P = P + 1
    else:
        print('\033[32m{}'.format(c), end=' ')
if P == 2:
    print('\n\033[0mEste número é primo pois só é divisivél {} vezes.'.format(P))
else:
    print('\n\033[0mEste número foi divisivél {} vezes, por isso não é primo.'.format(P))
