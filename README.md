# <img src="https://i.pinimg.com/originals/d9/cb/c3/d9cbc37ddc1843e3febf945180f60602.gif" width="40"> Pokedex em Python

Uma aplicação de terminal em **Python 3** que simula uma **Pokedex** com sistema de captura e **Box Pokémon**, permitindo:
-  **Listar** todos os Pokémon cadastrados (mesmo os bloqueados).
-  **Buscar** Pokémon por nome ou número.
-  **Capturar** Pokémon com **níveis aleatórios**.
-  **Guardar ou descartar** cada captura individualmente.
-  **Remover** Pokémon do Box pelo ID único.

Este projeto demonstra o uso de **estruturas de dados dinâmicas** (listas, dicionários e objetos), permitindo adicionar e remover elementos em tempo real.

---

 ## <img src="https://i.pinimg.com/originals/3c/06/59/3c06599306cca1e170ce8df10949cf91.gif" width="40">  Funcionalidades

 **Pokedex**  
- Mostra todas as espécies pré-cadastradas.  
- Desbloqueia automaticamente quando um Pokémon é capturado pela primeira vez.

 **Captura**  
- Cada captura gera um **nível aleatório** (entre 5 e 50).  
- Permite **capturar várias cópias** da mesma espécie.  
- O jogador escolhe guardar no **Box** ou descartar.

 **Box Pokémon**  
- Lista todos os Pokémon capturados individualmente.  
- Cada captura possui um **ID único**, permitindo remoção específica.

---

##  Estrutura de Dados
O projeto utiliza:
- **Dicionário (`dict`)**: para armazenar as espécies da Pokedex, permitindo buscas rápidas (`numero → Pokemon`).
- **Lista (`list`)**: para guardar capturas individuais, que podem ser adicionadas ou removidas dinamicamente.
- **Classes**: para modelar espécies (`Pokemon`) e capturas (`Captura`), separando conceitos de **espécie** e **indivíduo**.

---
##  <img src="https://i.pinimg.com/originals/46/04/8d/46048da1b8533b654955f33e5cf40438.gif" width="80"> Pokémon Pré-Cadastrados

| Nº  | Nome       | Tipo      | Gif       |
|----:|------------|-----------|-----------|
| 001 | Bulbasaur  | Planta    |<img src="https://i.pinimg.com/originals/e5/35/ad/e535ad30166d0121722774e0275bef3f.gif" width="80"> |
| 004 | Charmander | Fogo      |<img src="https://i.pinimg.com/originals/48/1e/af/481eafa3a380198012f80595c0dafeec.gif" width="50"> |
| 025 | Pikachu    | Elétrico  |<img src="https://i.pinimg.com/originals/a7/a8/d0/a7a8d06c754cfbbbc37e64cb118c513c.gif" width="50"> |

*(Outros Pokémon também estão incluídos no código.)*

---

##  Requisitos
- **Python 3.7+** ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)

---

##  Como Executar
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/pokedex-python.git
   cd pokedex-python

2. Execute o programa
python `pokedex_cute.py`

3. Use o menu interativo
```bash
=========================
      MENU POKEDEX
=========================
1. Capturar Pokémon
2. Mostrar Pokedex
3. Mostrar Box
4. Remover Pokémon da Box
5. Buscar Pokémon
0. Sair
--------------------------
Digite sua escolha (ou 2 para ver as opções)
```
Exemplo de Uso
 ```bash
=== MENU POKEDEX ===

1 - Capturar Pokémon

Qual o número do Pokémon para tentar capturar?: 001

Deseja guardar o Pokémon na Box se captura for bem-sucedida? (S/N): s
Parabéns! Você capturou e guardou um Bulbasour de Nível 29!
````

3 - Listar Box
```bash
 --- POKÉMONS NA BOX ---
ID: 6uwuew2 | #001 Bulbasaur Lv.29
----------------------------

