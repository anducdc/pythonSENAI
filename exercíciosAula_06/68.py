import os
import ope

def main():
    operacao = 'sim'

    while operacao == 'sim':
        ope.menu()
        try:
            opcao = int(input('Informe a ação desejada: '))
        except ValueError:
            print("Opção inválida. Por favor, insira um número.")
            continue

        if opcao == 1:
            ope.cadastrar_aluno()
        elif opcao == 2:
            matricula = input('Informe a matrícula do aluno que deseja atualizar: ')
            ope.atualizar_aluno(matricula)
        elif opcao == 3:
            matricula = input('Informe a matrícula do aluno que deseja remover: ')
            ope.excluir_aluno(matricula)
        elif opcao == 4:
            ope.listar_alunos()
        elif opcao == 5:
            matricula = input('Informe a matrícula do aluno que deseja visualizar: ')
            ope.mostrar_aluno(matricula)
        else:
            print('Opção inválida.')

        operacao = input('Deseja realizar outra operação? (sim/não): ').lower()
        os.system('clear')

        if operacao != 'sim':
            break

if __name__ == "__main__":
    main()
