from random import randint
N = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for b in N:
    print(f"{b} ", end='')
print(f'\nO maior número sorteado foi: {max(N)}')
print(f'O menor número sorteado foi: {min(N)}')
