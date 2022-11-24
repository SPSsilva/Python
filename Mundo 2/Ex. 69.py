E = G = R = 0
while True:
    F = ' '
    T = ' '
    S = int(input('Qual a idade? '))
    while F not in 'MF':
        F = str(input('Qual é o sexo?(M/F) ')).strip().upper()
    if S <= 18:
        E += 1
    if S <= 20 and F == 'F':
        R += 1
    if F == 'M':
        G += 1
    while T not in 'SN':
        T = input('Quer continuar?(S/N) ').upper().strip()
    if T == 'N':
        break
print('-=-'*20)
print(f'''Há {E} pessoas abaixo dos 18 anos, {R} mulher(es) abaixo
dos 20 anos e {G} homens cadrastado(s).''')
print('-=-'*20)
