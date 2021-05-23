# calculadora de fatorial
# Aluno: Deivison Rodrigues Jordão

num = int(input('digite um número: '))
fatorial = 1

if(num > 0):
    for i in range(num,0,-1):
        fatorial = fatorial * i

elif(num < 0):
    for i in range(num,0):
        fatorial = fatorial * i

print(' O fatorial de',num,'é ',fatorial)