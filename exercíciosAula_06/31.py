numero = int(input('Digite um número de 1 a 5\n'))

match numero:
    case 1:
        print('Número diferente de 3')
    case 2:
        print('Número diferente de 3')
    case 3:
        print('Número igual a 3!')
    case 4:
        print('Número diferente de 3')
    case 5:
        print('Número diferente de 3')
    case _:
        print('Número fora do escopo')