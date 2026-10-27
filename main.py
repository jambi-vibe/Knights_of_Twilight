import pygame
import character

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

current_player_pos = character.draw_player()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    #render game here
    pygame.draw.rect(screen, "white", current_player_pos)

    current_key_pressed = pygame.key.get_pressed()

    if current_key_pressed[pygame.K_RIGHT]:
        current_player_pos.x = current_player_pos.x + 5

    if current_key_pressed[pygame.K_LEFT]:
        current_player_pos.x = current_player_pos.x - 5

    if current_key_pressed[pygame.K_UP]:
        current_player_pos.y = current_player_pos.y - 5

    if current_key_pressed[pygame.K_DOWN]:
        current_player_pos.y = current_player_pos.y + 5


    pygame.display.flip()
                
    clock.tick(60)
        


pygame.quit()