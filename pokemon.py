class Pokemon:

    def __init__(
        self,
        name,
        pokemon_id,
        height,
        weight,
        types,
        abilities,
        evolutions
    ):

        self.name = name
        self.pokemon_id = pokemon_id
        self.height = height
        self.weight = weight
        self.types = types
        self.abilities = abilities
        self.evolutions = evolutions

    @classmethod
    def from_api_data(cls, data, evolutions=None):

        # If no evolutions are given,
        # create an empty list
        if evolutions is None:
            evolutions = []

        # Extract Pokemon types
        types = [
            t["type"]["name"]
            for t in data["types"]
        ]

        # Extract Pokemon abilities
        abilities = [
            a["ability"]["name"]
            for a in data["abilities"]
        ]

        # Return a Pokemon object
        return cls(
            data["name"],
            data["id"],
            data["height"],
            data["weight"],
            types,
            abilities,
            evolutions
        )

    def display_info(self):

        print("\n===== Pokemon Info =====")

        print(f"Name: {self.name.title()}")
        print(f"ID: {self.pokemon_id}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")

        print(
            f"Types: {', '.join(self.types)}"
        )

        print(
            f"Abilities: {', '.join(self.abilities)}"
        )

        print(
            f"Evolutions: {' -> '.join(self.evolutions)}"
        )
