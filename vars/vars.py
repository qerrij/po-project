import pygame

display_width = 800
display_height = 800
name_game = "Light'em up!"
time_for_game = 120
cell_width = cell_height =50
cell_margin = 2
difficult = 1
columns = 10
rows = 10

#Блок переменных(настроек игры)
button_sound = pygame.mixer.Sound("resource/button_sound.mp3")
cell_sound = pygame.mixer.Sound("resource/cell_sound.mp3")
text_font = "resource/font.ttf"
menu_background = pygame.image.load("resource/back.jpg")
cell_type_1_image = pygame.image.load("resource/cell_type_1.png")
cell_type_2_image = pygame.image.load("resource/cell_type_2.png")
cell_type_0_image = pygame.image.load("resource/cell_type_0.png")
cell_type_0_image_l = pygame.image.load("resource/cell_type_0_light.png")
cell_type_1_image_l = pygame.image.load("resource/cell_type_1_light.png")
cell_type_2_image_l = pygame.image.load("resource/cell_type_2_light.png")

icon_game = pygame.image.load("resource/icon.png")
display = pygame.display.set_mode((display_width, display_height))

objects = []