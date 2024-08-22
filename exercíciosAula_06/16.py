tipoCombustivel = str(input('Digite uma letra para selecionar o combustível desejado. G = Gasolina, E = Etanol, D = Diesel\n'))
litrosCombustivel = int (input('Digite a quantidade de litros\n'))

precoGasolina = 6.13
precoEtanol = 4.39
precoDiesel = 6.03

if tipoCombustivel == 'g':
    print('O valor total será de R$', precoGasolina * litrosCombustivel)
elif tipoCombustivel == 'e':
    print('O valor total será de R$',precoEtanol * litrosCombustivel)
elif tipoCombustivel == 'd':
    print('O valor total será de R$',precoDiesel * litrosCombustivel)
else:
    print('Parâmetro Inválido')