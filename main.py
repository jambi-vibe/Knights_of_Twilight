import pygame
import character
import world

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000), pygame.SCALED)
clock = pygame.time.Clock()
running = True

player_area = 1

current_player_pos = character.draw_player()

left_wall, right_wall, back_wall, small_left_wall, small_right_wall = world.starting_area()

while running:
    old_x_pos = current_player_pos.x
    old_y_pos = current_player_pos.y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")


    #render game here
    pygame.draw.rect(screen, "white", current_player_pos)

    current_key_pressed = pygame.key.get_pressed()

    #Left and Right movement and collision detection
    if current_key_pressed[pygame.K_RIGHT]:
        current_player_pos.x = current_player_pos.x + 5

    if current_key_pressed[pygame.K_LEFT]:
        current_player_pos.x = current_player_pos.x - 5

    if current_player_pos.colliderect(left_wall):
        current_player_pos.x = old_x_pos
    
    if current_player_pos.colliderect(right_wall):
        current_player_pos.x = old_x_pos

    if current_player_pos.colliderect(small_left_wall):
        current_player_pos.x = old_x_pos

    if current_player_pos.colliderect(small_right_wall):
            current_player_pos.x = old_x_pos

    #Up and Down movement and collision detection
    if current_key_pressed[pygame.K_UP]:
        current_player_pos.y = current_player_pos.y - 5

    if current_key_pressed[pygame.K_DOWN]:
        current_player_pos.y = current_player_pos.y + 5

    if current_player_pos.colliderect(back_wall):
        current_player_pos.y = old_y_pos

    if current_player_pos.colliderect(small_left_wall):
        current_player_pos.y = old_y_pos

    if current_player_pos.colliderect(small_right_wall):
            current_player_pos.y = old_y_pos

    if current_player_pos.bottom <= 0:
         player_area = player_area + 1
         current_player_pos.x = 300
         current_player_pos.y = 700
        

    
    
    #Draws the walls on screen
    if player_area == 1:
        left_wall, right_wall, back_wall, small_left_wall, small_right_wall = world.starting_area()
        walls = world.starting_area()
        for wall in walls:
            pygame.draw.rect(screen, "white", wall)

    if player_area == 2:
        left_wall, right_wall, back_wall, small_left_wall, small_right_wall = world.sword_area_locked()
        walls = world.sword_area_locked()
        for wall in walls:
            pygame.draw.rect(screen, "white", wall)
    

    pygame.display.flip()
                
    clock.tick(60)
        


pygame.quit()