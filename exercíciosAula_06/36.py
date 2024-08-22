numeroMes = int(input('Digite um número de 1 a 12 e descubra o mês referente\n'))

match numeroMes:
    case 1:
        print(' _______________')
        print('|____Janeiro____|')
        print('|_X_|___|___|___|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
    case 2:
        print(' _______________')
        print('|___Fevereiro___|')
        print('|___|_X_|___|___|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
    case 3:
        print(' _______________')
        print('|_____Março_____|')
        print('|___|___|_X_|___|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
    case 4:
        print(' _______________')
        print('|_____Abril_____|')
        print('|___|___|___|_X_|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
    case 5:
        print(' _______________')
        print('|______Maio_____|')
        print('|___|___|___|___|')
        print('|_X_|___|___|___|')
        print('|___|___|___|___|')
    case 6:
        print(' _______________')
        print('|_____Junho_____|')
        print('|___|___|___|___|')
        print('|___|_X_|___|___|')
        print('|___|___|___|___|')
    case 7:
        print(' _______________')
        print('|_____Julho_____|')
        print('|___|___|___|___|')
        print('|___|___|_X_|___|')
        print('|___|___|___|___|')
    case 8:
        print(' _______________')
        print('|____Agosto_____|')
        print('|___|___|___|___|')
        print('|___|___|___|_X_|')
        print('|___|___|___|___|')
    case 9:
        print(' _______________')
        print('|____Setembro___|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
        print('|_X_|___|___|___|')
    case 10:
        print(' _______________')
        print('|____Outubro____|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
        print('|___|_X_|___|___|')
    case 11:
        print(' _______________')
        print('|____Novembro___|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
        print('|___|___|_X_|___|')
    case 12:
        print(' _______________')
        print('|____Dezembro___|')
        print('|___|___|___|___|')
        print('|___|___|___|___|')
        print('|___|___|___|_X_|')
    case _:
        print('Número inválido')