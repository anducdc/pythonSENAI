from os import system

tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def desenhar_tabuleiro():
    system('clear')
    for indice, casa in enumerate(tabuleiro):
        if indice % 3 == 2:
            print(casa)
        else:
            print(casa, end=' | ')

def jogar(jogada, jogador):
    tabuleiro[jogada] = jogador

def troca_jogador(jogador):
    return 'O' if jogador == 'X' else 'X'

def verifica_vitoria():
    combinacoes = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                   (0, 3, 6), (1, 4, 7), (2, 5, 8),
                   (0, 4, 8), (2, 4, 6)]

    for (a, b, c) in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return True
    return False

def verifica_empate():
    return all(isinstance(casa, str) for casa in tabuleiro)

def jogada_valida(jogada):
    return 0 <= jogada <= 8 and isinstance(tabuleiro[jogada], int)

def resetar_tabuleiro():
    global tabuleiro
    tabuleiro = [0, 1, 2, 3, 4, 5, 6, 7, 8]
