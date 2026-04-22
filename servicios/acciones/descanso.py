from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES


# Define como funciona la accion de descanso.
class Descanso:
    def __init__(self, pokemon: Pokemon):
        self.resultado = self.recuperar_energia(pokemon)

    def recuperar_energia(self, pokemon: Pokemon):
        # No hace nada si la energia ya esta llena.
        if pokemon.energia_actual >= pokemon.energia_maxima:
            return {
                "exito": False,
                "mensaje": f"{pokemon.nombre} ya tiene la energia al maximo."
            }

        # Recupera energia segun la regla definida.
        pokemon.recuperar_energia(ACCIONES["descanso"])

        return {
            "exito": True,
            "mensaje": f"{pokemon.nombre} recupero energia y ahora tiene {pokemon.energia_actual}/{pokemon.energia_maxima} EP."
        }
