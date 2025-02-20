import pygame

class TextBox:
    def __init__(self, screen, width, height, font_size=24, font_color=(255, 255, 255), background_color=(0, 0, 0)):
        """
        Initialise une boîte de texte.

        :param screen: L'écran Pygame sur lequel la boîte de texte sera dessinée.
        :param width: La largeur de la boîte de texte.
        :param height: La hauteur de la boîte de texte.
        :param font_size: La taille de la police du texte.
        :param font_color: La couleur du texte (par défaut blanc).
        :param background_color: La couleur de fond de la boîte de texte (par défaut noir).
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font("assets/pokemon_pixel_font.ttf", font_size)  # Police par défaut
        self.font_color = font_color
        self.background_color = background_color
        self.text_lines = []  # Liste des lignes de texte à afficher
        self.rect = pygame.Rect(0, screen.get_height() - height, width, height)  # Position en bas de l'écran

    def add_text(self, text):
        """
        Ajoute une ligne de texte à la boîte de texte.

        :param text: Le texte à ajouter.
        """
        self.text_lines.append(text)
        # Limiter le nombre de lignes pour éviter de dépasser la hauteur de la boîte
        max_lines = self.height // (self.font.get_height() + 5)  # 5 pixels d'espace entre les lignes
        if len(self.text_lines) > max_lines:
            self.text_lines.pop(0)  # Supprimer la ligne la plus ancienne

    def draw(self):
        """
        Dessine la boîte de texte sur l'écran.
        """
        # Dessiner le fond de la boîte de texte
        pygame.draw.rect(self.screen, self.background_color, self.rect)
        
        # Dessiner chaque ligne de texte
        y_offset = self.rect.top + 10  # Commencer à 10 pixels du haut de la boîte
        for line in self.text_lines:
            text_surface = self.font.render(line, True, self.font_color)
            self.screen.blit(text_surface, (self.rect.left + 10, y_offset))
            y_offset += self.font.get_height() + 5  # Espacement entre les lignes
