# Aluno: Deivison rodrigues jordão
 # programa para calcular o salário líquido

SB = float(input('Informe seu salário bruto:'))

if( SB <= 420):
    print('seu salário líquido e de ', SB-(SB*(8/100)))
elif( 421 <= SB <= 1350):
    print('seu salário líquido e de ', SB-(SB*(9/100)))
else:
    print('seu salário líquido e de ', SB-(SB*(10/100)))