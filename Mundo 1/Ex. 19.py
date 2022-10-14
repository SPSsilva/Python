import random
a = str(input('Qual o nome do primeiro aluno? '))
b = str(input('Do segundo? '))
c = str(input('Do terceiro? '))
d = str(input('Do quarto? '))
e = str(input('Do quinto? '))
q = (a, b, c, d, e)
AB = random.choice(q)
print('O aluno escolhido foi: {}.'.format(AB))


