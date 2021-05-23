# Identificador de números primos
# Aluno: Deivison Rodrigues Jordão

numero = int(input("Digite um número: "))
divisores = 0


for divisor in range(1, numero):

    if numero % divisor == 0:
        divisores = divisores + 1

if divisores > 1:
  print("o seu número não é primo")

else:
  print("o seu número é primo")