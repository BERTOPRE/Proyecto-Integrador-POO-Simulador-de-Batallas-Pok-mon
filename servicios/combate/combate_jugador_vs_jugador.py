from modelos.jugador import jugador


class CombateJugadorVsJugador:
    def __init__(self, jugador_principal: jugador, jugador_secundario: jugador):
        # Guarda referencias simples de ambos jugadores.
        self.__jugador_principal = jugador_principal
        self.__jugador_secundario = jugador_secundario

    @property
    def jugador_principal(self):
        return self.__jugador_principal

    @property
    def jugador_secundario(self):
        return self.__jugador_secundario
