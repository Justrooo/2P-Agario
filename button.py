import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, path, text, x, y):
        super().__init__()
        self.image = pygame.image.load(path)
        self.text = text
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.clicked = False

    def click(self):
        action = False
        #  Get mouse pos
        pos = pygame.mouse.get_pos()

        #  Start checking
        #  Check if cursor is above the button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed(3)[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed(3)[0]:
            self.clicked = False
        return action
