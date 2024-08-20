print(' _________________________________________')
print('|                                         |')
print('|       BEM-VINDO AO CADASTRO SENAI       |')
print('|_________________________________________|')

nomeAluno = input('Informe o primeiro nome do aluno:\n')
sobreAluno = input('informe o sobrenome do aluno\n')
cidadeAluno = input('Informe a cidade do aluno:\n')
idadeAluno = int(input('Informe a idade do aluno\n'))
alturaAluno = float(input('infome a altura do aluno\n'))
pesoAluno = float(input('informe o peso do aluno\n'))
emailAluno  = input('Informe o email do aluno:\n')
anoNasci = int(input('informe o ano de nascimento\n' ))
mesNasci = int(input('informe o mês de nascimento\n' ))
diaNasci = int(input('informe o ano de nascimento\n' ))


print (f'SUCESSO! O aluno {nomeAluno} {sobreAluno} de {idadeAluno} anos de idade e da cidade de {cidadeAluno} foi matriculado no curso X do Senai\n')
print(f'O Aluno tem {alturaAluno} metros de altura, pesa {pesoAluno}kg e nasceu em {diaNasci}/{mesNasci}/{anoNasci}. Seu email é {emailAluno}')
