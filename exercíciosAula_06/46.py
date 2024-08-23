media = []

for i in range(10):
    media.append(int(input(f'Digite um número {i+1}: ')))

print('Seus números:', media)
mediaTotal = (sum(media)) / 10

print('A média dos números é de:', mediaTotal)
