from datetime import date
S = int(input('Qual a seu ano de nascimento? '))
P = date.today().year
N = (S-P)*-1
if N < 18:
    print('Você não irá se alistar agora, seu alistamento será no ano de {}.'.format((S-18)*1+P))
elif N == 18:
    print('Você está na hora de se alistar, apresente-se na junta militar mais proxima de você!')
else:
    print('Você já passou da hora de se alistar, está a {} anos atrasado.'.format(N-18))
