from modelos.pokemon import Pokemon
from datos.tipos_pokemon import TIPOS_POKEMON


class PokemonPlanta(Pokemon):
    def __init__(self, datos_pokemon):
        super().__init__(
            datos_pokemon["nombre"],
            TIPOS_POKEMON[3],
            datos_pokemon["hp_maximo"],
            datos_pokemon["energia_maxima"],
        )

    def atacar(self, oponente):
        # Planta tiene ventaja contra agua.
        from modelos.pokemon_agua import PokemonAgua

        multiplicador = 1

        if isinstance(oponente, PokemonAgua):
            multiplicador = 2

        oponente.recibir_danio(self.calcular_danio(multiplicador))
