A = float(input('Quantos quilometros sarão percorridos? '))
if A <= 200:
    print('Sua passagem será de: R${}'.format(A * 0.5))
else:
    print('Sua passagem será de: R${}'.format(A * 0.45))
