lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if len(lista) == 0 or num > lista[-1]:
        lista.append(num)
    else:
        step = 0
        while True:
            if num <= lista[step]:
                lista.insert(step, num)
                print(f'Posição: {step}')
                break
            step += 1
print(lista)
