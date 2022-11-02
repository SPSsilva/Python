S = ""
N = M = P = L = 0
while S != 0:
    S = int(input('Digite um número:(Digite 0 para terminar) '))
    N += 1
    M = M + S
    if P == 0:
        P = S
        L = S
    elif S < P and S != 0:
        P = S
    elif S > L:
        L = S
K = M/(N-1)
print(f'''A média entre os valores é {K:.2f}.
O menor valor obtido foi de {P}.
O maior foi de {L}.''')
