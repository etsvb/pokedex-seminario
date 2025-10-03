from pokedex2 import Pokedex

def menu():
    """Exibe o menu de opções."""
    print("\n" + "=" * 30)
    print("      MENU POKEDEX")
    print("=" * 30)
    print("1. Capturar Pokémon")
    print("2. Mostrar Pokedex ")
    print("3. Mostrar Box ")
    print("4. Remover Pokémon da Box")
    print("5. Adicionar Nova Espécie ")
    print("6. Buscar Pokémon")
    print("0. Sair")
    print("-" * 30)


def main():
    nome = input('Olá treinador! Digite seu nome aqui para iniciar sua jornada pokémon em nossa pokédex: ')
    print(f'Seja muito bem-vindo(a), {nome}!')

    escolha = input(f'Deseja entrar na nossa pokédex, {nome}? (s/n) ').strip().lower()

    if escolha != 's':
        print(f"Tudo bem! Até a próxima, {nome}.")
        return

    pokedex = Pokedex()
    print("Pokedex inicializada com 7 Pokémons base.")
    menu()

    while True:
        escolha = input("Digite sua escolha: ").strip()

        if escolha == '1':
            try:
                num = int(input("Qual o número do Pokémon para tentar capturar? "))
                guardar_input = input("Deseja guardar o Pokémon na Box se capturar? (S/N): ").strip().upper()
                guardar = guardar_input == 'S'
                
                resultado, desbloqueado_agora = pokedex.capturar(num, guardar=guardar) 
                
                print(resultado)
                if desbloqueado_agora:
                    print(f"*** NOVO REGISTRO DESBLOQUEADO: {pokedex.pokemons[num].nome} ***")
            except ValueError:
                print("Entrada inválida. Digite um número.")
            except TypeError:
                print("Erro de lógica: O método 'capturar' deve retornar (mensagem, status_desbloqueado).")

        elif escolha == '2':
            print("\n--- REGISTROS DA POKEDEX ---")
            registros = pokedex.mostrar_pokedex()
            for p in registros:
                print(f"#{p['Número']:03d} - {p['Nome']:<10} | Tipo: {p['Tipo']:<8} | Desbloqueado: {p['Desbloqueado']}")
            print("-" * 30)
        
        elif escolha == '3':
            print("\n--- POKÉMONS NO BOX ---")
            box = pokedex.mostrar_box()
            if box:
                for p_capturado in box:
                    print(f"ID: {p_capturado['ID da Captura']} | #{p_capturado['Número']:03d} - {p_capturado['Nome']} Lv.{p_capturado['Nível']}")
            else:
                print("A Box está vazia!")
            print("-" * 30)

        elif escolha == '4':
            id_captura = input("Digite o ID da Captura a ser removida da Box: ").strip()
            print(pokedex.remover_do_box(id_captura))
        
        elif escolha == '5':
            try:
                num = int(input("Número da nova espécie: "))
                nome = input("Nome da nova espécie: ")
                tipo = input("Tipo principal: ")
                print(pokedex.adicionar_pokemon(num, nome, tipo))
            except ValueError:
                print("Entrada inválida para o número.")

        elif escolha == '6':
            busca = input("Buscar por (N)úmero ou (O)ome? ").upper()
            if busca == 'N':
                try:
                    num = int(input("Digite o número do Pokémon: "))
                    print(pokedex.buscar_por_numero(num))
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            elif busca == 'O':
                nome = input("Digite o nome do Pokémon: ")
                print(pokedex.buscar_por_nome(nome))
            else:
                print("Opção de busca inválida.")
            
        elif escolha == '0':
            print("Saindo da Pokedex. Até mais!")
            break
            
        else:
            print("Opção inválida.")
            menu()
            

if __name__ == "__main__":
    main()
