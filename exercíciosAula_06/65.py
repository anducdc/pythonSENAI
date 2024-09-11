numeros = [int(input(f'Digite o {i+1}º número: ')) for i in range(5)]

maior = max(numeros)
menor = min(numeros)


print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
