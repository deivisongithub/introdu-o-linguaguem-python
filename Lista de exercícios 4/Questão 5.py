# Aluno: Deivison Rodrigues jordão
# vizualizador de probabilidades de um dado de 6 faces

from random import randint

NDL = int(input('digite o número de vezes que o dado será lançado(use 0 para parar): '))

if(NDL != 0):
    lista = []
    lados = [0] * 6
    for i in range(NDL):
        dado = randint(1,6)
        lista.append(dado)
        lados[dado-1]+= 1
    probabilidade = [(i/NDL)*100 for i in lados]

    print('probabilidades:'
    "\nFace 1 = ",probabilidade[0],
    "% \nFace 2 = ",probabilidade[1],
    "% \nFace 3 = ",probabilidade[2],
    "% \nFace 4 = ",probabilidade[3],
    "% \nFace 5 = ",probabilidade[4],
    "% \nFace 6 = ",probabilidade[5],'%')
else:
    print("*** Fim do programa ***")
    
