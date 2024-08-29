numSecreto = 8
palpite = int(input('Tente adivinhar o número secreto entre 1 e 10\n'))

while palpite != numSecreto:
  palpite = int(input('Tente novamente:\n'))
else:
  print('Parabéns!!!')
