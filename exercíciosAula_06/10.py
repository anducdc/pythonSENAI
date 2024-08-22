idadeAluno = int(input('Digite a sua idade\n'))

if idadeAluno >= 18:
    print('Você é maior de idade')
elif idadeAluno <0 and idadeAluno >120:
    print('idade inválida')
else:
    print('Você não tem a idade suficiente para acessar este conteúdo')