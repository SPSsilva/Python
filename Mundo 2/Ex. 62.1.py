import time
print('='*20)
print('Termos de uma PA')
print('='*20)
S = int(input('Primeiro Termo: '))
E = int(input('Razão: '))
M = S
L = 10
P = 0
K = 0
while L != 0:
    print('{} > '.format(M), end='')
    M += E
    L -= 1
    K = K + 1
    if L == 0:
        print('PAUSA!')
        P = int(input('Quantos termos você quer mais? '))
        if P == 0:
            L = 0
        else:
            L += P
print('Saindo...')
time.sleep(2)
print('Progreção finalizada após {} termos mostrados'.format(K))
