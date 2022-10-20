S = str(input('Digite uma frase: ')).strip().upper()
F = S.split()
E = ''.join(F)
#N = ''
Fatiamento = E[::-1]
#for c in range(len(E) -1, -1, -1):
#    N += E[c]
if Fatiamento == E:
    print('\nEsta frase é palíndroma.')
else:
    print('\nEsta frase não é palíndroma.')
