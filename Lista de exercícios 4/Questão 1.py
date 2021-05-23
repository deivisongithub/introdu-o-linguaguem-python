#Aluno: Deivison Rodrigues jordão
# programa para inverter uma lista de 5 elementos

vetor = [None] * 5
vetor2 = [None] * 5

for i in range(5):
    vetor[i] = float(input("Digite um número: "))

vetor2 = [vetor[4],vetor[3],vetor[2],vetor[1],vetor[0]]

print()
print(vetor2)