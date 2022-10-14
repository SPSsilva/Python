import random
import time
N = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar')
print('-=-' * 20)
A = int(input('Em que número pensei? '))
print('Processando...')
.time.sleep(3)
if N == A:
    print('Parabens você acertou!')
else:
    print('Você errou tente na proxima. ')
