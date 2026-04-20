from modelos.jugador import Jugador
from modelos.pokemon_electrico import PokemonElectrico
from modelos.pokemon_agua import PokemonAgua
from utilidades.determinar_inicio_combate import DeterminarInicioCombate
from utilidades.menu_pokedex import MenuPokedex
from utilidades.menu import Menu
from datos.pokedex import CATALOGO_POKEMON
from servicios.pokemon.crear_pokemon import CrearPokemon



# Ejemplo de estructura main en Python
def main():
    print("El programa ha iniciado")
    # Lógica principal aquí
    
    pokemon = CATALOGO_POKEMON["1"]
    seleccion_pokemon = str(input("Seleccione un pokemon: "))
    PokemonNuevo = CrearPokemon.nuevoPokemon(seleccion_pokemon)
    print(PokemonNuevo.nombre)

if __name__ == "__main__":
    main()
