import pygame
from vars.vars import *

class Cell:
    # Инициализируем переменные принадлежащие этому классу + загружаем картинку повернутую на 90 *rotate_id, где rotate_id - рандомно сгенерирвоанное число
    # также генерируем список road - в котором элементы массива отвечают за наличие дороги в данном направлении, ниже написано за какое направление отвечает индекс
    def __init__ (self, x, y, type, rotate_id, i, j, light = 0):
        self.x = x
        self.y = y
        self.type = type
        self.width = cell_width
        self.height = cell_height
        self.rotate_id = rotate_id
        self.road = [0, 0, 0, 0] # 0 - right, 1 - down, 2 - left, 3 - up
        self.i = i
        self.j = j
        if(self.type == 0):
            self.image = pygame.transform.rotate(cell_type_0_image, self.rotate_id*(-90))
            self.road[self.rotate_id%4] = 1
        if(self.type == 1):
            self.image = pygame.transform.rotate(cell_type_1_image, self.rotate_id*(-90))
            if self.rotate_id % 2 == 1:
                self.road[2] = self.road[0] = 1
            else:
                self.road[1] = self.road[3] = 1
        if(self.type == 2):
            self.image = pygame.transform.rotate(cell_type_2_image, self.rotate_id*(-90))
            self.road[self.rotate_id % 4] = self.road[(self.rotate_id + 1) % 4 ] = 1
        self.light = light

    #Функция отображения ячеек
    def draw(self):

        # Если light =1, то отображаем картинку подсвеченую, иначе обычную
        if(self.light == 1):
            if(self.type == 0):
                self.image = pygame.transform.rotate(cell_type_0_image_l, self.rotate_id*(-90))
            if(self.type == 1):
                self.image = pygame.transform.rotate(cell_type_1_image_l, self.rotate_id*(-90))
            if(self.type == 2):
                self.image = pygame.transform.rotate(cell_type_2_image_l, self.rotate_id*(-90))
        else:
            if(self.type == 0):
                self.image = pygame.transform.rotate(cell_type_0_image, self.rotate_id*(-90))
            if(self.type == 1):
                self.image = pygame.transform.rotate(cell_type_1_image, self.rotate_id*(-90))
            if(self.type == 2):
                self.image = pygame.transform.rotate(cell_type_2_image, self.rotate_id*(-90))

        # Тоже самое что и с классом кнопок, только при нажатии обновляем направления ячеек
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if (self.x < mouse[0] < self.x +self.width) and (self.y < mouse[1] < self.y+self.height):
            display.blit(self.image,(self.x,self.y, self.width, self.height))
            if click[0] == 1:
                pygame.mixer.Sound.play(cell_sound)
                self.image = pygame.transform.rotate(self.image, -90)

                if(self.type == 0):
                    self.road[self.rotate_id%4] = 0
                if(self.type == 1):
                    if self.rotate_id % 2 == 1:
                        self.road[2] = self.road[0] = 0
                    else:
                        self.road[1] = self.road[3] = 0
                if(self.type == 2):
                    self.road[self.rotate_id % 4] = self.road[(self.rotate_id +1 )% 4 ] = 0

                self.rotate_id += 1

                if(self.type == 0):
                    self.road[self.rotate_id%4] = 1
                if(self.type == 1):
                    if self.rotate_id % 2 == 1:
                        self.road[2] = self.road[0] = 1
                    else:
                        self.road[1] = self.road[3] = 1
                if(self.type == 2):
                    self.road[self.rotate_id % 4] = self.road[(self.rotate_id +1 )%4 ] = 1
                pygame.time.delay(200)
        else:
            display.blit(self.image,(self.x, self.y, self.width, self.height))


    #Функция проверки соединения ячеек
    def check(self):
        global rows, columns
        # Создаем из списка направлений вида [1,0,0,1] список вида [0,3], где будут содержатся индексы направлений
        road_add = [w for w in range(0, len(self.road)) if self.road[w] == 1 ]

        # Создаем переменную флага
        flag = 0

        #Идем по элементам списка road_add проверяем ячейки, с котороыми связана текущая ячейка и подсвечиваем при необходимости
        for el in range(len(road_add)):
            if road_add[el] == 0:
                if self.i + 1 < columns:
                    if(objects[self.j][self.i+1].light == 1 and objects[self.j][self.i+1].road[2]==1):
                        flag +=1

            if road_add[el]==1:
                if self.j + 1 < rows:
                    if(objects[self.j+1][self.i].light == 1 and objects[self.j+1][self.i].road[3]==1):
                        flag +=1

            if road_add[el]==2:
                if self.i-1 != -1:
                    if(objects[self.j][self.i-1].light == 1 and objects[self.j][self.i-1].road[0]==1):
                        flag +=1
            if road_add[el]==3:
                if self.j - 1 != -1:
                    if(objects[self.j-1][self.i].light == 1 and objects[self.j-1][self.i].road[1]==1):
                        flag +=1
        if(self.i == self.j == 0 or flag != 0):
            self.light = 1