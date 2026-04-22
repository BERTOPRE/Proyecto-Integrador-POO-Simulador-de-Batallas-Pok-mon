from modelos.jugador import Jugador
from utilidades.determinar_inicio_combate import DeterminarInicioCombate
from servicios.acciones.ataque import Ataque
from servicios.acciones.descanso import Descanso
from servicios.acciones.defensa import Defensa


class JugadorVsJugador:

    def __init__(self, jugador_principal: Jugador, jugador_secundario: Jugador):
        # Guarda a los jugadores y decide quien inicia.
        self.jugador_principal = jugador_principal
        self.jugador_secundario = jugador_secundario
        self.jugador_actual = DeterminarInicioCombate.determinar_inicio_combate(
            jugador_principal,
            jugador_secundario
        )
        self.jugador_rival = self.obtener_jugador_rival(self.jugador_actual)

    def iniciar_combate(self):
        # El combate sigue hasta que uno de los dos Pokemon se debilita.
        print("Inicia el combate")
        print(f"Primer turno: {self.jugador_actual.nombre_jugador}")

        while self.esta_vivo(self.jugador_principal) and self.esta_vivo(self.jugador_secundario):
            self.mostrar_estado()
            if self.jugador_actual.pokemon.puede_actuar():
                self.ejecutar_turno()
            else:
                print(f"{self.jugador_actual.pokemon.nombre} esta paralizado y pierde su turno.")

            if self.esta_vivo(self.jugador_principal) and self.esta_vivo(self.jugador_secundario):
                self.cambiar_turno()

        self.mostrar_ganador()

    def ejecutar_turno(self):
        # Muestra las acciones disponibles para el jugador actual.
        print(f"\nTurno de {self.jugador_actual.nombre_jugador}")
        print("1. Atacar")
        print("2. Defender")
        print("3. Descansar")

        opcion = input("Seleccione una accion: ")

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
        else:
            print("Opcion invalida. Pierdes el turno.")

    def cambiar_turno(self):
        # Cambia el turno entre el jugador actual y su rival.
        self.jugador_actual, self.jugador_rival = self.jugador_rival, self.jugador_actual

    def obtener_jugador_rival(self, jugador: Jugador):
        # Devuelve al oponente del jugador recibido.
        if jugador == self.jugador_principal:
            return self.jugador_secundario
        return self.jugador_principal

    def esta_vivo(self, jugador: Jugador):
        return jugador.pokemon.hp_actual > 0

    def mostrar_estado(self):
        print("\nEstado actual:")
        print(
            f"{self.jugador_principal.nombre_jugador} - "
            f"{self.jugador_principal.pokemon.nombre}: "
            f"{self.jugador_principal.pokemon.hp_actual}/{self.jugador_principal.pokemon.hp_maximo} HP | "
            f"{self.jugador_principal.pokemon.energia_actual}/{self.jugador_principal.pokemon.energia_maxima} EP"
        )
        print(
            f"{self.jugador_secundario.nombre_jugador} - "
            f"{self.jugador_secundario.pokemon.nombre}: "
            f"{self.jugador_secundario.pokemon.hp_actual}/{self.jugador_secundario.pokemon.hp_maximo} HP | "
            f"{self.jugador_secundario.pokemon.energia_actual}/{self.jugador_secundario.pokemon.energia_maxima} EP"
        )

    def mostrar_ganador(self):
        # El ganador es quien termina con HP mayor que cero.
        if self.esta_vivo(self.jugador_principal):
            ganador = self.jugador_principal
        else:
            ganador = self.jugador_secundario

        print(f"\nGano {ganador.nombre_jugador} con {ganador.pokemon.nombre}")
