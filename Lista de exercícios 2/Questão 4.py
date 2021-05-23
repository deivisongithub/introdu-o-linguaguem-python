# Contador de pessoas com mais de 18 anos que medem mais de 1.70
# Aluno : Deivison rodrigues jordão
# A QUESTÃO não deixou muito claro se os que tinha exatamente 18 anos ou exatamente 1.70 também entravam no grupo dos selicionados.
# Por via das dúvidas eu decidi contabilizalos também. 

idade = 0
altura = 0
N = 0

print('para o melhor desempenho do programa use as médidas metros e anos,respectivamente para altura e idade.')

while( idade >= 0):
    idade = int(input('digite a idade: '))
    if(idade >= 0):
        altura = float(input('digite a altura: '))
    
    if(idade >= 18 and altura >= 1.70):
        N = N + 1
    
print()
print('O total de pessoas com mais de 18 e mais altas que 1.70 é ',N)

