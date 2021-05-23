# Aluno: Deivison rodrigues jordão
 # programa para receber números e identificar o maior

N1 = float(input('informe o primeiro numero: '))
N2 = float(input('informe o segundo numero: '))
N3 = float(input('informe o terceiro numero: '))

if(N2 < N1 > N3):
    print( N1,' e o maior numero')
elif(N1 < N2 > N3):
    print( N2,' e o maior numero')
elif(N1 < N3 > N2):
    print(N3,' e o maior numero')
else:
    print('todos os valores são iguais')