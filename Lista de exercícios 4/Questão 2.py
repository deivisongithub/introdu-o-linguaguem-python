# Aluno: Deivison Rodrigues jordâo
# Programa para substituir os números pares pelo seu doblo e ímpares pelo seu triplo
# em um lista.

vetor = []
x = 1

while(x == 1):
    vetor.append(int(input("digite um número: ")))
    x = int(input("caso queira continuar fornecendo elementos digite 1,para obter o resultado digite 0 : "))

for i in range(len(vetor)):
  
    if(vetor[i] % 2 == 0):
        vetor[i] = vetor[i] * 2
 
    else:
        vetor[i] = vetor[i] * 3

print()
print(vetor)