A = str(input('Qual o sexo?(M/F) ')).strip().upper()
while A not in 'MFfm':
    A = str(input('Por favor escolha entre M (Masculino) e F (Feminino): '.strip().upper()))
print('Registrado com sucesso!')
