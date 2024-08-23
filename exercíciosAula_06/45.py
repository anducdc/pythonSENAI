maior = None
for i in range(5):
    numero = int(input(f'Digite o número {i+1}:'))

    if maior is None or numero > maior:
        maior = numero
print('O maior número é:', maior)
