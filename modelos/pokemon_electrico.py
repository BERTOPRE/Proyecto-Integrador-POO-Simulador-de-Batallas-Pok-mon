from modelos.pokemon import Pokemon
from datos.tipos_pokemon import TIPOS_POKEMON

class PokemonElectrico(Pokemon):
    def __init__(self, nombre, hp_actual, ep_actual):
        super().__init__(nombre, TIPOS_POKEMON[4], hp_actual, ep_actual)

