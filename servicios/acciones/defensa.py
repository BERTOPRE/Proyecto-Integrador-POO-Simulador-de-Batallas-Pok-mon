
from modelos.pokemon import Pokemon

#En este servicio defino como funciona el descanso en un turno 
class Defensa:
    def __init__(self, pokemon:Pokemon):
        pokemon.hp_actual -= 0 #TODO:: ESTO ES PROVISIONAL YA QUE EN ALGUN MOMENTO PUEDE QUE CAMBIE LA MANERA EN LA QUE LOS ATAQUES PUEDAN HACER DAÑO SI EN UN FUTURO SE TIENE DAÑO AUNQUE ESTE EN DEFENSA
        pass