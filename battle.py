import pygame
from pokemon import Pokemon
import json
import random
import time

pygame.init()

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
button_attack = pygame.transform.scale(button_attack, (175, 100))
rect_button_attack = button_attack.get_rect(topleft=(890, 600))

button_run = pygame.image.load(r"./assets/images/buttons/button_run.png")
button_run = pygame.transform.scale(button_run, (150, 100))
rect_button_run = button_run.get_rect(topleft=(650, 600))

pokemon_name_font = pygame.font.Font(None, 30)

def display_battle(pokemon_ally_sprite, pokemon_ennemy_sprite, ally, ennemy):
    screen.blit(background_game,(0,0))
    screen.blit(button_run,rect_button_run)
    screen.blit(button_attack,rect_button_attack)

    screen.blit(pokemon_ally_sprite, (-15, 350))
    screen.blit(pokemon_ennemy_sprite,(620, 200))

    text_name_ally = pokemon_name_font.render(ally.name, False, (255, 255, 255))
    text_name_ennemy = pokemon_name_font.render(ennemy.name, False, (255, 255, 255))

    screen.blit(text_name_ally, (150, 450))
    screen.blit(text_name_ennemy, (620, 200))

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
    pokemon_ally = loadPokemon(4)
    pokemon_ally_sprite = pygame.image.load(pokemon_ally.sprite_back)
    pokemon_ally_sprite = pygame.transform.scale(pokemon_ally_sprite, (600, 600))

    pokemon_ennemy = loadPokemon(1)
    pokemon_ennemy_sprite = pygame.image.load(pokemon_ennemy.sprite_front)
    pokemon_ennemy_sprite = pygame.transform.scale(pokemon_ennemy_sprite, (350, 350))

    battle = True
    while battle :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                battle = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button_attack.collidepoint(event.pos) :
                    action_attack(pokemon_ally, pokemon_ennemy)
                elif rect_button_run.collidepoint(event.pos) :
                    battle = False
        
        display_battle(pokemon_ally_sprite, pokemon_ennemy_sprite, pokemon_ally, pokemon_ennemy)