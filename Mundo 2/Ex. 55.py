G = 0
F = 0
for c in range(1, 6):
    A = float(input('Qual o peso da {}º pessoa? '.format(c)))
    if G == 0 and F == 0:
        G = G + A
        F = F + A
    else:
        if  A <= G:
            G = (G - G) + A
        elif A >= F:
            F = (F - F) + A
print('O maior peso foi de {}kg, e o menor foi de {}kg.'.format(F, G))
