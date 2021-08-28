import pygame


class InputBox(pygame.sprite.Sprite):
    uinput = ""

    def __init__(self, font, path, x, y):
        super().__init__()
        self.input_font = font
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.text_surface = self.input_font.render("", True, 0)
        self.char = 10
        self.active = False

    def update_text(self):
        self.text_surface = self.input_font.render(self.uinput, True, (0, 0, 0))
        return self.text_surface
