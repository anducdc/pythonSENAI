cidadeUser = str(input('Digite o nome de uma cidade\n'))

match cidadeUser:
    case 'brasilia':
        print('Essa é a capital do Brasil!')
    case 'brasília':
        print('Essa é a capital do Brasil!')
    case 'Brasilia':
        print('Essa é a capital do Brasil!')
    case 'Brasília':
        print('Essa é a capital do Brasil!')
    case _:
        print('Eu tenho uma tia que mora em', cidadeUser)