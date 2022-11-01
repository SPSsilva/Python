S = int(input('Quantos números de sequencia? '))
F = 0
K = 0
L = 0
G = 0
T = 0
P = 0
print('Na sequência de Fibonacci fica:')
while P != S:
    P += 1
    G = F + L
    print(' {} '.format(G), end='')
    print('-' if P != S else '- Limite atingido', end='')
    T = F
    if F == 0:
        F = 1
    F = F + K
    K = T
    L = G

