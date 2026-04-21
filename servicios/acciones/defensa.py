from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES

#En este servicio defino como funciona el descanso en un turno 
class Defensa:
    def __init__(self, pokemon:Pokemon):
        self.resultado = self.ejecutar(pokemon)

    def ejecutar(self, pokemon: Pokemon):
        if not pokemon.consumir_energia(ACCIONES["defensa"]):
            return {
                "exito": False,
                "mensaje": f"{pokemon.nombre} no tiene suficiente energia para defenderse."
            }

        pokemon.activar_defensa()
        return {
            "exito": True,
            "mensaje": f"{pokemon.nombre} activo su defensa y reducira a la mitad el proximo ataque recibido."
        }
        
