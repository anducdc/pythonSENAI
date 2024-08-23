tabuada = int(input('Digite um número para que sua tabuada seja mostrada:\n'))

print(f'Soma do número ( {tabuada} )')
for i in range(10):
    print(f'| {tabuada} + {i+1} é igual a', tabuada + (i+1))
print('======================================')

print(f'Subtração do número ( {tabuada} )')
for i in range(10):
    print(f'| {tabuada} - {i+1} é igual a', tabuada - (i+1))
print('======================================')

print(f'Multiplicação do número ( {tabuada} )')
for i in range(10):
    print(f'| {tabuada} * {i+1} é igual a', tabuada * (i+1))
print('======================================')

print(f'Divisão do número ( {tabuada} )')
for i in range(10):
    print(f'| {tabuada} / {i+1} é igual a', tabuada / (i+1))
print('======================================')
