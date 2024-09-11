numero = int(input('Digite um número de 1 a 3\n'))
print({1: 'um', 2: 'dois', 3: 'três'}.get(numero, 'ERRO! O número digitado deve ser entre 1 e 3'))
