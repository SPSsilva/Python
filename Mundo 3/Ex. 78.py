lista = []
G = M = 0
for c in range(0, 5):
    lista.append(int(input('Digite um número:')))
    if lista[c] > G:
        G = lista[c]
    if lista[c] < G or lista[c] < M:
        M = lista[c]
print(f'O maior valor digitado foi {G} na posição: ', end='')
for i, v in enumerate(lista):
    if v == G:
        print(f'{i}...', end='')
print()
print(f'\nO menor valor foi de {M} na posição ', end='')
for i, v in enumerate(lista):
    if v == M:
        print(f'{i}...', end='')
print()
print(f'\nOs valores que você digitou: {lista}')
