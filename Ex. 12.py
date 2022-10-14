l = float(input('Qual a largura da parede em metros? '))
a = float(input('Qual á altura em metros? '))
s = l*a
t = s/2
print('A área é de {}x{}, assim temos uma área de {:.2f}m².\n'
      'E a quantidade de tinta necessária para pintar a área será de {:.2f}L.'.format(l, a, s, t))
