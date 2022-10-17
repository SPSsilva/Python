import time
Y = int(input('Digite um número para ver sua tabuada: '))
print('_'*30)
for c in range(1, 11):
    print('{} X {:2} = {}'.format(Y, c, Y*c))
    time.sleep(1)
print('_'*30)
