from datetime import date
A = int(input('Que ano que analizar? Ou coloque 0 para saber o ano atual. '))
if A == 0:
    A = date.today().year
if A % 4 == 0 and A % 100 != 0 or A % 400 == 0:
    print('O ano de {} é bissexto.'.format(A))
else:
    print('O ano de {} não é bissexto.'.format(A))
