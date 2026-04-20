from modelos.jugador import Jugador
from utilidades.determinar_inicio_combate import DeterminarInicioCombate
from servicios.acciones.ataque import Ataque
from servicios.acciones.descanso import Descanso
from servicios.acciones.defensa import Defensa


class JugadorVsJugador:

    def __init__(self, jugador_principal: Jugador, jugador_secundario: Jugador):
        self.jugador_principal = jugador_principal
        self.jugador_secundario = jugador_secundario
        self.jugador_actual = DeterminarInicioCombate.determinar_inicio_combate(
            jugador_principal,
            jugador_secundario
        )
        self.jugador_rival = self.obtener_jugador_rival(self.jugador_actual)

    def iniciar_combate(self):
        print("Inicia el combate")
        print(f"Primer turno: {self.jugador_actual.nombre_jugador}")

        while self.esta_vivo(self.jugador_principal) and self.esta_vivo(self.jugador_secundario):
            self.mostrar_estado()
            self.ejecutar_turno()

            if self.esta_vivo(self.jugador_principal) and self.esta_vivo(self.jugador_secundario):
                self.cambiar_turno()

        self.mostrar_ganador()

    def ejecutar_turno(self):
        print(f"\nTurno de {self.jugador_actual.nombre_jugador}")
        print("1. Atacar")
        print("2. Defender")
        print("3. Descansar")

        opcion = input("Seleccione una accion: ")

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
        else:
            print("Opcion invalida. Pierdes el turno.")
            
            #aquí python me permite cambiar dos variables en una sola línea
    def cambiar_turno(self):
        self.jugador_actual, self.jugador_rival = self.jugador_rival, self.jugador_actual

    def obtener_jugador_rival(self, jugador: Jugador):
        if jugador == self.jugador_principal:
            return self.jugador_secundario
        return self.jugador_principal

    def esta_vivo(self, jugador: Jugador):
        return jugador.pokemon.hp_actual > 0

    def limitar_hp_minimo(self, jugador: Jugador):
        if jugador.pokemon.hp_actual < 0:
            jugador.pokemon.hp_actual = 0

    def mostrar_estado(self):
        print("\nEstado actual:")
        print(
            f"{self.jugador_principal.nombre_jugador} - "
            f"{self.jugador_principal.pokemon.nombre}: "
            f"{self.jugador_principal.pokemon.hp_actual} HP"
        )
        print(
            f"{self.jugador_secundario.nombre_jugador} - "
            f"{self.jugador_secundario.pokemon.nombre}: "
            f"{self.jugador_secundario.pokemon.hp_actual} HP"
        )

    def mostrar_ganador(self):
        if self.esta_vivo(self.jugador_principal):
            ganador = self.jugador_principal
        else:
            ganador = self.jugador_secundario

        print(f"\nGano {ganador.nombre_jugador} con {ganador.pokemon.nombre}")
