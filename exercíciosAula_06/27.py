numeroUm = int(input('Insira o primeiro número\n'))
numeroDois = int(input('Insira o segundo número\n'))
numeroTres = int(input('Insira o terceiro número\n'))


if numeroUm > numeroDois and numeroUm > numeroTres:
    print('O primeiro número é o maior dos três.')
elif numeroDois > numeroUm and numeroDois > numeroTres:
    print('O segundo número é o maior dos três.')
elif numeroTres > numeroUm and numeroTres > numeroDois:
    print('O terceiro número é o maior dos três.')
else:
    print('Todos os números são iguais')