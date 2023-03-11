lista = []
while True:
    P = int(input('Digite um número: '))
    if P not in lista:
        lista.append(P)
    else:
        print('Este número que você digitou já foi adicionado anteriormente. Por favor tente novamente!')
    S = str(input('Você quer continuar? [S/N]'))
    if S in 'nN':
        break
lista.sort()
print('-=-'*25)
print('A seguir a lista dos números unicos e digitados em ordem crescente.')
print(lista)
