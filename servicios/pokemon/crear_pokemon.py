from datos.pokedex import CATALOGO_POKEMON
from datos.tipos_pokemon import TIPOS_POKEMON
from modelos.pokemon_agua import PokemonAgua
from modelos.pokemon_electrico import PokemonElectrico
from modelos.pokemon_fuego import PokemonFuego
from modelos.pokemon_planta import PokemonPlanta

class CrearPokemon:

    @classmethod
    def nuevoPokemon(cls, index_pokemon: str):
        datos_pokemon = CATALOGO_POKEMON[index_pokemon]

        clases_pokemon = {
            TIPOS_POKEMON[1]: PokemonAgua,
            TIPOS_POKEMON[2]: PokemonFuego,
            TIPOS_POKEMON[3]: PokemonPlanta,
            TIPOS_POKEMON[4]: PokemonElectrico,
        }

        #get lo utilice para que el programa no se crashee y solo me indique none
        clase_pokemon = clases_pokemon.get(datos_pokemon["tipo"])
        if clase_pokemon:
            return clase_pokemon(datos_pokemon)
        
        raise ValueError("Tipo de Pokémon no válido")




            
        
    