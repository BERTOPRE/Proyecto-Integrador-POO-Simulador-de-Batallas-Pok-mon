import random

from modelos.jugador import Jugador
from servicios.acciones.ataque import Ataque
from servicios.acciones.descanso import Descanso
from servicios.acciones.defensa import Defensa
from servicios.combate.jugador_vs_jugador import JugadorVsJugador

#aquí heredo el jugador vs jugador, pero en este caso la computadora elegirá aleatoriamente con randmo.choice
class JugadorVsComputadora(JugadorVsJugador):

    def __init__(self, jugador_principal: Jugador, computadora: Jugador):
        super().__init__(jugador_principal, computadora)
        self.computadora = computadora

    def ejecutar_turno(self):
        if self.jugador_actual == self.computadora:
            self.ejecutar_turno_computadora()
        else:
            super().ejecutar_turno()

    def ejecutar_turno_computadora(self):
        print(f"\nTurno de {self.jugador_actual.nombre_jugador}")

        opcion = random.choice(["1", "2", "3"])

        if opcion == "1":
            Ataque(self.jugador_rival.pokemon)
            self.limitar_hp_minimo(self.jugador_rival)
            print(f"{self.jugador_actual.pokemon.nombre} ataco a {self.jugador_rival.pokemon.nombre}")
        elif opcion == "2":
            Defensa(self.jugador_actual.pokemon)
            print(f"{self.jugador_actual.pokemon.nombre} se defendio")
        elif opcion == "3":
            Descanso(self.jugador_actual.pokemon)
            print(f"{self.jugador_actual.pokemon.nombre} descanso")
