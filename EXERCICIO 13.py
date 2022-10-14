v = float(input('Quanto o produto custa? R$:'))
d = int(input('Porcentagem de desconto: '))
por = v/100
r = (100-d)*por
print('O produto que custava R${:.2f}, agora com o desconto de {}% custa R$:{:.2f}'.format(v, d, r))
