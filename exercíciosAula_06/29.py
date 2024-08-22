numero = int(input('Digite um número e descubra se ele é múltiplo de 3\n'))

numero = numero % 3

if numero == 0:
    print('Este número é múltiplo de 3')
else:
    print('Este número não é múltiplo de 3')