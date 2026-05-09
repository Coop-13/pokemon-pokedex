from api import (
    get_pokemon_data,
    get_evolution_chain
)

from pokemon import Pokemon


class Pokedex:

    def search_pokemon(self, name):

        # Get Pokemon data from API
        data = get_pokemon_data(name)

        # If Pokemon doesn't exist
        if not data:
            return None

        # Get evolution chain
        evolutions = get_evolution_chain(name)

        # Create and return Pokemon object
        return Pokemon.from_api_data(
            data,
            evolutions
        )
