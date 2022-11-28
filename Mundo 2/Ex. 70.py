G = H = K = T = 0
P = U = ' '
while True:
    print('-=-'*10, 'Loja do seu Zé', '-=-'*10)
    S = str(input('Produto: ')).strip().upper()
    N = float(input('Preço: '))
    G = G + N
    if N >= 1000:
        H += 1
    elif K <= K or K == 0:
        T = N
        P = S
    while U not in 'SN':
        U = str(input('Quer continuar?(S/N) ')).strip().upper()
    if U == 'N':
        break
print('-=-'*10, 'Recibo de compras!', '-=-'*10)
print(f'''O total das compras foi de: R${G}
Produtos que custam mais do que R$1000.00: {H}
O produto mais barato comprado foi: {P}''')
