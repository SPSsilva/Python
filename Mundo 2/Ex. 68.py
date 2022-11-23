from random import randint
N = 0
while True:
    U = int(input('Par ou ímpar?(1/2) '))
    S = randint(1, 10)
    L = S % 2
    if U == 1:
        if L == 0:
            print('Deu par! Você ganhou!')
        elif L != 0:
            print('Você perdeu.')
    elif U == 2:
        if L != 0:
            print('Deu ímpar! Você ganhou!')
        elif L == 0:
            print('Você perdeu!')
        break
