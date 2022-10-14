from datetime import date
S = int(input('Qua o seu ano de nascimento? '))
P = date.today().year
T = (S - P)*-1
print(f'Sua idade é {T}.')
if T <= 9:
    print('Sua categoria é a MIRIN.')
elif 9 < T <= 14:
    print('Sua cateria é a INFANTIL.')
elif 14 < T <= 19:
    print('Sua cateria é a JÚNIOR.')
elif 19 < T <= 25:
    print('Sua cateria é a SÊNIOR')
elif T > 25:
    print('Parabéns!! Sua categoria é a de MASTER.')
