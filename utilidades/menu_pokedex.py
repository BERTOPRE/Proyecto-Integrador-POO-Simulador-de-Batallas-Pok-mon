from datos.pokedex import mostrar_catalogo_disponible
from servicios.pokemon.crear_pokemon import CrearPokemon


class MenuPokedex:
    @classmethod
    def pokedex(self):
        # Muestra el catalogo completo en consola.
        mostrar_catalogo_disponible()
