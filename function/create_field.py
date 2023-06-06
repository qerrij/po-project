#Функция создания игрового поля соответствующей сложности
from classes.cell import Cell
from vars.vars import *
import random

def create_field(difficult, objects, columns, rows):
    rand_col = columns-1
    rand_row = rows - 1
    if(difficult == 1):
        for i in range(columns):
            for j in range (rows):
                x = 142 + i*cell_width + (i+1)*cell_margin
                y = 142 + j*cell_height + (j+1)*cell_margin
                if(x == y == 144):
                    objects[0].append(Cell(x ,y, 0, random.randint(0,3), i, j, light = 1))
                else:
                    if(i == rand_col and j == rand_row):
                        objects[j].append(Cell(x ,y, 0, random.randint(0,3), i, j))
                    else:
                        if(i==0 or i == (columns-1)):
                            objects[j].append(Cell(x ,y, random.randint(1,2), random.randint(0,3), i, j))
                        else:
                            objects[j].append(Cell(x ,y, 1, random.randint(0,3), i, j))
    if(difficult == 2):
        for i in range(columns):
            for j in range (rows):
                x = 142 + i*cell_width + (i+1)*cell_margin
                y = 142 + j*cell_height + (j+1)*cell_margin
                if(x == y == 144):
                    objects[0].append(Cell(x ,y, 0, random.randint(0,3), i, j, light = 1))
                else:
                    if(i == rand_col and j == rand_row):
                        objects[j].append(Cell(x ,y, 0, random.randint(0,3), i, j))
                    else:
                        if(i==0 or i == (columns-1) or j == 0 or j == (rows-1)):
                            objects[j].append(Cell(x ,y, random.randint(1,2), random.randint(0,3), i, j))
                        else:
                            objects[j].append(Cell(x ,y, 1, random.randint(0,3), i, j))
    if(difficult == 3):
        for i in range(columns):
            for j in range (rows):
                x = 142 + i*cell_width + (i+1)*cell_margin
                y = 142 + j*cell_height + (j+1)*cell_margin
                if(x == y == 144):
                    objects[0].append(Cell(x ,y, 0, random.randint(0,3), i, j, light = 1))
                else:
                    if(i == rand_col and j == rand_row):
                        objects[j].append(Cell(x ,y, 0, random.randint(0,3), i, j))
                    else:
                        objects[j].append(Cell(x ,y, random.randint(1,2), random.randint(0,3), i, j))