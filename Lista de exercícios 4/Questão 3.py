# Aluno: Deivison Rodrigues jordão
# programa que soma as colulas de uma matriz definida pelo usuário.

vetor = [None] * 3
matriz = [[None]*3 for i in range(0,2)]

for i in range(2):
    for j in range(3):
        matriz[i][j] = (int(input("digite um número para a linha [%d] e para a coluna [%d] :"%(i,j))))

for j in range(3):
        vetor[j] = matriz[0][j] + matriz[1][j]

print()
print(vetor)