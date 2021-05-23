# Contador de algarismos
# Aluno : Deivison rodrigues jordão

x = 0
N = int(input('Digite seu número:'))

while( N // 10 > 0 ):
    N = N/10
    x = x+1
x = x +1
   
    
print()
print('seu número tem ',x,' algarismos')