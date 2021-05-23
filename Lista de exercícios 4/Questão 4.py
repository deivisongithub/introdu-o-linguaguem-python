# Aluno: Deivison Rodrigues jordão
# tradutor de criptografia

Letras = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","r","s","t","u","v","w","x","y","z"]

print('digite os números separando-os com um espaço')
criptografia = input('digite sua mensagem criptografada: ')
criptografia = list(map(int,criptografia.split()))

criplista = []
for i in range(len(criptografia)):
    criplista.append(Letras[criptografia[i]])

tradução = ''.join(criplista)
print(f'sua mensagem: {tradução}')

    

