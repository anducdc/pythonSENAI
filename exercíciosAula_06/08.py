estadoCivil = input('Digite seu estado civil \(solteiro, casado, divorciado ou viúvo\)\n')

match estadoCivil:
    case 'solteiro':
        print('#Partiu boteco?')
    case 'casado':
        print('Respeita a patroa')
    case 'divorciado':
        print('Antes só do que mau acompanhado')
    case 'viúvo':
        print('Sinto muito =(')