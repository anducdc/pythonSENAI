import velha_funcoes as jv

jogador = 'X'
vencedor = False

while vencedor == False:

    jv.desenhar_tabuleiro()

    jogada = int(input('Onde deseja jogar?\n'))

    jv.jogar(jogada, jogador)

    jv.desenhar_tabuleiro()
    vencedor = jv.verifica_vitoria()
    jogador = jv.troca_jogador(jogador)

jogador = jv.troca_jogador(jogador)
print(f'O jogador{jogador} venceu!')
