from abc import ABC, abstractmethod


class Pokemon(ABC):
    # Daño base usado por todos los Pokemon al atacar.
    DANIO_BASE = 10

    def __init__(self, nombre, tipo_pokemon, hp_maximo, energia_maxima):
        # Se inicializan los valores principales del Pokemon.
        self.__nombre = nombre
        self.__tipo_pokemon = tipo_pokemon
        self.__hp_maximo = hp_maximo
        self.__hp_actual = hp_maximo
        self.__energia_maxima = energia_maxima
        self.__energia_actual = energia_maxima
        self.__defensa_activa = False
        self.__turnos_paralizado = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def tipo_pokemon(self):
        return self.__tipo_pokemon

    @property
    def hp_actual(self):
        return self.__hp_actual

    @hp_actual.setter
    def hp_actual(self, nuevo_hp):
        if nuevo_hp < 0:
            self.__hp_actual = 0
        elif nuevo_hp > self.__hp_maximo:
            self.__hp_actual = self.__hp_maximo
        else:
            self.__hp_actual = nuevo_hp

    @property
    def hp_maximo(self):
        return self.__hp_maximo

    @property
    def energia_actual(self):
        return self.__energia_actual

    @energia_actual.setter
    def energia_actual(self, nueva_energia):
        if nueva_energia < 0:
            self.__energia_actual = 0
        elif nueva_energia > self.__energia_maxima:
            self.__energia_actual = self.__energia_maxima
        else:
            self.__energia_actual = nueva_energia

    @property
    def energia_maxima(self):
        return self.__energia_maxima

    @property
    def defensa_activa(self):
        return self.__defensa_activa

    @property
    def turnos_paralizado(self):
        return self.__turnos_paralizado

    @property
    def ep_actual(self):
        return self.energia_actual

    @ep_actual.setter
    def ep_actual(self, nueva_energia):
        self.energia_actual = nueva_energia

    def recibir_danio(self, cantidad_danio):
        # Si estaba defendiendo, el siguiente golpe hace menos daño.
        if self.__defensa_activa:
            cantidad_danio = max(1, int(cantidad_danio / 2))
            self.__defensa_activa = False
        self.hp_actual -= cantidad_danio

    def consumir_energia(self, cantidad_energia):
        # Si no tiene energia suficiente, la accion no se puede ejecutar.
        if self.__energia_actual < cantidad_energia:
            return False

        self.energia_actual -= cantidad_energia
        return True

    def recuperar_energia(self, cantidad_energia):
        self.energia_actual += cantidad_energia

    def activar_defensa(self):
        self.__defensa_activa = True

    def paralizar(self):
        # La paralisis hace perder el siguiente turno.
        self.__turnos_paralizado = 1

    def puede_actuar(self):
        # Si sigue paralizado, pierde este turno y luego se libera.
        if self.__turnos_paralizado > 0:
            self.__turnos_paralizado -= 1
            return False
        return True

    def calcular_danio(self, multiplicador):
        # Ajusta el daño segun la ventaja o desventaja del ataque.
        return int(self.DANIO_BASE * multiplicador)

    @abstractmethod
    def atacar(self, oponente):
        pass
