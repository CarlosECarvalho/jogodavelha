# 🎮 Jogo da Velha

Um jogo da velha (tic-tac-toe) **completo e funcional** implementado em Python, desenvolvido como projeto de estudos em Fundamentos de Programação.

## 📋 Descrição

Este projeto implementa o clássico jogo da velha para dois jogadores, onde o objetivo é conseguir três símbolos iguais (X ou O) em linha, coluna ou diagonal em um tabuleiro 3x3. O jogo inclui sistema completo de partidas múltiplas, contagem de pontos e interface interativa.

## 🎯 Funcionalidades

- ✅ **Tabuleiro 3x3 interativo** com exibição clara das posições
- ✅ **Alternância automática entre jogadores** (X e O)
- ✅ **Validação completa de jogadas** (posições válidas e disponíveis)
- ✅ **Detecção automática de vitória** (linhas, colunas e diagonais)
- ✅ **Detecção de empate** quando todas as posições são preenchidas
- ✅ **Sistema de pontuação** com contagem de vitórias e empates
- ✅ **Partidas múltiplas** com opção de continuar jogando
- ✅ **Interface limpa** que limpa a tela a cada jogada
- ✅ **Tratamento de erros** para entradas inválidas

## 🎮 Como jogar

1. Execute o arquivo `jogodavelha.py`
2. O tabuleiro será exibido com números de 1 a 9 representando as posições:
   ```
   _1_|_2_|_3_
   _4_|_5_|_6_
   _7_|_8_|_9_
   ```
3. Digite o número da posição onde deseja fazer sua jogada (1-9)
4. O jogo alterna automaticamente entre os jogadores X e O
5. O primeiro jogador sempre é X
6. O jogo detecta automaticamente vitórias e empates
7. Ao final de cada partida, escolha se deseja continuar (S) ou sair (N)
8. O placar é mantido entre as partidas

## 🏆 Condições de Vitória

O jogo detecta vitória nas seguintes situações:
- **Linhas horizontais**: Três símbolos iguais em qualquer linha
- **Colunas verticais**: Três símbolos iguais em qualquer coluna  
- **Diagonais**: Três símbolos iguais na diagonal principal ou secundária

## 🗂️ Estrutura do projeto

```
jogodavelha/
├── jogodavelha.py            # Arquivo principal com a lógica completa do jogo
├── README.md                 # Documentação principal do projeto
├── DOCUMENTACAO_TECNICA.md   # Documentação técnica detalhada
├── EXEMPLOS.md               # Exemplos de uso e execução
└── .gitignore                # Arquivos ignorados pelo Git
```

## 📚 Documentação Adicional

- 📋 **[README.md](README.md)** - Documentação principal (este arquivo)
- 🔧 **[DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)** - Análise técnica do código, arquitetura e estrutura
- 📖 **[EXEMPLOS.md](EXEMPLOS.md)** - Exemplos de uso, casos de teste e cenários de jogo

## ⚙️ Pré-requisitos

- Python 3.x instalado no sistema
- Sistema operacional Windows (para o comando `cls` - pode ser adaptado para outros SOs)

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/CarlosECarvalho/jogodavelha.git
   ```

2. Navegue até o diretório:
   ```bash
   cd jogodavelha
   ```

3. Execute o jogo:
   ```bash
   python jogodavelha.py
   ```

## 🏗️ Arquitetura do Código

### Funções Principais:
- **`tabuleiro()`**: Exibe o tabuleiro formatado
- **`jogada()`**: Processa e valida as jogadas dos jogadores
- **`verificarvitoria()`**: Verifica todas as condições de vitória
- **`trocaJogador()`**: Alterna entre jogadores X e O

### Variáveis de Controle:
- **`qtdVitoriasX/O`**: Contadores de vitórias de cada jogador
- **`qtdEmpates`**: Contador de empates
- **`tab[]`**: Array que representa o estado do tabuleiro
- **`rodadas`**: Contador de jogadas na partida atual

## 🎯 Mapeamento do Tabuleiro

```
Posições do usuário:     Índices do array:
   1 | 2 | 3               0 | 1 | 2
   4 | 5 | 6               3 | 4 | 5
   7 | 8 | 9               6 | 7 | 8
```

## 🔧 Funcionalidades Implementadas

- [x] ✅ **Interface interativa completa**
- [x] ✅ **Validação de jogadas**
- [x] ✅ **Detecção de vitória/empate**
- [x] ✅ **Sistema de pontuação**
- [x] ✅ **Partidas múltiplas**
- [x] ✅ **Alternância de jogadores**
- [x] ✅ **Tratamento de erros**
- [x] ✅ **Interface limpa (clear screen)**

## 🎮 Exemplo de Execução

```
Rodada 2
_X_|_2_|_3_
_4_|_O_|_6_
_7_|_8_|_9_
Informe a posição que deseja marcar, jogador X.

Vitória do jogador X

Totais de vitórias do Jogador X: 1
Totais de vitórias do Jogador O: 0
Totais de Empates: 0
Deseja continuar? S ou N
```

## 👨‍💻 Autor

**Carlos Eduardo Carvalho**
- GitHub: [@CarlosECarvalho](https://github.com/CarlosECarvalho)
- Email: carlos_ferreira@id.uff.br
- Instituição: Universidade Federal Fluminense (UFF)

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso de Fundamentos de Programação.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests
- Adaptar para outros sistemas operacionais

## 📈 Status do Projeto

✅ **Projeto Completo** - Todas as funcionalidades básicas implementadas e funcionais
