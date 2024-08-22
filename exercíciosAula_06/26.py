numeroUm = int(input('Digite um número\n'))
numeroDois = int(input('Digite outro número\n'))

if numeroUm % 5 == 0 and numeroDois % 5 == 0:
    print('Ambos os números são divisíveis por 5')
else:
    print('Um ou ambos os números não são divisíveis por 5')