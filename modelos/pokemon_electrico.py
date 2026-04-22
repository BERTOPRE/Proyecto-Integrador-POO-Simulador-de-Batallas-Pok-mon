import random

from modelos.pokemon import Pokemon
from datos.tipos_pokemon import TIPOS_POKEMON


class PokemonElectrico(Pokemon):
    def __init__(self, datos_pokemon):
        super().__init__(
            datos_pokemon["nombre"],
            TIPOS_POKEMON[4],
            datos_pokemon["hp_maximo"],
            datos_pokemon["energia_maxima"],
        )

    def atacar(self, oponente):
        # Electrico hace daño normal y a veces paraliza.
        oponente.recibir_danio(self.calcular_danio(1))

        if random.random() <= 0.20:
            oponente.paralizar()
