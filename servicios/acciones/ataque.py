
from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES

#En este servicio defino como funciona el descanso en un turno 
class Ataque:
    def __init__(self, pokemon:Pokemon, daño:int = ACCIONES["ataque"]):
        pokemon.hp_actual += daño
        pass