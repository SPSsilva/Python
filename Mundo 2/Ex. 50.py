E = 0
R = 0
for c in range(1, 7):
    S = int(input('Digite um número: '))
    if S % 2 == 0:
        E = E + S
    else:
        R = R + S
print('A soma dos números pares são: {}.'.format(E))
print('A soma dos ímpares é: {}.'.format(R))
