from random import randint
C = str()
for t in range(0, 5):
    S = randint(0, 100)
    P = str(f'{S}, ')
    C = C + P
print(C)
