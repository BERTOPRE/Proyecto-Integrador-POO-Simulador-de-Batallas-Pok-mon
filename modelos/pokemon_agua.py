from modelos.pokemon import Pokemon
from datos.tipos_pokemon import TIPOS_POKEMON


class PokemonAgua(Pokemon):
    def __init__(self, datos_pokemon):
        super().__init__(
            datos_pokemon["nombre"],
            TIPOS_POKEMON[1],
            datos_pokemon["hp_maximo"],
            datos_pokemon["energia_maxima"],
        )

    def atacar(self, oponente):
        # Agua tiene ventaja contra fuego.
        from modelos.pokemon_fuego import PokemonFuego

        multiplicador = 1

        if isinstance(oponente, PokemonFuego):
            multiplicador = 2

        oponente.recibir_danio(self.calcular_danio(multiplicador))
