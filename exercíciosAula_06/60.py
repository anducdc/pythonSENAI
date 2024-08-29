numeroUser = int(input('Digite um número para verificar todos os seus divisores:\n'))
numeroInicial = 0
divisores = []

while numeroInicial <= numeroUser:
  numeroInicial +=1
  if numeroUser % numeroInicial == 0:
    divisores.append(numeroInicial)
print(f'{numeroUser} pode ser dividido por {divisores}')
