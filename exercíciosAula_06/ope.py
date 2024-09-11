import random

alunos = {}

def gerar_matricula():
    return str(random.randint(1000, 9999))

def validar_email(email):
    return "@" in email and "." in email

def cadastrar_aluno():
    nome = input('Nome: ')
    email = input('Email: ')
    while not validar_email(email):
        print('Email inválido. Tente novamente.')
        email = input('Email: ')
    
    data_nascimento = input('Data de nascimento (dd/mm/aaaa): ')
    matricula = gerar_matricula()

    alunos[matricula] = {
        'nome': nome,
        'email': email,
        'data_nascimento': data_nascimento,
        'matricula': matricula
    }

    print(f'Aluno cadastrado com sucesso! Matrícula: {matricula}')

def atualizar_aluno(matricula):
    if matricula in alunos:
        aluno = alunos[matricula]
        print(f'Atualizando dados de {aluno["nome"]}')
        aluno['nome'] = input('Novo nome: ')
        aluno['email'] = input('Novo email: ')
        while not validar_email(aluno['email']):
            print('Email inválido. Tente novamente.')
            aluno['email'] = input('Novo email: ')
        
        aluno['data_nascimento'] = input('Nova data de nascimento (dd/mm/aaaa): ')
        print('Dados atualizados com sucesso!')
    else:
        print('Matrícula não encontrada.')

def excluir_aluno(matricula):
    if matricula in alunos:
        del alunos[matricula]
        print('Aluno removido com sucesso.')
    else:
        print('Matrícula não encontrada.')

def listar_alunos():
    if alunos:
        for matricula, dados in alunos.items():
            print(f"\nMatrícula: {matricula}")
            print(f"Nome: {dados['nome']}")
            print(f"Email: {dados['email']}")
            print(f"Data de nascimento: {dados['data_nascimento']}")
    else:
        print('Nenhum aluno cadastrado.')

def mostrar_aluno(matricula):
    if matricula in alunos:
        aluno = alunos[matricula]
        print(f"\nMatrícula: {aluno['matricula']}")
        print(f"Nome: {aluno['nome']}")
        print(f"Email: {aluno['email']}")
        print(f"Data de nascimento: {aluno['data_nascimento']}")
    else:
        print('Matrícula não encontrada.')

def menu():
    print("\n---- Sistema de Cadastro de Alunos ----")
    print("1 - Cadastrar aluno")
    print("2 - Atualizar aluno")
    print("3 - Remover aluno")
    print("4 - Listar todos os alunos")
    print("5 - Mostrar dados de um aluno específico")
    print("--------------------------------------")
