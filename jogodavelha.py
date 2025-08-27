"""
JOGO DA VELHA (TIC-TAC-TOE)
===========================

Autor: Carlos Eduardo Carvalho
Email: carlos_ferreira@id.uff.br
Curso: Fundamentos de Programação
Data: Agosto 2025

Descrição:
----------
Este programa implementa um jogo da velha simples para dois jogadores.
O tabuleiro é representado por uma lista de 9 elementos, onde cada
posição corresponde a uma casa do tabuleiro 3x3.

Mapeamento do tabuleiro:
Posições mostradas ao usuário: 1-9
Índices da lista (tab): 0-8

 1 | 2 | 3     -->     0 | 1 | 2
 4 | 5 | 6     -->     3 | 4 | 5  
 7 | 8 | 9     -->     6 | 7 | 8
"""

# Variáveis de controle do placar
qtdvitoriasX = 0  # Contador de vitórias do jogador X
qtdvitoriasO = 0  # Contador de vitórias do jogador O
qtdempates = 0    # Contador de empates

# Inicialização do tabuleiro
# Cada posição contém o número que o usuário deve digitar para jogá-la
tab = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Exibição do tabuleiro inicial
print("=== JOGO DA VELHA ===")
print("Posições disponíveis:")
print('_' + tab[0] + '_|_' + tab[1] + '_|_' + tab[2] + '_')
print('_' + tab[3] + '_|_' + tab[4] + '_|_' + tab[5] + '_')
print('_' + tab[6] + '_|_' + tab[7] + '_|_' + tab[8] + '_')
print()

# Definição do jogador inicial
jogadoratual = 'X'  # Jogador X sempre começa

# Entrada do usuário
print(f"Vez do jogador: {jogadoratual}")
pos = int(input('Informe a posição que deseja marcar (1-9): '))

# Validação e processamento da jogada
# Verifica se a posição escolhida está livre e faz a jogada

# PRIMEIRA LINHA (posições 1, 2, 3 -> índices 0, 1, 2)
if pos == 1 and tab[0] == '1':
    tab[0] = jogadoratual
elif pos == 2 and tab[1] == '2':
    tab[1] = jogadoratual
elif pos == 3 and tab[2] == '3':
    tab[2] = jogadoratual

# SEGUNDA LINHA (posições 4, 5, 6 -> índices 3, 4, 5)
elif pos == 4 and tab[3] == '4':
    tab[3] = jogadoratual
elif pos == 5 and tab[4] == '5':
    tab[4] = jogadoratual
elif pos == 6 and tab[5] == '6':
    tab[5] = jogadoratual

# TERCEIRA LINHA (posições 7, 8, 9 -> índices 6, 7, 8)
elif pos == 7 and tab[6] == '7':
    tab[6] = jogadoratual
elif pos == 8 and tab[7] == '8':
    tab[7] = jogadoratual
elif pos == 9 and tab[8] == '9':
    tab[8] = jogadoratual

# Validação de entrada inválida
elif (pos < 1) or (pos > 9):
    print('Posição inválida! Digite um número entre 1 e 9.')
else:
    print('Posição já ocupada! Escolha outra posição.')

# Exibição do tabuleiro atualizado
print("\nTabuleiro atualizado:")
print('_' + tab[0] + '_|_' + tab[1] + '_|_' + tab[2] + '_')
print('_' + tab[3] + '_|_' + tab[4] + '_|_' + tab[5] + '_')
print('_' + tab[6] + '_|_' + tab[7] + '_|_' + tab[8] + '_')