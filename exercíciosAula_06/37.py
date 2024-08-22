multiplo = int(input('Digite um número e verifique se ele é múltiplo de 2 ou 5\n'))

if multiplo % 2 == 0 and multiplo % 5 == 0:
    print('O número é múltiplo de 2 e de 5')
elif multiplo % 2 == 0:
    print('O número é múltiplo de 2')
elif multiplo % 5 == 0:
    print('O número  múltiplo de 5')
else:
    print('O número não é divisível por 2 nem 5')