S = int(input('Quantos números de sequencia? '))
F = 0
K = 1
L = 3
print('Na sequência de Fibonacci fica:')
print('{} - {} -'.format(F, K), end='')
while L <= S:
    G = F + K
    print(' {} '.format(G), end='')
    F = K
    K = G
    L += 1
    print('-' if L <= S else '- Limite atingido', end='')
