def exibir_tabuleiro(tabuleiro):
    print(tabuleiro[0] + ' | ' + tabuleiro[1] + ' | ' + tabuleiro[2])
    print('--+---+--')
    print(tabuleiro[3] + ' | ' + tabuleiro[4] + ' | ' + tabuleiro[5])
    print('--+---+--')
    print(tabuleiro[6] + ' | ' + tabuleiro[7] + ' | ' + tabuleiro[8])


def verificar_vitoria(tabuleiro):
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
        [0, 4, 8], [2, 4, 6]  # diagonais
    ]

    for vitoria in vitorias:
        a, b, c = vitoria
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != ' ':
            return True

    return False


def jogar():
    tabuleiro = [' '] * 9
    jogador_atual = 'X'
    jogo_acabou = False

    while not jogo_acabou:
        exibir_tabuleiro(tabuleiro)
        posicao = int(input('Digite a posição (0-8): '))

        if tabuleiro[posicao] == ' ':
            tabuleiro[posicao] = jogador_atual

            if verificar_vitoria(tabuleiro):
                exibir_tabuleiro(tabuleiro)
                print('Jogador', jogador_atual, 'venceu!')
                jogo_acabou = True
            elif ' ' not in tabuleiro:
                exibir_tabuleiro(tabuleiro)
                print('O jogo empatou!')
                jogo_acabou = True
            else:
                jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print('Posição inválida. Tente novamente.')

    print('Fim do jogo.')


jogar()
