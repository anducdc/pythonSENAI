numeroUm = int(input('Digite um número\n'))
numeroDois = int(input('Digite um número\n'))
numeroTres = int(input('Digite um número\n'))

if numeroUm >= 0:
    print(numeroUm,'é um número positivo')
else:
    print(numeroUm,'é um número negativo')
    
if numeroDois >= 0:
    print(numeroDois,'é um número positivo')
else:
    print(numeroDois,'é um número negativo')

if numeroTres >= 0:
    print(numeroTres,'é um número positivo')
else:
    print(numeroTres,'é um número negativo')

if numeroUm >= 0 and numeroDois >= 0 and numeroTres >= 0:
    print('Todos os números são positivos')