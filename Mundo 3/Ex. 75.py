S = []
nove = 0
pares = []
for T in range(0, 5):
    R = int(input('Digite um número: '))
    S.append(R)
    if R == 9:
        nove += 1
    if R % 2 == 0:
        pares.append(R)
tuplepares = tuple(pares)
mytuple = tuple(S)
print(mytuple)
print(f'O valor 9 apareceu na tupla {nove} vezes.')
if 3 in mytuple:
    print(f'O valor 3 foi digitado primeiro na posição {mytuple.index(3)+1}.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print(f'Os números pares foram: {tuplepares}')
