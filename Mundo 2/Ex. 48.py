A = 0
J = 0
for S in range(1, 500, 2):
    if S % 3 == 0:
        J = J + S
        A = A + 1
print('A soma de todos os {} números acima são de {}.'.format(A,J))
