import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, font_path, font_res):
        super().__init__()
        self.text = ""
        self.font = pygame.font.Font(font_path, font_res)
        self.text_surface = self.font.render("", True, 0)

    def update_text(self):
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        return self.text_surface
