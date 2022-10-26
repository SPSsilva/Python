print('='*20)
print('Termos de uma PA')
print('='*20)
S = int(input('Primeiro Termo: '))
E = int(input('Razão: '))
M = S
L = 0
while L != 10:
    print('{} > '.format(M), end='')
    M += E
    L += 1
print('Acabou!')
