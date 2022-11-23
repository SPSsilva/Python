import time
while True:
    S = int(input('Quer ver a tabuada de qual valor? '))
    if S < 0:
        print('''Programa será encerrado!
        Encerrando...''')
        time.sleep(1)
        break
    print('='*40)
    for c in range(1, 11):
        print(f'{S} x {c} = {S*c}')
        time.sleep(0.4)
    print('='*40)
