# 🎮 Jogo da Velha

Um jogo da velha (tic-tac-toe) implementado em Python, desenvolvido como projeto de estudos em Fundamentos de Programação.

## 📋 Descrição

Este projeto implementa o clássico jogo da velha para dois jogadores, onde o objetivo é conseguir três símbolos iguais (X ou O) em linha, coluna ou diagonal em um tabuleiro 3x3.

## 🎯 Funcionalidades

- ✅ Tabuleiro 3x3 interativo
- ✅ Alternância automática entre jogadores (X e O)
- ✅ Validação de posições ocupadas
- ✅ Controle de vitórias, derrotas e empates
- ✅ Interface simples via terminal

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

## 🗂️ Estrutura do projeto

```
jogodavelha/
├── jogodavelha.py            # Arquivo principal com a lógica do jogo
├── README.md                 # Documentação principal do projeto
├── DOCUMENTACAO_TECNICA.md   # Documentação técnica detalhada
├── EXEMPLOS.md               # Exemplos de uso e execução
└── .gitignore                # Arquivos ignorados pelo Git
```

## 📚 Documentação Adicional

- 📋 **[README.md](README.md)** - Documentação principal (este arquivo)
- 🔧 **[DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md)** - Análise técnica do código, arquitetura e melhorias
- 📖 **[EXEMPLOS.md](EXEMPLOS.md)** - Exemplos de uso, casos de teste e cenários de jogo

## ⚙️ Pré-requisitos

- Python 3.x instalado no sistema

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

## 📊 Variáveis do Sistema

O jogo mantém controle de:
- `qtdvitoriasX`: Número de vitórias do jogador X
- `qtdvitoriasO`: Número de vitórias do jogador O  
- `qtdempates`: Número de jogos empatados
- `tab[]`: Array que representa o tabuleiro (posições 0-8)

## 🎯 Mapeamento do Tabuleiro

```
Posições do usuário:     Índices do array:
   1 | 2 | 3               0 | 1 | 2
   4 | 5 | 6               3 | 4 | 5
   7 | 8 | 9               6 | 7 | 8
```

## 🛠️ Melhorias Futuras

- [ ] Implementar verificação de vitória/empate
- [ ] Adicionar loop para múltiples partidas
- [ ] Implementar modo contra computador
- [ ] Melhorar a interface visual
- [ ] Adicionar sistema de placar persistente

## 👨‍� Autor

**Carlos Eduardo Carvalho**
- GitHub: [@CarlosECarvalho](https://github.com/CarlosECarvalho)
- Email: carlos_ferreira@id.uff.br

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do curso de Fundamentos de Programação.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📈 Status do Projeto

🚧 **Em desenvolvimento** - Versão inicial funcional, melhorias planejadas
