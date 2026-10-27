import pygame

def starting_area():
    wall_1 = pygame.Rect(0, 0, 200, 1000)
    wall_2 = pygame.Rect(800, 0, 200, 1000)
    wall_3 = pygame.Rect(200, 800, 600, 200)
    wall_4 = pygame.Rect(200, 0, 200, 200)
    wall_5 = pygame.Rect(600, 0, 200, 200)


    return wall_1, wall_2, wall_3, wall_4, wall_5

def sword_area():
    wall_1 = pygame.Rect()