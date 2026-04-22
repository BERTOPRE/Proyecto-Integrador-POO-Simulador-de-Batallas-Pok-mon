from modelos.pokemon import Pokemon
from datos.tipos_pokemon import TIPOS_POKEMON


class PokemonFuego(Pokemon):
    def __init__(self, datos_pokemon):
        super().__init__(
            datos_pokemon["nombre"],
            TIPOS_POKEMON[2],
            datos_pokemon["hp_maximo"],
            datos_pokemon["energia_maxima"],
        )

    def atacar(self, oponente):
        # Fuego tiene ventaja contra planta.
        from modelos.pokemon_planta import PokemonPlanta

        multiplicador = 1

        if isinstance(oponente, PokemonPlanta):
            multiplicador = 2

        oponente.recibir_danio(self.calcular_danio(multiplicador))
