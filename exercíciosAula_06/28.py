nomeAluno = str(input('Digite o seu primeiro nome'))

if len(nomeAluno) > 5:
    print('Seu nome tem mais que cinco letras')
elif len(nomeAluno) >= 1 and len(nomeAluno) <=5:
    print('Que nome curto!')
else:
    print('Parâmetro Inválido')