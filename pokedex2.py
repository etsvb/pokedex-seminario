import random

class Pokemon:
    def __init__(self, numero, nome, tipo):
        self.numero = numero
        self.nome = nome
        self.tipo = tipo

    def to_dict(self, desbloqueado=False):
        return {
            'Número': self.numero,
            'Nome': self.nome,
            'Tipo': self.tipo,
            'Desbloqueado': desbloqueado
        }

class Pokedex:
    def __init__(self):
     
        self.pokemons = {
            1: Pokemon(1, "Bulbasaur", "Grama"),
            4: Pokemon(4, "Charmander", "Fogo"),
            7: Pokemon(7, "Squirtle", "Água"),
            25: Pokemon(25, "Pikachu", "Elétrico"),
            143: Pokemon(143, "Snorlax", "Normal"),
            150: Pokemon(150, "Mewtwo", "Psíquico"),
            151: Pokemon(151, "Mew", "Psíquico")
        }
       
        self.registros = {1: True, 4: True, 7: True} 
        
       
        self.box = []
        self.next_capture_id = 1 

   
    def capturar(self, numero: int, guardar: bool = False):
        if numero not in self.pokemons:
            return "Erro: Número da espécie não encontrado na Pokedex.", False
        
        pokemon_especie = self.pokemons[numero]
        
        chance = random.randint(1, 100)
        
        if chance > 50: 
            
            desbloqueado_agora = False
            if numero not in self.registros:
                self.registros[numero] = True
                desbloqueado_agora = True
                
            mensagem = f"Sucesso! Você capturou um {pokemon_especie.nome}!"
            
            if guardar:
                nivel = random.randint(5, 50)
                captura = {
                    'ID da Captura': str(self.next_capture_id),
                    'Número': numero,
                    'Nome': pokemon_especie.nome,
                    'Nível': nivel
                }
                self.box.append(captura)
                self.next_capture_id += 1
                mensagem += f" Ele foi enviado para a Box (ID: {captura['ID da Captura']})."
                
            return mensagem, desbloqueado_agora
        else:
            desbloqueado_agora = False
            if numero not in self.registros:
                self.registros[numero] = True
                desbloqueado_agora = True

            return f"O {pokemon_especie.nome} escapou! Tente novamente.", desbloqueado_agora

    def mostrar_pokedex(self):
        lista = []
        for num, p_obj in self.pokemons.items():
            desbloqueado = num in self.registros
            lista.append(p_obj.to_dict(desbloqueado))
        
        return sorted(lista, key=lambda p: p['Número'])
    
    def mostrar_box(self):
        return self.box

    def remover_do_box(self, id_captura):
        try:
            id_captura = str(id_captura)
            
            for i, p in enumerate(self.box):
                if p['ID da Captura'] == id_captura:
                    nome = self.box.pop(i)['Nome']
                    return f"Pokémon {nome} (ID {id_captura}) removido da Box."
            
            return f"Erro: ID da Captura '{id_captura}' não encontrado na Box."
        except Exception:
            return "Erro ao tentar remover o Pokémon."

    def adicionar_pokemon(self, numero: int, nome: str, tipo: str):
        if numero in self.pokemons:
            return f"Erro: O número #{numero} já está ocupado por {self.pokemons[numero].nome}."
        
        self.pokemons[numero] = Pokemon(numero, nome, tipo)
        return f"Nova espécie #{numero} - {nome} ({tipo}) adicionada com sucesso!"

    def buscar_por_numero(self, numero: int):
        if numero in self.pokemons:
            p_obj = self.pokemons[numero]
            desbloqueado = numero in self.registros
            dados = p_obj.to_dict(desbloqueado)
            
            status = "Desbloqueado" if desbloqueado else "Ainda não registrado!"
            return f"#{dados['Número']:03d} | Nome: {dados['Nome']} | Tipo: {dados['Tipo']} | Status: {status}"
        return f"Erro: Pokémon de número #{numero} não encontrado."

    def buscar_por_nome(self, nome: str):
        nome = nome.strip().lower()
        for num, p_obj in self.pokemons.items():
            if p_obj.nome.lower() == nome:
                desbloqueado = num in self.registros
                dados = p_obj.to_dict(desbloqueado)
                
                status = "Desbloqueado" if desbloqueado else "Ainda não registrado!"
                return f"#{dados['Número']:03d} | Nome: {dados['Nome']} | Tipo: {dados['Tipo']} | Status: {status}"
        return f"Erro: Pokémon de nome '{nome}' não encontrado."