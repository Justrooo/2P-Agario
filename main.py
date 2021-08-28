import pygame
import player  # ./player.py
import textbox  # ./textbox.py
import ui_scripts.ui_bg  # ./ui_scripts/ui_bg.py
import ui_scripts.ui_panel  # ./ui_scripts/ui_panel.py
import ui_scripts.ui_text
from sys import exit
from random import choice, randint

pygame.init()
clock = pygame.time.Clock()

# Screen -------------------------------------------------------------------
sc = pygame.display.Info()  # info class object
w, h = 1200, 800
screen = pygame.display.set_mode((sc.current_w, sc.current_h-55))
pygame.display.set_caption("Agario but bad")
bg = ui_scripts.ui_bg.Background("Images/background.png")
menu_bg = ui_scripts.ui_bg.Background("Images/UI/background.png")
# Screen -------------------------------------------------------------------

# Players ------------------------------------------------------------------
rand_x = randint(0, w)
rand_y = randint(0, h)
# Player1
texture = choice(player.player_textures)
pr = player.Player("Gamer", texture, rand_x, rand_y)
# Player2
texture2 = choice(player.player_textures)
pr2 = player.Player("Gamer2", texture2, rand_x+100, rand_y+100)
# Player Group
pr_group = pygame.sprite.Group()
pr_group.add(pr)
pr_group.add(pr2)

if texture == texture2:
    if pr.image != player.player_textures[5]:
        pr2.image = pygame.image.load(player.player_textures[5])
        for x in range(3):  # Animation bc why not :D
            if x == 0: print("[class: Player] player1's texture was same as player2's texture. REMOVING.")
            elif x == 1: print("[class: Player] player1's texture was same as player2's texture. REMOVING..")
            else: print("[class: Player] player1's texture was same as player2's texture. REMOVING...")

    else:
        print("ELSE")
        pr2.image = pygame.image.load(player.player_textures[4])
else: pass
# Players ------------------------------------------------------------------
# Fonts & Texts ------------------------------------------------------------
input_font = pygame.font.Font("Fonts/input_font.ttf", 32)
button_font = pygame.font.Font("Fonts/button_font.ttf", 78)
# pr.nick = ui_scripts.ui_text.Text("Fonts/button_font.ttf", 78)  # FINISH LATER

# Fonts & Texts ------------------------------------------------------------
# Panels -------------------------------------------------------------------
# Left panel
panel_left = ui_scripts.ui_panel.Panel("Images/UI/box.png", 500, 600)
# Right panel
panel_right = ui_scripts.ui_panel.Panel("Images/UI/box.png", sc.current_w-500, 600)
# Group
panel_group = pygame.sprite.Group()
panel_group.add(panel_left)
panel_group.add(panel_right)
# Panels -------------------------------------------------------------------
# InputBox -----------------------------------------------------------------
inputBox = textbox.InputBox(input_font, "Images/UI/inputbox.png", panel_left.rect.centerx,
                            panel_left.image.get_height()-370)
input_group = pygame.sprite.Group()
input_group.add(inputBox)
print(panel_left.image.get_width())
print(panel_left.image.get_height())
# InputBox -----------------------------------------------------------------

menu_state = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if menu_state == 0:
            if inputBox.active:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        inputBox.uinput = inputBox.uinput[:-1]
                    else:
                        inputBox.uinput += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inputBox.rect.collidepoint(event.pos):
                    inputBox.active = True
                else:
                    inputBox.active = False

    if menu_state == 0:
        screen.blit(menu_bg.image, (0, 0))  # Background

        panel_group.draw(screen)  # Panel
        input_group.draw(screen)  # InputBox

        screen.blit(inputBox.update_text(), (inputBox.rect.x+5, inputBox.rect.y))  # Input Text

        if len(inputBox.uinput) > inputBox.char:
            inputBox.uinput = inputBox.uinput[:inputBox.char]
            if "wwwwww" in inputBox.uinput: inputBox.char = 6
            elif "mmmmmm" in inputBox.uinput: inputBox.char = 6
            else: inputBox.char = 10

        button_text_surface = button_font.render(pr.nick, True, (64, 64, 64))  # Nick
        screen.blit(button_text_surface, panel_left.rect.center)

    elif menu_state == 1:
        keys = pygame.key.get_pressed()
        # Movement ---------------------------------------------------------
        if keys[pygame.K_LEFT]: pr.rect.x -= pr.vel
        if keys[pygame.K_RIGHT]: pr.rect.x += pr.vel
        if keys[pygame.K_UP]: pr.rect.y -= pr.vel
        if keys[pygame.K_DOWN]: pr.rect.y += pr.vel

        # Player2's movement

        if keys[pygame.K_a]: pr2.rect.x -= pr2.vel
        if keys[pygame.K_d]: pr2.rect.x += pr2.vel
        if keys[pygame.K_w]: pr2.rect.y -= pr2.vel
        if keys[pygame.K_s]: pr2.rect.y += pr2.vel
        # Movement ---------------------------------------------------------
        # Border
        if pr.rect.left <= 0: pr.rect.left = pr.rect.x + 10
        if pr.rect.right >= sc.current_w: pr.rect.left = pr.rect.x - 10
        if pr.rect.top <= 0: pr.rect.top = pr.rect.y + 10
        if pr.rect.bottom >= sc.current_h: pr.rect.top = pr.rect.y - 10

        # Draw background
        screen.blit(bg.image, (0, 0))
        pr_group.draw(screen)
        pr_group.update()

    pygame.display.update()
    clock.tick(60)
