numero = int(input('Digite um número:\n'))

while numero >= 0:
    numero = int(input('Continue tentando!\n'))
    if numero <  0:
        print('Parabéns!')
        break