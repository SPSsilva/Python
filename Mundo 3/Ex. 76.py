print('-' * 35)
print(' ' * 7, 'Listagem de Preços', ' ' * 7)
print('=' * 35)
lista = ('Lápis', 0.50,
         'Borracha', 0.25,
         'Caderno', 12.00,
         'Estojo', 5.00,
         'Tranferidor', 2.50,
         'Compasso', 10.00,
         'Mochila', 80.00,
         'Caneta', 1.00,
         'Livros', 400.00)
for p in range(0, len(lista)):
    if p % 2 == 0:
        print(f'{lista[p]:.<25}', end='')
    else:
        print(f'R$:{lista[p]:>7.2F}')

