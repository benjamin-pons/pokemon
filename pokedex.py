import json
import pygame

pygame.init()


class Pokédex :
    def __init__(self) :
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")
        
    def get_pokemon_sprite(self, name) :
        """Gets pokemon sprite from name"""
        sprite = pygame.image.load(f"./assets/images/sprites/front/{name.lower()}_front.png")
        sprite = pygame.transform.scale(sprite, (200, 200))
        return sprite

    def load_pokedex(self):
        """Loads caught Pokemon list from json file"""
        try:
            with open("pokedex.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  

    def save_pokedex(self, pokedex):
        """Saves caught Pokemon list from json file"""
        with open("pokedex.json", "w", encoding="utf-8") as f:
            json.dump(pokedex, f, indent=4)
    
    def add_pokemon_in_pokedex(self, pokemon):
        """Adds pokemon to caught list"""
        self.pokedex = self.load_pokedex()
        pokemon_sprite = pygame.image.load(pokemon.sprite_front)
        pokemon_sprite = pygame.transform.scale(pokemon_sprite, (100, 100))
        if pokemon.name not in self.pokedex: 
            self.pokedex.append(pokemon.name)
            self.save_pokedex(self.pokedex)

    def display_pokedex(self):
        """Display caught pokemon list"""
        background_pokedex = pygame.image.load(r"./assets/images/background/background_pokedex.jpg")
        background_pokedex = pygame.transform.scale(background_pokedex, (1100, 800))
        button_back = pygame.image.load(r"./assets/images/buttons/button_back.png")
        button_back = pygame.transform.scale(button_back, (80, 80))
        rect_button_back = button_back.get_rect(topleft=(100, 60))
        self.screen.blit(background_pokedex,(0,0))
        pokedex_list = self.load_pokedex()
        for i, pokemon_name in enumerate(pokedex_list):
            self.screen.blit(self.get_pokemon_sprite(pokemon_name), (50, 50 + i * 130))
        in_pokedex = True
        while in_pokedex :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_pokedex = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_button_back.collidepoint(event.pos):
                        in_pokedex = False
            pygame.display.update()


# For testing pokedex
if __name__ == "__main__":
    pokedex = Pokédex()
    pokedex.display_pokedex()