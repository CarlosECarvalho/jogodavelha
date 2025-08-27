# 📖 Exemplos de Uso - Jogo da Velha

## 🎮 Exemplo de Execução

### Cenário 1: Jogada Válida

```
=== JOGO DA VELHA ===
Posições disponíveis:
_1_|_2_|_3_
_4_|_5_|_6_
_7_|_8_|_9_

Vez do jogador: X
Informe a posição que deseja marcar (1-9): 5

Tabuleiro atualizado:
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_
```

### Cenário 2: Posição Inválida

```
=== JOGO DA VELHA ===
Posições disponíveis:
_1_|_2_|_3_
_4_|_5_|_6_
_7_|_8_|_9_

Vez do jogador: X
Informe a posição que deseja marcar (1-9): 10
Posição inválida! Digite um número entre 1 e 9.

Tabuleiro atualizado:
_1_|_2_|_3_
_4_|_5_|_6_
_7_|_8_|_9_
```

### Cenário 3: Posição Já Ocupada

```
=== JOGO DA VELHA ===
Posições disponíveis:
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_

Vez do jogador: O
Informe a posição que deseja marcar (1-9): 5
Posição já ocupada! Escolha outra posição.

Tabuleiro atualizado:
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_
```

## 🎯 Estratégias de Jogo

### Posições Estratégicas

1. **Centro (posição 5)**: Melhor primeira jogada
2. **Cantos (posições 1, 3, 7, 9)**: Segunda melhor opção
3. **Meios (posições 2, 4, 6, 8)**: Menos estratégicas

### Exemplo de Jogo Completo (Conceitual)

```
Jogada 1 (X): Centro
_1_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_

Jogada 2 (O): Canto
_O_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_9_

Jogada 3 (X): Canto oposto
_O_|_2_|_3_
_4_|_X_|_6_
_7_|_8_|_X_
```

## ⚠️ Limitações Atuais

- ❌ Aceita apenas uma jogada por execução
- ❌ Não verifica condições de vitória
- ❌ Não alterna jogadores automaticamente
- ❌ Não permite reiniciar o jogo

## 🔄 Fluxo de Trabalho Recomendado

1. Execute o programa: `python jogodavelha.py`
2. Observe o tabuleiro inicial
3. Digite uma posição válida (1-9)
4. Verifique o resultado
5. Para continuar jogando, execute novamente

## 🐛 Tratamento de Erros

### Tipos de Erro Tratados:
- **Posição fora do intervalo**: Números < 1 ou > 9
- **Posição ocupada**: Tentativa de jogar em casa já marcada

### Tipos de Erro NÃO Tratados:
- **Entrada não numérica**: Letras ou símbolos causarão erro
- **Entrada vazia**: Pressionar Enter sem digitar número

### Exemplo de Erro Não Tratado:
```python
Informe a posição que deseja marcar (1-9): abc
ValueError: invalid literal for int() with base 10: 'abc'
```

## 📝 Notas para Desenvolvimento

### Para Testar o Programa:
1. Teste posições válidas (1-9)
2. Teste posições inválidas (0, 10, -1)
3. Teste entradas não numéricas
4. Verifique a formatação do tabuleiro

### Para Melhorar:
1. Adicionar try/except para entradas inválidas
2. Implementar loop para múltiplas jogadas
3. Adicionar verificação de vitória
4. Melhorar a interface visual

---

*Exemplos criados para o projeto Jogo da Velha v1.0*
