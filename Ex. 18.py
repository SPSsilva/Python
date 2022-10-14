from math import sin, radians, cos, tan
a = float(input('Qual é o ângulo? '))
b = sin(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}. '.format(a, b))
c = cos(radians(a))
d = tan(radians(a))
print('O ânglo de {} tem um COSENO de {:.2f}, e TANGENTE de {:.2f}.'.format(a, c, d))
