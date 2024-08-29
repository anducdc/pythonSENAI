numeroUm = int(input('Digite o primeiro número:\n'))
numeroDois = int(input('Digite o segundo número:\n'))

while numeroUm <= numeroDois:
  numeroUm = int(input('Digite um número maior que o segundo número:\n'))
else:
  print(f'{numeroUm} é maior que {numeroDois}!')
