from modelos.jugador import jugador
class Combate:
    def __init__(self, jugador_principal:jugador, jugador_secundario:jugador):
        self.__jugador_principal = jugador_principal
        self.__jugador_secundario = jugador_secundario
        
    
    @property
    def jugador_principal(self):
        return self.__jugador_principal
    
    @property
    def jugador_secundario(self):
        return self.__jugador_secundario
