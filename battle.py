import pygame
from pokemon import Pokemon
import json
import random
import time

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

pokemon_ally = loadPokemon(1)
pokemon_ennemy = loadPokemon(4)



#Attack
def action_attack(target) :
    pokemon_ally.attack(target)
    time.sleep(1)
    pokemon_ennemy.print_info()

def start_battle() :

    battle = True
    while battle :
        for event in pygame.event :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button_attack.collidepoint(event.pos) :
                    action_attack(pokemon_ennemy)
                elif rect_button_change_pokemon.collidepoint(event.pos) :
                    action
                elif rect_button_escape.collidepoint(event.pos) :
                    action
    

