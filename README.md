# 📜 Pokedex em Python

Uma aplicação de terminal em **Python 3** que simula uma **Pokedex** com sistema de captura e **Box Pokémon**, permitindo:
-  **Listar** todos os Pokémon cadastrados (mesmo os bloqueados).
-  **Buscar** Pokémon por nome ou número.
-  **Capturar** Pokémon com **níveis aleatórios**.
-  **Guardar ou descartar** cada captura individualmente.
-  **Remover** Pokémon do Box pelo ID único.

Este projeto demonstra o uso de **estruturas de dados dinâmicas** (listas, dicionários e objetos), permitindo adicionar e remover elementos em tempo real.

---

##  Funcionalidades
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

##  Pokémon Pré-Cadastrados
| Nº  | Nome       | Tipo      |
|----:|------------|-----------|
| 001 | Bulbasaur  | Planta    |
| 004 | Charmander | Fogo      |
| 025 | Pikachu    | Elétrico  |

*(Outros Pokémon também estão incluídos no código.)*

---

##  Requisitos
- **Python 3.7+**

---

##  Como Executar
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/pokedex-python.git
   cd pokedex-python

2. Execute o programa
python pokedex.py

3. Use o menu interativo
```bash
1 → Listar Pokedex

2 → Capturar Pokémon

3 → Listar Box

4 → Remover Pokémon do Box

5 → Buscar por número

6 → Buscar por nome

0 → Sair
```
Exemplo de Uso
 ```bash
=== MENU POKEDEX ===

2 - Capturar Pokémon

Digite o número do Pokémon: 25

🎉 Pikachu foi DESBLOQUEADO na Pokedex!

🌟 Você encontrou um Pikachu Lv.22!

Deseja guardar no Box? (s/n): s

✅ Pikachu Lv.22 foi adicionado ao Box (ID a1b2c3)!
````

3 - Listar Box
```bash
 BOX POKÉMON:
1. [a1b2c3] #025 - Pikachu Lv.22 (Tipo Elétrico)

