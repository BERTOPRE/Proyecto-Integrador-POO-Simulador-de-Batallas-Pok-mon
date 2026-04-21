#Determinar que jugador irá primero a accionar
from modelos.jugador import Jugador
import random

class DeterminarInicioCombate:
    @classmethod
    def determinar_inicio_combate(cls, jugador_uno:Jugador, jugador_dos:Jugador):
        jugador_seleccionado = random.choice([jugador_uno, jugador_dos])
        return jugador_seleccionado
        
