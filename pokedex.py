import pygame
import pokemon
import battle
import json 



def sauvegarder_pokedex(pokedex, fichier="caughtpokemon.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(pokedex, f, indent=4)

def charger_pokedex(fichier="caughtpokemon.json"):
    """Charge le Pokédex depuis un fichier JSON."""
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def capturer_pokemon(new_pokemon):
    pokedex = charger_pokedex()
    nom_pokemon = new_pokemon.get('name', 'Inconnu')
    if nom_pokemon not in pokedex:
        pokedex[nom_pokemon] = new_pokemon
        sauvegarder_pokedex(pokedex)
        print(f"{nom_pokemon} a été ajouté au Pokédex !")
    else:
        print(f"{nom_pokemon} est déjà dans le Pokédex !")


pokemon = charger_pokemon_depuis_json(2)
if pokemon:
    capturer_pokemon(pokemon)
else:
    print("Pokémon non trouvé dans le fichier JSON.")