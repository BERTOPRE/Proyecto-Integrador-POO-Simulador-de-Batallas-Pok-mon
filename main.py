from modelos.jugador import Jugador
from modelos.pokemon_electrico import PokemonElectrico
from modelos.pokemon_agua import PokemonAgua
from utilidades.determinar_inicio_combate import DeterminarInicioCombate



# Ejemplo de estructura main en Python
def main():
    print("El programa ha iniciado")
    # Lógica principal aquí
    
    pokemon_jugador_uno = PokemonElectrico("Pikachu", 100, 50)    
    jugador_uno = Jugador(pokemon_jugador_uno, "Luis Miguel")
    
    pokemon_jugador_dos = PokemonAgua("Totodile", 100, 50)
    jugador_dos = Jugador(pokemon_jugador_dos, "Luis Angel")
    
    print(DeterminarInicioCombate.determinar_inicio_combate(jugador_uno, jugador_dos))
if __name__ == "__main__":
    main()
