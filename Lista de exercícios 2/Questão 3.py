# Gerenciador de conta bancaria
# Aluno : Deivison rodrigues jordão
x = 0
saldo = 0
deposito = 0

while(x != 4):
    print('1.Depositar')
    print('2.Sacar')
    print('3.Consultar saldo')
    print('4.sair')
    
    x = int(input('digite a operação desejada:'))
    
    if(x == 1):
        deposito = float(input('Digite o valor que deseja depositar: '))
        saldo = saldo + deposito
    elif(x == 2):
        saque = float(input('Digite o valor que deseja sacar: '))
        if(saque > saldo):
            print('saldo insuficiente')
        else:
            saldo = saldo - saque
            print('saque realizado com sucesso')
    elif(x == 3):
        print('seu saldo é de ',saldo)

print('Obrigado pela preferência,volte sempre')