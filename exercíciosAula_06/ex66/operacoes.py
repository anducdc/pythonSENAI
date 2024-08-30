nomes = []

def menu():
    opcoes = ['cadastre o nome', 'atualize o nome', 'exclua nome', 'listar nomes']

    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')

def listar_nomes():
    for indice, nome in enumerate(nomes):
        print(f'{indice + 1} - {nome}')

def cadastrar_nome(nome):
    nomes.append(nome)

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome

def excluir_nome(nome):
    nomes.remove(nome)