numeroUm = int(input('Digite um número\n'))
numeroDois = int(input('Digite outro número\n'))

numeroUm = numeroUm %2
numeroDois = numeroDois %2

if numeroUm == 0 and numeroDois == 0:
    print('Ambos os números são pares')
else:
    print('Um ou ambos os números são ímpares')