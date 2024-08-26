numero = int(input('Digite um número:\n'))

while numero <= 100:
    numero = int(input('Continue tentando!\n'))
    if numero >  100:
        print('Parabéns!')
        break