# Visualizador fibonacci
# Aluno: Deivison Rodrigues jordão

num = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1

if (num == 1):
     print("0")

elif(num == 2):
     print("0")
     print("1")
     
elif(num == 3):
     print("0")
     print("1")
     print("1")
     
elif(num == 0):
    print("é impossivel mostrar 0 termos")
    
else:
   
    print("0")
    print("1")
    print("1")
    
    for contador in range(2,num-1):
        termos = ultimo + penultimo
        penultimo = ultimo
        ultimo = termos
        contador += 1
        print(termos)