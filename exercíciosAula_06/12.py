print('Escolha o meio de transporte:')
meioTransporte = str(input('carro, bicicleta, a pé\n'))

match meioTransporte:
    case 'carro':
        print('  ____________________________________________________')
        print('|   o                                                |')
        print('|    \_____________                                  |')
        print('|                   \__________x                     |')
        print('|____________________________________________________|')
        print('A viagem levará cerca de 16 minutos a 40km/h até seu destino')
    case 'bicicleta':
        print('  ____________________________________________________')
        print('|   o                                                |')
        print('|    \_____________                                  |')
        print('|                   \__________x                     |')
        print('|____________________________________________________|')
        print('A viagem levará cerca de 27 minutos a 22km/h até seu destino')
    case 'a pé':
        print('  ____________________________________________________')
        print('|   o                                                |')
        print('|    \_____________                                  |')
        print('|                   \__________x                     |')
        print('|____________________________________________________|')
        print('A viagem levará cerca de 46 minutos a 6km/h até seu destino')