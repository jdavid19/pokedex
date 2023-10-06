import requests

def input_name():
    i = 0
    while i < 6:
        try:
            name = input("Enter Pokemon Name: ").lower()
            search_pokemon(name)
            i += 1
        except:
            print("Pokemon name does not exist. Try again.")
            print("----------------------------")

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()
    get_data(pokemon)

def get_data(pokemon):
    pokemon_name(pokemon)
    pokemon_hp(pokemon)
    pokemon_attack(pokemon)
    pokemon_item(pokemon)

def pokemon_name(pokemon):
    print("Name:",pokemon["name"].capitalize())

def pokemon_hp(pokemon):
    print("HP:",str(pokemon["stats"][0]["base_stat"]))

def pokemon_attack(pokemon):
    print("Attacks:",pokemon["moves"][0]["move"]["name"].title())

def pokemon_item(pokemon):
    try:
        print("Held Items:",pokemon["held_items"][0]["item"]["name"].title())
        print("----------------------------")
    except:
        print("Held Items: None")
        print("----------------------------")
        

if __name__ == "__main__":
    input_name()