import random

from pokedex import Pokedex


def main():

  pokedex = Pokedex()
  
  print("==== Pokemnon Pokedex ====")
  
  while True: 

    print("\nChoose an option:")
    print("1. Search Pokemon")
    print("2. Random Pokemon")
    print("3. Exit")

    choice = input("Enter choice:")

     # Search for a Pokemon
        if choice == "1":

            name = input("\nEnter Pokemon name: ")

            pokemon = pokedex.search_pokemon(name)

            if pokemon:
                pokemon.display_info()
            else:
                print("Pokemon not found.")

        # Random Pokemon
        elif choice == "2":

            random_id = random.randint(1, 1025)

            pokemon = pokedex.search_pokemon(str(random_id))

            if pokemon:
                pokemon.display_info()

        # Exit program
        elif choice == "3":

            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
