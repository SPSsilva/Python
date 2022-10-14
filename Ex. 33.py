A = int(input('Qual o primeiro valor? '))
B = int(input('Qual o segundo valor? '))
C = int(input('Qual o terceiro valor? '))
if A < B and A < C:
    print('O menor valor digitado foi: {}'.format(A))
if B < A and B < C:
    print('O menor valor digitado foi: {}'.format(B))
if C < A and C < B:
    print('O menor valor digitado foi: {}'.format(C))
if A > B and A > C:
    print('O maior valor digitado foi: {}'.format(A))
if B > A and B > C:
    print('O maior valor digitado foi: {}'.format(B))
else:
    print('O maior valor digitado foi: {}'.format(C))
