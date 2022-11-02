C = 0
G = 0
L = 0
while L != 999:
    L = int(input('Digite um valor:(999 para parar) '))
    C += 1
    G = G + L
print(f'Você digitou {C-1} números seguidos, e a soma total dos números foram: {G-999}.')
