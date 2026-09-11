import os
os.system ('cls')

print ('''
forma de pagamento
1 - a vista
2 - prazo ''')
pagamento = int(input ('1 / 2: '))
valor = 100
desconto = valor * 0.10

match pagamento:
    case 1:
        print ('valor do produto R$ 100')
        print ('forma de pagamento')
        print ('valor do desconto R$ 10')
        print (f'desconto: {valor - desconto}')

    case 2:
        print ('valor do produto R$ 100')
        parcela =int(input('Digite a quantidade de parcelas:'))
        print(f'parcelas: {parcela}')
        print(f'sua parcela será: {valor / parcela}')
        print ('valor total R$ 100')