import pytest
from main import run_game

# Положительный тест для создания поля 22 при сложности "Easy"
def test_run_game_easy_2x2():
    global difficult, columns, rows, objects
    difficult = "Easy"
    columns = 2
    rows = 2    
    objects = []
    run_game()
    assert len(objects) == 2
    assert len(objects[0]) == 2
    assert len(objects[1]) == 2

# Отрицательный тест для создания поля 1x1
def test_run_game_1x1():
    global difficult, columns, rows, objects
    difficult = "Easy"
    columns = 1
    rows = 1
    objects = []
    with pytest.raises(SystemExit):
        run_game()

# Отрицательный тест для создания поля с отрицательными размерами
def test_run_game_negative_size():
    global difficult, columns, rows, objects
    difficult = "Easy"
    columns = -2
    rows = -2
    objects = []
    with pytest.raises(ValueError):
        run_game()