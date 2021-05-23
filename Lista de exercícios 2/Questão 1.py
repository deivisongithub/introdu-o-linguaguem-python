# Leitor de números para exibir o menor,o maior e a soma entre eles
# Aluno : Deivison rodrigues jordão
chave = 0
chave2 = 0
x = 0
y = 0
z = 0

while( chave != -1):
    x = float(input('digite um número: '))
  
    while(chave2 == 0):
       y = x
       z = x
       chave2 = chave2 + 1
   
    if( chave2 != 0):
        if(x >= y ):
            y = x
        if(x <= z):
            z = x
   
    print('digite 0 para continuar ou -1 para obter o resultado')
    chave = int(input('deseja continuar? :'))

print(' O maior número é ',y, ', o menor é ',z, ', e a soma dos dois é  ',y + z,'.')

