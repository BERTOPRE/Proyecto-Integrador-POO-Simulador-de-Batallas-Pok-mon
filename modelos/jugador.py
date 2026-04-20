from modelos.pokemon import Pokemon

class Jugador:
    def __init__(self,pokemon: Pokemon, nombre_jugador):
        #aquí el jugador tiene un pokémon
        self.__nombre_jugador = nombre_jugador
        self.__pokemon = pokemon
        
    @property
    def pokemon(self):
        return self.__pokemon
    
    @property
    def nombre_jugador(self):
        return self.__nombre_jugador