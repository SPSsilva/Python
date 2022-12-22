print('#' * 20, 'CLASSIFICAÇÃO DO BRASILEIRÃO', '#' * 30)
C = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
     'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
     'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
     'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO',
     'Avaí', 'Juventude')
print(f'''Os 5 primeiros colocados do Brasileirão são:
{C[:5]}''')
print(f'''Os 5 últimos 4 colocados são:
{C[-5:]}''')
print(f'''Em ordem alfabetica:
{sorted(C)}''')
print(f'Flamengo está na {C.index("Flamengo")+1}º posição. ')
