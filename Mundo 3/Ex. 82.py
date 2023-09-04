lista = list()
while True:
    lista.append(int(input("Digite um número: ")))
    continuar = input('Quer continuar?(N/S) ').upper()
    if 'N' in continuar:
        break
listaa = list()
listab = list()
for t in range(len(lista)):
    if lista[t] % 2 == 0:
        listaa.append(lista[t])
    else:
        listab.append(lista[t])
print(lista)
print(f'Os números pares são: {listaa}')
print(f'Os números ímpares são: {listab}')
