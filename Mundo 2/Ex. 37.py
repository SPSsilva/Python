S = int(input('Digite um número: '))
K = int(input('''Digite um número de acordo com as opções:
              [1] Para converter para binário.
              [2] Para converter para octal.
              [3] Para converter para hexadecimal.
              Qual a sua escolha? '''))
if K == 1:
    print('Na base binária este número decimal é {}.'.format(bin(S)))
elif K == 2:
    print('Na base octal este número decimal é {}.'.format(oct(S)))
elif K == 3:
    print('Na base octal este número decimal é {}.'.format(hex(S)))
else:
    print('Por favor digite um dos nímero citados a cima.')
