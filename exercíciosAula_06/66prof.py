nomes = []

operacao = 'sim'

while operacao == 'sim':

    print('1 cadastre o nome')
    print('2 atualize o nome')
    print('3 exclua nome')
    print('4 listar nomes')

    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('Que nome deseja cadastrar? ')
            nomes.append(nome)
        case 2:
            nome = input('que nome deseja atualizar? ')
            novo_nome = input('Qual será o novo nome? ')
            
            nomes[nomes.index(nome)] = novo_nome
        case 3:
            nome = input('Que nome deseja remover? ')
            nomes.remove(nome)
        case 4:
            for indice, nome in enumerate(nomes, start = 1):
                print(indice, nome)
        case _:
            print('opção inválida')

    operacao = input('deseja realizar outra operacao? ').lower()

    if operacao != 'sim':
        break
