P = ('ZERO', 'UM', 'DOIS', 'TRÊS',
     'QUATRO', 'CINCO', 'SEIS', 'SETE',
     'OITO', 'NOVE', 'DEZ', 'ONZE',
     'DOZE', 'TREZE', 'QUATORZE',
     'QUINZE', 'DEZESEIS', 'DEZESETE',
     'DEZOITO', 'DEZENOVE', 'VINTE')

while True:
    S = int(input('Digite um número de 0 a 20 ou digite 100 para sair: '))
    if 0 >= S <= 20:
        print(P[S])
    elif S == 100:
        break
