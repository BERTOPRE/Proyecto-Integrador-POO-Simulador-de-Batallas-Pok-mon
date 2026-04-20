
from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES
#En este servicio defino como funciona el descanso en un turno 
class Descanso:
    def __init__(self, pokemon:Pokemon):
        self.validacion_hp(pokemon)
        
    
    def validacion_hp(self, pokemon:Pokemon):
        if pokemon.hp_actual >= 100:
            return f"No se puede aumentar la salud del pokemon, ya se encuentra con {pokemon.hp_actual}"

        pokemon.hp_actual += ACCIONES["descanso"]

        if pokemon.hp_actual > 100:
            pokemon.hp_actual = 100

        return f"HP aumentando a {pokemon.hp_actual}"
        
