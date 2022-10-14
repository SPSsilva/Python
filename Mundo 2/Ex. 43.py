S = float(input('Para calcular seu imc, insira seu peso: '))
N = float(input('Sua altura: '))
E = S/(N*N)
if E < 18.5:
    print(f'Seu IMC é de {E:.2f}. Cuidado você está abaixo do peso, consulte seu nutricionista.')
elif E >= 18.5 and E < 25:
    print(f'Seu IMC é de {E:2f}. Seu peso é o ideal. Parabéns!!')
elif E >= 25 and E < 30:
    print(f'Seu IMC é de {E:2f}. Você está com sobrepeso')
elif E >= 30 and E < 40:
    print(f'Seu IMC é de {E:2f}. Você está obeso, cuidado.')
else:
    print(f'Seu IMC é de {E:2f}. Você está com obesidade Mórbida, procure imédiatamente um médico e nutricionista!')
