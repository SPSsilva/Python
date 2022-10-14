s = float(input('Qual o salário do funcionário? R$:'))
a = int(input('Qual o reajuste salárial? '))
r = ((s*a)/100)+s
print('O salário de R${:.2f}, com aumento de {}% será reajustado pará R$:{}'.format(s, a, r))
