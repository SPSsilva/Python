V = float(input('Qual a velocidade? '))
if V > 80:
    print('Você foi multado em R${:2f} por ultrapassar 80km/h a velocidade maxíma da via.'.format((V - 80) * 7))
else:
    print('Tudo certo! Dentro dos comformes.')

