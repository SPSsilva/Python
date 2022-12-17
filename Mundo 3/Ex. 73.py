print('#' * 20, 'CLASSIFICAÇÃO DO BRASILEIRÃO', '#' * 30)
C = ('1 - Palmeiras', '2 - Internacional', '3 - Fluminense',
     '4 - Corinthians', '5 - Flamengo', '6 - Athletico-PR',
     '7 - Atlético-MG', '8 - Fortaleza', '9 - São Paulo',
     '10 - América-MG', '11 - Botafogo', '12 - Santos',
     '13 - Goiás', '14 - Bragantino', '15 - Coritiba',
     '16 - Cuiabá', '17 - Ceará', '18 - Atlético-GO',
     '19 - Avaí', '20 - Juventude')
print(f'''Os 5 primeiros colocados do Brasileirão são:
{C[:5]}''')
print(f'''Os 5 últimos 4 colocados são:
{C[15:]}''')

print(C)