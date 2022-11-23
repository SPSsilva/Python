S = int(input('Digite um número: '))
V = 1
M = S
while True:
    S = int(input('Digite mais um número ou digite 999 para parar: '))
    if S == 999:
        break
    else:
        V += 1
        M = M + S
print(f'Foram digitados {V} números e a soma foi de {M}.')
