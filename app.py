import streamlit as st
from pokedex_core import Pokedex  

if "pokedex" not in st.session_state:
    st.session_state.pokedex = Pokedex()
    st.session_state.nome = None
    st.session_state.iniciado = False

st.title("Pokedex Interativa")

if not st.session_state.iniciado:
    nome = st.text_input("Digite seu nome para iniciar sua jornada Pokémon:")
    if st.button("Iniciar"):
        if nome.strip():
            st.session_state.nome = nome
            st.session_state.iniciado = True
            st.success(f"Seja bem-vindo(a), {nome}!")
        else:
            st.error("Por favor, insira um nome válido.")
else:
    st.sidebar.title("Menu")
    opcao = st.sidebar.radio(
        "Escolha uma opção:",
        ["Capturar Pokémon", "Mostrar Pokedex", "Mostrar Box",
         "Remover Pokémon da Box", "Adicionar Nova Espécie", "Buscar Pokémon", "Sair"]
    )

    pokedex = st.session_state.pokedex

    if opcao == "Capturar Pokémon":
        num = st.number_input("Número do Pokémon:", min_value=1, step=1)
        guardar = st.checkbox("Guardar na Box ao capturar?", value=True)
        if st.button("Capturar"):
            try:
                resultado, desbloqueado_agora = pokedex.capturar(num, guardar=guardar)
                st.write(resultado)
                if desbloqueado_agora:
                    st.success(f"NOVO REGISTRO DESBLOQUEADO: {pokedex.pokemons[num].nome}")
            except Exception as e:
                st.error(f"Erro: {e}")

    elif opcao == "Mostrar Pokedex":
        st.subheader("Registros da Pokedex")
        registros = pokedex.mostrar_pokedex()
        st.table(registros)

    elif opcao == "Mostrar Box":
        st.subheader("Pokémon na Box")
        box = pokedex.mostrar_box()
        if box:
            st.table(box)
        else:
            st.info("A Box está vazia!")

    elif opcao == "Remover Pokémon da Box":
        id_captura = st.text_input("Digite o ID da Captura a ser removida:")
        if st.button("Remover"):
            resultado = pokedex.remover_do_box(id_captura)
            st.write(resultado)

    elif opcao == "Adicionar Nova Espécie":
        num = st.number_input("Número da nova espécie:", min_value=1, step=1)
        nome = st.text_input("Nome da nova espécie:")
        tipo = st.text_input("Tipo principal:")
        if st.button("Adicionar"):
            try:
                resultado = pokedex.adicionar_pokemon(num, nome, tipo)
                st.success(resultado)
            except Exception as e:
                st.error(f"Erro: {e}")

    elif opcao == "Buscar Pokémon":
        busca = st.radio("Buscar por:", ["Número", "Nome"])
        if busca == "Número":
            num = st.number_input("Digite o número do Pokémon:", min_value=1, step=1)
            if st.button("Buscar por número"):
                st.write(pokedex.buscar_por_numero(num))
        else:
            nome = st.text_input("Digite o nome do Pokémon:")
            if st.button("Buscar por nome"):
                st.write(pokedex.buscar_por_nome(nome))

    elif opcao == "Sair":
        st.warning("Encerrando a Pokedex. Até mais!")
        st.session_state.iniciado = False

        #comando para rodar python -m streamlit run app.py