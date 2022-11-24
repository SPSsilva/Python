from random import randint
import time
N = V = K = S = 0
while True:
    print('-=-' * 20)
    K = int(input('Digite um número de 1 a 10: '))
    S = randint(1, 10)
    L = (K + S) % 2
    N += 1
    G = str(input('Par ou ímpar? ')).strip().upper()
    if G == 'PAR':
        if L == 0:
            print('Deu par! Você ganhou!')
            V += 1
            print(f'Você escolheu {K} e o computador {S}, de deu {K + S}.')
            time.sleep(2)
        elif L != 0:
            print('Você perdeu, deu ímpar!.')
            break
    elif G == 'ÍMPAR' or 'IMPAR':
        if L != 0:
            print('Deu ímpar! Você ganhou!')
            V += 1
            print(f'Você escolheu {K} e o computador {S}, de deu {K+S}.')
            time.sleep(2)
        elif L == 0:
            print('Você perdeu, deu par!')
            break
print('-=-'*20)
print(f'Você escolheu {K} e o computador {S}, de deu {K+S}.')
time.sleep(1)
print(f'Você ganhou {V} vezes consecutivas.')
print('-=-'*20)
