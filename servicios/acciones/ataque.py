from modelos.pokemon import Pokemon
from datos.reglas_acciones import ACCIONES

#En este servicio defino como funciona el ataque en un turno
class Ataque:
    def __init__(self, pokemon_atacante: Pokemon, pokemon_oponente: Pokemon):
        self.resultado = self.ejecutar(pokemon_atacante, pokemon_oponente)

    def ejecutar(self, pokemon_atacante: Pokemon, pokemon_oponente: Pokemon):
        if not pokemon_atacante.consumir_energia(ACCIONES["ataque"]):
            return {
                "exito": False,
                "mensaje": f"{pokemon_atacante.nombre} no tiene suficiente energia para atacar."
            }

        pokemon_atacante.atacar(pokemon_oponente)
        return {
            "exito": True,
            "mensaje": f"{pokemon_atacante.nombre} ataco a {pokemon_oponente.nombre}."
        }
        
