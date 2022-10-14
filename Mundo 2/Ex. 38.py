S = int(input('Digite um número: '))
N = int(input('Digite mais um número: '))
if S > N:
    print('O primeiro número é maior.')
elif N > S:
    print('O segundo número é maior.')
else:
    print('Não existe valor maior os dois são iguais.')
