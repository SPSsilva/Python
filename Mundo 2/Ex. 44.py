N = float(input('Qual o valor das compras? '))
S = int(input('''Qual vai ser sua forma de pagamento?
Insira apatir das opções a seguir o número correspondente:            
    [1] Á vista no dinheiro ou cheque com 10% de desconto.
    [2] Á vista no cartão com 5% de desconto.
    [3] Em 2x no cartão sem juros.
    [4] 3x ou mais no cartão com 20% de juros.
Qual a sua escolha? '''))
print('O valor total a ser pago será de R$', end='')
if S == 1:
    print('{}.'.format(N/-10+N))
elif S == 2:
    print('{}.'.format(N/-20+N))
elif S == 3:
    print('{}.'.format(N))
elif S == 4:
    print('{}.'.format(N/5+N))
else:
    print('Por favor insira umas das opções.')
