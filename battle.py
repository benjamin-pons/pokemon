import pygame
from pokemon import Pokemon
import json
import random
import time

# Load pokemon list file
with open("pokemonList.json", "r") as json_file :
    pokemonList = json.load(json_file)

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon")

background_game = pygame.image.load(r"./assets/images/background/background_game.jpg")
background_game = pygame.transform.scale(background_game, (1100, 800))

# In combat UI
button_attack = pygame.image.load(r"./assets/images/buttons/button_attack.png")
button_attack = pygame.transform.scale(button_attack, (200, 200))
rect_button_attack = button_attack.get_rect(topleft=(890, 600))

button_run = pygame.image.load(r"./assets/images/buttons/button_run.png")
button_run = pygame.transform.scale(button_run, (200, 200))
rect_button_run = button_run.get_rect(topleft=(720, 600))

def display_battle():
    screen.blit(background_game,(0,0))
    screen.blit(button_run,rect_button_run)
    screen.blit(button_attack,rect_button_attack)
    pygame.display.update()

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


# Attack
def action_attack(ally, target) :
    ally.attack(target)
    time.sleep(1)
    target.print_info()

def start_battle() :
    pokemon_ally = loadPokemon(1)
    pokemon_ennemy = loadPokemon(4)

    battle = True
    while battle :
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button_attack.collidepoint(event.pos) :
                    action_attack(pokemon_ally, pokemon_ennemy)
                elif rect_button_run.collidepoint(event.pos) :
                    battle = False
        
        display_battle()