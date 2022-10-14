A = float(input('Qual é o seu salário atual? R$'))
if A <= 1250:
    print('Seu salário atual será de: R${}'.format(A * 0.15 + A))
else:
    print('Seu salário atual será de: R${}'.format(A * 0.10 + A))
