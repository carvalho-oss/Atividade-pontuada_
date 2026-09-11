import os
os.system ('cls')

genero = input('M para masculino ou F para ferminino: ').upper()
altura = float(input('Digite sua altura:' ))
peso = float(input('Digite seu peso: '))

match genero:
    case 'M':
        print('genero masculino')
        print(f'altura: {altura}')
        print(f'peso: {peso}')
        print ( f'peso ideal:{(72.7 * altura) - 58}')

    case 'F':
        print('genero feminino')
        print(f'altura:{altura}')
        print(f'peso: {peso}')
        print(f'peso ideal: ({62.1 * altura - 44.7}')
