S = float(input('Insira sua primeira média: '))
N = float(input('Insira sua segunda nota: '))
P = (S+N)/2
print('Sua média é {:.1f}.'.format(P))
if P >= 7:
    print('Você está aprovado.')
elif P < 5:
    print('Você está reprovado')
else:
    print('Você está de recuperação, bons estudos!')
