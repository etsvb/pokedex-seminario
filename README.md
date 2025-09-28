# Pokédex Avançada em Python 

Uma Pokédex interativa construída em **Python** utilizando **estruturas de dados dinâmicas**.  
O projeto permite gerenciar Pokémon, criar times, batalhar contra NPCs e Pokémon selvagens, e capturar novos Pokémon.

---

## Funcionalidades

- Adicionar, remover e listar Pokémon na Pokédex  
- Criar e gerenciar **múltiplos times** de Pokémon  
- Adicionar/remover Pokémon em times  
- Batalhar com times contra Pokémon selvagens  
- Ganhar Pokémon sorteados após vitórias  
- Submenus interativos sem reiniciar o menu principal  

---

## Estrutura do Projeto

│pokedex-avancada/


├─ main.py # Código principal da Pokédex

├─ README.md # Este arquivo

└─ .gitignore # (Opcional)


---

## Classes e Funções

| Classe/Função           | Descrição |
|-------------------------|-----------|
| `Pokemon`               | Representa cada Pokémon com `nome`, `tipo`, `nivel` e `next` (para lista encadeada) |
| `Pokedex`               | Lista encadeada de Pokémon. Métodos: `adicionar()`, `remover()`, `listar()`, `buscar()` |
| `Time`                  | Lista encadeada de Pokémon de um time. Métodos: `adicionar_pokemon()`, `listar()`, `get_pokemons()` |
| `SistemaTimes`          | Gerencia múltiplos times. Métodos: `criar_time()`, `listar_times()`, `selecionar_time()` |
| `gerar_npc()`           | Gera Pokémon selvagem aleatório para batalhas |
| `sorteio_pokemon()`     | Gera Pokémon aleatório como prêmio de vitória |
| `batalha_de_times()`    | Simula batalha entre um time e um Pokémon selvagem |

---

## Estruturas de Dados Usadas

| Estrutura          | Onde é usada                      | Função                                                                 |
|-------------------|----------------------------------|------------------------------------------------------------------------|
| Lista encadeada     | Pokédex e Times                   | Armazenar Pokémon dinamicamente, permitindo adicionar/remover fácil.   |
| Lista simples       | SistemaTimes                       | Armazena múltiplos times.                                             |
| Funções aleatórias | `random.randint()`                | Determinar resultado de batalhas e Pokémon sorteados.                 |

---

## Fluxo de Navegação do Programa


graph TD
A[Menu Principal] --> B[Pokédex]

A --> C[Times e Batalhas]

B --> D[Adicionar Pokémon]

B --> E[Remover Pokémon]

B --> F[Listar Pokémon]

C --> G[Criar Time]

C --> H[Adicionar Pokémon a Time]

C --> I[Listar Times]

C --> J[Batalhar com Time]

## Exemplos de Uso
Menu Principal

=== Menu Principal da Pokédex ===
1. Adicionar Pokémon à Pokédex
2. Remover Pokémon da Pokédex
3. Listar Pokémon
4. Menu de Times e Batalhas
0. Sair

## Criar Time
Nome do novo time: Time Pikachu
Time Time Pikachu criado!

## Adicionar Pokémon ao Time
Nome do Pokémon da Pokédex: Pikachu

Pikachu adicionado ao time Time Pikachu!

## Batalha de Time
Um Pokémon selvagem apareceu: Rattata (Nv 4) - Tipo: Normal

Pikachu entra na batalha!

Pikachu venceu a batalha!

Você ganhou Eevee do sorteio e adicionou à Pokédex!

## Listar Time
Time Time Pikachu 
Pikachu - Tipo: Elétrico - Nível: 5
