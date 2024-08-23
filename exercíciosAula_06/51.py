numero = int(input('Digite números para somar. Digite o número 0 para encerrar\n'))
soma = 0

while numero != 0:
    soma = soma + numero
    numero = int(input('Digite outro número (0 para sair)\n'))
    if numero == 0:
        break

print(f'Soma total dos números: {soma}')