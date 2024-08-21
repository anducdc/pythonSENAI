numeroUm = int(input('Digite um número\n'))
numeroDois = int(input('Digite outro número\n'))

numeroUm = numeroUm %2
numeroDois = numeroDois %2

if numeroUm == 0:
    print('O primeiro número é par')
else:
    print('O primeiro número é ímpar')

if numeroDois == 0:
    print('O segundo número é par')
else:
    print('O segundo número é ímpar')