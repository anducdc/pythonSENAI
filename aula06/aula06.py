#atribuição de valores a uma variável

numero = 10
print(numero)

numero = numero + 10
#numero += 10
print(numero)

numero = numero - 10
#numero -= 10
print(numero)

numero = numero * 10
#numero *= 10
print(numero)

numero = numero / 10
#numero /= 10
print(numero)


if numero % 2 == 0:
    print('numero é par')
else:
    print('numero é impar')


for i in range(5):
    print(i)




frutas = ['banana', 'maçã', 'morango', 'laranja']

for item in frutas:
    print(item)

for indice, fruta in enumerate(frutas):
    print(f'Suas frutas são {indice}: {frutas}')