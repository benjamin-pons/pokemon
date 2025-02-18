import pokemon
import pokedex
import pygame


class SelectPokemon :
    def __init__(self) :
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")

        self.background_pokedex = pygame.image.load(r"./assets/images/background/background_pokedex.jpg")
        self.background_pokedex = pygame.transform.scale(self.background_pokedex, (1100, 800))
        
        self.selecting = False

    def display_menu_select() :
        self.screen.blit(self.background_pokedex, (0,0))
        sprite = self.screen.blit(, (50, 50))

    def open_menu(self) :
        self.selecting = True
        while self.selecting :
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.selecting = False
            pygame.display.update()

if __name__ == "__main__":
    select_obj = SelectPokemon()
    select_obj.open_menu()