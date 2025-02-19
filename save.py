import pygame
import json

class Save:
    def __init__(self):
        pygame.init()
        self.BUTTON_SIZE = (400, 100)
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 800
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pokemon")

        self.save_files = {
            "save_1": "./saves/pokedex1.json",
            "save_2": "./saves/pokedex2.json",
            "save_3": "./saves/pokedex3.json"
        }

    def display_save(self):
        background_save = pygame.image.load(r"./assets/images/background/background_save.jpg")
        background_save = pygame.transform.scale(background_save, (1100, 800))
        self.screen.blit(background_save,(0,0))

        self.button_save1 = pygame.image.load(r"./assets/images/buttons/save_1.png")
        self.button_save1 = pygame.transform.scale(self.button_save1, self.BUTTON_SIZE)
        rect_button_save1 = self.button_save1.get_rect(topleft=(350, 150))

        self.button_save2 = pygame.image.load(r"./assets/images/buttons/save_2.png")
        self.button_save2 = pygame.transform.scale(self.button_save2, self.BUTTON_SIZE)
        rect_button_save2 = self.button_save2.get_rect(topleft=(350, 300))

        self.button_save3 = pygame.image.load(r"./assets/images/buttons/save_3.png")
        self.button_save3 = pygame.transform.scale(self.button_save3, self.BUTTON_SIZE)
        rect_button_save3 = self.button_save3.get_rect(topleft=(350, 450))

        self.screen.blit(self.button_save1, rect_button_save1)
        self.screen.blit(self.button_save2, rect_button_save2)
        self.screen.blit(self.button_save3, rect_button_save3)
        pygame.display.update()

    def save_pokedex(self, file_path, pokedex_data):
        """Sauvegarde le Pokédex dans un fichier JSON."""
        with open(file_path, "w") as file:
            json.dump(pokedex_data, file, indent=4)

    def load_pokedex(self, file_path):
        """Charge le Pokédex depuis un fichier JSON."""
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                return json.load(file)
        return {}

        in_save_menu = True
        while in_save_menu :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_save_menu = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button_save1.collidepoint(event.pos):
                        selected_save = self.save_files["save_1"]
                        menu_pokemon.display_main_menu()
                elif self.rect_button_save2.collidepoint(event.pos):
                    selected_save = self.save_files["save_2"]
                    menu_pokemon.display_main_menu()
                elif self.rect_button_save3.collidepoint(event.pos):
                    selected_save = self.save_files["save_3"]
                    menu_pokemon.display_main_menu()

                if selected_save:
                    pokedex = self.load_pokedex(selected_save)
                    print(f"Sauvegarde chargée depuis {selected_save}: {pokedex}")



if __name__ == "__main__":
    save = Save()
    save.display_save()