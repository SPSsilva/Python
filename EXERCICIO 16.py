dia = int(input('Quantos dias o carro foi usado até ser entregue? '))
km = float(input('Quantos km rodados? '))
print('O valor total do aluguel é de R${:.2f}'.format((dia*60)+(km*0.15)))
