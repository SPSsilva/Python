S = N = V = B = P = 0
while S == 0:
    S = int(input('Qual o valor de saque? '))
    if S >= 50:
        N = S // 50
        S = S % 50
    if S >= 20:
        V = S // 20
        S = S % 20
    if S >= 10:
        B = S // 10
        S = S % 10
    if S < 10:
        P = S // 1
print('Vão ser ', end='')
if N != 0:
    print(f'{N} notas de R$:50.')
if V != 0:
    print(f'{V} de R$20.')
if B != 0:
    print(f'{B} de R$10.')
if P != 0:
    print(f'{P} de R$1.')
