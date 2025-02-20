import pokemon
import pokedex
import pygame


class SelectPokemon :
    def __init__(self) :
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 800
        self.SPRITE_SIZE = 100
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")

        self.background_select = pygame.image.load(r"./assets/images/background/background_select.png")
        self.background_select = pygame.transform.scale(self.background_select, (1100, 800))

        self.selected_pokemon = None

        self.pokedex_obj = pokedex.Pokédex()
        self.pokedex = self.pokedex_obj.load_pokedex()
        self.sprites = self.load_sprites()
        self.available_pokemon = [pokemon["name"].lower() for pokemon in self.pokedex]

    def load_sprites(self):
        sprites = []
        for pokemon in self.pokedex:  # Parcourir les Pokémon dans le pokedex
            sprite_path = f"./assets/images/sprites/front/{pokemon['name'].lower()}_front.png"
            sprite = pygame.image.load(sprite_path)
            sprite = pygame.transform.scale(sprite, (self.SPRITE_SIZE, self.SPRITE_SIZE))
            sprites.append((sprite, sprite_path, pokemon['name']))  # Ajouter le nom du Pokémon
        return sprites

    def draw_sprites(self):
        self.screen.blit(self.background_select,(0,0))
        for i, (sprite, sprite_path, pokemon_name) in enumerate(self.sprites):
            x = (i % 9) * (self.SPRITE_SIZE + 10) + 50
            y = (i // 9) * (self.SPRITE_SIZE + 10) + 50
            if pokemon_name.lower() in self.available_pokemon:
                self.screen.blit(sprite, (x, y))
    
    def handle_click(self, pos):
        for i, (sprite, sprite_path, pokemon_name) in enumerate(self.sprites):
            if sprite:
                x = (i % 9) * (self.SPRITE_SIZE + 10) + 50
                y = (i // 9) * (self.SPRITE_SIZE + 10) + 50
                rect = pygame.Rect(x, y, self.SPRITE_SIZE, self.SPRITE_SIZE)
                if rect.collidepoint(pos):
                    if pokemon_name.lower() in self.available_pokemon:
                        self.selected_pokemon = pokemon_name
                        return pokemon_name

    def open_menu(self) :
        self.pokedex = self.pokedex_obj.load_pokedex()
        selecting = True
        while selecting :
            self.draw_sprites()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    selecting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_pokemon = self.handle_click(event.pos)
                    if clicked_pokemon:
                        print(f"Pokémon sélectionné : {clicked_pokemon}")
                        selecting = False
                        return clicked_pokemon

if __name__ == "__main__":
    select_obj = SelectPokemon()
    select_obj.open_menu()