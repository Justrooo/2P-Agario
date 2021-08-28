import pygame

player_textures = ["Images/Player/blue.png", "Images/Player/cyan.png",
                   "Images/Player/green.png", "Images/Player/lime.png",
                   "Images/Player/pink.png", "Images/Player/purple.png",
                   "Images/Player/red.png", "Images/Player/yellow.png"]


class Player(pygame.sprite.Sprite):
    interia = 10
    vel = interia*2 - interia

    def __init__(self, nick, path, x, y):
        super().__init__()
        self.nick = nick
        self.x = x
        self.y = y
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        pass
