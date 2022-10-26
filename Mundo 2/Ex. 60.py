import time

S = int(input('Digite um número, para calcular seu fatorial: '))
N = S
L = 1
print('Calculando... ', end='')
time.sleep(2)
print('{}! = '.format(S), end='')
while N > 0:
    print('{}'.format(N), end='')
    print(' X ' if N > 1 else ' = ', end='')
    L *= N
    N -= 1
print('{}'.format(L))
