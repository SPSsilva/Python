A = str(input('Qual é o seu nome completo? ')).strip()
N = A.split()
print('Seu primero nome é {}'.format(N[0]))
print('Seu ultimo nome é {}'.format(N[len(N)-1]))
