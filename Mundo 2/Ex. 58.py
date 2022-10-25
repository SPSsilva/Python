import random
import time
print('-=-' * 7, 'Jogo Da Adivinhação', '-=-' * 7)
print('Vou pensar em um número de 0 a 10, tente adivinhar!')
print('-=-' * 21)
N = random.randint(1, 10)
A = ''
P = 0
while A != 0:
    N = random.randint(1, 10)
    A = int(input('''Em que número pensei? Ou digite 0 para sair.
    Digite o número: '''))
    print('Processando...')
    time.sleep(1)
    P = P + 1
    if N == A:
        print('Parabens você acertou!')
        A = 0
    elif A == 0:
        print('OK! Saindo...')
        time.sleep(2)
    else:
        print('Você errou tente na proxima.')
print('Até ganhar você tentou {} vezes.'.format(P))
