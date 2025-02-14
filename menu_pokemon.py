import pygame
from battle import start_battle

pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon")

background_image = pygame.image.load(r"./assets/images/background/background_display_menu.png")
background_image = pygame.transform.scale(background_image, (1100, 800))

background_pokedex = pygame.image.load(r"./assets/images/background/background_pokedex.jpg")
background_pokedex = pygame.transform.scale(background_pokedex, (1100, 800))

background_game = pygame.image.load(r"./assets/images/background/background_game.jpg")
background_game = pygame.transform.scale(background_game, (1100, 800))

logo = pygame.image.load(r"./assets/images/logo.png")
logo = pygame.transform.scale(logo, (400, 150))

# Play music
pygame.mixer.init()
pygame.mixer.music.load(r"./assets/sound/sound_theme.mp3")
pygame.mixer.music.play(-1)  # Loops music

# Buttons
button_play = pygame.image.load(r"./assets/images/buttons/play_button.png")
button_play = pygame.transform.scale(button_play, (800, 400))
rect_button_play = button_play.get_rect(topleft=(-80, 100))

button_quit = pygame.image.load(r"./assets/images/buttons/button_quit.png")
button_quit = pygame.transform.scale(button_quit, (800, 400))
rect_button_quit = button_quit.get_rect(topleft=(160, 400))

button_pokedex = pygame.image.load(r"./assets/images/buttons/button_pokedex.png")
button_pokedex = pygame.transform.scale(button_pokedex, (800, 400))
rect_button_pokedex = button_pokedex.get_rect(topleft=(400, 100))  

button_back = pygame.image.load(r"./assets/images/buttons/button_back.png")
button_back = pygame.transform.scale(button_back, (80, 80))
rect_button_back = button_back.get_rect(topleft=(100, 60))  


def display_main_menu():
    screen.blit(background_image, (0, 0))
    screen.blit(logo,(350,80))
    screen.blit(button_play, rect_button_play.topleft)
    screen.blit(button_quit, rect_button_quit.topleft)
    screen.blit(button_pokedex, rect_button_pokedex.topleft)
    pygame.display.update()

def display_pokedex():
    screen.blit(background_pokedex,(0,0))
    screen.blit(button_back,rect_button_back)
    pygame.display.update()

def display_game():
    screen.blit(background_game,(0,0))
    screen.blit(button_back,rect_button_back)
    pygame.display.update()

current_screen = "menu"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "menu":
                if rect_button_play.collidepoint(event.pos):
                    current_screen = "game"
                if rect_button_pokedex.collidepoint(event.pos):
                    current_screen = "pokedex"
                if rect_button_quit.collidepoint(event.pos):
                    running = False
            elif current_screen in ["game", "pokedex"]:
                if rect_button_back.collidepoint(event.pos):
                    current_screen = "menu"

    if current_screen == "menu":
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(r"./assets/sound/sound_theme.mp3")
            pygame.mixer.music.play(-1)
        display_main_menu()
    elif current_screen == "pokedex":
        display_pokedex()
    elif current_screen == "game":
        pygame.mixer.music.stop()
        display_game()

pygame.quit()