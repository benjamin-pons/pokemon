import json
import pygame

pygame.init()


class Pokédex :
    def __init__(self) :
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")

        self.SPRITE_SIZE = 100

        self.background_pokedex = pygame.image.load(r"./assets/images/background/background_pokedex.jpg")
        self.background_pokedex = pygame.transform.scale(self.background_pokedex, (1100, 800))
        
        
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

    def reset(self):
        """Reset the pokemons in pokedex"""
        with open("pokedex_starter.json", "r") as s :
            starters = json.load(s)
        with open("pokedex.json", "w", encoding="utf-8") as f:
            json.dump(starters, f, indent=4)
    

    def save_pokemon_to_json(self, pokemon) :
        """Loads pokedex.json file then saves or updates pokemon inside"""
        try:
            with open("pokedex.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        # Check if pokemon is already in pokedex
        pokemon_found = False
        for p in data:
            if p["name"] == pokemon.name:
                # Updates info
                p["level"] = pokemon.lvl
                p["hp"] = pokemon.get_hp()
                p["max_hp"] = pokemon.max_hp
                p["attack"] = pokemon.atk
                p["defense"] = pokemon.defense
                p["type1"] = pokemon.type1
                p["type2"] = pokemon.type2
                p["alive"] = pokemon.alive
                pokemon_found = True
                break

        # If pokemon isn't in pokedex
        if not pokemon_found:
            pokemon_data = {
                "name": pokemon.name,
                "level": pokemon.lvl,
                "hp": pokemon.get_hp(),
                "max_hp": pokemon.max_hp,
                "attack": pokemon.atk,
                "defense": pokemon.defense,
                "type1": pokemon.type1,
                "type2": pokemon.type2,
                "alive": pokemon.alive
            }
            data.append(pokemon_data)

        with open("pokedex.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_sprites(self, pokedex_list):
        sprites = []
        for pokemon in pokedex_list:  # Go though the pokedex
            sprite_path = f"./assets/images/sprites/front/{pokemon['name'].lower()}_front.png"
            sprite = pygame.image.load(sprite_path)
            sprite = pygame.transform.scale(sprite, (self.SPRITE_SIZE, self.SPRITE_SIZE))
            sprites.append((sprite, sprite_path, pokemon['name']))  # Add pokemon name
        return sprites

    def draw_sprites(self, sprites):
        self.screen.blit(self.background_pokedex,(0,0))
        for i, (sprite, sprite_path, pokemon_name) in enumerate(sprites):
            x = (i % 9) * (self.SPRITE_SIZE + 10) + 50
            y = (i // 9) * (self.SPRITE_SIZE + 10) + 50
            self.screen.blit(sprite, (x, y))

    def display_pokedex(self):
        """Display caught pokemon list"""
        self.screen.blit(self.background_pokedex,(0,0))
        pokedex_list = self.load_pokedex()
        sprites = self.load_sprites(pokedex_list)
        self.draw_sprites(sprites)

        in_pokedex = True
        while in_pokedex :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_pokedex = False
            pygame.display.update()


# For testing pokedex
if __name__ == "__main__":
    pokedex_obj = Pokédex()
    pokedex_obj.display_pokedex()