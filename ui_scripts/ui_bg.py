import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
