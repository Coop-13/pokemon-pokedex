import requests

# Base URLs for the API
BASE_POKEMON_URL = "https://pokeapi.co/api/v2/pokemon/"
BASE_SPECIES_URL = "https://pokeapi.co/api/v2/pokemon-species/"


def get_pokemon_data(name):
    """
    Retrieves basic Pokemon data from PokeAPI.
    """

    response = requests.get(
        f"{BASE_POKEMON_URL}{name.lower()}"
    )

    # Check if request worked
    if response.status_code == 200:
        return response.json()

    return None


def get_evolution_chain(name):
    """
    Retrieves a Pokemon's evolution chain.
    """

    # Get species data first
    species_response = requests.get(
        f"{BASE_SPECIES_URL}{name.lower()}"
    )

    if species_response.status_code != 200:
        return []

    species_data = species_response.json()

    # Get evolution chain URL
    evolution_url = species_data["evolution_chain"]["url"]

    # Request evolution chain data
    evolution_response = requests.get(evolution_url)

    if evolution_response.status_code != 200:
        return []

    evolution_data = evolution_response.json()

    evolutions = []

    # Start at the beginning of the chain
    chain = evolution_data["chain"]

    # Loop through evolutions
    while chain:

        evolutions.append(
            chain["species"]["name"]
        )

        # Move to next evolution
        if chain["evolves_to"]:
            chain = chain["evolves_to"][0]
        else:
            chain = None

    return evolutions
