import pygame
from vars.vars import *
from function.print_text import print_text
class Button:

    #Инициализируем переменные принадлежащие этому классу
    def __init__ (self, x, y, width, height):
        self.width = width
        self.height = height
        self.inactivecolor = (128,218,235)
        self.activecolor = (0,191,255)
        self.x = x
        self.y = y

    #Функция отображения кнопки
    def draw(self, message,indent_x = 10, indent_y = 15, action = None, font = 30):

        # Считываем позицию мышки и клики её клавиш
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Если курсор на кнопке, то
        if (self.x < mouse[0] < self.x +self.width) and (self.y < mouse[1] < self.y+self.height):

            #Отрисовываем прямоугольник цвета - активной кнопки
            pygame.draw.rect(display, self.activecolor, (self.x, self.y, self.width, self.height))
            # Если была левая кнопки мыши в границах кнопки, то
            if click[0] == 1:

                # Воспроизводим звук
                pygame.mixer.Sound.play(button_sound)
                # Выполняем действие с задержкой в 150 мс
                pygame.time.delay(150)
                if action is not None:
                    action()
        else:

            # Иначе отрисовываем кнопку цвета - неактивной кнопки
            pygame.draw.rect(display, self.inactivecolor, (self.x, self.y, self.width, self.height))

        #Отображаем текст на кнопке
        print_text(message, self.x + indent_x, self.y + indent_y, size = font)