import pygame # PARA CARREGAR QUAL IMAGEM VOCÊ QUER

helicopter_1 = pygame.image.load('sprites/helicopter_1.png')
helicopter_2 = pygame.image.load('sprites/helicopter_2.png')
#QUANDO O PLAY E ATINGIDO
helicopter_crach_1 = pygame.image.load('sprites/helicopter_crash_1.png')
helicopter_crach_2 = pygame.image.load('sprites/helicopter_crash_2.png')
helicopter_crach_3 = pygame.image.load('sprites/helicopter_crash_3.png')
helicopter_crach_4 = pygame.image.load('sprites/helicopter_crash_4.png')
#QUANDO FOR DESTRUIDO
helicopter_damaged_1 = pygame.image.load('sprites/helicopter_damaged_1.png')
helicopter_damaged_2 = pygame.image.load('sprites/helicopter_damaged_2.png')
#IMAGEM DO INIMIGO
enemy_helicopter_1 = pygame.image.load('sprites/enemy_helicopter_1.png')
enemy_helicopter_2 = pygame.image.load('sprites/enemy_helicopter_2.png')
#DO NAVIO INIMIGO
boat = pygame.image.load('sprites/boat.png')
#LISTAS
helicopter_list = [helicopter_1, helicopter_2]
damaged_helicopter_list = [helicopter_damaged_1, helicopter_damaged_2]
enemy_helicopter_list = [enemy_helicopter_1, enemy_helicopter_2]
#BALÃO
balloon = pygame.image.load('sprites/balloon.png')
spaceship = pygame.image.load('sprites/spaceship.png')
#ICONE DO GAME
icon = pygame.image.load('sprites/icon.png')
background = pygame.image.load('sprites/background.png')
cloud = pygame.image.load('sprites/cloud.png')

all_sprites = [helicopter_1, helicopter_2, helicopter_damaged_1, helicopter_damaged_2, enemy_helicopter_1,
               enemy_helicopter_2, helicopter_crach_1, helicopter_crach_2, helicopter_crach_3,
               helicopter_crach_4, boat, balloon, spaceship, icon, background, cloud]
