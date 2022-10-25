import time
S = int(input('Digite um número: '))
N = int(input('Digite mais um número: '))
P = 10
while P != 0:
    print('''       MENU DE OPÇÕES:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair o programa''')
    P = int(input('Digite um número correspondente as opções: '))
    if P == 1:
        print(f'{S} + {N} = {S+N}')
        time.sleep(5)
    elif P == 2:
        print(f'{S} * {N} = {S*N}')
        time.sleep(5)
    elif P == 3:
        if S > N:
            print('{} é maior que {}!'.format(S, N))
        elif S == N:
            print('Os número são iguais, portanto não há maior.')
        else:
            print('{} é maior que {}!'.format(N, S))
        time.sleep(5)
    elif P == 4:
        S = int(input('Digite um número: '))
        N = int(input('Digite mais um número: '))
    elif P == 5:
        P = 0
    else:
        P = 10
print('Saindo...')
time.sleep(2)
