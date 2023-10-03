import requests
import sys

def search_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
    pokemon = response.json()
    get_data(pokemon)

def get_data(pokemon):
     pokemon_name(pokemon)
     pokemon_id(pokemon)
     pokemon_exp(pokemon)

def pokemon_name(pokemon):
        print("Name: "+pokemon["name"].capitalize())

def pokemon_id(pokemon):
    print("ID: "+(str(pokemon["id"])))

def pokemon_exp(pokemon):
    print("Base XP: "+(str(pokemon["base_experience"])))

if __name__ == "__main__":
    search_pokemon(sys.argv[1])