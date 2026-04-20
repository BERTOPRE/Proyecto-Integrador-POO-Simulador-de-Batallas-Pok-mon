
class Pokemon:
    def __init__(self, nombre, tipo_pokemon, hp_actual, ep_actual ):
        self.__nombre = nombre
        self.tipo_pokemon = tipo_pokemon
        self.__hp_actual = hp_actual
        self.__ep_actual = ep_actual
        
    @property
    def nombre(self):
        return self.__nombre
    @property
    def hp_actual(self):
        return self.__hp_actual
    
    @hp_actual.setter
    def hp_actual(self, nuevo_hp):
        self.__hp_actual = nuevo_hp
    
    @property
    def ep_actual(self):
        return self.__ep_actual
    
    @ep_actual.setter    
    def ep_actual(self, nuevo_ep):
        self.__ep_actual = nuevo_ep
        
        