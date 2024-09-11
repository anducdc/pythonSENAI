import velha_funcoes2 as jv

def main():
    while True:
        jogador = 'X'
        vencedor = False
        empate = False
        jv.resetar_tabuleiro()

        while not vencedor and not empate:
            jv.desenhar_tabuleiro()

            jogada = int(input(f'Onde deseja jogar, jogador {jogador}? '))

            while not jv.jogada_valida(jogada):
                jogada = int(input('Jogada inválida! Escolha outro lugar: '))

            jv.jogar(jogada, jogador)
            jv.desenhar_tabuleiro()

            vencedor = jv.verifica_vitoria()
            if vencedor:
                print(f'O jogador {jogador} venceu!')
                break

            empate = jv.verifica_empate()
            if empate:
                print('O jogo terminou em empate!')
                break

            jogador = jv.troca_jogador(jogador)

        nova_partida = input('Deseja jogar outra partida? (sim/não): ').lower()
        if nova_partida != 'sim':
            break

if __name__ == "__main__":
    main()
