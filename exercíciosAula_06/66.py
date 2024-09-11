import os
#from operacoes import menu (operacoes.menu() se torna apenas menu() )
#import operacoes as op --> importa renomeando para chamar as funções com menos letras1
import operacoes

operacao = 'sim'

while operacao == 'sim':
    operacoes.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('Que nome deseja cadastrar? ')
            operacoes.cadastrar_nome(nome)
        case 2:
            nome = input('que nome deseja atualizar? ')
            novo_nome = input('Qual será o novo nome? ')
            
            operacoes.atualiza_nome(nome, novo_nome)
        case 3:
            nome = input('Que nome deseja remover? ')
            operacoes.excluir_nome(nome)
        case 4:
            operacoes.listar_nomes()
        case _:
            print('opção inválida')

    operacao = input('Deseja realizar outra operacao? ').lower()
    os.system('clear')

    if operacao != 'sim':
        break
