#Determinar que jugador irá primero a accionar
from modelos.jugador import Jugador
import random

class DeterminarInicioCombate:
    lista_jugadores = []
    @classmethod
    def determinar_inicio_combate(cls, jugador_uno:Jugador, jugador_dos:Jugador):
        cls.lista_jugadores.append(jugador_uno)
        cls.lista_jugadores.append(jugador_dos)
        jugador_seleccionado = random.choice(cls.lista_jugadores)
        return jugador_seleccionado.nombre_jugador
        