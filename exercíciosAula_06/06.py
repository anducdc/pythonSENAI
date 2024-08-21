operaMate = input('Escolha uma operação matemática digitando +, -, * ou /\n')
numeroUm = int(input('Digite o primeiro número\n'))
numeroDois = int(input('Digite o segundo número\n'))

if (operaMate == '+'):
    print (numeroUm + numeroDois)
elif (operaMate == '-'):
    print (numeroUm - numeroDois)
elif (operaMate == '*'):
    print(numeroUm * numeroDois)
elif (operaMate == '/'):
    print(numeroUm / numeroDois)
else:
    print('Operação inválida')