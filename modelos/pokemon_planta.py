#PokemonPlanta
from modelos.pokemon import Pokemon
from datos.tipos_pokemon import TIPOS_POKEMON

class PokemonPlanta(Pokemon):
    def __init__(self, datos_pokemon):
        super().__init__(datos_pokemon["nombre"], TIPOS_POKEMON[3], datos_pokemon["hp_maximo"], datos_pokemon["energia_maxima"])
    
