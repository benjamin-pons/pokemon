import pygame

class TextBox:
    def __init__(self, screen, width, height, font_size=24, font_color=(255, 255, 255), background_color=(0, 0, 0)):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font("assets/pokemon_pixel_font.ttf", font_size)
        self.font_color = font_color
        self.background_color = background_color
        self.text_lines = [] 
        self.rect = pygame.Rect(0, screen.get_height() - height, width, height)

    def add_text(self, text):
        """Add a line to textbox"""
        self.text_lines.append(text)
        # Maximum number of lines
        max_lines = self.height // (self.font.get_height() + 5)
        if len(self.text_lines) > max_lines:
            self.text_lines.pop(0)  # Deletes first line

    def draw(self):
        """Displays the textbox"""
        pygame.draw.rect(self.screen, self.background_color, self.rect)
        
        y_offset = self.rect.top + 10
        for line in self.text_lines:
            text_surface = self.font.render(line, True, self.font_color)
            self.screen.blit(text_surface, (self.rect.left + 10, y_offset))
            y_offset += self.font.get_height() + 5
