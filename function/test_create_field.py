import pytest
from function.create_field import create_field

# Положительный тест для проверки создания поля на легком уровне сложности
def test_create_field_easy():
    objects = [[]]
    create_field(1, objects, 5, 5)
    assert len(objects) == 5
    assert len(objects[0]) == 5

# Положительный тест для проверки создания поля на среднем уровне сложности
def test_create_field_medium():
    objects = [[]]
    create_field(2, objects, 7, 7)
    assert len(objects) == 7
    assert len(objects[0]) == 7

# Положительный тест для проверки создания поля на тяжелом уровне сложности
def test_create_field_hard():
    objects = [[]]
    create_field(3, objects, 10, 10)
    assert len(objects) == 10
    assert len(objects[0]) == 10

# Отрицательный тест для проверки некорректного значения уровня сложности
def test_create_field_invalid_difficulty():
    objects = [[]]
    with pytest.raises(ValueError):
        create_field(4, objects, 5, 5)

# Отрицательный тест для проверки некорректного значения количества столбцов
def test_create_field_invalid_columns():
    objects = [[]]
    with pytest.raises(ValueError):
        create_field(1, objects, 0, 5)

# Отрицательный тест для проверки некорректного значения количества строк
def test_create_field_invalid_rows():
    objects = [[]]
    with pytest.raises(ValueError):
        create_field(1, objects, 5, -1)