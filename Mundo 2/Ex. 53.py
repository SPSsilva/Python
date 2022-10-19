S = str(input('Digite uma frase: ')).strip().upper()
F = ''
for c in range(3, 0, -1):
    print(c, end='')
    F = F + c
if F == S:
    print('\nEsta frase é palíndroma.')
else:
    print('\nEsta frase não é palíndroma.')
