from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES
#En este servicio defino como funciona el descanso en un turno 
class Descanso:
    def __init__(self, pokemon:Pokemon):
        self.resultado = self.recuperar_energia(pokemon)
        
    
    def recuperar_energia(self, pokemon:Pokemon):
        if pokemon.energia_actual >= pokemon.energia_maxima:
            return {
                "exito": False,
                "mensaje": f"{pokemon.nombre} ya tiene la energia al maximo."
            }

        pokemon.recuperar_energia(ACCIONES["descanso"])

        return {
            "exito": True,
            "mensaje": f"{pokemon.nombre} recupero energia y ahora tiene {pokemon.energia_actual}/{pokemon.energia_maxima} EP."
        }
        
