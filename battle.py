import pygame
from pokemon import Pokemon
import json
import random
import time
from healthbar import HealthBar

pygame.init()

# Load pokemon list file
with open("pokemonList.json", "r") as json_file :
    pokemonList = json.load(json_file)


SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon")

background_game = pygame.image.load(r"./assets/images/background/battle_background.png")
background_game = pygame.transform.scale(background_game, (1100, 800))

# In combat UI
button_attack = pygame.image.load(r"./assets/images/buttons/button_attack.png")
button_attack = pygame.transform.scale(button_attack, (175, 100))
rect_button_attack = button_attack.get_rect(topleft=(890, 700))

button_run = pygame.image.load(r"./assets/images/buttons/button_run.png")
button_run = pygame.transform.scale(button_run, (150, 100))
rect_button_run = button_run.get_rect(topleft=(650, 700))

ally_bar = pygame.image.load(r"assets/images/ui/health_bar_ally_nohealth.png")
ally_bar = pygame.transform.scale(ally_bar, (350, 110))

ennemy_bar = pygame.image.load(r"assets/images/ui/health_bar_ennemy_nohealth.png")
ennemy_bar = pygame.transform.scale(ennemy_bar, (350, 110))

pokemon_name_font = pygame.font.Font('assets/pokemon_pixel_font.ttf', 32)

health_bar_ennemy = HealthBar(200, 155, 213, 15, 100)
health_bar_ally = HealthBar(750, 610, 213, 15, 100)

def display_battle(pokemon_ally_sprite, pokemon_ennemy_sprite, ally, ennemy):
    screen.blit(button_run,rect_button_run)
    screen.blit(button_attack,rect_button_attack)    

    health_bar_ally.draw(screen)
    health_bar_ennemy.draw(screen)

    pygame.display.update()

def display_ui(ally, ennemy) :
    screen.blit(background_game,(0,0))
    screen.blit(ally_bar, (650, 550))
    screen.blit(ennemy_bar, (120, 100))

    text_name_ally = pokemon_name_font.render(ally.name, False, BLACK)
    text_lvl_ally = pokemon_name_font.render(f"LVL {ally.lvl}", False, BLACK)
    
    text_name_ennemy = pokemon_name_font.render(ennemy.name, False, BLACK)
    text_lvl_ennemy = pokemon_name_font.render(f"LVL {ennemy.lvl}", False, BLACK)

    screen.blit(text_name_ally, (700, 570))
    screen.blit(text_lvl_ally, (900, 570))    
    screen.blit(text_name_ennemy, (150, 125))
    screen.blit(text_lvl_ennemy, (350, 125))


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
    target.print_info()
    ally.attack(target)
    health_bar_ennemy.hp = (target.get_hp()/target.max_hp)*100

    time.sleep(1)
    target.print_info()


def start_battle() :
    pokemon_ally = loadPokemon(33)
    pokemon_ally_sprite = pygame.image.load(pokemon_ally.sprite_back)
    pokemon_ally_sprite = pygame.transform.scale(pokemon_ally_sprite, (400, 400))

    pokemon_ennemy = loadPokemon(52)
    pokemon_ennemy_sprite = pygame.image.load(pokemon_ennemy.sprite_front)
    pokemon_ennemy_sprite = pygame.transform.scale(pokemon_ennemy_sprite, (350, 350))

    display_ui(pokemon_ally, pokemon_ennemy)

    screen.blit(pokemon_ally_sprite, (150, 300))
    screen.blit(pokemon_ennemy_sprite,(600, 140))
    
    health_bar_ally.hp = 100
    health_bar_ennemy.hp = 100

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