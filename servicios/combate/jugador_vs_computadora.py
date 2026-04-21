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
        print(f"La computadora eligio la opcion {opcion}.")

        if opcion == "1":
            accion = Ataque(self.jugador_actual.pokemon, self.jugador_rival.pokemon)
            print(accion.resultado["mensaje"])

            if self.jugador_rival.pokemon.turnos_paralizado > 0:
                print(f"{self.jugador_rival.pokemon.nombre} quedo paralizado.")
        elif opcion == "2":
            accion = Defensa(self.jugador_actual.pokemon)
            print(accion.resultado["mensaje"])
        elif opcion == "3":
            accion = Descanso(self.jugador_actual.pokemon)
            print(accion.resultado["mensaje"])
