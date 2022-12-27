tupla = ('Bola', 'Cigano', 'Yakusa', 'La-ele',
         'Python', 'MLBB', 'Impeachman', 'Bestificada')
print('-=-'*5, 'PALAVRAS', '-=-'*5)
for t in tupla:
    print(f'\nNa palavra {t} temos: ', end='')
    for letra in t:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
