import random

from modelos.jugador import Jugador
from datos.pokedex import CATALOGO_POKEMON, mostrar_catalogo_disponible
from servicios.combate.jugador_vs_computadora import JugadorVsComputadora
from servicios.combate.jugador_vs_jugador import JugadorVsJugador
from servicios.pokemon.crear_pokemon import CrearPokemon
from utilidades.menu import Menu


def seleccionar_pokemon(nombre_jugador):
    while True:
        seleccion_pokemon = input(f"{nombre_jugador}, seleccione un pokemon: ")

        if seleccion_pokemon in CATALOGO_POKEMON:
            return CrearPokemon.nuevoPokemon(seleccion_pokemon)

        print("Seleccion invalida. Intente de nuevo.")


def seleccionar_pokemon_computadora():
    #esto me sirve para que en randmo obtener los indices del catálogo, despues se convierte en lista para que choice escoja uno aleatoriamente
    seleccion_pokemon = random.choice(list(CATALOGO_POKEMON.keys()))
    pokemon = CrearPokemon.nuevoPokemon(seleccion_pokemon)
    print(f"La computadora selecciono a {pokemon.nombre}")
    return pokemon

#JUGADOR VS JUGADOR
def iniciar_jugador_vs_jugador():
    nombre_jugador_uno = input("Ingrese el nombre del jugador 1: ")
    nombre_jugador_dos = input("Ingrese el nombre del jugador 2: ")

    mostrar_catalogo_disponible()

    pokemon_jugador_uno = seleccionar_pokemon(nombre_jugador_uno)
    pokemon_jugador_dos = seleccionar_pokemon(nombre_jugador_dos)

    jugador_uno = Jugador(pokemon_jugador_uno, nombre_jugador_uno)
    jugador_dos = Jugador(pokemon_jugador_dos, nombre_jugador_dos)

    combate = JugadorVsJugador(jugador_uno, jugador_dos)
    combate.iniciar_combate()

#JUGADOR VS COMPUTADORA
def iniciar_jugador_vs_computadora():
    nombre_jugador = input("Ingrese el nombre del jugador: ")

    mostrar_catalogo_disponible()

    pokemon_jugador = seleccionar_pokemon(nombre_jugador)
    pokemon_computadora = seleccionar_pokemon_computadora()

    jugador = Jugador(pokemon_jugador, nombre_jugador)
    computadora = Jugador(pokemon_computadora, "Computadora")

    combate = JugadorVsComputadora(jugador, computadora)
    combate.iniciar_combate()


def main():
    print("El programa ha iniciado")

    opcion = Menu.mostrar_menu()

    if opcion == 1:
        iniciar_jugador_vs_jugador()
    elif opcion == 2:
        iniciar_jugador_vs_computadora()


if __name__ == "__main__":
    main()
