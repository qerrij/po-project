# Импортируем  библиотеки необходимые для работы кода (pygame - для механики игры и основного окна, random - для генерации радномных чисел, tkinter - для вывода диалоговых окон)
import pygame
# Инициализируем игру
pygame.init()

from vars.vars import *
from tkinter import *
from tkinter import messagebox
from function.create_field import create_field
from function.print_text import print_text
from classes.cell import Cell
from classes.button import Button

# Инициализируем игру


# Создаем основное окно tkinter и делаем его невидимым
tk = Tk()
tk.withdraw()


#Создаем окно игры
pygame.display.set_caption(name_game)
pygame.display.set_icon(icon_game)

#Функция игры
def run_game():

    # Объявляем глобальные переменные
    # global difficult, columns, rows, objects

    # Если пользователь хочет создать поле 1 на 1, выдаем ошибку
    if(columns * rows == 1):
        messagebox.showinfo("Game not started!", "Unable to create 1 by 1 field!\nChange amount columns or rows!")
        show_menu()
    game = True
   
    #Создание кнопок Quit и New game
    button_quit = Button(580, 740, 220, 60)
    button_new_game = Button(0, 740, 220, 60)

    # Запоминаем время старта программы для таймера
    time_start = pygame.time.get_ticks()
    
    # Создаем список objects - в нем будут хранится наши ячейки в виде двухмерного списка
    objects.clear()
    for j in range(rows):
        objects.append([])
    
    # Вызываем функцию создания поля
    create_field(difficult, objects, columns, rows)
    
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        
        #Создаем белый фон
        display.fill((255, 255 ,255))

        # Создаем границу для игрового поля
        pygame.draw.rect(display,(0,0,0),(139, 139, 528, 528), 3)
        
        #Создание и отображение таймера
        timer = str((time_for_game-(pygame.time.get_ticks()-time_start)//1000)//60)+':'
        if (time_for_game-(pygame.time.get_ticks()-time_start)//1000)%60 < 10:
            timer = timer + '0'+str((time_for_game-(pygame.time.get_ticks()-time_start)//1000)%60)
        else:
            timer = timer +str((time_for_game-(pygame.time.get_ticks()-time_start)//1000)%60)
        print_text(timer, 363, 760)

        # Если таймер = 0:00 то выходим с сообщением о поражении 
        if(timer=="0:00"):
            end_game("end_time")

        #Отображение кнопок Quit и New game
        button_quit.draw("Quit", 60, 15, font = 36, action = show_menu)
        button_new_game.draw("New game", font = 36, action = run_game )
        
        #Отображение игрового поля, обновляем 10 раз чтобы корректно отображать изменения
        for k in range(10):
            for j in range(rows):
                for i in range(columns):
                    objects[j][i].check()

        for j in range(rows):
            for i in range(columns):
                objects[j][i].check()
                objects[j][i].draw()
        
        #Обновляем дисплей(основное окно)
        pygame.display.update()

        #Смотрим условие победы, если выполняется выходим с индексом победы
        wincondition=0
        for j in range(rows):
            for i in range(columns):
                if objects[j][i].light == 1:
                    wincondition += 1
        if(wincondition == rows * columns):
            end_game("end_win")
        
        #Обнуляем у всех ячеек подсветку, чтобы не подсвечивать ячейки, которые были подключены на прошлом ходу, а на этом они уже отключены
        for j in range(rows):
            for i in range(columns):
                if(i == j == 0):
                    pass
                else:
                    objects[j][i].light = 0

#Функция показа меню
def show_menu():

    #Создаем необходимые кнопки
    start_game_button = Button(230,300,340,80)
    settings_game_button =  Button(265,400,270,80)
    quit_game_button = Button(310,500,180,80)
    
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        display.blit(menu_background, (0,0))
        start_game_button.draw("Start game", indent_x = 13, font = 50, action = run_game)
        settings_game_button.draw("Settings", indent_x = 13, font = 50, action = show_settings)
        quit_game_button.draw("Quit", font = 50, indent_x = 24, action = quit_game)
       
        pygame.display.update()

#Функция выхода из игры
def quit_game():
    pygame.quit()
    quit()

#Функция окончания игры
def end_game(x):
    pygame.time.delay(200)

    # Отображаем последнее изменение
    for j in range(rows):
        for i in range(columns):
            objects[j][i].draw()
    pygame.display.update()
    pygame.time.delay(150)
    end = True
    
    # Создаем кнопки
    button_quit = Button(580, 740, 220, 60)
    button_new_game = Button(0, 740, 220, 60)
    
    # Если выиграли выводим соответсвующее сообщение, также для поражения
    if(x=="end_time"):
        messagebox.showinfo("Game over!", "Time is over!")
    if(x == "end_win"):
        messagebox.showinfo("Game over!", "You win!")
   
    while  end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            #Отображение кнопок Quit и New game
            button_quit.draw("Quit", 60, 15, font = 36, action = show_menu)
            button_new_game.draw("New game", font = 36, action = run_game)
            pygame.display.update()

#Функция отвечающая за отображение меню настроек в главном окне
def show_settings():
    show = True

    #Создаесм все необходимые в этом меню кнопки
    button_quit = Button(580, 740, 220, 60)
    button_change_difficult = Button(390, 190, 150, 56)
    button_change_columns = Button(390, 290, 150, 56)
    button_change_rows = Button(390, 390, 150, 56)

    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        #Отображаем задний фон
        display.blit(menu_background, (0,0))

        #Отображаем кнопку и тексы на них
        button_quit.draw("Quit", 60, 15, font = 36, action = show_menu)
       
        pygame.draw.rect(display, (255, 255, 255), (90, 190, 300, 55))
        print_text("Difficult:", 100, 200)
        print_text(str(difficult), 330, 200)

        pygame.draw.rect(display, (255, 255, 255), (90, 290, 300, 55))
        print_text("Columns:", 100, 300)
        print_text(str(columns), 320, 300)

        pygame.draw.rect(display, (255, 255, 255), (90, 390, 300, 55))
        print_text("Rows:", 135, 400)
        print_text(str(rows), 320, 400)

        button_change_difficult.draw("Change", action = inc_dif)
        button_change_columns.draw("Change", action = inc_col)
        button_change_rows.draw("Change", action = inc_row)
        pygame.display.update()
#Функции отвечающие за действие кнопок изменения сложности, кол-ва столбцов и кол-во строк соответственно
def inc_dif():
    global difficult
    if difficult < 3:
        difficult = difficult + 1
    else:
        difficult = 1
def inc_col():
    global columns
    if columns <10:
        columns = columns + 1
    else:
        columns = 1
def inc_row():
    global rows
    if rows <10:
        rows= rows + 1
    else:
        rows = 1


#Запуск игры
show_menu()