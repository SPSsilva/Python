lista = []
parar = ''
while parar != 'N':
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    parar = str(input("Deseja continuar?[S/N] ")).upper()
    while parar not in 'SNsn':
        parar = str(input('Por favor, Sim ou Não?[S/N] '))
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos no total.')
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado.')
else:
    print('O valor 5 não foi digitado.')
