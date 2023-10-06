import requests

# Input function
def input_name():
    i = 0
    while i < 6:
        try:
            name = input("Enter Pokemon Name: ").lower()
            search_pokemon(name)
            i += 1
        except:
            print("Pokemon does not exist. Try again.")
            print("----------------------------")

# Search Pokemon by name
def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()
    get_data(pokemon)

# Get the response by assigning a value into the print functions
def get_data(pokemon):
    pokemon_name(pokemon)
    pokemon_hp(pokemon)
    pokemon_attack(pokemon)
    pokemon_item(pokemon)

# Print Pokemon Name
def pokemon_name(pokemon):
    print("Name:",pokemon["name"].capitalize())

# Print Pokemon Health
def pokemon_hp(pokemon):
    print("HP:",str(pokemon["stats"][0]["base_stat"]))

# Print Pokemon Attack
def pokemon_attack(pokemon):
    print("Attacks:",pokemon["moves"][0]["move"]["name"].title())

# Print Pokemon Held Items
def pokemon_item(pokemon):
    try:
        print("Held Items:",pokemon["held_items"][0]["item"]["name"].title())
        print("----------------------------")
    except:
        print("Held Items: None")
        print("----------------------------")
        

if __name__ == "__main__":
    input_name()