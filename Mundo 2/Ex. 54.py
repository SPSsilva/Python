from datetime import date
F = 0
M = 0
G = date.today().year
for C in range(1, 8, 1):
    N = int(input('Qual a data de nasciemnto da {} pessoa? '.format(C)))
    U = G - N
    if U >= 21:
        F = F + 1
    else:
        M = M + 1
print('{} pessoas são maiores de idade, e {} são menores de idade.'.format(F, M))
