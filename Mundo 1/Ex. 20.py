import random
A = str(input("Qual é o nome do primeiro aluno? "))
B = str(input("Do segundo? "))
C = str(input("Do Terceiro? "))
D = str(input("Do quarto? "))
N = [A, B, C, D]
random.shuffle(N)
print("Foram sorteados na seguinte ordem:")
print(N)
