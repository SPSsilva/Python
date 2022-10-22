media = 0
F = ''
K = 0
M = 0
for c in range(1, 5):
    A = str(input('Qual é o nome da {}° pessoa? '.format(c)))
    B = int(input('Qual a idade da {}° pessoa? '.format(c)))
    C = str(input('Qual o sexo da {}° pessoa? '.format(c))).strip().upper()
    media = media + B
    if B > K and C[:9] == 'MASCULINO':
        K = (K - K) + B
        F = A
    elif B < 20 and C[:8] == 'FEMININO':
        M = M + 1
print('''O homen mais velho tem {} anos, e se chama {}.
Há {} mulher(es) a baixo dos 20 anos.
A média de idade é de {}'''.format(K, F, M, media /4))
