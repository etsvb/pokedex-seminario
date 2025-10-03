# <img src="https://i.pinimg.com/originals/d9/cb/c3/d9cbc37ddc1843e3febf945180f60602.gif" width="40"> Pokedex em Python

<img src="https://64.media.tumblr.com/32fb03cdcaad3379e63ed8eb7339b9fe/dc870f3e8d826c15-ce/s400x600/3679cc8b04fdec8e82ae1b9ae02e451d9ad5f70b.gif" width="1000">

| <img src="https://64.media.tumblr.com/ad2b88829d03f9f03e88134a0cfed516/c5a631b42bf6d503-b8/s400x600/29493c58d0f5cecf3ff204b60bea86528a2935fe.gif" alt="Pokedex" width="150"> | Uma aplicação de terminal em **Python 3** que simula uma **Pokedex** com sistema de captura e Box Pokémon, permitindo:<br><br> - **Adicionar** Pokémons novos.<br> - **Listar** todos os Pokémon cadastrados.<br> - **Buscar** Pokémon por nome ou número.<br> - **Capturar** Pokémon com *níveis aleatórios*.<br> - **Guardar** ou descartar cada captura individualmente.<br> - **Remover** Pokémon do Box pelo ID único.<br><br> |
|---------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<img src="https://64.media.tumblr.com/32fb03cdcaad3379e63ed8eb7339b9fe/dc870f3e8d826c15-ce/s400x600/3679cc8b04fdec8e82ae1b9ae02e451d9ad5f70b.gif" width="1000">

Este projeto demonstra o uso de **estruturas de dados dinâmicas** (listas, dicionários e objetos), permitindo adicionar e remover elementos em tempo real.

**Pokédex: Lista encadeada.**

---

 ## <img src="https://64.media.tumblr.com/e7ecce28a79842122e6faf8853183708/f72828b12c6f8d7f-b0/s400x600/bf4a0827f4c8edd3cfe27b1612834a2c6ad6e171.gif" width="50"> Interfaces gráficas usadas

 ![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white) <img src="https://miro.medium.com/v2/1*AIlWq29GeP1eny3wA7aMgA.png" width="80">
 </div>
 
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

##  <img src="https://64.media.tumblr.com/66ebd74acd32a3fd62c26aad77026d0c/130cb53d5c4bca5c-9a/s250x400/63a287d5a2e1b9a8358ba4c683ad3c98f9145214.gif" width="50"> Estrutura de Dados
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

##  Requisitos <img src="https://64.media.tumblr.com/b19aa6cdcf1fb672fb4e7333eb994573/31c486a7eb1b7a6c-f9/s500x750/943d2fe64e5392fa33efa7f90b5d9425e81c2bc6.gif" width="500">

- **Python 3.7+** ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)

---

##  Como Executar  <img src="https://64.media.tumblr.com/65860273016c3b7089dacd1728b1464c/9c78cd16d5cd77b4-bf/s250x400/74ac58099061fc2e6bec3c84c3d45da63f2af503.gif" width="80">
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/pokedex-python.git
   cd pokedex-python

2. Execute o programa
python `pokedex_core.py`

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

