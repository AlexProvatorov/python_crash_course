"""

Кубики: модуль random содержит функции для генерирования случайных чисел разными
способами. Функция randint() возвращает целое число в заданном диапазоне. 
Следующий код возвращает число от 1 до 6:
from random import randint
x = randint(1, 6)
Создайте класс Die с одним атрибутом с именем sides, который содержит значение 
по умолчанию 6. Напишите метод roll_die() для вывода случайного числа от 1 до 
количества сторон кубика. Создайте экземпляр, моделирующий 6-гранный кубик, и 
имитируйте 10 бросков. Создайте модели 10- и 20-гранного кубика. Имитируйте 10 
бросков каждого кубика. 

"""
from random import randint

class Dice():
    """Иммитация кубика"""

    def __init__(self, sides=6):
        """Инициализируем кол-во сторон кубиков."""
        self.sides = sides
    
    def update_dace(self, verge):
        """Задаем кол-во граней кубика."""
        self.sides = verge

    def roll_dice(self):
        """Имитация броска кубика."""
        self.roll = randint(1, self.sides)
        print("Бросок кубика: " + str(self.roll))

print("\nИмитация бросков 6-гранного кубика:\n")
my_dice = Dice()
for i in range(10):
    my_dice.roll_dice()

print("\nИмитация бросков 10-гранного кубика:\n")
my_dice = Dice()
my_dice.update_dace(10)
for i in range(10):
    my_dice.roll_dice()

print("\nИмитация бросков 20-гранного кубика:\n")
my_dice = Dice()
my_dice.update_dace(20)
for i in range(10):
    my_dice.roll_dice()