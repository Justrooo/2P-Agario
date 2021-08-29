import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, font_path, font_res, text, x, y):
        super().__init__()
        self.text = text
        self.font = pygame.font.Font(font_path, font_res)
        self.text_surface = self.font.render("", True, 0)
        self.rect = self.text_surface.get_rect()
        self.rect.center = [x, y]

    def update_text(self):
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        return self.text_surface
