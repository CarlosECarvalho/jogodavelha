# Documentação Técnica - Jogo da Velha

## 🏗️ Arquitetura do Código

### Estrutura de Dados

**Tabuleiro (`tab`)**
- Tipo: Lista de strings
- Tamanho: 9 elementos
- Inicialização: `['1', '2', '3', '4', '5', '6', '7', '8', '9']`
- Função: Representa o estado atual do tabuleiro

**Variáveis de Controle**
```python
qtdVitoriasX = 0        # Contador de vitórias do jogador X
qtdVitoriasO = 0        # Contador de vitórias do jogador O  
qtdEmpates = 0          # Contador de empates
jogadorAtual = 'X'      # Jogador atual ('X' ou 'O')
vitoria = False         # Flag de vitória
verificarJogada = False # Flag de validação de jogada
continuar = True        # Flag de controle do loop principal
rodadas = 0             # Contador de jogadas na partida atual
```

### Mapeamento de Posições

O tabuleiro é exibido ao usuário com números de 1 a 9, mas internamente usa índices de 0 a 8:

```
Interface do Usuário:    Índices da Lista:
    1 | 2 | 3               0 | 1 | 2
    4 | 5 | 6               3 | 4 | 5
    7 | 8 | 9               6 | 7 | 8
```

## 🔧 Funções Implementadas

### 1. `tabuleiro(tabuleiro)`
**Propósito**: Exibe o tabuleiro formatado na tela
```python
def tabuleiro(tabuleiro):
    print('_' + tabuleiro[0] + '_|_' + tabuleiro[1] + '_|_' + tabuleiro[2] + '_')
    print('_' + tabuleiro[3] + '_|_' + tabuleiro[4] + '_|_' + tabuleiro[5] + '_')
    print('_' + tabuleiro[6] + '_|_' + tabuleiro[7] + '_|_' + tabuleiro[8] + '_')
```

### 2. `jogada(posicao, jogadorAtual, verificarJogada)`
**Propósito**: Processa e valida as jogadas dos jogadores
- Verifica se a posição está no intervalo válido (1-9)
- Verifica se a posição está disponível
- Marca a posição com o símbolo do jogador
- Retorna flag de validação da jogada

### 3. `verificarvitoria(tabuleiro, vitoria)`
**Propósito**: Verifica todas as condições de vitória
- **Linhas horizontais**: Posições [0,1,2], [3,4,5], [6,7,8]
- **Colunas verticais**: Posições [0,3,6], [1,4,7], [2,5,8]
- **Diagonal principal**: Posições [0,4,8]
- **Diagonal secundária**: Posições [2,4,6]

### 4. `trocaJogador(jogador)`
**Propósito**: Alterna entre jogadores X e O
```python
def trocaJogador(jogador):
    if jogador == 'X':
        jogador = 'O'
        return jogador
    else:
        jogador = 'X'
        return jogador
```

## 🔄 Fluxo de Execução

### 1. **Inicialização**
- Declaração de variáveis de controle
- Criação do tabuleiro inicial
- Definição do jogador inicial (X)

### 2. **Loop Principal do Jogo**
```python
while continuar == True:
    while vitoria == False:
        # Jogada atual
    # Verificação de nova partida
```

### 3. **Fluxo de uma Jogada**
1. Limpa a tela (`os.system("cls")`)
2. Exibe o tabuleiro atual
3. Solicita posição do jogador atual
4. Valida e processa a jogada
5. Verifica vitória ou empate
6. Alterna jogador (se jogo continua)

### 4. **Finalização de Partida**
1. Atualiza contador de vitórias/empates
2. Exibe placar geral
3. Pergunta se deseja continuar
4. Reinicia variáveis se continuar

## 🎯 Análise do Código

### Pontos Fortes
- ✅ **Estrutura modular** com funções bem definidas
- ✅ **Validação completa** de entradas do usuário
- ✅ **Sistema de pontuação** implementado
- ✅ **Interface limpa** com limpeza de tela
- ✅ **Verificação completa** de todas as condições de vitória
- ✅ **Tratamento de empate** quando tabuleiro está cheio
- ✅ **Sistema de partidas múltiplas** funcional
- ✅ **Comentários** organizados por seções

### Características Técnicas
- **Paradigma**: Programação procedural
- **Estruturas de controle**: if/elif/else, while loops
- **Estruturas de dados**: Listas (arrays)
- **Entrada/Saída**: input() e print()
- **Sistema**: Dependente de Windows (`os.system("cls")`)

## 🧪 Casos de Teste

### Entradas Válidas
- ✅ Posições 1-9 em casas livres
- ✅ Resultado: Marca a posição corretamente

### Entradas Inválidas
- ✅ Números fora do intervalo (0, 10, -1)
- ✅ Posições já ocupadas
- ✅ Resultado: Exibe mensagem de erro apropriada

### Condições de Vitória
- ✅ Linhas horizontais (todas testadas)
- ✅ Colunas verticais (todas testadas)
- ✅ Diagonais (principal e secundária)

### Condições de Empate
- ✅ Tabuleiro completo sem vitória
- ✅ Resultado: Incrementa contador de empates

## 🚀 Melhorias Possíveis

### 1. Compatibilidade Multiplataforma
```python
import os
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
```

### 2. Tratamento de Exceções
```python
try:
    pos = input(f'Rodada {rodadas}\nInforme a posição...\n')
    # Validação adicional
except ValueError:
    print("Entrada inválida! Digite apenas números.")
```

### 3. Refatoração da Função de Jogada
```python
def jogada_melhorada(posicao, jogadorAtual, tabuleiro):
    try:
        pos_int = int(posicao)
        if 1 <= pos_int <= 9 and tabuleiro[pos_int-1] == str(pos_int):
            tabuleiro[pos_int-1] = jogadorAtual
            return True
        return False
    except ValueError:
        return False
```

## 📊 Métricas do Projeto

- **Linhas de código**: ~144 linhas
- **Funções**: 4 funções principais
- **Complexidade ciclomática**: Baixa-Média
- **Cobertura de funcionalidades**: 100% das regras do jogo
- **Robustez**: Alta (tratamento de erros básicos)

## 🏆 Funcionalidades Completas

- [x] ✅ **Jogo funcional completo**
- [x] ✅ **Todas as regras implementadas**
- [x] ✅ **Sistema de pontuação**
- [x] ✅ **Partidas múltiplas**
- [x] ✅ **Interface interativa**
- [x] ✅ **Validação de entradas**
- [x] ✅ **Detecção de vitória/empate**

---

*Documentação atualizada para o projeto Jogo da Velha v2.0 - Versão Completa*

## 🚀 Sugestões de Melhorias

### 1. Refatoração das Condições
```python
# Atual (repetitivo)
if pos == 1 and tab[0] == '1':
    tab[0] = jogadoratual
elif pos == 2 and tab[1] == '2':
    tab[1] = jogadoratual
# ... etc

# Sugerido (mais eficiente)
if 1 <= pos <= 9 and tab[pos-1] == str(pos):
    tab[pos-1] = jogadoratual
else:
    print("Posição inválida ou ocupada!")
```

### 2. Função para Exibir Tabuleiro
```python
def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro formatado"""
    print('_' + tabuleiro[0] + '_|_' + tabuleiro[1] + '_|_' + tabuleiro[2] + '_')
    print('_' + tabuleiro[3] + '_|_' + tabuleiro[4] + '_|_' + tabuleiro[5] + '_')
    print('_' + tabuleiro[6] + '_|_' + tabuleiro[7] + '_|_' + tabuleiro[8] + '_')
```

### 3. Verificação de Vitória
```python
def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador atual ganhou"""
    # Linhas
    for i in range(0, 9, 3):
        if all(tabuleiro[i+j] == jogador for j in range(3)):
            return True
    
    # Colunas  
    for i in range(3):
        if all(tabuleiro[i+j*3] == jogador for j in range(3)):
            return True
    
    # Diagonais
    if all(tabuleiro[i*4] == jogador for i in range(3)):
        return True
    if all(tabuleiro[2+i*2] == jogador for i in range(3)):
        return True
    
    return False
```

## 📚 Conceitos de Programação Demonstrados

1. **Estruturas de Dados**: Listas
2. **Estruturas de Controle**: if/elif/else
3. **Entrada/Saída**: input() e print()
4. **Validação de Dados**: Verificação de intervalos
5. **Manipulação de Strings**: Concatenação e comparação
6. **Comentários**: Documentação inline

## 🧪 Casos de Teste

### Entradas Válidas
- Posições 1-9 em casas livres ✅
- Resultado: Marca a posição corretamente

### Entradas Inválidas
- Números fora do intervalo (0, 10, -1) ✅
- Posições já ocupadas ✅
- Resultado: Exibe mensagem de erro

### Limitações Atuais
- ❌ Não testa vitória/empate
- ❌ Não permite múltiplas jogadas
- ❌ Não alterna jogadores automaticamente

---

*Documentação gerada para o projeto Jogo da Velha v1.0*
