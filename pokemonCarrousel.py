import pygame
import json
import os

class SelectPokemon:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.Font(None, 40)

        # Charger la liste des Pokémon
        with open("pokemonList.json", "r", encoding="utf-8") as file:
            self.pokemon_list = json.load(file)

        self.index = 0  # Pokémon actuel
        self.selected_pokemon = None

        # Charger les images
        self.load_sprites()

        # Définir les boutons
        self.button_next = pygame.Rect(self.width - 150, self.height // 2, 100, 50)
        self.button_prev = pygame.Rect(50, self.height // 2, 100, 50)
        self.button_validate = pygame.Rect(self.width // 2 - 75, self.height - 100, 150, 50)

    def load_sprites(self):
        """ Charge les sprites des Pokémon. """
        self.sprites = []
        sprite_path = "assets/images/sprites/front/"

        for pokemon in self.pokemon_list:
            image_path = os.path.join(sprite_path, pokemon["sprite"])
            if os.path.exists(image_path):
                image = pygame.image.load(image_path)
                self.sprites.append(image)
            else:
                print(f"Image manquante : {image_path}")
                self.sprites.append(None)

    def draw_text(self, text, x, y):
        """ Affiche un texte à l'écran. """
        render = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(render, (x, y))

    def draw_buttons(self):
        """ Dessine les boutons. """
        pygame.draw.rect(self.screen, (0, 200, 0), self.button_validate)
        self.draw_text("Valider", self.button_validate.x + 20, self.button_validate.y + 10)

        pygame.draw.rect(self.screen, (200, 0, 0), self.button_prev)
        self.draw_text("<", self.button_prev.x + 40, self.button_prev.y + 10)

        pygame.draw.rect(self.screen, (0, 0, 200), self.button_next)
        self.draw_text(">", self.button_next.x + 40, self.button_next.y + 10)

    def draw(self):
        """ Affiche l'écran de sélection. """
        self.screen.fill((30, 30, 30))  # Fond sombre

        if self.sprites[self.index]:
            sprite = self.sprites[self.index]
            sprite_rect = sprite.get_rect(center=(self.width // 2, self.height // 3))
            self.screen.blit(sprite, sprite_rect)

        # Afficher le nom du Pokémon
        self.draw_text(self.pokemon_list[self.index]["nom"], self.width // 2 - 50, self.height // 2 - 50)

        # Dessiner les boutons
        self.draw_buttons()

    def handle_event(self, event):
        """ Gère les interactions utilisateur. """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_next.collidepoint(event.pos):
                self.index = (self.index + 1) % len(self.pokemon_list)
            elif self.button_prev.collidepoint(event.pos):
                self.index = (self.index - 1) % len(self.pokemon_list)
            elif self.button_validate.collidepoint(event.pos):
                self.selected_pokemon = self.pokemon_list[self.index]["nom"]
                print(f"Pokémon sélectionné : {self.selected_pokemon}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Sélection de Pokémon")

    selector = SelectPokemon(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            selector.handle_event(event)

        selector.draw()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
