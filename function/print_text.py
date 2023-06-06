import pygame
from vars.vars import *
#Фунцкия вывода текста на экран
def print_text(message, x, y, color = (0,0,0), type = text_font, size = 36):
    font_type = pygame.font.Font(type, size)
    text =  font_type.render(message, True, color)
    display.blit(text, (x, y))