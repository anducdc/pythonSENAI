palindromo = str(input('Digite uma palavra para verificar se ela é um palíndromo\n'))

if palindromo == palindromo[::-1]:
    print('A palavra é um palíndromo')
else:
    print('não é um palíndromo')