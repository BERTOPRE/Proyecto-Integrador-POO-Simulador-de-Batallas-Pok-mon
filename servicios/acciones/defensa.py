from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES


# Define como funciona la accion de defensa.
class Defensa:
    def __init__(self, pokemon: Pokemon):
        self.resultado = self.ejecutar(pokemon)

    def ejecutar(self, pokemon: Pokemon):
        # Defender tambien consume energia.
        if not pokemon.consumir_energia(ACCIONES["defensa"]):
            return {
                "exito": False,
                "mensaje": f"{pokemon.nombre} no tiene suficiente energia para defenderse."
            }

        # La defensa reduce el proximo daño recibido.
        pokemon.activar_defensa()
        return {
            "exito": True,
            "mensaje": f"{pokemon.nombre} activo su defensa y reducira a la mitad el proximo ataque recibido."
        }
