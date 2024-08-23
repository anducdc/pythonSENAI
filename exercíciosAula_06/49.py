maior = []

for i in range(7):
    maior.append(int(input(f'Digite o numero {i+1}: ')))

copia = []
for i in maior:
    if i > 10:
        copia.append(i)    

print(f'Estes números são maiores do que 10: {copia}')