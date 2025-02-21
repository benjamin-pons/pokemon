import pygame
from pokemon import Pokemon
import json
import random
import time
import pokedex
import selectPokemon
from healthbar import HealthBar
import textbox

class Battle:
    def __init__(self):
        pygame.init()

        # Load pokemon list file
        with open("pokemonList.json", "r") as json_file:
            self.pokemonList = json.load(json_file)

        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 800
        self.WHITE = (255, 255, 255)
        self.BLACK = (10, 10, 10)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")

        self.background_game = pygame.image.load(r"./assets/images/background/battle_background.png")
        self.background_game = pygame.transform.scale(self.background_game, (1100, 800))

        # In combat UI
        self.button_attack = pygame.image.load(r"./assets/images/buttons/button_attack.png")
        self.button_attack = pygame.transform.scale(self.button_attack, (175, 100))
        self.rect_button_attack = self.button_attack.get_rect(topleft=(890, 670))

        self.button_run = pygame.image.load(r"./assets/images/buttons/button_run.png")
        self.button_run = pygame.transform.scale(self.button_run, (150, 100))
        self.rect_button_run = self.button_run.get_rect(topleft=(650, 670))

        self.ally_bar = pygame.image.load(r"assets/images/ui/health_bar_ally_nohealth.png")
        self.ally_bar = pygame.transform.scale(self.ally_bar, (350, 110))

        self.ennemy_bar = pygame.image.load(r"assets/images/ui/health_bar_ennemy_nohealth.png")
        self.ennemy_bar = pygame.transform.scale(self.ennemy_bar, (350, 110))

        self.pokemon_name_font = pygame.font.Font('assets/pokemon_pixel_font.ttf', 32)

        self.health_bar_ennemy = HealthBar(200, 155, 213, 15, 100)
        self.health_bar_ally = HealthBar(750, 610, 213, 15, 100)

        self.textbox = textbox.TextBox(self.screen, 600, 120)
        self.pokedex_obj = pokedex.Pokédex()

    def display_battle(self, pokemon_ally_sprite, pokemon_ennemy_sprite, ally, ennemy):
        self.screen.blit(self.button_run, self.rect_button_run)
        self.screen.blit(self.button_attack, self.rect_button_attack)
        self.health_bar_ally.draw(self.screen)
        self.health_bar_ennemy.draw(self.screen)

        self.screen.blit(self.pokemon_ally_sprite, (150, 300))
        self.screen.blit(self.pokemon_ennemy_sprite, (600, 140))
        pygame.display.update()

    def display_ui(self, ally, ennemy):
        self.screen.blit(self.background_game, (0, 0))
        self.screen.blit(self.ally_bar, (650, 550))
        self.screen.blit(self.ennemy_bar, (120, 100))

        text_name_ally = self.pokemon_name_font.render(ally.name, False, self.BLACK)
        text_lvl_ally = self.pokemon_name_font.render(f"LVL {ally.lvl}", False, self.BLACK)
        
        text_name_ennemy = self.pokemon_name_font.render(ennemy.name, False, self.BLACK)
        text_lvl_ennemy = self.pokemon_name_font.render(f"LVL {ennemy.lvl}", False, self.BLACK)

        self.screen.blit(text_name_ally, (700, 570))
        self.screen.blit(text_lvl_ally, (900, 570))    
        self.screen.blit(text_name_ennemy, (150, 125))
        self.screen.blit(text_lvl_ennemy, (350, 125))

    def loadAllyPokemon(self, pokemon_name):
        """Create a pokemon from json file"""
        with open("pokedex.json", "r") as file:
            pokedex = json.load(file)
        for pokemon in pokedex:
            if pokemon["name"].lower() == pokemon_name.lower():
                return Pokemon(pokemon["name"], pokemon["max_hp"], pokemon["attack"], pokemon["defense"], pokemon["level"], pokemon["type1"], pokemon["type2"])
    
    def loadEnnemyPokemon(self, number) :
        name = self.pokemonList[number]["name"]
        base_hp = self.pokemonList[number]["hp"]
        atk = self.pokemonList[number]["attack"]
        defense = self.pokemonList[number]["defense"]
        lvl = random.randint(self.pokemon_ally.lvl - 3, self.pokemon_ally.lvl + 3)
        type1 = self.pokemonList[number]["type1"]
        type2 = self.pokemonList[number]["type2"]
        return Pokemon(name, base_hp, atk, defense, lvl, type1, type2)

    # Attack
    def action_attack(self, ally, target):
        """Plays a turn of the battle, your pokemon attacks first"""
        # Your pokemon attacks
        if random.randint(1, 100) >= 5 :
            ally.attack(target)
        else :
            self.textbox.add_text(f"{ally.name} a rate son attaque")
            self.textbox.draw()
            pygame.display.flip()
            time.sleep(2)

        self.health_bar_ennemy.hp = (target.get_hp() / target.max_hp) * 100
        

        self.display_ui(ally, target)
        self.display_battle(self.pokemon_ally_sprite, self.pokemon_ennemy_sprite, ally, target)

        time.sleep(1)
        if target.get_hp() == 0: # Victory
            self.battle = False
            self.textbox.add_text(f"{target.name} est K.O, victoire")
            self.textbox.draw()
            pygame.display.flip()

            time.sleep(2)

            self.textbox.add_text(f"{target.name} est ajoute au Pokedex")
            self.textbox.draw()
            pygame.display.flip()
            self.catch_pokemon(target)

            time.sleep(2)

            ally.lvl += 2

            self.textbox.add_text(f"{ally.name} passe au niveau {ally.lvl}")
            self.textbox.draw()
            pygame.display.flip()

            time.sleep(2)
            self.pokedex_obj.save_pokemon_to_json(ally)

            self.evolution(ally)
            time.sleep(2)

            return

        

        # Ennemy attacks
        if random.randint(1, 100) >= 5 :
            target.attack(ally)
        else :
            self.textbox.add_text(f"{target.name} a rate son attaque")
            self.textbox.draw()
            pygame.display.flip()
            time.sleep(2)
        self.health_bar_ally.hp = (ally.get_hp() / ally.max_hp) * 100
        
        
        self.display_ui(ally, target)
        self.display_battle(self.pokemon_ally_sprite, self.pokemon_ennemy_sprite, ally, target)
        
        time.sleep(1)

        if ally.get_hp() == 0 : # Defeat
            self.battle = False
            self.textbox.add_text(f"{ally.name} est K.O, defaite")
            self.textbox.draw()
            pygame.display.flip()
            time.sleep(2)
            return

    def catch_pokemon(self, pokemon) :
        pokemon.hp = pokemon.set_hp(pokemon.max_hp) # Heal pokemon after being caught
        
        self.pokedex_obj.save_pokemon_to_json(pokemon)
    
    def evolution(self, pokemon) :
        if pokemon.name in ["Snivy", "Chimchar", "Mudkip", "Dwebble", "Totodile", "Scyther", "Pidgey", "Slakoth", "Stunky", 
                "Drilbur", "Magikarp", "Gastly", "Gible", "Solosis", "Sandshrew", "Snover", "Honedge", "Azurill", "Pichu", "Riolu", "Litwick"] :
            if pokemon.lvl >= 16 :
                i = 0
                for p in self.pokemonList :
                    if pokemon.name == p["name"] :
                        name = self.pokemonList[i + 1]["name"]
                        base_hp = self.pokemonList[i + 1]["hp"]
                        atk = self.pokemonList[i + 1]["attack"]
                        defense = self.pokemonList[i + 1]["defense"]
                        lvl = pokemon.lvl
                        type1 = self.pokemonList[i + 1]["type1"]
                        type2 = self.pokemonList[i + 1]["type2"]
                        pokemon_evo = Pokemon(name, base_hp, atk, defense, lvl, type1, type2)
                        self.pokedex_obj.save_pokemon_to_json(pokemon_evo)
                        self.textbox.add_text(f"{pokemon.name} a evolue, {pokemon_evo.name} a ete ajoute au pokedex")
                        self.textbox.draw()
                        pygame.display.flip()
                    i += 1

        if pokemon.name in ["Servine", "Monferno", "Marshtomp", "Croconaw", "Pidgeotto", "Vigoroth", "Haunter", "Gabite",
                 "Duosion", "Doublade", "Marill", "Pikachu", "Lampent"] :
            if pokemon.lvl >= 36 :
                i = 0
                for p in self.pokemonList :
                    if pokemon.name == p["name"] :
                        name = self.pokemonList[i + 1]["name"]
                        base_hp = self.pokemonList[i + 1]["hp"]
                        atk = self.pokemonList[i + 1]["attack"]
                        defense = self.pokemonList[i + 1]["defense"]
                        lvl = pokemon.lvl
                        type1 = self.pokemonList[i + 1]["type1"]
                        type2 = self.pokemonList[i + 1]["type2"]
                        pokemon_evo = Pokemon(name, base_hp, atk, defense, lvl, type1, type2)
                        self.pokedex_obj.save_pokemon_to_json(pokemon_evo)
                        self.textbox.add_text(f"{pokemon.name} a evolue, {pokemon_evo.name} a ete ajoute au pokedex")
                        self.textbox.draw()
                        pygame.display.flip()
                    i += 1

    
    def start_battle(self):
        select_obj = selectPokemon.SelectPokemon()
        select_pokemon = select_obj.open_menu()
        if select_pokemon == None :
            return
        self.pokemon_ally = self.loadAllyPokemon(select_pokemon)
        self.pokemon_ally_sprite = pygame.image.load(self.pokemon_ally.sprite_back)
        self.pokemon_ally_sprite = pygame.transform.scale(self.pokemon_ally_sprite, (400, 400))

        random_ennemy = random.randint(1, 61)
        self.pokemon_ennemy = self.loadEnnemyPokemon(random_ennemy)
        self.pokemon_ennemy_sprite = pygame.image.load(self.pokemon_ennemy.sprite_front)
        self.pokemon_ennemy_sprite = pygame.transform.scale(self.pokemon_ennemy_sprite, (350, 350))

        self.display_ui(self.pokemon_ally, self.pokemon_ennemy)

        self.screen.blit(self.pokemon_ally_sprite, (150, 300))
        self.screen.blit(self.pokemon_ennemy_sprite, (600, 140))

        self.health_bar_ally.hp = 100
        self.health_bar_ennemy.hp = 100

        self.battle = True
        while self.battle:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.battle = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect_button_attack.collidepoint(event.pos):
                        self.action_attack(self.pokemon_ally, self.pokemon_ennemy)
                    elif self.rect_button_run.collidepoint(event.pos):
                        self.battle = False


            self.display_battle(self.pokemon_ally_sprite, self.pokemon_ennemy_sprite, self.pokemon_ally, self.pokemon_ennemy)



# For testing combat
if __name__ == "__main__":
    battle = Battle()
    battle.start_battle()