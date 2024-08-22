numeroUm = int(input('Digite um número de 0 a 20:\n'))

if numeroUm > 9 and numeroUm < 16:
    print('Este número está entre 10 e 15')
elif numeroUm > -1 and numeroUm <=9 or numeroUm >= 16 and numeroUm <=20:
    print('Número fora do escopo 10-15')
else:
    print('Número Inválido')