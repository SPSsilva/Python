S = float(input('Bem vindo ao simulador de aprovação de crédito Bradesco!'
                ' Qual o valor do imóvel? R$:'))
N = float(input('Qual a sua renda mensal? R$:'))
H = int(input('Em quantos anos ira pagar? '))
M = (S/(H*12))
L = (N/10)*3
if M <= L:
    print('Parabéns seu crédido foi aprovado!')
elif M > L:
    print('Que pena não podemos aprovar seu crédito.')
