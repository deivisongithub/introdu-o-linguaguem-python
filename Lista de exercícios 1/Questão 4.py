# Aluno: Deivison rodrigues jordão
 # programa para calcular o desconto de um bijuteria

Valor = float(input('Informe o valor da compra: '))

print('Use 1 para dinheiro,2 para cheque e 3 para outras formas de pagamentos')

MdP = int(input('Informe a forma de pagamento: ')) #modo de pagamento

VcD = float(Valor - (Valor * 10/100)) #Valor com desconto




if( Valor >= 100 and MdP == 1):
    print('O valor a ser pago e ',VcD)
else:
    print('O valor a ser pago e ', Valor)







