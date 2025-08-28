# 📖 Exemplos de Uso - Jogo da Velha

## 🎮 Exemplo de Execução Completa

### Cenário 1: Partida com Vitória do Jogador X

```
Rodada 0
_1_|_2_|_3_
_4_|_5_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador X.
5

Rodada 1
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador O.
1

Rodada 2
_O_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador X.
3

Rodada 3
_O_|_2_|_X_
_4_|_X_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador O.
9

Rodada 4
_O_|_2_|_X_
_4_|_X_|_6_
_7_|_8_|_O_
Informe a posição que deseja marcar, jogador X.
7

Vitória do jogador X

Totais de vitórias do Jogador X: 1
Totais de vitórias do Jogador O: 0
Totais de Empates: 0
Deseja continuar? S ou N
```

### Cenário 2: Partida com Empate

```
Rodada 8
_X_|_O_|_X_
_O_|_X_|_O_
_X_|_O_|_9_
Informe a posição que deseja marcar, jogador X.
9

Este jogo terminou em empate.

Totais de vitórias do Jogador X: 1
Totais de vitórias do Jogador O: 0
Totais de Empates: 1
Deseja continuar? S ou N
```

### Cenário 3: Posição Já Ocupada

```
Rodada 2
_X_|_O_|_3_
_4_|_5_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador X.
1
Posição 1 já marcada, pressione qualquer tecla para jogar novamente

Rodada 2
_X_|_O_|_3_
_4_|_5_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador X.
```

### Cenário 4: Posição Inválida

```
Rodada 1
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador O.
10
Posição inválida, pressione qualquer tecla para jogar novamente.

Rodada 1
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador O.
```

## 🏆 Condições de Vitória - Exemplos

### Vitória por Linha Horizontal

```
Vitória na linha 1:     Vitória na linha 2:     Vitória na linha 3:
_X_|_X_|_X_            _1_|_2_|_3_            _1_|_2_|_3_
_4_|_5_|_6_            _X_|_X_|_X_            _4_|_5_|_6_
_7_|_8_|_9_            _7_|_8_|_9_            _X_|_X_|_X_
```

### Vitória por Coluna Vertical

```
Vitória na coluna 1:    Vitória na coluna 2:    Vitória na coluna 3:
_X_|_2_|_3_            _1_|_X_|_3_            _1_|_2_|_X_
_X_|_5_|_6_            _4_|_X_|_6_            _4_|_5_|_X_
_X_|_8_|_9_            _7_|_X_|_9_            _7_|_8_|_X_
```

### Vitória por Diagonal

```
Diagonal Principal:     Diagonal Secundária:
_X_|_2_|_3_            _1_|_2_|_X_
_4_|_X_|_6_            _4_|_X_|_6_
_7_|_8_|_X_            _X_|_8_|_9_
```

## 🎯 Estratégias de Jogo

### Posições Estratégicas

1. **Centro (posição 5)**: Melhor primeira jogada - controla 4 linhas de vitória
2. **Cantos (posições 1, 3, 7, 9)**: Segunda melhor opção - controla 3 linhas cada
3. **Meios (posições 2, 4, 6, 8)**: Menos estratégicas - controla 2 linhas cada

### Exemplo de Estratégia Defensiva

```
Jogada 1 (X): Centro
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_

Jogada 2 (O): Canto (defesa)
_O_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_

Jogada 3 (X): Canto oposto
_O_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_X_

Jogada 4 (O): Deve bloquear posição 7!
_O_|_2_|_3_
_4_|_X_|_6_
_O_|_8_|_X_
```

## 🔄 Fluxo de Trabalho do Sistema

### Início de Nova Partida
1. Tabuleiro resetado para posições 1-9
2. Jogador X sempre começa
3. Contador de rodadas resetado
4. Flags de controle resetadas

### Durante uma Jogada
1. Tela limpa automaticamente
2. Tabuleiro atual exibido
3. Prompt para jogador atual
4. Validação da entrada
5. Atualização do tabuleiro (se válida)
6. Verificação de vitória/empate
7. Alternância de jogador (se jogo continua)

### Final de Partida
1. Mensagem de vitória ou empate
2. Atualização do placar geral
3. Exibição do placar acumulado
4. Prompt para continuar ou sair

## 🐛 Tratamento de Erros

### Tipos de Erro Tratados:
- ✅ **Posição fora do intervalo**: Números < 1 ou > 9
- ✅ **Posição ocupada**: Tentativa de jogar em casa já marcada
- ✅ **Entrada não numérica**: Caracteres que não são números
- ✅ **Resposta inválida**: No prompt S/N de continuar

### Comportamento do Sistema:
- **Erro de posição**: Mantém o mesmo jogador, solicita nova entrada
- **Posição ocupada**: Mantém o mesmo jogador, solicita nova entrada
- **Resposta inválida**: Loop até resposta válida (S ou N)

## 📊 Sistema de Pontuação

### Contadores Mantidos:
```
Totais de vitórias do Jogador X: 3
Totais de vitórias do Jogador O: 1
Totais de Empates: 2
```

### Persistência:
- Placar mantido durante toda a sessão
- Reset apenas quando programa é reiniciado
- Exibido ao final de cada partida

## 🧪 Casos de Teste Recomendados

### Teste 1: Funcionalidade Básica
1. Execute o programa
2. Jogue uma partida completa
3. Verifique se a vitória é detectada corretamente
4. Confirme atualização do placar

### Teste 2: Tratamento de Erros
1. Digite posições inválidas (0, 10, -1, abc)
2. Tente jogar em posições ocupadas
3. Verifique mensagens de erro apropriadas

### Teste 3: Empate
1. Preencha o tabuleiro sem formar linha de 3
2. Verifique detecção de empate
3. Confirme incremento do contador de empates

### Teste 4: Partidas Múltiplas
1. Complete uma partida
2. Escolha continuar (S)
3. Verifique reset do tabuleiro
4. Confirme manutenção do placar
5. Teste opção de sair (N)

### Teste 5: Todas as Condições de Vitória
- Teste vitória por linha (3 casos)
- Teste vitória por coluna (3 casos)  
- Teste vitória por diagonal (2 casos)

---

*Exemplos atualizados para o projeto Jogo da Velha v2.0 - Versão Completa*

---

*Exemplos criados para o projeto Jogo da Velha v1.0*
