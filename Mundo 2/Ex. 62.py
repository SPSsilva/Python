import time

print('='*20)
print('Termos de uma PA')
print('='*20)
S = int(input('Primeiro Termo: '))
E = int(input('Razão: '))
M = S
L = 10
while L != 0:
    print('{} > '.format(M), end='')
    M += E
    L -= 1
    if L == 0:
        print('Acabou!')
        M = int(input('Insira outro termo ou insira 0 para sair: '))
        if M == 0:
            L = 0
        else:
            E = int(input('Insira a razão: '))
            L = 10
print('Saindo...')
time.sleep(2)
