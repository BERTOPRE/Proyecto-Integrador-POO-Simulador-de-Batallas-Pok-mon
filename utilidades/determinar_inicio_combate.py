# Decide aleatoriamente que jugador comienza el combate.
import random

from modelos.jugador import Jugador


class DeterminarInicioCombate:
    @classmethod
    def determinar_inicio_combate(cls, jugador_uno: Jugador, jugador_dos: Jugador):
        # Elige uno de los dos jugadores al azar.
        jugador_seleccionado = random.choice([jugador_uno, jugador_dos])
        return jugador_seleccionado
