from pokemon import Pokemon
import json
import random

with open("pokemonList.json", "r") as json_file :
    pokemonList = json.load(json_file)

# Input pokedex index to load corresponding pokemon
def loadPokemon(number) :
    """Create a pokemon from json file"""
    name = pokemonList[number]["name"]
    base_hp = pokemonList[number]["hp"]
    atk = pokemonList[number]["attack"]
    defense = pokemonList[number]["defense"]
    lvl = random.randint(50, 60)
    type1 = pokemonList[number]["type1"]
    type2 = pokemonList[number]["type2"]
    return Pokemon(name, base_hp, atk, defense, lvl, type1, type2)

# Create a random pokemon
number = random.randint(1, 61)

pokemon1 = loadPokemon(number)
pokemon2 = loadPokemon(50)
pokemon1.print_info()
pokemon2.print_info()