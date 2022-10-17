print('='*20)
print('Termos de uma PA')
print('='*20)
S = int(input('Primeiro Termo: '))
E = int(input('Razão: '))
R = S + (10 - 1) * E
for c in range(S, R, E):
    print('{} > '.format(c), end="" )
print('Acabou.')
