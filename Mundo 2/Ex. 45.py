import random
S = int(input('''Qual a sua escolha?
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
Qual é a sua jogada? '''))
P = random.randint(1, 3)
if S == P:
    print('Deu empate, ambos escolheram ', end='')
    if S == 1 == P:
        print('Pedra.')
    elif S == 2 == P:
        print('PAPEL.')
    elif S == 3 == P:
        print('TESOURA.')
elif S != P and P < 4 and S < 4:
    if S == 1 and P == 2:
        print('Papel enrola Pedra, você perdeu!')
    elif S == 1 and P == 3:
        print('Pedra quebra Tesoura, você ganhou!')
    elif S == 2 and P == 1:
        print('Papel enrola Pedra, você ganhou!')
    elif S == 2 and P == 3:
        print('Tesoura corta Papel, você perdeu!')
    elif S == 3 and P == 1:
        print('Pedra quebra Tesoura, você perdeu!')
    elif S == 3 and P == 2:
        print('Tesoura corta Papel, você ganhou!')
else:
    print('Escolha um número de 1 a 3.')
print(P)
