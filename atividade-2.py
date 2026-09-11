import os
os.system('cls')

nome = input('Digite seu nome: ')
genero = input('M para masculino ou F para feminino: ').upper()
estado_civil= ('''
1- Solteiro(a)
2- Casado(a)
3 - Divorciado(a)
4 - Viúvo(a)''')

match genero:
    case 'M':
        print ('genero masculino')
        print(f'nome:{nome}:')

        match estado_civil:
            case '1':
                print('solteiro(a):')

            case '2':
                print ('casado(a):')

    case '3':
        print('viúvo(a)')

    case 'F':
                print ('genero feminino')
                print (f'nome{nome}')
                
if estado_civil == '2':
    tempo = int(input('quanto tempo casado  ?: '))
    print(f'anos casado(a){tempo}:')

