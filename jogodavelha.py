import os

def tabuleiro(tabuleiro):
    print('_' + tabuleiro[0] + '_|_' + tabuleiro[1] + '_|_' + tabuleiro[2] + '_')
    print('_' + tabuleiro[3] + '_|_' + tabuleiro[4] + '_|_' + tabuleiro[5] + '_')
    print('_' + tabuleiro[6] + '_|_' + tabuleiro[7] + '_|_' + tabuleiro[8] + '_')


def jogada(posicao, jogadorAtual, verificarJogada):
    # primeira linha
    if posicao == '1' and tab[0] == '1':
        tab[0] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    elif posicao == '2' and tab[1] == '2':
        tab[1] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    elif posicao == '3' and tab[2] == '3':
        tab[2] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    # segunda linha
    elif posicao == '4' and tab[3] == '4':
        tab[3] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    elif posicao == '5' and tab[4] == '5':
        tab[4] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    elif posicao == '6' and tab[5] == '6':
        tab[5] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    # terceira linha
    elif posicao == '7' and tab[6] == '7':
        tab[6] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    elif posicao == '8' and tab[7] == '8':
        tab[7] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    elif posicao == '9' and tab[8] == '9':
        tab[8] = jogadorAtual
        verificarJogada = True
        return verificarJogada
    
    if verificarJogada == False and (posicao in '123456789'):
        print(f'Posição {posicao} já marcada, pressione qualquer tecla para jogar novamente')
        input()
        verificarJogada = False
        return verificarJogada
    
    if posicao not in '123456789':
        print('Posição inválida, pressione qualquer tecla para jogar novamente.')
        input()
        verificarJogada = False
        return verificarJogada


def verificarvitoria(tabuleiro, vitoria):
    if tabuleiro[0] == tabuleiro[1] and tabuleiro[1] == tabuleiro[2]:
        vitoria = True
    elif tabuleiro[3] == tabuleiro[4] and tabuleiro[4] == tabuleiro[5]:
        vitoria = True
    elif tabuleiro[6] == tabuleiro[7] and tabuleiro[7] == tabuleiro[8]:
        vitoria = True
    elif tabuleiro[0] == tabuleiro[4] and tabuleiro[4] == tabuleiro[8]:
        vitoria = True
    elif tabuleiro[2] == tabuleiro[4] and tabuleiro[4] == tabuleiro[6]:
        vitoria = True
    elif tabuleiro[0] == tabuleiro[3] and tabuleiro[3] == tabuleiro[6]:
        vitoria = True
    elif tabuleiro[1] == tabuleiro[4] and tabuleiro[4] == tabuleiro[7]:
        vitoria = True
    elif tabuleiro[1] == tabuleiro[4] and tabuleiro[4] == tabuleiro[7]:
        vitoria = True
    elif tabuleiro[2] == tabuleiro[5] and tabuleiro[5] == tabuleiro[8]:
        vitoria = True
    
    return vitoria


def trocaJogador(jogador):
    if jogador == 'X':
        jogador = 'O'
        return jogador
    else:
        jogador = 'X'
        return jogador


vitoria, verificarJogada, continuar = False, False, True
qtdVitoriasX, qtdVitoriasO, qtdEmpates, rodadas = 0, 0, 0, 0
tab = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
jogadorAtual, resp = 'X', 'a'

while continuar == True:
    while vitoria == False:
        os.system("cls")
        tabuleiro(tab)
        pos = (input(f'Rodada {rodadas}\nInforme a posição que deseja marcar, jogador {jogadorAtual}.\n'))
        verificarJogada = jogada(pos, jogadorAtual, verificarJogada)
        
        if verificarJogada == True or rodadas == 9:
            vitoria = verificarvitoria(tab, vitoria)
            rodadas += 1
            if vitoria == True:
                if jogadorAtual == 'X':
                    qtdVitoriasX += 1
                elif jogadorAtual == 'O':
                    qtdVitoriasO += 1
                print(f'Vitória do jogador {jogadorAtual}')
                break
            elif rodadas == 9:
                qtdEmpates += 1
                print(f'Este jogo terminou em empate.')
                break
            jogadorAtual = trocaJogador(jogadorAtual)
        
        verificarJogada = False
    
    os.system("cls")
    tabuleiro(tab)
    print(f'Totais de vitórias do Jogador X: {qtdVitoriasX}\nTotais de vitórias do Jogador O: {qtdVitoriasO}\nTotais de Empates: {qtdEmpates}')
    
    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? S ou N\n').upper()
        if resp == 'N':
            continuar = False
            break
        elif resp == 'S':
            vitoria = False
            tab = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            rodadas = 0
            resp = 'a'
            jogadorAtual = 'X'
            continuar = True
            break
        else:
            print('Resposta inválida, pressione qualquer tecla para responder novamente')
            input()