
from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES
#En este servicio defino como funciona el descanso en un turno 
class Descanso:
    def __init__(self, pokemon:Pokemon):
        self.validacion_hp()
        
    
    def validacion_hp(self, pokemon:Pokemon, hp_actual):
        if pokemon.hp_actual == 100:
            return "No se puede aumentar la salud del pokémon, ya se encuentra con {pokemon.hp_actual}"
        elif pokemon.hp_actual == 0:
            pokemon.hp_actual += ACCIONES["descanso"]
            return "HP aumentando en {hp_actual}"
        